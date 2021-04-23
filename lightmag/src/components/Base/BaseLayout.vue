<template>
	<ion-page>
		<base-header :PageTitle="PageTitle"></base-header>
	</ion-page>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonPage} from '@ionic/vue';
	import BaseHeader from '../Header/BaseHeader.vue';
	export default defineComponent({
		name: "BaseLayout",
		props: ["PageTitle"],
		components:{
			IonPage,
			BaseHeader
		}
	});
</script>