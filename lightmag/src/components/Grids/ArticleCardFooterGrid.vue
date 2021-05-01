<template>
	<ion-grid>
		<ion-row>
			<ion-col size-sm="6" size-xs="12" class="ion-text-center">
					<ion-note>
						<ion-icon :icon="chatbubbles"></ion-icon>
							<p>{{comments}} comment</p>
					</ion-note>
			</ion-col>
			<ion-col size-sm="6" size-xs="12" class="ion-text-center">
					<ion-note>
						<ion-icon :icon="time"></ion-icon>
							<p>{{readTime}} min read</p>
					</ion-note>
			</ion-col>
		</ion-row>
	</ion-grid>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonGrid, IonRow, IonCol, IonIcon, IonNote} from '@ionic/vue';
	import {chatbubbles, time} from 'ionicons/icons';

	export default defineComponent({
		name: "ArticleCardFooterGrid",
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
			IonGrid,
			IonRow,
			IonCol,
			IonIcon,
			IonNote
		},
		setup(){
			return{
				chatbubbles,
				time
			}
		}
	});
</script>