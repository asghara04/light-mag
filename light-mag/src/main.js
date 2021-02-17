import { createApp } from 'vue';
import App from './App.vue';
//contation for using wich route!
import router from '@/router/index.js';
import store from '@/store.js'

createApp(App).use(router).use(store).mount('#app')
