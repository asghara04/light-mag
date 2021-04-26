<template>
	<ion-header>
		<base-menu-toolbar></base-menu-toolbar>
	</ion-header>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonHeader} from '@ionic/vue';
	import BaseMenuToolbar from '../Toolbar/BaseMenuToolbar.vue';

	export default defineComponent({
		name: "BaseMenuHeader",
		components:{
			IonHeader,
			BaseMenuToolbar,
		}
	});
</script>