<template>
	<ion-list>
		<ion-menu-toggle>
			<ion-item detail="false" router-link="/" lines="none" router-direction="root" button>
				<ion-icon slot="start" :icon="home"></ion-icon>
				<ion-label>
					<h2>Home</h2>
				</ion-label>
			</ion-item>
		</ion-menu-toggle>
		<ion-item lines="none" detail="false">
			<searchbar></searchbar>
		</ion-item>
		<ion-menu-toggle>
			<ion-item detail="false" :router-link="{name: 'CategoriesPage'}" lines="full" button>
				<ion-icon slot="start" :icon="albums"></ion-icon>
				<ion-label>
					<h2>Categories</h2>
				</ion-label>
			</ion-item>
		</ion-menu-toggle>
	</ion-list>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonList, IonMenuToggle, IonItem, IonIcon, IonLabel} from '@ionic/vue';
	import {home, albums} from 'ionicons/icons';
	import Searchbar from '../Search/Searchbar.vue';

	export default defineComponent({
		name: "BaseSideMenuContentList",
		components:{
			IonList,
			IonMenuToggle,
			IonItem,
			IonIcon,
			IonLabel,
			Searchbar
		},
		setup(){
			return{
				home,
				albums
			}
		}
	});
</script>