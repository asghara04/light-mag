<template>
	<IonSlide class="ion-slide-main ion-margin-vertical">
		<article-small-card :key="article" v-bind="$props"></article-small-card>
	</IonSlide>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonSlide} from '@ionic/vue';
	import ArticleSmallCard from '../Cards/ArticleSmallCard.vue';

	export default defineComponent({
		name: "Articleslide",
		props:{
			article:{
				type: Object,
				required: true
			}
		},
		components:{
			IonSlide,
			ArticleSmallCard
		}
	});
</script>