import {createStore} from 'vuex';
import {axiosBase} from './axios.js';

const store = createStore({
	state:{
		APIData: '',
		accessToken: localStorage.getItem('access_token')||null,
		refreshToken: localStorage.getItem('refresh_token')||null,
		loged: false
	},
	getters:{
		logedIn(state){
			return state.loged;
		},
		Access(state){
			return state.accessToken;
		},
		Refresh(state){
			return state.refreshToken;
		}
	},
	mutations:{
		updateLocalStorage(state, {access, refresh}){
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
		},
		updateLoged(state, r){
			state.loged = r||false;
		}
	},
	actions:{
		RefreshToken({commit,getters,dispatch}){
			return new Promise((resolve, reject)=>{
				axiosBase.post("/users/auth/refresh_token/", {token: getters.refreshToken})
				.then(response => {
					console.log("new access successfully created.")
					commit("updateAccess", response.data.token)
					resolve(response)
				})
				.catch(err => {
					dispatch("logoutUser");
					reject(err);
				})
			})
		},
		loginUser({commit}, credentials){
			return new Promise((resolve, reject)=> {
				axiosBase.post("users/auth/obtain_token/", {
					email: credentials.email,
					password: credentials.password
				})
				.then(response => {
					commit("updateLocalStorage", {access: response.data.token, refresh: response.data.token});
					commit("updateLoged",true);
					resolve(response);
				})
				.catch(err => {
					reject(err)
				})
			})
		},
		logoutUser({commit,getters}){
			if(getters.logedIn){
				return new Promise((resolve, reject)=> {
					axiosBase.post("rest_auth/mapi/")//bug!'fix it later, its easy.'
					.then(res=>{
						localStorage.removeItem('access_token');
						localStorage.removeItem('refresh_token');
						commit("destroyToken");
						window.location.reload();
						resolve(res);
					})
					.catch(err=>{
						localStorage.removeItem("access_token");
						localStorage.removeItem("refresh_token");
						commit("destroyToken");
						window.location.reload();
						reject(err);
					})
					.finalli(()=>{
						commit("updateLoged",false);
					})
				})
			}
		},
		isUser({commit,getters}){
			if(getters.Access){
				return new Promise((resolve,reject)=>{
					axiosBase.post("users/auth/verify_token/",{token: getters.Access,})
					.then(res=>{
						commit('updateLoged',true);
						resolve(res);
					})
					.catch(err=>{
						console.log(err);
						console.log(err.response);
						commit('updateLoged',false);
						reject(err);
					})
				})
			}else{
				commit('updateLoged',false);
			}
		}
	}
})

export default store