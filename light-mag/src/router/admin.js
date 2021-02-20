import {createRouter,createWebHistory} from 'vue-router';

const routes = [
	{
		path: "/login",
		name: "Login",
		component: import("@/views/Loger.vue")
	},
]

const arouter = createRouter({
	history: createWebHistory(),
	routes
})

export default arouter