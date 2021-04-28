<template>
	<ion-buttons slot="end">
		<open-search-modal-button></open-search-modal-button>
		<menu-button menu-id="baseMenu"></menu-button>
	</ion-buttons>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonButtons} from '@ionic/vue';
	import OpenSearchModalButton from '../Buttons/OpenSearchModalButton.vue';
	import MenuButton from '../Buttons/MenuButton.vue';

	export default defineComponent({
		name: "EndBaseToolbar",
		components:{
			IonButtons,
			OpenSearchModalButton,
			MenuButton
		}
	});
</script>