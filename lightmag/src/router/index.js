import { createRouter, createWebHistory } from '@ionic/vue-router';
import HomePage from '@/pages/HomePage.vue';

const routes = [
	{
		path: '/',
		name: 'HomePage',
		component: HomePage
	},
	{
		path: "/categories",
		name: "CategoriesPage",
		// component
	},
	{
		path: "/about",
		name: "AboutPage",
		component: ()=>import("@/pages/AboutPage.vue")
	},
	{
		path: "/contact",
		name: "ContactPage",
		// component
	}
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
