import Vue from 'vue';
import App from './App.vue';
import router from './routes.js';
import store from './store.js';

Vue.config.productionTip = false


// router.beforeEach((to, from, next) => {
//   // if any of the routes in ./router.js has a meta named 'requiresAuth: true'
//   // then check if the user is logged in before routing to this path:
//   if (to.matched.some(record => record.meta.requiresAuth)) {
//     if (!store.getters.loggedIn) {
//       next({ name: 'login' })
//     } else {
//       next()
//     }
//   } else if (to.matched.some(record => record.meta.requiresLogged)) {
//     // else if any of the routes in ./router.js has a meta named 'requiresLogged: true'
//     // then check if the user is logged in; if true continue to home page else continue routing to the destination path
//     // this comes to play if the user is logged in and tries to access the login/register page
//     if (store.getters.loggedIn) {
//       next({ name: 'home' })
//     } else {
//       next()
//     }
//   } else {
//     next()
//   }
// })

new Vue({
	router,
	store,
	render: h => h(App),
}).$mount('#app')