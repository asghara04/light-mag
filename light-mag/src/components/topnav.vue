<template>
	<nav id="topnav" :class="{'smallopenul':showmenu&&smallscreen}">
		<img v-if="smallscreen" src="../assets/imgs/menu.svg" class="imgbutton" id="menu-icon" @click="menu()">
		<h1><router-link to="/" class="text-icon ed-color" name="مجله نور"><img src="../assets/imgs/light.svg">مجله نور</router-link></h1>
		<ul id="topul">
			<li><router-link to="/" name="مجله نور" class="li-icon ed-color"><img src="../assets/imgs/home.svg">صفحه اصلی</router-link></li>
			<li><router-link to="/categories" class="li-icon ed-color"  name="مجله نور"><img src="../assets/imgs/cats.svg">موضوعات</router-link></li>
			<span v-if="smallscreen">
				<li>hellll</li>
				<li v-for="cat in categories" :key="cat.id"><router-link :to="{name: 'category',params:{catslug: cat.slug}}">{{cat.name}}</router-link></li>
			</span>
			<li><router-link to="/games" class="li-icon ed-color"><img src="../assets/imgs/game.svg">گیم ها</router-link></li>
			<li v-if="user"><a href="https://admin.light-mag.ir" target="_blank">پنل</a></li>
		</ul>
		<div v-if="smallscreen" @click="exit()" id="topsmalluloverlay"></div>

		<img v-if="avragescreen||smallscreen" class="imgbutton" src="../assets/imgs/search.svg" @click.prevent="search()">
		<form :class="{'block':showsearch}" id="search-form">
			<input type="search" required="" maxlength="100" placeholder="جستوجو..." name="search" class="search-field">
			<button type="submit" class="search-button"><img src="../assets/imgs/search.svg"></button>	
		</form>
	</nav>
</template>
<script>
	import {getAPI} from '@/axios.js';
	import {ref} from 'vue';
	import {useStore} from 'vuex';
	export default{
		name: "topnav",
		props:["wich"],
		setup(){
			const store = useStore();
			const user = store.getters.logedIn||false;
			const smallscreen = ref(window.innerWidth<475||false);
			const avragescreen = ref((window.innerWidth>475&&window.innerWidth<775)||false);
			const showmenu = ref(false);
			const showsearch = ref(false);
			const categories = ref(null);
			function resize(){
				if(window.innerWidth > 775){
					smallscreen.value = false;
					avragescreen.value = false;
					document.body.classList.remove("freeze");
				}else if(window.innerWidth > 475){
					smallscreen.value = false;
					avragescreen.value = true;
					document.body.classList.remove("freeze");
				}else{
					smallscreen.value = true;
					get_cats();
				}
			}
			resize()
			window.addEventListener("resize", resize)

			function get_cats(){
				getAPI.get("categories/all/api/v1/")
				.then(res => categories.value = res.data)
				.catch(err => console.log(err))
			}
			function menu(){
				showmenu.value = !showmenu.value;
				if(showmenu.value){
					showsearch.value = false;
					document.body.classList.add("freeze");
				}else{
					document.body.classList.remove("freeze");
				}
			}
			function search(){
				showsearch.value = !showsearch.value;
				if(showsearch.value){
					showmenu.value = false;
					document.getElementById('search-form')['search'].focus();
				}
			}
			function exit(){
				showmenu.value = false;
				showsearch.value = false;
				document.body.classList.remove('freeze');
			}

			return{user, smallscreen, avragescreen, showmenu, showsearch, categories, menu, search, exit}
		}
	};
</script>
<style scoped>
	@import '../assets/topnav.css';
	@import '../assets/sidebar.css';
</style>