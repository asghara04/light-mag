<template>
	<ion-content>
		<slot name="start"></slot>
		<!-- ion-item's with router-link are not clickable should add button, find better way -->
		<side-menu-base-list></side-menu-base-list>
		<side-menu-other-list></side-menu-other-list>
		<slot name="end"></slot>
	</ion-content>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonContent} from '@ionic/vue';
	import SideMenuBaseList from './SideMenuBaseList.vue';
	import SideMenuOtherList from './SideMenuOtherList.vue';

	export default defineComponent({
		name: "BaseSideMenuContent",
		components:{
			IonContent,
			SideMenuBaseList,
			SideMenuOtherList
		}
	});
</script>