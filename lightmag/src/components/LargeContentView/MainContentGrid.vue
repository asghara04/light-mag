<template>
	<ion-grid v-if="data">
		<ion-row>
			<ion-col size-md="5" size-xs="12">
				<ion-card>
					<ion-img :src="data[0].image.image" :alt="data[0].image.alt" :name="data[0].image.name"></ion-img>
					<ion-card-header>
						<ion-card-title>{{data[0].title}}</ion-card-title>
						<ion-note>{{data[0].}}</ion-note>
					</ion-card-header>
					<ion-card-cntent>
						<p class="ion-margin">{{data[0].description}}</p>
					</ion-card-cntent>
					<ion-footer>
						<ion-icon :icon="clock"></ion-icon>

					</ion-footer>
				</ion-card>
			</ion-col>
			<ion-col size-md="6" size-xs="12" v-for="article in data" :key="article.id">
				<ion-card>
					<ion-card-header>
						<ion-card-title>{{article.title}}</ion-card-title>
					</ion-card-header>
					<ion-card-content>
						<p>{{article.description}}</p>
					</ion-card-content>
				</ion-card>
			</ion-col>
		</ion-row>
	</ion-grid>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonGrid, IonRow, IonCol, IonCard, IonCardHeader, IonCardTitle, IonCardContent} from '@ionic/vue';

	export default defineComponent({
		name: "MainContentGrid",
		components:{
			IonGrid,
			IonRow,
			IonCol,
			IonCard,
			IonCardHeader,
			IonCardTitle,
			IonCardContent
		},
		props:{
			data:{
				required: true
			}
		}
	});
</script>