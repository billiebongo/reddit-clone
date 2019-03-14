<template>
    <div class="ui secondary menu">
        <!--put website logo here?-->
        <router-link to="/">Home</router-link>

        <!--just placing this search bar function here for fun-->
        <div class="item">
            <div class="ui icon input">
                <input type="text" placeholder="Search...">
                <i class="search link icon"></i>
            </div>
        </div>

        <div class="right menu">
            <!--if user is not signed in, show this-->
            <!--sign up/ sign in-->
            <div class="item" v-if="!auth">
                <div class="ui buttons">
                    <router-link to="/signup">
                        <button class="ui basic blue button">Sign Up</button>
                    </router-link>
                    <div class="or"></div>
                    <router-link to="/signin">
                        <button class="ui blue button">Log In</button>
                    </router-link>
                </div>
            </div>

            <!--else if the user is signed in, show their profile picture-->
            <!--user profile picture-->
            <div class="item" v-if="auth">

            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Header",
        computed: {
            auth() {
                return this.$store.getters.isAuthenticated
            }
        },
    }
</script>

<style scoped>

</style>