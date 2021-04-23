<template>
	<ion-header>
		<base-toolbar :PageTitle="PageTitle"></base-toolbar>
	</ion-header>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonHeader} from '@ionic/vue';
	import BaseToolbar from './BaseToolbar.vue';
	export default defineComponent({
		name: "BaseHeader",
		props: ["PageTitle"],
		components:{
			IonHeader,
			BaseToolbar
		}
	});
</script>