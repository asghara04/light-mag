<template>
	<ion-row>
		<ion-col size="auto">
			<ion-item lines="none">
				<ion-icon size="small" :icon="chatbubbles"></ion-icon>
				<ion-label>{{comments}}</ion-label>
			</ion-item>
		</ion-col>
		<ion-col size="auto">
			<ion-item lines="none">
				<ion-icon size="small" :icon="time"></ion-icon>
				<ion-label>{{readTime}}min read</ion-label>
			</ion-item>
		</ion-col>
	</ion-row>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonRow, IonCol, IonItem, IonIcon, IonLabel} from '@ionic/vue';
	import {chatbubbles, time} from 'ionicons/icons';

	export default defineComponent({
		name: "ArticleCardFooter",
		props:{
			comments:{
				type: Number,
				required: false,
				default: 0
			},
			readTime:{
				type: Number,
				required: false,
				default: 3
			}
		},
		components:{
			IonRow,
			IonCol,
			IonItem,
			IonIcon,
			IonLabel
		},
		setup(){
			return{
				chatbubbles,
				time
			}
		}
	});
</script>