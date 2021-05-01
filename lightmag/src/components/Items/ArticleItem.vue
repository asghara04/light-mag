<template>
	<ion-item lines="full" v-if="article">
		<ion-thumbnail slot="start" v-if="article.image">
			<ion-img v-if="article.image" :src="article.image.image" :alt="article.image.alt"></ion-img>
		</ion-thumbnail>
		<ion-label>
			<h2>{{article.title}}</h2>
			<article-card-footer-grid :comments="article.coms" :readTime="article.read_time_m"></article-card-footer-grid>
		</ion-label>
	</ion-item>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonItem, IonThumbnail, IonImg, IonLabel} from '@ionic/vue';
	import ArticleCardFooterGrid from '../Grids/ArticleCardFooterGrid.vue';

	export default defineComponent({
		name: "ArticleItem",
		props:{
			article:{
				required: true
			}
		},
		components:{
			IonItem,
			IonThumbnail,
			IonImg,
			IonLabel,
			ArticleCardFooterGrid
		}
	});
</script>