import { createApp } from 'vue';
import App from './App.vue';
import store from '@/store.js';
import router from '@/router/index.js';
import arouter from '@/router/admin.js';
const parts = window.location.host.split(".");
const len = 3;
function routes(){
	let routes = router;
	if(parts.length<=len-1||(parts.length===len&&parts[0]==="www")){
		routes = router;
	}else if(parts.length<=len&&parts[0]==="admin"){
		routes = arouter;
	}
	return routes
}
createApp(App).use(routes()).use(store).mount('#app')