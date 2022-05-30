import Booklist from "./comps/BookList";
import AddBook from "./comps/AddBook";

function App() {
  return (
      <div className="App" id='main'>
        <h1>My Reading List</h1>
        <Booklist/>
        <AddBook/>
      </div>
  );
}

export default App;