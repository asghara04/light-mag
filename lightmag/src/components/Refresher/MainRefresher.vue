<template>
	<ion-refresher slot="fixed" @ion-refresh="call($event)">
		<ion-refresher-content
		:pulling-icon="refresh"
		pulling-text="pull to refresh"
		refreshing-spinner="crescent"
		refreshing-text="Refreshing..."
		></ion-refresher-content>
	</ion-refresher>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonRefresher, IonRefresherContent} from '@ionic/vue';
	import {refresh} from 'ionicons/icons';
	import {useStore} from 'vuex';

	export default defineComponent({
		name: "MainRefresher",
		props:{
			module:{
				type: String,
				required: true
			},
			action:{
				type: String,
				required: true
			}
		},
		components:{
			IonRefresher,
			IonRefresherContent
		},
		setup(props){
			const store = useStore();
			const call = (event)=>{
				store.dispatch(`${props.module}/${props.action}`)
				.then(function(){
					event.target.complete();
				})
			}
			return{
				call,
				refresh
			}
		}
	});
</script>