<template>
	<div v-if="arts" id="topslider">
		<!--
		a short hight manual slider in all page who remainds popular articles! 4- and sort by the 6 reachest comments
		-->
		<article v-for="art in arts.results" :key="art.id" class="topslide">
			<router-link :name="art.title" :rel="art.title" :to="{name: 'article',params: {slug: art.slug}}">
				<img v-if="art.image" :rel="art.image.name" :src="art.image.image" :name="art.image.name" :alt="art.image.alt">
				<h3 class="centered-top-slide">{{art.title}}</h3>
			</router-link>
			<div v-if="!art.image" class="centered-top-slide">
				<hr>
				<p>{{art.description}}</p>
			</div>
		</article>
	</div>
</template>

<script>
	import {getAPI} from '@/axios.js';
	import {ref} from 'vue';
	export default{
		name: "topslider",
		setup(){
			const arts = ref(null);

			function get_arts(){
				getAPI.get('articles/api/v1/')
				.then(res=> arts.value = res.data)
				.catch(err=> console.log(err))
			}
			get_arts()

			return{arts}
		}
	};
</script>

<style>
	@import '../assets/slider.css';
</style>