<template>
	<ion-header>
		<base-toolbar :PageTitle="PageTitle" :BackLink="BackLink"></base-toolbar>
	</ion-header>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonHeader} from '@ionic/vue';
	import BaseToolbar from '../Toolbar/BaseToolbar.vue';
	export default defineComponent({
		name: "BaseHeader",
		props: ["PageTitle", "BackLink"],
		components:{
			IonHeader,
			BaseToolbar
		}
	});
</script>