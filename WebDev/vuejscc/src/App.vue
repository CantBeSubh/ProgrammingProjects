<template>
    <div class="container">
        <Header title="Task Tracker" />
        <Tasks
            @toggle-reminder="toggleReminder"
            @delete-task="deleteTask"
            :tasks="tasks"
        />
        <!-- dynamic so using v-bind:tasks -->
    </div>
</template>

<script>
import Header from "./components/Header";
import Tasks from "./components/Tasks";

export default {
    name: "App",
    components: {
        Header,
        Tasks,
    },
    data() {
        return {
            tasks: [],
        };
    },
    methods: {
        deleteTask(id) {
            if (confirm("Are you sure?")) {
                this.tasks = this.tasks.filter((task) => task.id !== id);
            }
        },
        toggleReminder(id) {
            this.tasks = this.tasks.map((task) =>
                task.id === id ? { ...task, reminder: !task.reminder } : task
            );
        },
    },
    created() {
        this.tasks = [
            {
                id: 1,
                text: "Doctors Appointment",
                day: "Feb 5th at 2:30pm",
                reminder: true,
            },
            {
                id: 2,
                text: "Meeting at School",
                day: "Feb 6th at 1:30pm",
                reminder: true,
            },
            {
                id: 3,
                text: "Food Shopping",
                day: "Feb 5th at 2:30pm",
                reminder: false,
            },
        ];
    },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap");

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    /* //css to disable selecting text */
    -webkit-touch-callout: none; /* iOS Safari */
    -webkit-user-select: none; /* Safari */
    -khtml-user-select: none; /* Konqueror HTML */
    -moz-user-select: none; /* Old versions of Firefox */
    -ms-user-select: none; /* Internet Explorer/Edge */
    user-select: none; /* Non-prefixed version, currently
                                    supported by Chrome, Edge, Opera and Firefox */
}

body {
    font-family: "Poppins", sans-serif;
    /* background-color: #222;
  color: #fff; */
}

.container {
    max-width: 500px;
    margin: 30px auto;
    overflow: auto;
    min-height: 300px;
    border: 1px solid steelblue;
    padding: 30px;
    border-radius: 5px;
}

.btn {
    display: inline-block;
    background: #000;
    color: #fff;
    border: none;
    padding: 10px 20px;
    margin: 5px;
    border-radius: 5px;
    cursor: pointer;
    text-decoration: none;
    font-size: 15px;
    font-family: inherit;
}

.btn:focus {
    outline: none;
}

.btn:active {
    transform: scale(0.98);
}

.btn-block {
    display: block;
    width: 100%;
}
</style>
