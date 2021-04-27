<template>
	<ion-grid class="ion-grid-no-padding-md-sm-xs-screen" v-if="data">
		<ion-row>
			<ion-col size-md="5" size-xs="12">
				{{data[0]}}
			</ion-col>
			<ion-col size-md="7" size-xs="12">
				<articles-small-card-items :articles="data.slice(1,)"></articles-small-card-items>
			</ion-col>
		</ion-row>
	</ion-grid>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonGrid, IonRow, IonCol} from '@ionic/vue';
	import ArticlesSmallCardItems from '../Cards/ArticlesSmallCardItems.vue';

	export default defineComponent({
		name: "MainContentGrid",
		components:{
			IonGrid,
			IonRow,
			IonCol,
			ArticlesSmallCardItems
		},
		props:{
			data:{
				required: true
			}
		}
	});
</script>