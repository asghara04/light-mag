/*
	* probebly later i need to add "next" and "previous" data states to the state for pagination
*/

// action name values
import {
	FETCH_ARTICLES
} from '../actions.type.js';

// mutation name values
import {
	SET_ARTICLES,
	SET_ERROR
} from '../mutations.type.js';

// article api services
import ArticleServices from '../../APIService/articles/ArticleServices.js';


// name space allows to use same action,mutation,getter name in difrent modules in store
const namespaced = true;

const state = {
	articles: [],

	// holds all articles count
	articlesCount: 0,

	// holds store module error
	error: null
}

const getters = {
	articles(state){
		return state.articles;
	},
	articlesCount(state){
		return state.articlesCount;
	},
	error(state){
		return state.error;
	}
}

const mutations = {
	// setting articles and their count to the states
	[SET_ARTICLES](state, data){
		state.articles = data.results;
		state.articlesCount = data.count;
	},
	[SET_ERROR](state, err){
		state.error = err;
	}
}

const actions = {
	// commit its in context(self in python :))
	[FETCH_ARTICLES]({ commit }, ){
		return ArticleServices.query()
		.then(res => {
			commit(SET_ARTICLES, res.data);
		})
		.catch(err => {
			commit(SET_ERROR, err);
		})
	}
}

export default {
	namespaced,
	state,
	getters,
	mutations,
	actions,
}