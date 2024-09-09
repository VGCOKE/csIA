<script>
export default {
    props: ['id'], 
    data() {
        return {
        recordId: this.id, 
        // ... other data properties to fetch and display detailed record information
        };
    },
    mounted() {
        // Fetch the detailed record data from your backend using the recordId
    },
};
</script>

<template>
    <div>
        <h2>History Record Details</h2>
        <p>ID: {{ recordId }}</p>
    </div>
</template>

