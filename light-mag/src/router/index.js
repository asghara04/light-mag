import {createRouter, createWebHistory} from 'vue-router';

const routes = [
		{
			path: '/',
			name: "Home",
			component: import("@/views/Home.vue"),
			props: route => ({num: parseInt(route.query.page)})
		},
		{
			path: "/article/:address",
			name: 'article',
			props: true,
			component: import("@/views/article.vue")
		},
		{
			path: "/categories",
			name: "categories",
			component: import("@/views/categories.vue"),
			props: route => ({num: parseInt(route.query.page)})
		},
		{
			path: "/login",
			name: "Login",
			component: import("@/views/Loger.vue")
		},
		{
			path: "/about",
			name: "about",
			component: import("@/views/about.vue")
		},
		{
			path: "/contact",
			name: "contact",
			component: import("@/views/contact.vue")
		},
]

const router = createRouter({
	history: createWebHistory(),
	routes
})

export default router;