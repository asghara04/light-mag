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
		component: () => import("@/views/lm-admin.vue"),
	},
	{
		path: "/LM-admin/articles",
		name: "lm-articles",
		component: () => import("@/views/lm-articles.vue")
	},
	{
		path: "/LM-admin/categories",
		name: "lm-categories",
		component: () => import("@/views/lm-categories.vue")
	},
	{
		path: "/LM-admin/comments",
		name: "lm-comments",
		component: () => import("@/views/lm-comments.vue")
	},
	{
		path: "/LM-admin/tags",
		name: "lm-tags",
		component: () => import("@/views/lm-tags.vue")
	},
	{
		path: '/LM-admin/users',
		name: 'lm-users',
		component: () => import('@/views/lm-users.vue')
	},
	{
		path: "/LM-admin/settings",
		name: "lm-settings",
		component: () => import('@/views/lm-settings.vue')
	}
]

const arouter = createRouter({
	history: createWebHistory(),
	routes
})

export default arouter