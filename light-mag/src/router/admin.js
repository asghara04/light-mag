import {createRouter,createWebHistory} from 'vue-router';

const routes = [
	{
		path: "/login",
		name: "Login",
		component: () => import("@/views/Loger.vue")
	},
	{
		path: "/LM-admin",
		name: "admin-panel",
		component: () => import("@/views/lm-admin.vue")
	}
]

const arouter = createRouter({
	history: createWebHistory(),
	routes
})

export default arouter