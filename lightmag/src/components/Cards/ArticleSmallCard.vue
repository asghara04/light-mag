<template>
	<ion-card class="ion-slide-main ion-text-capitalize">
		<ion-img v-if="article.image" style="pointer-events:none" :src="article.image.image"></ion-img>
		<ion-card-header>
			<ion-card-subtitle class="ion-text-start">{{article.author.name}}</ion-card-subtitle>
			<ion-card-title>{{article.title.substr(0,35)}}</ion-card-title>
		</ion-card-header>
		<article-card-footer :readTime="article.read_time_m" :comments="article.coms"></article-card-footer>
	</ion-card>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonCard, IonImg, IonCardHeader, IonCardSubtitle, IonCardTitle} from '@ionic/vue';
	import ArticleCardFooter from '../Footer/ArticleCardFooter.vue';

	export default defineComponent({
		name: "ArticleSmallCard",
		props:{
			article:{
				tpye: Object,
				required: true
			}
		},
		components:{
			IonCard,
			IonImg,
			IonCardHeader,
			IonCardSubtitle,
			IonCardTitle,
			ArticleCardFooter
		}
	});
</script>