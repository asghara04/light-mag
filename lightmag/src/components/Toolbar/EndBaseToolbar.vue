<template>
	<ion-buttons slot="end">
		<open-search-modal-button></open-search-modal-button>
		<ion-menu-button menu="baseMenu"></ion-menu-button>
	</ion-buttons>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonButtons, IonMenuButton} from '@ionic/vue';
	import OpenSearchModalButton from '../Buttons/OpenSearchModalButton.vue';

	export default defineComponent({
		name: "EndBaseToolbar",
		components:{
			IonButtons,
			OpenSearchModalButton,
			IonMenuButton
		},
	});
</script>