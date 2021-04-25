<template>
	<ion-button @click.prevent="modalController.dismiss()">
		<ion-icon slot="icon-only" :icon="close"></ion-icon>
	</ion-button>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonButton ,modalController, IonIcon} from '@ionic/vue';
	import {close} from 'ionicons/icons';

	export default defineComponent({
		name: "CloseModalButton",
		components:{
			IonButton,
			IonIcon
		},
		setup(){
			return{
				modalController,
				close
			}
		}
	});
</script>