<template>
	<base-layout>
		<template v-slot:main-content>
			<popular-articles></popular-articles>
			<main-and-sidebar>
				<template v-slot:main>
					<article-grid v-if="articles" :articles="articles"></article-grid>
				</template>
			</main-and-sidebar>
		</template>
	</base-layout>
</template>
<script>
	import {defineComponent,ref,computed} from 'vue';
	import ArticleServices from '@/APIService/articles/ArticleServices.js';
	import ArticleGrid from '@/components/Grids/ArticleGrid.vue';
	import PopularArticles from '@/components/Dynamic/PopularArticles.vue';
	import MainAndSidebar from '@/components/Base/MainAndSidebar.vue';

	export default defineComponent({
		name: "HomePage",
		components:{
			PopularArticles,
			ArticleGrid,
			MainAndSidebar
		},
		setup(){
			const data = ref(null);
			const articles = computed(()=>data.value);

			(async function(){
				try{
					const res = await ArticleServices.query();
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