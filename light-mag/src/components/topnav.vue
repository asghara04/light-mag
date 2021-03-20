<template>
	<nav id="topnav" :class="{'smallopenul':showmenu&&smallscreen}">
		<img v-if="smallscreen" src="../assets/imgs/menu.svg" class="imgbutton" id="menu-icon" @click="menu()">
		<h1><router-link to="/" class="text-icon ed-color" name="لایت مگ"><img src="../assets/imgs/light.svg">لایت مگ</router-link></h1>
		<ul id="topul">
			<li><router-link to="/" name="لایت مگ" class="li-icon ed-color"><img src="../assets/imgs/home.svg">صفحه اصلی</router-link></li>
			<li><router-link to="/categories" class="li-icon ed-color"  name="لایت مگ"><img src="../assets/imgs/cats.svg">موضوعات</router-link></li>
			<div v-if="smallscreen">
				<li v-for="cat in categories" :key="cat.id"><router-link :to="{name: 'category',params:{catslug: cat.slug}}" class="li-icon ed-color"><img v-if="cat.image" :src="cat.image.image" :alt="cat.image.alt" :name="cat.image.name">{{cat.name}}</router-link></li>
			</div>
		</ul>
		<div v-if="smallscreen" @click="exit()" id="topsmalluloverlay"></div>

		<img v-if="avragescreen||smallscreen" class="imgbutton" src="../assets/imgs/search.svg" @click.prevent="search()">
		<form :class="{'block':showsearch}" id="search-form" @submit.prevent="q()">
			<input type="search" required="" maxlength="100" placeholder="جستوجو..." name="q" class="search-field">
			<button type="submit" class="search-button"><img src="../assets/imgs/search.svg"></button>
		</form>
	</nav>
</template>
<script>
	import {getAPI} from '@/axios.js';
	import {ref} from 'vue';
	import {useRouter} from 'vue-router';
	export default{
		name: "topnav",
		props:["wich"],
		setup(){
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
					let field = document.getElementById("search-form")['q'];
					if(field){
						field.focus();
					}
				}
			}
			function exit(){
				showmenu.value = false;
				showsearch.value = false;
				document.body.classList.remove('freeze');
			}
			const router = useRouter();
			function q(){
				let field = document.getElementById("search-form")['q'];
				if(field){
					router.push({name:'search',query:{q:field.value}})
				}
			}
			return{smallscreen,avragescreen,showmenu,showsearch,categories,menu,search,exit,q}
		}
	};
</script>
<style scoped>
	@import '../assets/topnav.css';
	@import '../assets/sidebar.css';
</style>