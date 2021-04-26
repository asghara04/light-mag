<template>
	<ion-searchbar show-cancel-button="never" :clear-icon="status"></ion-searchbar>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonSearchbar} from '@ionic/vue';

	export default defineComponent({
		name: "Searchbar",
		components:{
			IonSearchbar
		},
		props:{
			status:{
				type: String,
				default: "focus",
				required: false
			}
		}
	});
</script>