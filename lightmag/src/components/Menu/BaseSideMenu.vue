<template>
	<ion-menu side="start" menu-id="baseMenu" content-id="main">
		<base-menu-header></base-menu-header>

		<!-- should be refactor when wanna use really -->
		<ion-content>
			<ion-list>
				<ion-item>Home Page</ion-item>
				<ion-item>Categories</ion-item>
				<ion-item>all categories with their subcats</ion-item>
				<ion-item>Tuggle Dark/Light Theme</ion-item>
			</ion-list>
		</ion-content>

	</ion-menu>
	<ion-router-outlet id="main"></ion-router-outlet>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonMenu, IonContent, IonList, IonItem, menuController, IonRouterOutlet} from '@ionic/vue';
	import BaseMenuHeader from '../Header/BaseMenuHeader.vue';

	export default defineComponent({
		name: "BaseSideMenu",
		components:{
			IonMenu,
			BaseMenuHeader,
			IonContent,
			IonItem,
			IonList,
			IonRouterOutlet
		},
		setup(){
			function openBaseMenu(){
				menuController.enable(true, "baseMenu");
				menuController.open("baseMenu");
			}
			return{
				openBaseMenu
			}
		}
	});
</script>