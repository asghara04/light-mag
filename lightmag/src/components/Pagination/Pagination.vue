<template>
	<ion-card>
		<ion-item detail='false' lines='none'>
			<ion-label>page {{current}} of {{allPages}}</ion-label>
			<ion-buttons slot="end">
				<ion-button :disabled="current<=1" target="_blank" :rel="'light magazine page '+(current-1)" :href="this.$route.path+'?page='+(current-1)">
					<ion-icon slot="icon-only" :icon="chevronBack"></ion-icon>
				</ion-button>
				<ion-button :disabled="allPages<=current" target="_blank" :rel="'light magazine page '+(current+1)" :href="this.$route.path+'?page='+(current+1)">
					<ion-icon slot="icon-only" :icon="chevronForward"></ion-icon>
				</ion-button>
			</ion-buttons>
		</ion-item>
	</ion-card>
</template>
<script>
	import {defineComponent} from 'vue';
	import {mapGetters} from 'vuex';
	import {IonCard, IonItem, IonLabel, IonButtons, IonButton, IonIcon} from '@ionic/vue';
	import {chevronBack, chevronForward} from 'ionicons/icons';

	export default defineComponent({
		name: "Pagination",
		props:{
			module:{
				type: String,
				required: true
			},
			action:{
				type: String,
				required: true
			},
			current:{
				type: Number,
				required: true,
				default: 1
			}
		},
		components:{
			IonCard,
			IonItem,
			IonLabel,
			IonButtons,
			IonButton,
			IonIcon
		},
		// ---should be consume api later---
		computed:{
			...mapGetters('home', ['allPages']),
		},
		setup(){
			return{
				chevronBack,
				chevronForward
			}
		}
	});
</script>