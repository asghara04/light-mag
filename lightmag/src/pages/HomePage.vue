<template>
	<base-layout>
		<template v-slot:main-content>
			<!-- <popular-articles></popular-articles> -->

			<main-and-sidebar>
				<template v-slot:main>
					<article-list module="home"></article-list>
				</template>
			</main-and-sidebar>
		
		</template>
		<!-- an ion-router-outlet or router-view or somthing for home children -->
	</base-layout>
</template>
<script>
	import {defineComponent} from 'vue';
	import MainAndSidebar from '@/components/Base/MainAndSidebar.vue';
	import ArticleList from '@/components/Lists/ArticleList.vue';
	// import PopularArticles from '@/components/Dynamic/PopularArticles.vue';

	export default defineComponent({
		name: "HomePage",
		components:{
			// PopularArticles,
			ArticleList,
			MainAndSidebar
		}
	});
</script>