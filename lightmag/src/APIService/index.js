//---- base axios module ----
import axios from 'axios';

//---- instance simple changable configurations ----
import API_URL from './config.js';

/*
query => gets a list and can filter it by params like:
axios.get("/articles", {
	---- author: "raha" ----
	params: params
	---- and basicly it should return all the articles been writen by raha ----
})
*/
const APIServie = axios.create({
	baseURL: API_URL,
});

export default APIServie;