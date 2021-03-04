<template>
	<aside id="sidebar">
		<p v-if="art_count">کل نوشته ها: {{art_count.count}}</p>
		<hr>
		<h3 class="down-name"><router-link class="text-icon" name='لایت مگ' to="/"><img src="../assets/imgs/light.svg" alt="LM" name="مجله نور">مجله نور</router-link></h3>
	</aside>
</template>

<script>
	import {ref} from 'vue';
	import {getAPI} from '@/axios.js';
	export default{
		name: "sidebar",
		setup(){
			const art_count = ref(null);

			function art_counter(){
				getAPI.get("articles/api/v1/count/")
				.then(res => art_count.value = res.data)
				.catch(err => console.log(err))
			}
			art_counter()

			return{art_count}
		}
	};
</script>

<style>
	@import '../assets/sidebar.css';
</style>