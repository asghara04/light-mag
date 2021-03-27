<template>
	<aside id="sidebar">
		<p v-if="art_count" class="count">کل نوشته ها: {{art_count}}</p>
		<div v-if="last_arts">
			<div v-for="art in last_arts" :key="art.id" class="siders">
				<router-link v-if="art.image" :to="{name: 'article',params:{artslug: art.slug}}"><img :src="art.image.image" :alt="art.image.alt" :name="art.image.name"></router-link>
				<h3><router-link :to="{name: 'article',params:{artslug: art.slug}}">{{art.title}}</router-link></h3>
			</div>
		</div>
		<div class="cen">
			<a href="https://linuxstory.ir" target="_blank"><img src="../assets/imgs/add.gif"></a>
		</div>
		<hr>
		<h3 class="down-name"><router-link class="text-icon" name='لایت مگ' to="/" rel="لایت مگ"><img src="../assets/imgs/light.svg" alt="LM" name="لایت مگ">لایت مگ</router-link></h3>
	</aside>
</template>
<script>
	import {ref} from 'vue';
	import {getAPI} from '@/axios.js';
	export default{
		name: "sidebar",
		setup(){
			const art_count = ref(null);
			async function art_counter(){
				try{
					const res = await getAPI.get('articles/api/v1/count/')
					art_count.value = res.data.count;
				}catch(err){
					alert('متاسفیم خطایی رخ داد.')
				}
			}
			art_counter()
			const last_arts = ref(null);
			async function get_last_arts(){
				try{
					const res = await getAPI.get("articles/api/v1/lasts/");
					last_arts.value = res.data;
				}catch(err){
					alert('متاسفیم خطایی رخ داد.')
				}
			}
			get_last_arts();
			return{art_count,last_arts}
		}
	};
</script>
<style>
	@import '../assets/sidebar.css';
</style>