<template>
    <button
        :style="{ backgroundColor: color }"
        class="btn"
        @click="$emit('toggle-add-task')"
    >
        {{ text }}
    </button>
</template>

<script>
export default {
    name: "Button",
    props: {
        text: String,
        color: String,
    },
    emits: ["toggle-add-task"],
};
</script>
