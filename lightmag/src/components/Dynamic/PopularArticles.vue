<template>
	<slot name="content">
		<styled-article-grid :data="articles"></styled-article-grid>
	</slot>
</template>
<script>
	import {defineComponent,ref,computed} from 'vue';
	import requester from '@/axios/requester.js';
	import StyledArticleGrid from '../Grids/StyledArticleGrid.vue';

	export default defineComponent({
		name: "PopularArticles",
		components:{
			StyledArticleGrid
		},
		setup(){
			const data = ref(false);
			const articles = computed(()=>data.value);

			(async function(){
				try{
					const res = await requester.get("articles/most/api/v1/comment/");
					data.value = res.data;
				}catch(err){
					// now should somthing happen to the err like alerting it
				}
			})();

			return{
				articles
			}
		}
	});
</script>