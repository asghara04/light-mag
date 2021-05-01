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
	import {defineComponent,computed} from 'vue';

	import ArticleGrid from '@/components/Grids/ArticleGrid.vue';
	import PopularArticles from '@/components/Dynamic/PopularArticles.vue';
	import MainAndSidebar from '@/components/Base/MainAndSidebar.vue';

	import {useStore} from 'vuex';
	import {FETCH_ARTICLES} from '../store/actions.type.js';

	export default defineComponent({
		name: "HomePage",
		components:{
			PopularArticles,
			ArticleGrid,
			MainAndSidebar
		},
		setup(){
			const store = useStore();
			const articles = computed(()=>store.state.home.articles);

			store.dispatch(`home/${FETCH_ARTICLES}`);

			return{
				articles
			}
		}
	});
</script>