<template>
	<ion-toolbar>
		<start-base-toolbar :BackLink="BackLink"></start-base-toolbar>
		
		<ion-title>
			<ion-icon src="assets/icon/lightmag.svg"></ion-icon>
			Light Mag
		</ion-title>
		<ion-title v-if="PageTitle" size="small">{{PageTitle}}</ion-title>

		<end-base-toolbar></end-base-toolbar>
	</ion-toolbar>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonToolbar, IonTitle, IonIcon} from '@ionic/vue';
	import StartBaseToolbar from './StartBaseToolbar.vue';
	import EndBaseToolbar from './EndBaseToolbar.vue';

	export default defineComponent({
		name: "BaseToolbar",
		props: ["PageTitle", "BackLink"],
		components:{
			IonToolbar,
			StartBaseToolbar,
			IonTitle,
			IonIcon,
			EndBaseToolbar
		}
	});
</script>