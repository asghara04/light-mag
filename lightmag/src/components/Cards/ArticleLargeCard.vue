<template>
	<ion-card>
		<ion-img v-if="article.image" :src="article.image.image" :alt="article.image.alt"></ion-img>
		<ion-card-header>
			<ion-card-title>{{article.title}}</ion-card-title>
		</ion-card-header>
		<ion-card-content>
			<p>{{article.description}}</p>
		</ion-card-content>
		<article-card-footer :comments="article.coms" :readTime="article.read_time_m"></article-card-footer>
	</ion-card>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonCard, IonImg, IonCardHeader, IonCardContent, IonCardTitle} from '@ionic/vue';
	import ArticleCardFooter from '../Footer/ArticleCardFooter.vue';

	export default defineComponent({
		name: "ArticleLargeCard",
		props:{
			article:{
				required: true,
				type: Object
			}
		},
		components:{
			IonCard,
			IonImg,
			IonCardHeader,
			IonCardContent,
			IonCardTitle,
			ArticleCardFooter
		}
	});
</script>