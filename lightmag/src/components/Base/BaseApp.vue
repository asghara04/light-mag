<template>
	<ion-split-pane content-id="baseMenu" disabled="true">

		<slot name="base-menu">
			<base-side-menu></base-side-menu>
		</slot>

		<ion-router-outlet id="baseMenu"></ion-router-outlet>
	</ion-split-pane>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonSplitPane, IonRouterOutlet} from '@ionic/vue';
	import BaseSideMenu from '../Menu/BaseSideMenu.vue';

	export default defineComponent({
		name: "BaseApp",
		components:{
			IonSplitPane,
			IonRouterOutlet,
			BaseSideMenu
		}
	});
</script>