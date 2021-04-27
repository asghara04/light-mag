<template>
	<ion-list>
		<ion-menu-toggle>
			<ion-item router-link="/about" button>
				<ion-icon slot="start" :icon="people"></ion-icon>
				<ion-label>about</ion-label>
			</ion-item>
		</ion-menu-toggle>
		<ion-item>Contact</ion-item>
		<ion-item>Rate</ion-item>
		<ion-item>Other Apps</ion-item>
		<ion-item>Website</ion-item>
	</ion-list>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonList, IonMenuToggle, IonItem, IonIcon, IonLabel} from '@ionic/vue';
	import {people} from 'ionicons/icons';

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
				people
			}
		}
	});
</script>