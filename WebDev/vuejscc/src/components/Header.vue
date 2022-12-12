<template>
    <header>
        <h1>{{title}}</h1>
    </header>
</template>

<script>
    export default {
        name: 'Header',
        props:['title']
    }   
</script>

<style scoped>
    header{
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 20px;
    }
</style>