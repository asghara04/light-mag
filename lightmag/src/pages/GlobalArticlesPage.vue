<template>
	<main-and-sidebar>
		<template v-slot:main>
			<article-list module="home"></article-list>
		</template>
	</main-and-sidebar>
</template>
<script>
	import {defineComponent} from 'vue';
	import MainAndSidebar from '@/components/Base/MainAndSidebar.vue';
	import ArticleList from '@/components/Lists/ArticleList.vue';

	export default defineComponent({
		name: "GlobalArticles",
		components:{
			ArticleList,
			MainAndSidebar
		}
	});	
</script>