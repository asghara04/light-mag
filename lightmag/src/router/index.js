import { createRouter, createWebHistory } from '@ionic/vue-router';
import HomePage from '@/pages/HomePage.vue';

const routes = [
	{
		path: '/',
		name: 'Home',
		component: HomePage
	}
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
