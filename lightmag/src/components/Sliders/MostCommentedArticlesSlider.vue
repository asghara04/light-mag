<template>
	<ion-slides v-if="articles!=false" :options="slideOpts">
		<article-slide v-for="article in articles" :key="article.id" :article="article"></article-slide>
	</ion-slides>
</template>
<script>
	import {defineComponent} from 'vue';
	import {useStore, mapGetters} from 'vuex';
	import {FETCH_ARTICLES} from '../../store/actions.type.js';
	import {IonSlides} from '@ionic/vue';
	import ArticleSlide from '../Slides/ArticleSlide.vue';

	export default defineComponent({
		name: "MostCommentedArticlesSlider",
		components:{
			IonSlides,
			ArticleSlide
		},
		computed:{
			...mapGetters("mostCommented", ["articles"])
		},
		setup(){
			const store = useStore();
			store.dispatch(`mostCommented/${FETCH_ARTICLES}`);

			const slideOpts = {
				speed: 500,
				zoom: false,
				slidesPerView: 'auto',
				grabCursor: true
			}
			return {
				slideOpts
			}
		}
	});
</script>