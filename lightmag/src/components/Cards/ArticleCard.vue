<template>
	<ion-card>
		<ion-img :src="article.image.image" :alt="article.image.alt"></ion-img>
		<ion-card-header>
			<ion-card-title>{{article.title}}</ion-card-title>
		</ion-card-header>
		<ion-card-content>
			<p>{{article.decsription}}</p>
		</ion-card-content>
		<ion-footer>
			<ion-row>
				<ion-col>
					comments
					{{article.coms}}
				</ion-col>
				<ion-col>
					date
					{{article.publish_date}}
				</ion-col>
				<ion-col>
					read_time
					{{article.read_time_m}}
				</ion-col>
			</ion-row>
		</ion-footer>
	</ion-card>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonCard, IonImg, IonCardHeader, IonCardTitle, IonCardContent, IonFooter, IonRow, IonCol} from '@ionic/vue';

	export default defineComponent({
		name: "ArticleCard",
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
			IonCardTitle,
			IonCardContent,
			IonFooter,
			IonRow,
			IonCol
		}
	});
</script>