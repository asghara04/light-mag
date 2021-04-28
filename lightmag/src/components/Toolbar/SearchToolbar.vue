<template>
	<ion-toolbar color="primary">
		<searchbar status="never"></searchbar>

		<ion-buttons slot="end">
			<close-modal-button></close-modal-button>
		</ion-buttons>
	</ion-toolbar>
</template>
<script>
	import {defineComponent} from 'vue';
	import CloseModalButton from '../Buttons/CloseModalButton.vue';
	import {IonToolbar, IonButtons} from '@ionic/vue';
	import Searchbar from '../Search/Searchbar.vue';

	export default defineComponent({
		name: "SearchToolbar",
		components:{
			IonToolbar,
			IonButtons,
			Searchbar,
			CloseModalButton
		}
	});
</script>