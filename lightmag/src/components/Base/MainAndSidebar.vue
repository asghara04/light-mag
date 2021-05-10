<template>
	<ion-grid class="ion-no-padding ion-no-margin">
		<ion-row>
			<ion-col size-xs="12" size-lg="10">
				<slot name="main"></slot>
			</ion-col>
			<ion-col class="ion-padding-horizontal" size-xs="12" size-lg="2">
				<slot name="sidebar">
					some long texts about emma sh watson
					some long texts about emma sh watson
					some long texts about emma sh watson
					some long texts about emma sh watson
					some long texts about emma sh watson
					some long texts about emma sh watson
					some long texts about emma sh watson
					some long texts about emma sh watson
					some long texts about emma sh watson
					some long texts about emma sh watson
					some long texts about emma sh watson
					some long texts about emma sh watson
					some long texts about emma sh watson
					some long texts about emma sh watson
					some long texts about emma sh watson
					<sidebar></sidebar>
				</slot>
			</ion-col>
		</ion-row>
	</ion-grid>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonGrid, IonRow, IonCol} from '@ionic/vue';
	import Sidebar from '../Sidebar/Sidebar.vue';

	export default defineComponent({
		name: "MainAndSidebar",
		components:{
			IonGrid,
			IonRow,
			IonCol,
			Sidebar
		}
	});
</script>