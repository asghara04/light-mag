<template>
	<ion-menu side="start" type="overlay" menu-id="baseMenu" content-id="baseMenu">
		<base-menu-header></base-menu-header>
		<base-side-menu-content></base-side-menu-content>
	</ion-menu>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonMenu, menuController} from '@ionic/vue';
	import BaseMenuHeader from '../Header/BaseMenuHeader.vue';
	import BaseSideMenuContent from './BaseSideMenuContent.vue';

	export default defineComponent({
		name: "BaseSideMenu",
		components:{
			IonMenu,
			BaseMenuHeader,
			BaseSideMenuContent
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