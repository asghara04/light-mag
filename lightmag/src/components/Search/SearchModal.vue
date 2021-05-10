<template>
	<ion-header>
		<search-toolbar></search-toolbar>
	</ion-header>
	<ion-content>
		--- COMMING SOON! ---<br>
		holla - hello - bunjor - slm
	</ion-content>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonHeader, IonContent} from '@ionic/vue';
	import SearchToolbar from '../Toolbar/SearchToolbar.vue';

	export default defineComponent({
		name: "SearchModal",
		components:{
			IonHeader,
			IonContent,
			SearchToolbar
		}
	});
</script>