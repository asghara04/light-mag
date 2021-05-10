<template>
	<ion-searchbar animated class="search-input" autocorrect="on"></ion-searchbar>
</template>
<script>
	import {IonSearchbar} from '@ionic/vue';
	export default{
		name: "Search",
		components:{
			IonSearchbar
		}
	};
</script>