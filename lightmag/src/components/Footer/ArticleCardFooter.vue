<template>
	<ion-footer>
		<article-card-footer-grid v-bind="$props"></article-card-footer-grid>
	</ion-footer>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonFooter} from '@ionic/vue';
	import ArticleCardFooterGrid from '../Grids/ArticleCardFooterGrid.vue';

	export default defineComponent({
		name: "ArticleCardFooter",
		props:{
			comments:{
				type: Number,
				required: true,
				default: 0
			},
			readTime:{
				type: Number,
				required: true,
				default: 0
			}
		},
		components:{
			IonFooter,
			ArticleCardFooterGrid
		}
	});
</script>