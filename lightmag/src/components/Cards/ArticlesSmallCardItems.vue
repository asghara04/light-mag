<template>
	<ion-card>
		<article-list-item v-for="article in articles" :key="article.id" button :article="article"></article-list-item>
	</ion-card>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonCard} from '@ionic/vue';
	import ArticleListItem from '../Items/ArticleListItem.vue';

	export default defineComponent({
		name: "ArticlesSmallCardItems",
		props:{
			articles:{
				required: true,
				type: Object
			}
		},
		components:{
			IonCard,
			ArticleListItem
		},
		setup(){

		}
	});
</script>