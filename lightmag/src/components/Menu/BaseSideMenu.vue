<template>
		<ion-menu side="start" type="overlay" menu-id="baseMenu" content-id="baseMenu">
			<base-menu-header></base-menu-header>

			<!-- should be refactor when wanna use really -->
			<ion-content>
				<ion-list>
					<ion-item>Home Page</ion-item>
					<ion-item>Categories</ion-item>
					<ion-item>all categories with their subcats</ion-item>
					<theme-button></theme-button>
				</ion-list>
			</ion-content>

		</ion-menu>

</template>
<script>
	import {defineComponent} from 'vue';
	import {IonMenu, IonContent, IonList, IonItem, menuController} from '@ionic/vue';
	import BaseMenuHeader from '../Header/BaseMenuHeader.vue';
	import ThemeButton from '../Buttons/ThemeButton.vue';

	export default defineComponent({
		name: "BaseSideMenu",
		components:{
			IonMenu,
			BaseMenuHeader,
			IonContent,
			IonList,
			IonItem,
			ThemeButton,
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