<script>
export default {
    props: ['id'], 
    data() {
        return {
        recordId: this.id, 
        };
    },
    mounted() {
    },
};
</script>

<template>
    <div>
        <h2>History Record Details</h2>
        <p>ID: {{ recordId }}</p>
    </div>
</template>

