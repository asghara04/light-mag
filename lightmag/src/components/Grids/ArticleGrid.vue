<template>
	<ion-grid>
		<ion-row>
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