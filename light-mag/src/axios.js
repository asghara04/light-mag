import axios from 'axios';
import store from './store.js';
const base_url = 'http://127.0.0.1:8000/';

const getAPI = axios.create({
	baseURL: base_url
})
getAPI.interceptors.response.use(undefined, function (err){
	if(err.config&&err.response&&err.response.data===401){
		store.dispatch("refreshToken")
		.then(access=>{
			axios.request({
				baseURL: base_url,
				method: 'get',
				headers: {Authorization: `{JWT ${access}}`},
				url: 'users/mapi/v1'
			})
			.then(res => {
				console.log("login was successfully");
				store.state.APIData = res.data;
			})
			.catch(err => {
				console.log("ERR!");
				return Promise.reject(err)
			})
		})
		.catch(err=>{
			return Promise.reject(err)
		})
	}
})

const axiosBase = axios.create({
	baseURL: base_url,
	headers: {contentType: "application/json"}
})

export {getAPI, axiosBase}