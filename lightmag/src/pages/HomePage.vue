<template>
	<base-layout>
		<template v-slot:main-content>
			<ion-refresher slot="fixed" @ion-refresh="doRefresh($event)">
				<ion-refresher-content
				:pulling-icon="refresh"
				pulling-text="pull to refresh"
				refreshing-spinner="crescent"
				refreshing-text="Refreshing..."
				></ion-refresher-content>
			</ion-refresher>
			<most-commented-articles-slider/>
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
	import {refresh} from 'ionicons/icons';

	export default defineComponent({
		name: "HomePage",
		components:{
			MostCommentedArticlesSlider,
			ArticleList,
			MainAndSidebar
		},
		setup(){
			const doRefresh = (event) => {
				console.log('Begin ASYNC.');
				console.log('some store actions.');
				console.log('and end.');
				alert("hi")
				event.target.complete();
			}

			return{
				doRefresh,
				refresh
			}
		}
	});
</script>