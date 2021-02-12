import Vue from 'vue';
import Vuex from 'vuex';
import {axiosBase} from './axios.js';

Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		APIData: '',
		accessToken: localStorage.getItem('access_token') || null,
		refreshToken: localStorage.getItem("refresh_token") || null
	},
	getters:{
		logedIn(state){
			return state.accessToken != null
		}
	},
	mutations: {
		updateLcalStorage(state, {access, refresh}){
			localStorage.setItem("access_token", access)
			localStorage.setItem("refresh_token", refresh)
			state.accessToken = access
			state.refreshToken = refresh
		},
		updateAccess(state, access){
			state.accessToken = access
		},
		destroyToken(state){
			state.accessToken = null
			state.refreshToken = null
		}
	},
	actions: {
		refreshToken(context){
			return new Promise((resolve, reject) => {
				axiosBase.post("/users/auth/refresh_token/", {
					token: context.state.refreshToken
				})
				.then(response => {
					console.log("new access token suuccessfully generated")
					context.commit("updateAccess", response.data.token)
					resolve(response)
				})
				.catch(err => {
					console.log("error in refresh token request")
					reject(err)
				})
			})
		},
		logoutUser(context){
			if(context.getters.loggedIn){
				return new Promise((resolve, reject) => {
					axiosBase.post("rest_auth/mapi/")
					.then(response => {
						localStorage.removeItem("access_token")
						localStorage.removeItem("refresh_token")
						context.commit("destroyToken")
						resolve(response)
					})
					.catch(err => {
						localStorage.removeItem("access_token")
						localStorage.removeItem("refresh_token")
						context.commit("destroyToken")
						reject(err)
					})
				})
			}
		},
		loginUser(context, credentials){
			return new Promise((resolve, reject) => {
				axiosBase.post("users/auth/obtain_token/login", {
					email: credentials.email,
					password: credentials.password
				})
				.then(response => {
					context.commit("updateLcalStorage", {access: response.data.token, refresh: resolve.data.token})
					resolve()
				})
				.catch(err => {
					reject(err)
				})
			})
		}
	}

})