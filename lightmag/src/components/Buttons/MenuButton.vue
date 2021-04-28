<template>
	<ion-menu-button :menu="menuId">
		<ion-icon :icon="menu"></ion-icon>
	</ion-menu-button>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonMenuButton, IonIcon} from '@ionic/vue';
	import {menu} from 'ionicons/icons';

	export default defineComponent({
		name: "MenuButton",
		props:{
			menuId:{
				type: String,
				required: true
			}
		},
		components:{
			IonMenuButton,
			IonIcon
		},
		setup(){
			return{
				menu
			}
		}
	});
</script>