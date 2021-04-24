<template>
	<ion-toolbar>
		<ion-buttons :collapse="true" slot="start">
			<ion-button>
				<ion-icon slot="icon-only" :icon="menu"></ion-icon>
			</ion-button>
		</ion-buttons>
		<ion-title>
			LM Light Mag
		</ion-title>
		<ion-img></ion-img>
		<ion-title v-if="PageTitle" size="small">{{PageTitle}}</ion-title>
		<ion-buttons :collapse="true" slot="end">
			<ion-button>
				<ion-icon slot="icon-only" :icon="search"></ion-icon>
			</ion-button>
		</ion-buttons>
	</ion-toolbar>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonToolbar, IonTitle, IonButtons, IonButton, IonIcon, IonImg} from '@ionic/vue';
	import {menu, search} from 'ionicons/icons';

	export default defineComponent({
		name: "BaseToolbar",
		props: ["PageTitle"],
		components:{
			IonToolbar,
			IonTitle,
			IonButtons,
			IonButton,
			IonIcon,
			IonImg
		},
		setup(){
			return{
				menu,
				search
			}
		}
	});
</script>