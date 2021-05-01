<template>
	<ion-grid>
		<ion-row>
			<ion-col size-xs="12" size-lg="10">
				<slot name="main"></slot>
			</ion-col>
			<ion-col size-xs="12" size-lg="2">
				<slot name="sidebar">
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