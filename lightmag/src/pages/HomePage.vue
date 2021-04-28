<template>
	<base-layout>
		<template v-slot:main-content>
			<popular-articles></popular-articles>
			<article-grid v-if="articles" :articles="articles"></article-grid>
		</template>
	</base-layout>
</template>
<script>
	import {defineComponent,ref,computed} from 'vue';
	import requester from '@/axios/requester.js';
	import ArticleGrid from '@/components/Grids/ArticleGrid.vue';
	import PopularArticles from '@/components/Dynamic/PopularArticles.vue';

	export default defineComponent({
		name: "HomePage",
		components:{
			PopularArticles,
			ArticleGrid
		},
		setup(){
			const data = ref(null);
			const articles = computed(()=>data.value);

			(async function(){
				try{
					const res = await requester.get("articles/api/v1/");
					data.value = res.data.results;
				}catch(err){
					// somthing shall happen to err like alert
				}
			})();

			return{
				articles
			}
		}
	});
</script>