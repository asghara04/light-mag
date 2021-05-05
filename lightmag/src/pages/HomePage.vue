<template>
	<base-layout>
		<template v-slot:main-content>
			<most-commented-articles-slider/>

			<main-and-sidebar>
				<template v-slot:main>
					<article-list module="home"></article-list>
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

	export default defineComponent({
		name: "HomePage",
		components:{
			MostCommentedArticlesSlider,
			ArticleList,
			MainAndSidebar
		}
	});
</script>