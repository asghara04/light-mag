<template>
	<ion-list>
		<ion-item router-link="/">
			<ion-icon slot="start" :icon="home"></ion-icon>
			<ion-label>
				<h2>Home</h2>
			</ion-label>
		</ion-item>
		<ion-item>Categories</ion-item>
	</ion-list>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonList, IonItem, IonIcon, IonLabel} from '@ionic/vue';
	import {home} from 'ionicons/icons';

	export default defineComponent({
		name: "BaseSideMenuContentList",
		components:{
			IonList,
			IonItem,
			IonIcon,
			IonLabel,
		},
		setup(){
			return{home}
		}
	});
</script>