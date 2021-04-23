<template>
	<ion-toolbar>
		<ion-buttons slot="start">
			<ion-button>
				<ion-icon slot="icon-only" name="menu-outline"></ion-icon>
			</ion-button>
		</ion-buttons>
		<ion-title>لایت مگ</ion-title>
		<ion-Title v-if="PageTitle" size="small">{{PageTitle}}</ion-Title>
		<ion-buttons slot="end">
			<ion-button>
				<ion-icon slot="icon-only" name="search-outline"></ion-icon>
			</ion-button>
		</ion-buttons>
	</ion-toolbar>
</template>
<script>
	import {IonToolbar, IonTitle, IonButtons, IonButton, IonIcon} from '@ionic/vue';

	export default{
		name: "BaseToolbar",
		props: ["PageTitle"],
		components:{
			IonToolbar,
			IonTitle,
			IonButtons,
			IonButton,
			IonIcon
		}
	};
</script>