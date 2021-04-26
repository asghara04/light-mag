<template>
	<ion-list>
		<ion-item router-link="/about">
			<ion-icon slot="start" :icon="people"></ion-icon>
			<ion-label>
				<h2>about</h2>
			</ion-label>
		</ion-item>
		<ion-item>Contact</ion-item>
		<ion-item>Rate</ion-item>
		<ion-item>Other Apps</ion-item>
		<ion-item>Website</ion-item>
	</ion-list>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonList, IonItem, IonIcon, IonLabel} from '@ionic/vue';
	import {people} from 'ionicons/icons';

	export default defineComponent({
		name: "BaseSideMenuOtherList",
		components:{
			IonList,
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