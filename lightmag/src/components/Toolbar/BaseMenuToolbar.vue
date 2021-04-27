<template>
	<ion-toolbar>
		<ion-title>Light Magazine</ion-title>
		<ion-note class="ion-margin" mode='ios'>Learning To gether :)</ion-note>
	</ion-toolbar>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonToolbar, IonTitle, IonNote} from '@ionic/vue';

	export default defineComponent({
		name: "BaseMenuToolbar",
		components:{
			IonToolbar,
			IonTitle,
			IonNote
		}
	});
</script>