<template>
	<ion-col sise-xl="4" size-lg="4" size-md="6" size-sm="6" size-xs="12" v-for="article in articles" :key="article.id" class="ion-col-full-height">
		<article-card :article="article"></article-card>
	</ion-col>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonCol} from '@ionic/vue';
	import ArticleCard from '../Cards/ArticleCard.vue';

	export default defineComponent({
		name: "ArticleCols",
		props:{
			articles:{
				required: true,
				type: Object
			}
		},
		components:{
			ArticleCard,
			IonCol
		}
	});
</script>