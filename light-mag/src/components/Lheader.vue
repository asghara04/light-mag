<template>
	<header>
		<div id="top-header">
			<div id="lightmag-head">
				<h1><router-link to='/'>مجله نور</router-link></h1>
				<h2>لایت مگ, مجله ای برای تازش با نور!</h2>
			</div>
			<div class="add"></div>
		</div>

		<nav if="cats">
			<ul class="menuul">
				<img class="imgbutton li-icon" src="../assets/imgs/previous.svg" alt="بعد" onclick="window.history.back()">
				<li v-for="cat in cats" :key="cat.id" class="uli">
					<a href="#">{{cat.name}}</a>
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

	export default{
		name: "LHeader",
		data(){
			return{
				cats: null,
				littlescr: false
			}
		},
		created(){
			getAPI.get("categories/all/api/v1/")
			.then(response => {
				this.cats = response.data
			})
			.catch(err => {
				console.log(err)
			})

			window.addEventListener("resize", this.resize);
		},
		methods:{
			resize(){
				if(window.innerWidth<950){
					this.littlescr = true
				}else{
					this.littlescr = false
				}
			}
		}
	};
</script>

<style>
	@import '../assets/header.css';
	@import '../assets/horizental-menu.css';
</style>