<template>
	<!-- there should be an error component wich gets two or three properties and give an error right midlle of the page with icon and simple error expelenaition or meybe some time error code like 400 or 404 ,... -->
	<div v-if="error">
		{{error}}
	</div>
	<!--
		if there was a data before and getting new data got error then we should still show old data for ofline viewing so that how it works
	-->

	<div v-if="articles.length">
		<article-horizontal-card v-for="article in articles" :key="article.id" :article="article"></article-horizontal-card>

		<pagination :current="page" :module="module" :action="FETCH_ARTICLES"/>
	</div>
	<p v-else>
		sorry, there is nothing to show yet!
	</p>
</template>
<script>
	import {defineComponent, computed} from 'vue';
	import {useStore, mapGetters} from 'vuex';
	import {useRoute} from 'vue-router';
	import {FETCH_ARTICLES} from '@/store/actions.type.js';

	// components
	import ArticleHorizontalCard from '@/components/Cards/ArticleHorizontalCard.vue';
	import Pagination from '@/components/Pagination/Pagination.vue';

	export default defineComponent({
		name: "ArticleList",
		props:{
			module:{
				type: String,
				required: true,
				default: "home"
			},
			author:{
				type: Number,
				required: false
			},
			category:{
				type: Number,
				required: false
			},
			subcat:{
				type: Number,
				required: false
			},
			tag:{
				type: Number,
				required: false
			},
			q:{
				type: String,
				required: false
			}
		},
		components:{
			ArticleHorizontalCard,
			Pagination
		},
		computed:{
			...mapGetters("home", ["articles", "error"])
		},
		setup(props){
			const store = useStore();
			const route = useRoute();
			const page = computed(()=>parseInt(route.query.page)||1);

			store.dispatch(`${props.module}/${FETCH_ARTICLES}`, page.value);

			return{
				FETCH_ARTICLES,
				page
			}
		}
	});
</script>