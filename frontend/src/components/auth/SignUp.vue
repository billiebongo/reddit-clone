<template>
    <div class="ui container">
        <app-header></app-header>
        <div class="ui centered card">
            <div class="image">
                <!--placeholder image-->
                <img src="../../assets/logo.png" height="200" width="200"/></div>
            <div class="content">
                <a class="header">The record for filling out this form is 15.82s...
                    Goooooo!</a>
            </div>
        </div>
        <form class="ui form" >
            <div class="field">
                <label>First Name</label>
                <input type="text" name="first-name" placeholder="First Name">
            </div>
            <div class="field">
                <label>Last Name</label>
                <input type="text" name="last-name" placeholder="Last Name">
            </div>
            <div class="grouped fields" @click="genderCheckbox">
                <label for="gender">Gender</label>
                <div class="field">
                    <div class="ui radio checkbox">
                        <input type="radio" name="gender" tabindex="0" class="hidden">
                        <label>Male</label>
                    </div>
                </div>
                <div class="field">
                    <div class="ui radio checkbox">
                        <input type="radio" name="gender" tabindex="0" class="hidden">
                        <label>Female</label>
                    </div>
                </div>
                <div class="field">
                    <div class="ui radio checkbox">
                        <input type="radio" name="gender" tabindex="0" class="hidden">
                        <label>Others</label>
                    </div>
                </div>
                <div class="field">
                    <div class="ui radio checkbox">
                        <input type="radio" name="gender" tabindex="0" class="hidden">
                        <label>Prefer not to say</label>
                    </div>
                </div>
            </div>
            <div class="field">
                <label>Email Address</label>
                <input class="round-input" type="email" name="email" placeholder="ladybossj@gmail.com">
            </div>
            <div class="field">
                <label>Confirm Email Address</label>
                <input class="round-input" type="email" name="email-confirm" placeholder="ladybossj@gmail.com">
            </div>
            <div class="field">
                <label>Password</label>
                <input class="round-input" type="password" name="email" placeholder="not password123">
            </div>
            <div class="field">
                <label>Confirm Password</label>
                <input class="round-input" type="password" name="email" placeholder="not password123">
            </div>
            <button class="ui button" type="submit">Submit</button>

        </form>
        <div class="ui hidden divider"></div>
    </div>
</template>

<script>
    import Header from '../Header.vue';
    export default {
        name: "SignUp",
        components: {
            appHeader: Header
        },
        methods: {
            genderCheckbox() {
                $('.ui.radio.checkbox')
                    .checkbox()
                ;
            }
        },
        created() {

        }
    }
</script>

<style scoped>

</style>