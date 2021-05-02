<template>
	<!-- there should be an error component wich gets two or three properties and give an error right midlle of the page with icon and simple error expelenaition or meybe some time error code like 400 or 404 ,... -->
	<div v-if="error">
		{{error}}
	</div>
	<!--
		if there was a data before and getting new data got error then we should still show old data for ofline viewing so that how it works
	-->
	<p v-if="articles.length">
		<!-- some for loop on a component or somthing! -->
		{{articles}}
	</p>
	<p v-else>
		sorry, there is nothing to show yet!
	</p>
</template>
<script>
	import {defineComponent} from 'vue';
	import {useStore, mapGetters} from 'vuex';

	import {FETCH_ARTICLES} from '@/store/actions.type.js';

	// an computed method should be on "module" property
	// computed data and store map getters
	// ---- pagination ----

	export default defineComponent({
		name: "ArticleList",
		props:{
			module:{
				type: String,
				required: true,
				default: "home"
			},
			author:{
				type: String,
				required: false
			},
			category:{
				type: String,
				required: false
			},
			subcat:{
				type: String,
				required: false
			},
			q:{
				type: String,
				required: false
			}
		},
		components:{

		},
		computed:{
			...mapGetters("home", ["articles", "error"])
		},
		setup(props){
			const store = useStore();

			/* **--important--:**
			 there should be an error data statement in each vuex module for handling each module errors its cleaner this way :) instead of this shit below
			*/

			store.dispatch(`${props.module}/${FETCH_ARTICLES}`);
		}
	});
</script>