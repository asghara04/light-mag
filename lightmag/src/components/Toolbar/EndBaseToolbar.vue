<template>
	<ion-buttons slot="end">
		<ion-button>
			<ion-icon slot="icon-only" :icon="search"></ion-icon>
		</ion-button>
	</ion-buttons>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonButtons, IonButton, IonIcon} from '@ionic/vue';
	import {search} from 'ionicons/icons';

	export default defineComponent({
		name: "EndBaseToolbar",
		components:{
			IonButtons,
			IonButton,
			IonIcon
		},
		setup(){
			return{
				search
			}
		}
	});
</script>