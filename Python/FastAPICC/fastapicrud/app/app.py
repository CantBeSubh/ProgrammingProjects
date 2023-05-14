from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=["ROOT"])
async def root() -> dict:
    return {"message": "Hello World"}


@app.get("/todo", tags=["TODO"])
async def get_todo() -> dict:
    return {"data": todos}


@app.post("/todo", tags=["TODO"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {"data": "Todo Added"}


@app.put("/todo/{id}", tags=["TODO"])
async def update_todo(id: int, body: dict) -> dict:
    # todos = map(lambda x: body if x.id == id else x, todos)
    for todo in todos:
        if int(todo["id"]) == id:
            todo["title"] = body["title"]
            return {"data": "1 Row Updated"}
    return {"data": f"No entry with id: {id}"}


@app.delete("/todo/{id}", tags=["TODO"])
async def del_todo(id: int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {"data": "1 Row Deleted"}
    return {"data": f"No entry with id: {id}"}


todos = [
    {
        "id": 1,
        "title": "Create a todo",
        "description": "Learn how to create a todo with FastAPI",
        "done": False,
    },
    {
        "id": 2,
        "title": "Create a todo with a PUT request",
        "description": "Learn how to create a todo with a PUT request",
        "done": False,
    },
    {
        "id": 3,
        "title": "Create a todo with a DELETE request",
        "description": "Learn how to create a todo with a DELETE request",
        "done": False,
    },
]
