<template>
	<ion-page>
		<base-header :PageTitle="PageTitle"></base-header>
		<base-side-menu></base-side-menu>
		<ion-content>
			<slot name="main-content"></slot>
		</ion-content>
	</ion-page>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonPage, IonContent} from '@ionic/vue';
	import BaseHeader from '../Header/BaseHeader.vue';
	import BaseSideMenu from '../Menu/BaseSideMenu.vue';

	export default defineComponent({
		name: "BaseLayout",
		props: ["PageTitle"],
		components:{
			IonPage,
			BaseHeader,
			IonContent,
			BaseSideMenu
		}
	});
</script>