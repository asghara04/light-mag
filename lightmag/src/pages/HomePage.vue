<template>
	<base-layout>
		<template v-slot:main-content>
			<ion-grid>
				<ion-row>
					<ion-col size-xs="12" size-lg="6">
						<ion-card color="secondary" desabled="true">

							<ion-img src="../../public/assets/icon/favicon.png" alt="not found"></ion-img>

							<ion-card-title>title</ion-card-title>
							<ion-card-subtitle>subtitle</ion-card-subtitle>

							<ion-card-content>
								Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
								tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
								quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
								consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
								cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
								proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
							</ion-card-content>
						</ion-card>
					</ion-col>
					<ion-col size-xs="12" size-lg="6">
						<ion-card>
							<ion-item href="#">
								<ion-icon slot="start" :icon="map"></ion-icon>
								<ion-label>ion icon in a card. icon in start. button in end</ion-label>
								<ion-button fill="outline" slot="end">More...</ion-button>
							</ion-item>

							<ion-card-content>this the content without any paragraph or header tag</ion-card-content>
						</ion-card>

						<ion-card>
							<ion-item href="#" class="ion-activated">
								<ion-icon :icon="wifi" slot='start'></ion-icon>
								<ion-label>your wifi is off now</ion-label>
							</ion-item>

							<ion-item>
								<ion-icon :icon="wine" slot="start"></ion-icon>
								<ion-label>card item 2</ion-label>
							</ion-item>

							<ion-item class="ion-activated">
								<ion-icon :icon="wine" slot="start"></ion-icon>
								<ion-label>card item 2</ion-label>
							</ion-item>
						</ion-card>
					</ion-col>
				</ion-row>
			</ion-grid>
			<ion-grid>
				<ion-row >
					<ion-col size-xs="12" size-lg="10">
						<div>
							main-content
						</div>
					</ion-col>
					<ion-col size-xs="12" size-lg="2">
						<div>
							sidebar
						</div>
					</ion-col>
				</ion-row>
			</ion-grid>
		</template>
	</base-layout>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonGrid, IonRow, IonCol, IonCard, IonItem, IonCardSubtitle, IonCardTitle, IonCardContent, IonIcon, IonLabel, IonImg, IonButton} from '@ionic/vue';
	import {map, wifi, wine} from 'ionicons/icons';
	export default defineComponent({
		name: "HomePage",
		components:{
			IonGrid,
			IonRow,
			IonCol,
			IonCard,
			IonCardSubtitle,
			IonCardTitle,
			IonCardContent,
			IonIcon,
			IonItem,
			IonLabel,
			IonImg,
			IonButton
		},
		setup(){
			return{
				map,
				wifi,
				wine
			}
		}
	});
</script>