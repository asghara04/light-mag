<template>
	<ion-card>
		<article-item v-for="article in articles" :key="article.id" button :article="article"></article-item>
	</ion-card>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonCard} from '@ionic/vue';
	import ArticleItem from '../Items/ArticleItem.vue';

	export default defineComponent({
		name: "ArticleSmallItemCard",
		props:{
			articles:{
				required: true,
				type: Object
			}
		},
		components:{
			IonCard,
			ArticleItem
		},
		setup(){

		}
	});
</script>