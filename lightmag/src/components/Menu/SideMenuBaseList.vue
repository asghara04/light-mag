<template>
	<ion-list>
		<ion-menu-toggle>
			<ion-item router-link="/" router-direction="root" button>
				<ion-icon slot="start" :icon="home"></ion-icon>
				<ion-label>
					<h2>Home</h2>
				</ion-label>
			</ion-item>
			<ion-item>Categories</ion-item>
		</ion-menu-toggle>
	</ion-list>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonList, IonMenuToggle, IonItem, IonIcon, IonLabel} from '@ionic/vue';
	import {home} from 'ionicons/icons';

	export default defineComponent({
		name: "BaseSideMenuContentList",
		components:{
			IonList,
			IonMenuToggle,
			IonItem,
			IonIcon,
			IonLabel,
		},
		setup(){
			return{home}
		}
	});
</script>