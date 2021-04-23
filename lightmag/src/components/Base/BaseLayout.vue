<template>
	<ion-page>
		<base-header :PageTitle="PageTitle"></base-header>
		<ion-content class="ion-padding">
			<slot name="main-content"></slot>
		</ion-content>
	</ion-page>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonPage, IonContent} from '@ionic/vue';
	import BaseHeader from '../Header/BaseHeader.vue';
	export default defineComponent({
		name: "BaseLayout",
		props: ["PageTitle"],
		components:{
			IonPage,
			BaseHeader,
			IonContent
		}
	});
</script>