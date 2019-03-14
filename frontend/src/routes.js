import Home from './components/Home.vue';
import SignIn from './components/auth/SignIn.vue';

export const routes = [
    {path: "/", component: Home},
    {path: "/signin", component: SignIn}
];