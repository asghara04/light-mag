<template>
	<ion-card>
		<ion-img :src="article.image.image" :alt="article.image.alt"></ion-img>
		<ion-card-header>
			<ion-card-title>{{article.title}}</ion-card-title>
		</ion-card-header>
		<ion-card-content>
			<p>{{article.description}}</p>
		</ion-card-content>
	</ion-card>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonCard, IonImg, IonCardHeader, IonCardContent, IonCardTitle} from '@ionic/vue';

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
			IonCardTitle
		}
	});
</script>