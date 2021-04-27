<template>
	<slot name="content">
		<main-content-grid :data="articles"></main-content-grid>
	</slot>
</template>
<script>
	import {defineComponent,ref} from 'vue';
	import requester from '@/axios/requester.js';
	import MainContentGrid from '../LargeContentView/MainContentGrid.vue';

	export default defineComponent({
		name: "PopularArticles",
		components:{
			MainContentGrid
		},
		setup(){
			/* fetching data methods and algorithm should be refactor */
			/* fetching data methods and algorithm should be refactor */
			/* fetching data methods and algorithm should be refactor */
			const articles = ref(null);
			(async function(){
				const res = await requester.get("articles/most/api/v1/comment/");
				articles.value = res.data;
			})();

			return{
				articles
			}
		}
	});
</script>