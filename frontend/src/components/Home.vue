<template>
    <div>
        <div class="ui container">
            <app-header></app-header>
        </div>
    </div>
</template>

<script>
    import Header from "./Header.vue";
    export default {
        components: {
            'app-header': Header
        }
    }
</script>

<style scoped>

</style>