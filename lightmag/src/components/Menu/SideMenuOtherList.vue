<template>
	<ion-list>
		<ion-menu-toggle>
			<ion-item router-link="/about" button>
				<ion-icon slot="start" :icon="people"></ion-icon>
				<ion-label>About</ion-label>
			</ion-item>
		</ion-menu-toggle>
		<ion-menu-toggle>
			<ion-item router-link="/contact" button>
				<ion-icon slot="start" :icon="call"></ion-icon>
				<ion-label>Contact</ion-label>
			</ion-item>
		</ion-menu-toggle>
		<ion-item>
			<ion-icon slot="start" :icon="starHalf"></ion-icon>
			<ion-label>Rate Us</ion-label>
		</ion-item>
		<ion-item>
			<ion-icon slot="start" :icon="apps"></ion-icon>
			<ion-label>Other Apps</ion-label>
		</ion-item>
		<ion-item href="https://www.light-mag.ir" target="_blank">
			<ion-icon slot="start" :icon="earth"></ion-icon>
			<ion-label>Website</ion-label>
		</ion-item>
	</ion-list>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonList, IonMenuToggle, IonItem, IonIcon, IonLabel} from '@ionic/vue';
	import {people, call, starHalf, apps, earth} from 'ionicons/icons';

	export default defineComponent({
		name: "BaseSideMenuOtherList",
		components:{
			IonList,
			IonMenuToggle,
			IonItem,
			IonIcon,
			IonLabel
		},
		setup(){
			return{
				people,
				call,
				starHalf,
				apps,
				earth
			}
		}
	});
</script>