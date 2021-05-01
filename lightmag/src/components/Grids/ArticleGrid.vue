<template>
	<ion-grid class="ion-grid-no-padding-md-sm-xs-screen">
		<ion-row class="ion-justify-content-center">
			<article-cols v-bind="$props"></article-cols>
		</ion-row>
	</ion-grid>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonGrid, IonRow} from '@ionic/vue';
	import ArticleCols from '../Columns/ArticleCols.vue';

	export default defineComponent({
		name: "ArticleLarge",
		props:{
			articles:{
				required: true,
				type: Object
			}
		},
		components:{
			IonGrid,
			IonRow,
			ArticleCols
		}
	});
</script>