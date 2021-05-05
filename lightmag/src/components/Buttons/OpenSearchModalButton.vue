<template>
	<ion-button @click.prevent="openSearchModal">
		<ion-icon slot="icon-only" :icon="search"></ion-icon>
	</ion-button>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonButton, modalController, IonIcon} from '@ionic/vue';
	import {search} from 'ionicons/icons';
	import SearchModal from '../Search/SearchModal.vue';

	export default defineComponent({
		name: "openSearchModalButton",
		components:{
			IonButton,
			IonIcon
		},
		setup(){
			async function openSearchModal(){
				const search_modal = await modalController
				.create({
					component: SearchModal,
					componentProps:{
						swipeToClose: true
					}
				})
				return search_modal.present();
			}
			return{
				openSearchModal,
				search
			}
		}
	});
</script>