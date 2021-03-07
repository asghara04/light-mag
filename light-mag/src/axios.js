import axios from 'axios';
import router from '@/router/index.js';
import store from '@/store.js'
const base_url = 'http://127.0.0.1:8000/';
const getAPI = axios.create({
	baseURL: base_url
})
getAPI.interceptors.response.use((res)=>{return res;},(err)=>{
	if(err.config&&err.response&&err.response.status===404){
		router.push({name: "not_found"});
	}else if(err.config&&err.response&&err.response.status===401){
		store.dispatch("RefreshToken")
	}
	return Promise.reject(err);
})
const axiosBase = axios.create({
	baseURL: base_url,
	headers: {'content-type': 'application/json'}
})

export {getAPI, axiosBase}