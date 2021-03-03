<template>
	<header>
		<div id="top-header">
			<div id="lightmag-head">
				<h1><router-link :to="{name: 'Home'}">مجله نور</router-link></h1>
				<h2>لایت مگ, مجله ای برای تازش با نور!</h2>
			</div>
			<div class="add"></div>
		</div>

		<nav v-if="cats">
			<ul class="menuul">
				<img class="imgbutton li-icon" src="../assets/imgs/previous.svg" alt="بعد" onclick="window.history.back()">
				<li v-for="cat in cats" :key="cat.id" class="uli">
					<router-link :to="{name: 'category', params:{catslug: cat.slug}}">{{cat.name}}</router-link>
					<img v-if='cat.subcats==true&&!littlescr' src="../assets/imgs/down.svg">
					<ul v-if="cat.subcats==true&&!littlescr" class="itemul">
						<li v-for="subcat in cat.subcats" :key="subcat.id" class="iuli"><a href="#">{{subcat.name}}</a></li>
					</ul>
				</li>
				<img class="imgbutton li-icon" src="../assets/imgs/next.svg" onclick="window.history.forward()" alt='قبل'>

			</ul>
		</nav>
	</header>
</template>

<script>
	import {getAPI} from '@/axios.js';
	import {ref} from 'vue';
	export default{
		name: "LHeader",
		setup(){
			const cats = ref(null);
			const littlescr = ref(false);

			function get_cats(){
				getAPI.get("categories/all/api/v1/")
				.then(res => cats.value = res.data)
				.catch(err => console.log(err))
			}
			get_cats()

			function resize(){
				if(window.innerWidth<950){
					littlescr.value = true
				}else{
					littlescr.value = false
				}				
			}
			resize()

			window.addEventListener("resize", resize)

			return {littlescr, cats}
		}
	};
</script>

<style>
	@import '../assets/header.css';
	@import '../assets/horizental-menu.css';
</style>