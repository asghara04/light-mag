<template>
	<ion-grid class="ion-grid-no-padding-md-sm-xs-screen" v-if="data">
		<ion-row>
			<ion-col class="ion-col-full-height" size-md="5" size-xs="12">
				<article-large-card :article="data[0]"></article-large-card>
			</ion-col>
			<ion-col class="ion-col-full-height" size-md="7" size-xs="12">
				<article-small-item-card :articles="data.slice(1,)"></article-small-item-card>
			</ion-col>
		</ion-row>
	</ion-grid>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonGrid, IonRow, IonCol} from '@ionic/vue';
	import ArticleSmallItemCard from '../Cards/ArticleSmallItemCard.vue';
	import ArticleLargeCard from '../Cards/ArticleLargeCard.vue';

	export default defineComponent({
		name: "StyledArticleGrid",
		components:{
			IonGrid,
			IonRow,
			IonCol,
			ArticleLargeCard,
			ArticleSmallItemCard
		},
		props:{
			data:{
				required: true
			}
		}
	});
</script>