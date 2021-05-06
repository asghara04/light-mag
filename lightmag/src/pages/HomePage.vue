<template>
	<base-layout>
		<template v-slot:main-content>
			<!-- page refsher -->
			<main-refresher module="home" :action="FETCH_ARTICLES"></main-refresher>

			<!-- most commented articles date -->
			<most-commented-articles-slider/>

			<!-- main page and sidebar -->
			<main-and-sidebar>
				<template #main>
					<article-list module='home'></article-list>
				</template>
			</main-and-sidebar>
		</template>
	</base-layout>
</template>
<script>
	import {defineComponent} from 'vue';
	import MainAndSidebar from '@/components/Base/MainAndSidebar.vue';
	import ArticleList from '@/components/Lists/ArticleList.vue';
	import MostCommentedArticlesSlider from '@/components/Sliders/MostCommentedArticlesSlider.vue';
	import MainRefresher from '@/components/Refresher/MainRefresher.vue';
	import {FETCH_ARTICLES} from '@/store/actions.type.js';

	export default defineComponent({
		name: "HomePage",
		components:{
			MostCommentedArticlesSlider,
			ArticleList,
			MainAndSidebar,
			MainRefresher
		},
		setup(){
			return{
				FETCH_ARTICLES
			}
		}
	});
</script>