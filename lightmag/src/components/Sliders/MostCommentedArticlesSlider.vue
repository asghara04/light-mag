<template>
	<ion-slides v-if="articles!=false" :options="slideOpts">
		<ion-slide v-for="article in articles" :key="article.id" class="ion-slide-main ion-margin-vertical">
			<ion-card class="ion-slide-main ion-text-capitalize">
				<ion-img v-if="article.image" style="pointer-events:none" :src="article.image.image"></ion-img>
				<ion-card-header>
					<ion-card-subtitle class="ion-text-start">{{article.author.name}}</ion-card-subtitle>
					<ion-card-title>{{article.title.substr(0,35)}}</ion-card-title>
				</ion-card-header>
				<article-card-footer :readTime="article.read_time_m" :comments="article.coms"></article-card-footer>
			</ion-card>
		</ion-slide>
	</ion-slides>
</template>
<script>
	import {defineComponent} from 'vue';
	import {useStore, mapGetters} from 'vuex';
	import {FETCH_ARTICLES} from '../../store/actions.type.js';
	import {IonSlides, IonSlide} from '@ionic/vue';
	import ArticleCardFooter from '../Footer/ArticleCardFooter.vue';

	export default defineComponent({
		name: "MostCommentedArticlesSlider",
		components:{
			IonSlides,
			IonSlide,
			ArticleCardFooter
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