import axios from 'axios';
import store from './store';

const base_url = "http://127.0.0.1:8000/";

const axiosBase = axios.create({
	baseURL: base_url,
	headers: {contentType: 'application/json'}
})



const getAPI = axios.create({
	baseURL: base_url
})
getAPI.interceptors.response.use(undefined, function (err){
	//if error response status is 401, it means the request was invalid due to expired access token
	if (err.config && err.response && err.response.status === 401){
		store.dispatch("refreshToken")// attempt to obtain new access token by runing refreshToken action
		.then(access => {
			//if successfully resend the request to get the data from server
			axios.request({
				baseURL: base_url,
				method: "get",
				headers: {Authorization: `JWT ${access}`},//new access token in header now
				url: 'users/mapi/v1'
			})
			.then(response => {
				console.log("getting the mods done successfully.")
				store.state.APIData = response.data
			})
			.catch(err => {
				console.log("ERR")
				return Promise.reject(err)
			})
		})
		.catch(err => {
			return Promise.reject(err)
		})

	}
})


export {axiosBase, getAPI}