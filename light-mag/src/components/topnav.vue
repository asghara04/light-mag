<template>
	<nav v-if="wich!=='admin'&&!user" id="topnav" :class="{'smallopenul':showmenu&&smallscreen}">
		<img v-if="smallscreen" src="../assets/imgs/menu.svg" class="imgbutton" id="menu-icon" @click="menu()">
		<h1><router-link to="/" class="text-icon ed-color" name="مجله نور"><img src="../assets/imgs/light.svg">مجله نور</router-link></h1>

		<ul id="topul">
			<li><router-link to="/" name="مجله نور" class="li-icon ed-color"><img src="../assets/imgs/home.svg">صفحه اصلی</router-link></li>
			<li><router-link to="/categories" class="li-icon ed-color"  name="مجله نور"><img src="../assets/imgs/cats.svg">موضوعات</router-link></li>
			<span v-if="smallscreen">
				<li>hellll</li>
				<li v-for="cat in categories" :key="cat.id">{{cat.name}}</li>
			</span>
			<li v-if="user"><a href="https://admin.light-mag.ir">پنل</a></li>
		</ul>
		<div v-if="smallscreen" @click="exit()" id="topsmalluloverlay"></div>

		<img v-if="avragescreen||smallscreen" class="imgbutton" src="../assets/imgs/search.svg" @click="search()">
		<form :class="{'block':showsearch}" id="search-form">
			<input type="search" required="" maxlength="100" placeholder="جستوجو..." name="search" class="search-field">
			<button type="submit" class="search-button"><img src="../assets/imgs/search.svg"></button>	
		</form>
	</nav>
	<nav v-else id="topnav">
		hi
	</nav>
</template>
<script>
	import {getAPI} from '@/axios.js';

	export default{
		name: "topnav",
		created(){
			this.resize()
			window.addEventListener("resize", this.resize);
		},
		props:["wich"],
		data(){
			return{
				user: false,
				smallscreen: false,
				avragescreen: false,
				showmenu: false,
				showsearch: false,
				categories: null
			}
		},
		methods:{
			resize(){
				if(window.innerWidth > 775){
					this.smallscreen = false
					this.avragescreen = false
				}else if(window.innerWidth > 475){
					this.smallscreen = false
					this.avragescreen = true
				}else{
					this.smallscreen = true
					this.cats()
				}
			},
			menu(){
				if(!this.showmenu){
					this.showsearch = false
					this.showmenu = true
				}else{
					this.showmenu = false
				}
			},
			search(){
				if(!this.showsearch){
					this.showmenu = false
					this.showsearch = true
				}else{
					this.showsearch = false
				}
			},
			exit(){
				this.showmenu = false
				this.showsearch = false
			},
			cats(){
				getAPI("categories/all/api/v1/")
				.then(res => this.categories = res.data)
				.catch(err => console.log(err))
			}
		},
	};
</script>
<style scoped>
	@import '../assets/topnav.css';
</style>