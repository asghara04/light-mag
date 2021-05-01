import {createStore} from 'vuex';
import home from './home/module.js';

const store = createStore({
	// state handle the data: mutations
	// mutations change the data in state: commit
	// actions commits mutations and cannot chang data in state but can access: dispatch
	// getters get data from state


	// we can break our store to each seperate modules and state :)
	modules:{
		home
	}
});

export default store;