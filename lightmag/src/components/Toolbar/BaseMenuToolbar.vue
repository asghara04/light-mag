<template>
	<ion-toolbar>
		<ion-title size="large">LM</ion-title>
		<ion-title>Light Magazine</ion-title>
	</ion-toolbar>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonToolbar, IonTitle} from '@ionic/vue';

	export default defineComponent({
		name: "BaseMenuToolbar",
		components:{
			IonToolbar,
			IonTitle
		}
	});
</script>