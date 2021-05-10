<template>
	<ion-list color="light">
		<ion-menu-toggle>
			<ion-item detail="false" router-link="/about" button lines="none">
				<ion-icon slot="start" :icon="people"></ion-icon>
				<ion-label>About</ion-label>
			</ion-item>
		</ion-menu-toggle>
		<ion-menu-toggle>
			<ion-item detail="false" router-link="/contact" button lines="none">
				<ion-icon slot="start" :icon="call"></ion-icon>
				<ion-label>Contact</ion-label>
			</ion-item>
		</ion-menu-toggle>
		<ion-item detail="false" href="https://myket.ir/app/ir.LightMag.LightMagazine" target="_blank" lines="none">
			<ion-icon slot="start" :icon="starHalf"></ion-icon>
			<ion-label>Rate Us</ion-label>
		</ion-item>
		<ion-item detail="false" href="https://myket.ir/developer/dev-61611" target="_blank" lines="none">
			<ion-icon slot="start" :icon="apps"></ion-icon>
			<ion-label>Other Apps</ion-label>
		</ion-item>
		<ion-item detail="false" href="https://www.light-mag.ir" target="_blank" lines="none">
			<ion-icon slot="start" :icon="earth"></ion-icon>
			<ion-label>light-mag.ir</ion-label>
		</ion-item>
		<ion-item download="lightmag" lines="none">
			<ion-icon slot="start" :icon="logoAndroid"></ion-icon>
			Android App
		</ion-item>
		<ion-item lines="none" download="lightmag">
			<ion-icon slot="start" :icon="logoApple"></ion-icon>
			IOS App
		</ion-item>
	</ion-list>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonList, IonMenuToggle, IonItem, IonIcon, IonLabel} from '@ionic/vue';
	import {people, call, starHalf, apps, earth, logoAndroid, logoApple} from 'ionicons/icons';

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
				earth,
				logoAndroid,
				logoApple
			}
		}
	});
</script>