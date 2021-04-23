import { createApp } from 'vue';
import App from './App.vue';
import store from '@/store.js';
import router from '@/router/index.js';
import arouter from '@/router/admin.js';
const parts = window.location.host.split(".");
function routes(){
	if(parts[0]==="admin"){
		return arouter;
	}
	return router
}
createApp(App).use(routes()).use(store).mount('#app')