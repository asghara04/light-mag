<template>
	<ion-buttons slot="start">
		<ion-back-button v-if="BackLink" :default-href="BackLink"></ion-back-button>
	</ion-buttons>
</template>
<script>
	import {defineComponent} from "vue";
	import {IonButtons, IonBackButton} from '@ionic/vue';

	export default defineComponent({
		name: "StartBaseToolbarButtons",
		props:{
			BackLink:{
				type: String,
				required: false
			},
		},
		components:{
			IonButtons,
			IonBackButton
		}
	});
</script>