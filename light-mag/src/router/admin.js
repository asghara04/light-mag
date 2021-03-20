import {createRouter,createWebHistory} from 'vue-router';
import store from '@/store.js';

const routes = [
	{
		path: "/login",
		name: "Login",
		component: () => import("@/views/Loger.vue"),
		meta:{
			requiresUnAuth: true
		}
	},
	{
		path: "/LM-admin",
		name: "admin-panel",
		component: () => import("@/views/lm-admin.vue"),
		meta:{
			requiresAuth: true
		}
	},
	{
		path: '/',
		name: 'nothing',
		meta:{
			requiresAuth: true,
			requiresUnAuth: true
		}
	},
	{
		path: '/LM-admin/add',
		name: "add",
		component: () => import("@/views/lm-form.vue"),
		meta:{
			requiresAuth: true
		},
		children:[
			{
				path: "image",
				meta:{requiresAuth: true},
				component: () => import("@/views/lm-add-image.vue")
			},
			{
				path: "category",
				meta:{requiresAuth:true},
				component: ()=>import("@/views/lm-add-category.vue")
			},
			{
				path: "subcat",
				meta:{requiresAuth:true},
				component: ()=>import("@/views/lm-add-subcat.vue")
			},
		]
	},
	{
		path: "/LM-admin/change",
		name: "change",
		component: ()=>import("@/views/lm-form.vue"),
		meta:{
			requiresAuth: true
		},
		children:[
			{
				path: "image/:id",
				meta:{requiresAuth:true},
				props: true,
				name: "change-image",
				component:()=>import("@/views/lm-change-image.vue")
			},
			{
				path: "category/:catslug",
				meta: {requiresAuth:true},
				props: true,
				name: "change-category",
				component:()=>import('@/views/lm-change-category')
			},
			{
				path:"subcat/:cat/:sub",
				meta: {requiresAuth:true},
				props: true,
				name: "change-subcat",
				component:()=>import("@/views/lm-change-subcat.vue")
			}
		]
	},
	{
		path: "/LM-admin/articles",
		name: "lm-articles",
		component: () => import("@/views/lm-articles.vue"),
		meta:{
			requiresAuth: true
		}
	},
	{
		path: "/LM-admin/categories",
		name: "lm-categories",
		component: () => import("@/views/lm-categories.vue"),
		props: route => ({page: parseInt(route.query.page)}),
		meta:{
			requiresAuth: true
		}
	},
	{
		path: "/LM-admin/categories/:slug",
		name: "lm-category",
		component: () => import("@/views/lm-category.vue"),
		meta:{
			requiresAuth: true
		}
	},
	{
		path: "/LM-admin/comments",
		name: "lm-comments",
		component: () => import("@/views/lm-comments.vue"),
		meta:{
			requiresAuth: true
		}
	},
	{
		path: "/LM-admin/images",
		name: 'lm-images',
		component: () => import("@/views/lm-images.vue"),
		props: route => ({page: parseInt(route.query.page)}),
		meta:{
			requiresAuth: true
		}
	},
	{
		path: "/LM-admin/tags",
		name: "lm-tags",
		component: () => import("@/views/lm-tags.vue"),
		meta:{
			requiresAuth: true
		}
	},
	{
		path: '/LM-admin/users',
		name: 'lm-users',
		component: () => import('@/views/lm-users.vue'),
		meta:{
			requiresAuth: true
		}
	},
	{
		path: "/LM-admin/settings",
		name: "lm-settings",
		component: () => import('@/views/lm-settings.vue'),
		meta:{
			requiresAuth: true
		}
	}
]

const arouter = createRouter({
	history: createWebHistory(),
	routes
})

arouter.beforeEach((to, from, next) => {
	if(to.matched.some(record => record.meta.requiresAuth)){
		if(!store.getters.logedIn){
			next({name: 'Login'});
		}else{
			next();
		}
	}else if(to.matched.some(record => record.meta.requiresUnAuth)){
		if(store.getters.logedIn){
			next({name: "admin-panel"});
		}else{
			next();
		}
	}else{
		next()
	}
})

export default arouter