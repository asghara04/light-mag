<template>
	<ion-buttons slot="end">
		<open-search-modal-button></open-search-modal-button>
	</ion-buttons>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonButtons} from '@ionic/vue';
	import OpenSearchModalButton from '../Buttons/OpenSearchModalButton.vue';

	export default defineComponent({
		name: "EndBaseToolbar",
		components:{
			IonButtons,
			OpenSearchModalButton
		},
	});
</script>