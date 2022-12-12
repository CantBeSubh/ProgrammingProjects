<template>
    <header>
        <h1>{{ title }}</h1>
        <Button text="Add Task" color="green" />
    </header>
</template>

<script>
import Button from "./Button";

export default {
    name: "Header",
    props: ["title"],
    components: {
        Button,
    },
};
</script>

<style scoped>
header {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
}
</style>
