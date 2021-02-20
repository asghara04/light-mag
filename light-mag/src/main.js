import { createApp } from 'vue';
import App from './App.vue';
import store from '@/store.js';
import router from '@/router/index.js';
import arouter from '@/router/admin.js';
const parts = window.location.host.split(".");
const len = 3;
const routes = ()=>{
	let route;
	if(parts.length===len-1||(parts.length===len&&parts[0]==="www")){
		route = router
	}else if(parts.length===len&&parts[0]==="admin"){
		route = arouter
	}
	return route
}
createApp(App).use(routes()).use(store).mount('#app')