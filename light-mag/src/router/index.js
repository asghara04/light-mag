import {createRouter, createWebHistory} from 'vue-router';

const routes = [
	{
		path: '/',
		name: "Home",
		component: () => import("@/views/Home.vue"),
		props: route => ({page: parseInt(route.query.page)})
	},
	{
		path: "/article/:artslug",
		name: 'article',
		props: true,
		component: () => import("@/views/article.vue")
	},
	{
		path: "/categories",
		name: "categories",
		component: () => import("@/views/categories.vue"),
		props: route => ({page: parseInt(route.query.page)}),
	},
	{
		path: "/categories/:catslug",
		name: "category",
		component: ()=> import("@/views/category.vue"),
		props: true,
		children:[
			{
				path: ":subcatname",
				name: "subcat",
				props: true,
				component: () => import("@/views/subcat.vue")
			}
		]
	},
	{
		path: "/user/:username/profile",
		name: 'userprofile',
		props: true,
		component: ()=> import('@/views/userprofile.vue')
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
		path: "/:pathMatch(.*)*",
		name: "not_found",
		component: () => import("@/views/404.vue")
	},
]

const router = createRouter({
	history: createWebHistory(),
	routes
})

export default router;