import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '@/views/Home.vue';
import about from '@/views/about.vue';
import contact from '@/views/contact.vue';
import categories from '@/views/categories.vue';
import article from '@/views/article.vue';
import Loger from '@/views/Loger.vue';

Vue.use(VueRouter)

export default new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes: [
		{
			path: '/',
			name: "Home",
			component: Home,
			props: route => ({num: parseInt(route.query.page)})
		},
		{
			path: "/article/:address",
			name: 'article',
			props: true,
			component: article
		},
		{
			path: "/categories",
			name: "categories",
			component: categories,
			props: route => ({num: parseInt(route.query.page)})
		},
		{
			path: "/login",
			name: "Login",
			component: Loger
		},
		{
			path: "/about",
			name: "about",
			component: about
		},
		{
			path: "/contact",
			name: "contact",
			component: contact
		},
	]
})