<template>
	<ion-slides pager="true" v-if="articles" :options="slideOpts">
		<ion-slide v-for="article in articles" :key="article.id">
			<ion-card class="ion-text-start">
				<ion-img v-if="article.image" :src="article.image.image" class="slide-img" :alt="article.image.alt"></ion-img>
				<ion-card-header>
					<ion-card-subtitle>by {{article.author.name}}</ion-card-subtitle>
					<ion-card-title>{{article.title}}</ion-card-title>
				</ion-card-header>
				<ion-card-content class="ion-hide-md-down">
					<p>{{article.description}}</p>
				</ion-card-content>
			</ion-card>
		</ion-slide>
	</ion-slides>
</template>
<script>
	import {defineComponent} from 'vue';
	import {useStore, mapGetters} from 'vuex';
	import {FETCH_ARTICLES} from '../../store/actions.type.js';
	import {IonSlides, IonSlide, IonCard, IonImg, IonCardHeader, IonCardSubtitle, IonCardTitle, IonCardContent} from '@ionic/vue';

	export default defineComponent({
		name: "MostCommentedArticlesSlider",
		components:{
			IonSlides,
			IonSlide,
			IonCard,
			IonImg,
			IonCardTitle,
			IonCardHeader,
			IonCardSubtitle,
			IonCardContent
		},
		computed:{
			...mapGetters("mostCommented", ["articles"])
		},
		setup(){
			const store = useStore();
			store.dispatch(`mostCommented/${FETCH_ARTICLES}`);

			const slideOpts = {
				initialSlide: 1,
				speed: 500
			}
			return {
				slideOpts
			}
		}
	});
</script>