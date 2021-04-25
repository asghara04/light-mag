<template>
	<ion-toolbar>
		<ion-title>Search in Light Mag</ion-title>
		<ion-buttons slot="end">
			<close-modal-button></close-modal-button>
		</ion-buttons>
	</ion-toolbar>
</template>
<script>
	import {defineComponent} from 'vue';
	import CloseModalButton from '../Buttons/CloseModalButton.vue';
	import {IonToolbar, IonTitle, IonButtons} from '@ionic/vue';

	export default defineComponent({
		name: "SearchToolbar",
		components:{
			IonToolbar,
			IonTitle,
			IonButtons,
			CloseModalButton
		}
	});
</script>