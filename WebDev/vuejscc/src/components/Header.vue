<template>
    <header>
        <h1>{{ title }}</h1>
        <Button
            @toggle-add-task="$emit('toggle-add-task')"
            text="Add Task"
            color="green"
        />
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
    emits: ["toggle-add-task"],
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
