import {createRouter, createWebHistory} from 'vue-router';

const routes = [
	{
		path: '/',
		name: "Home",
		component: () => import("@/views/Home.vue"),
		props: route => ({num: parseInt(route.query.page)})
	},
	{
		path: "/article/:slug",
		name: 'article',
		props: true,
		component: () => import("@/views/article.vue")
	},
	{
		path: "/categories",
		name: "categories",
		component: () => import("@/views/categories.vue"),
		props: route => ({num: parseInt(route.query.page)}),
	},
	{
		path: "/categories/:slug",
		name: "category",
		component: ()=> import("@/views/category.vue"),
		props: true,
		children:[
			{
				path: ":name",
				name: "subcat",
				props: true,
				component: () => import("@/views/subcat.vue")
			}
		]
	},
	{
		path: "/games",
		name: "games",
		component: () => import("@/views/games.vue")
	},
	{
		path: "/about",
		name: "about",
		component: () => import("@/views/about.vue")
	},
	{
		path: "/contact",
		name: "contact",
		component: () => import("@/views/contact.vue")
	},
	{
		path: "/*",
		name: "not found",
		component: () => import("@/views/404.vue")
	}
]

const router = createRouter({
	history: createWebHistory(),
	routes
})

export default router;