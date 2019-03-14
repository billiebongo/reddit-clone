import Home from './components/Home.vue';
import SignIn from './components/auth/SignIn.vue';
import SignUp from "./components/auth/SignUp";

export const routes = [
    {path: "/", component: Home},
    {path: "/signin", component: SignIn},
    {path: "/signup", component: SignUp}
];