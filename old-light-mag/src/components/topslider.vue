<template>
	<div v-if="arts" id="topslider">
		<article v-for="art in arts" :key="art.id" class="topslide">
			<router-link :name="art.title" :rel="art.title" :to="{name: 'article',params: {artslug: art.slug}}">
				<img v-if="art.image" :rel="art.image.name" :src="art.image.image" :name="art.image.name" :alt="art.image.alt">
				<h3 class="centered-top-slide">{{art.title}}</h3>
			</router-link>
			<div v-if="!art.image" class="centered-top-slide">
				<hr>
				<p>{{art.description}}</p>
			</div>
		</article>
		<article class="topslide"><div id="pos-article-display-23260"></div></article>
	</div>
</template>
<script>
	import {getAPI} from '@/axios.js';
	import {ref} from 'vue';
	export default{
		name: "topslider",
		setup(){
			const arts = ref(null);
			async function get_arts(){
				try{
					const res = await getAPI.get("articles/most/api/v1/comment/");
					arts.value = res.data
				}catch(err){
					console.log(err)
				}
			}get_arts()
			return{arts}
		}
	};
</script>
<style>
	@import '../assets/slider.css';
</style>