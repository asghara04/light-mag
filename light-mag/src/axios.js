import axios from 'axios';
import store from '@/store.js';
import router from '@/router/index.js';
// const base_url = 'https://ubuntuarchpaperfriendspals-lightmag.ir/';
const base_url = 'http://127.0.0.1:8000/';
const getAPI = axios.create({
	baseURL: base_url
})
getAPI.interceptors.response.use((res)=>{return res;},(err)=>{
	if(err.config&&err.response&&err.response.status===401){
		store.dispatch("RefreshToken")
	}else if(err.response&&err.response.status===404){
		alert("صفحه مورد نظر پیدا نشد.");
		router.push("/");
	}
	return Promise.reject(err);
})
const axiosBase = axios.create({
	baseURL: base_url,
	headers: {'content-type': 'application/json'}
})

export {getAPI, axiosBase}