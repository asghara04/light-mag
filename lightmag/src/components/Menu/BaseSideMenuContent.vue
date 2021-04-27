<template>
	<ion-content>
		<!-- side menu content start slot -->
		<slot name="start"></slot>

		<!-- side menu base content -->
		<side-menu-base-list></side-menu-base-list>
		<side-menu-other-list></side-menu-other-list>

		<!-- side menu content end slot -->
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