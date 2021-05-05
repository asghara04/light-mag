import {
	FETCH_ARTICLES
} from '../actions.type.js';

import {
	SET_ARTICLES
} from '../mutations.type.js';

import ArticleServices from '@/APIService/articles/ArticleServices.js';

const state = {
	articles: []
}

const getters = {
	articles(state){
		return state.articles;
	}
}

const mutations = {
	[SET_ARTICLES](state, data){
		state.articles = data;
	}
}

const actions = {
	[FETCH_ARTICLES]({commit}){
		return ArticleServices.MostCommented()
		.then((res) => {
			commit(SET_ARTICLES, res.data);
		})
	}
}

export default{
	state,
	getters,
	mutations,
	actions
}