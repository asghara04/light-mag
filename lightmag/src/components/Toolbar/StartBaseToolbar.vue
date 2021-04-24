<template>
	<ion-buttons slot="start">
			<ion-menu-button menu="baseMenu"></ion-menu-button>
	</ion-buttons>
</template>
<script>
	import {defineComponent} from "vue";
	import {IonButtons, IonMenuButton} from '@ionic/vue';

	export default defineComponent({
		name: "StartBaseToolbarButtons",
		components:{
			IonButtons,
			IonMenuButton
		}
	});
</script>