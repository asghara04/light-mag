<template>
	<!-- there should be an error component wich gets two or three properties and give an error right midlle of the page with icon and simple error expelenaition or meybe some time error code like 400 or 404 ,... -->
	<div v-if="error">
		{{error}}
	</div>
	<!--
		if there was a data before and getting new data got error then we should still show old data for ofline viewing so that how it works
	-->
	<div v-if="articles.length">
		<ion-card class="ion-no-padding ion-text-wrap" v-for="article in articles" :key="article.id">
			<ion-row class="ion-no-padding">
				<ion-col v-if="article.image" size-xs="3" size-md="2">
					<ion-img :src="article.image.image" :alt="article.image.image"></ion-img>
				</ion-col>
				<ion-col size-xs="9" size-md="10">
					<ion-card-header>
						<ion-item>
							<ion-avatar slot="start" size="small" v-if="article.author.prof_picture">
								<ion-img :src="article.author.prof_picture.image"></ion-img>
							</ion-avatar>
							<ion-card-subtitle class="ion-text-capitalize">{{article.author.name}}</ion-card-subtitle>
						</ion-item>
						<ion-card-title class="ion-text-capitalize">{{article.title}}</ion-card-title>
					</ion-card-header>
					<ion-card-content class="text-md">
						<!-- should be hide in low then MD -->
						<p class="ion-text-capitalize ion-hide-md-down">{{article.description}}</p>
					</ion-card-content>
					<ion-row>
						<ion-col size="auto" class="ion-padding-horizontal">
							<ion-icon :icon="chatbubbles"></ion-icon>
							{{article.coms}}
						</ion-col>
						<ion-col size="auto" class="ion-padding-horizontal">
							<ion-icon :icon="time"></ion-icon>
							{{article.read_time_m}} min read
						</ion-col>
					</ion-row>
				</ion-col>
			</ion-row>
		</ion-card>
	</div>
	<p v-else>
		sorry, there is nothing to show yet!
	</p>
</template>
<script>
	import {defineComponent} from 'vue';
	import {useStore, mapGetters} from 'vuex';

	import {FETCH_ARTICLES} from '@/store/actions.type.js';

	import {IonRow, IonCol, IonImg, IonCard, IonCardContent, IonCardHeader, IonCardTitle} from '@ionic/vue';

	import {chatbubbles, time} from 'ionicons/icons';

	// an computed method should be on "module" property
	// computed data and store map getters
	// ---- pagination ----

	export default defineComponent({
		name: "ArticleList",
		props:{
			module:{
				type: String,
				required: true,
				default: "home"
			},
			author:{
				type: Number,
				required: false
			},
			category:{
				type: Number,
				required: false
			},
			subcat:{
				type: Number,
				required: false
			},
			tag:{
				type: Number,
				required: false
			},
			q:{
				type: String,
				required: false
			}
		},
		components:{
			IonCard,
			IonRow,
			IonCol,
			IonCardHeader,
			IonCardTitle,
			IonCardContent,
			IonImg
		},
		computed:{
			...mapGetters("home", ["articles", "error"])
		},
		setup(props){
			const store = useStore();

			/* **--important--:**
			 there should be an error data statement in each vuex module for handling each module errors its cleaner this way :) instead of this shit below
			*/

			store.dispatch(`${props.module}/${FETCH_ARTICLES}`);

			return{
				chatbubbles,
				time
			}
		}
	});
</script>