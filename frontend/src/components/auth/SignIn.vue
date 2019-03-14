<template>
    <div>
        <div class="ui container">
            <app-header></app-header>
        </div>
        <div class="ui middle aligned two column centered grid">
            <div class="row">
                <div class="column">
                    <div class="ui placeholder segment">
                        <div class="ui two column very relaxed stackable grid">
                            <div class="column">
                                <div class="ui large form">
                                    <div class="field">
                                        <label>Username</label>
                                        <div class="ui left icon input">
                                            <input type="text" placeholder="Username">
                                            <i class="user icon"></i>
                                        </div>
                                    </div>
                                    <div class="field">
                                        <label>Password</label>
                                        <div class="ui left icon input">
                                            <input type="password" placeholder="Password">
                                            <i class="lock icon"></i>
                                        </div>
                                    </div>
                                    <div class="ui blue submit button">Login</div>
                                </div>
                            </div>
                            <div class="middle aligned column">
                                <router-link to="/signup">
                                    <div class="ui big button">
                                        <i class="signup icon"></i>
                                        Sign Up
                                    </div>
                                </router-link>
                            </div>
                        </div>

                        <div class="ui vertical divider">
                            Or
                        </div>
                    </div>
                </div>

            </div>

        </div>
    </div>

</template>

<script>
    import Header from "../Header.vue";

    export default {
        name: "SignIn",
        components: {
            appHeader: Header
        }
    }
</script>

<style scoped>

</style>