<template>
	<ion-toolbar color="primary">
		<ion-title>
			<ion-icon src="assets/icon/lightmag.svg"></ion-icon>
			Light Magazine
		</ion-title>
		<ion-note color="medium" class="ion-margin ion-padding">Learning To gether :)</ion-note>
	</ion-toolbar>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonToolbar, IonTitle, IonIcon, IonNote} from '@ionic/vue';

	export default defineComponent({
		name: "BaseMenuToolbar",
		components:{
			IonToolbar,
			IonTitle,
			IonIcon,
			IonNote
		}
	});
</script>