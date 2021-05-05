<template>
	<ion-toolbar color="primary">
		<start-base-toolbar :BackLink="BackLink"></start-base-toolbar>

		<ion-title>
			<ion-icon src="assets/icon/lightmag.svg"></ion-icon>
			Light Mag
		</ion-title>

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
		props:{
			BackLink:{
				type: String,
				required: false,
			}
		},
		components:{
			IonToolbar,
			StartBaseToolbar,
			IonTitle,
			IonIcon,
			EndBaseToolbar
		}
	});
</script>