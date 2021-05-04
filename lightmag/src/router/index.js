import { createRouter, createWebHistory } from '@ionic/vue-router';

// components
import HomePage from '@/pages/HomePage.vue';

const routes = [
	{
		path: '/',
		name: "HomePage",
		component: HomePage
	},
	{
		path: "/categories",
		name: "CategoriesPage",
		component: ()=>import("@/pages/CategoriesPage.vue")
	},
	{
		path: "/about",
		name: "AboutPage",
		component: ()=>import("@/pages/AboutPage.vue")
	},
	{
		path: "/contact",
		name: "ContactPage",
		component: ()=>import("@/pages/ContactPage.vue")
	}
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
