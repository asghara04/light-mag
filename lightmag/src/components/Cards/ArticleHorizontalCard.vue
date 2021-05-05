<template>
	<ion-card>
		<ion-row>
			<ion-col size="2.5" v-if="article.image" class="ion-no-padding">
				<ion-img :src="article.image.image" :alt="article.image.alt"></ion-img>
			</ion-col>
			<ion-col size="9.5" class="ion-text-capitalize">
				<user-item :user="article.author" class="ion-hide-md-down"></user-item>
				<ion-card-header>
					<ion-card-title>{{article.title}}</ion-card-title>
				</ion-card-header>
				<ion-card-content class="ion-hide-md-down">
					<p>{{article.description}}</p>
				</ion-card-content>
				<article-card-footer :comments="article.coms" :readTime="article.read_time_m"></article-card-footer>
			</ion-col>
		</ion-row>
	</ion-card>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonCard, IonRow, IonCol, IonImg, IonCardHeader, IonCardTitle, IonCardContent} from '@ionic/vue';
	import UserItem from '../Items/UserItem.vue';
	import ArticleCardFooter from '../Footer/ArticleCardFooter.vue';

	export default defineComponent({
		name: "ArticleHorizontalCard",
		props:{
			article:{
				type: Object,
				required: true
			}
		},
		components:{
			IonCard,
			IonRow,
			IonCol,
			IonImg,
			UserItem,
			IonCardHeader,
			IonCardTitle,
			IonCardContent,
			ArticleCardFooter
		}
	});
</script>