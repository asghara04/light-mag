<template>
	<nav id="topnav" class="lm-nav">
		<img src="../assets/imgs/menu.svg" class="imgbutton lm-menu" id="menu-icon" @click="menu()" alt="منو">
		<div id="topdiv" class="allflex">
			<h3><router-link to="/" class="text-icon ed-color" name="مجله نور"><img src="../assets/imgs/light.svg">مجله نور</router-link></h3>
			<img class="imgbutton" src="../assets/imgs/previous.svg" alt="بعد" onclick="window.history.back()">
			<img class="imgbutton" src="../assets/imgs/next.svg" onclick="window.history.forward()" alt='قبل'>
		</div>
	</nav>
	<aside id="highsidebar" :class="{'open-side':showmenu&&largescreen,'close-side':!showmenu&&largescreen,'open':showmenu&&smallscreen}">
		<ul>
			<li id="dashboard-li"><router-link :to="{name: 'admin-panel'}" class="text-icon link-like"><img src="../assets/imgs/dashboard.svg"><span>داشبورد</span></router-link></li>
			<li id="categories-li"><img v-if="showmenu" @click="liopener('categories-li')" class="left-float" src="../assets/imgs/down.svg"><router-link to="/LM-admin/categories" class="text-icon link-like"><img src="../assets/imgs/category.svg"><span>دسته ها</span></router-link><ul v-if="showmenu"><li><router-link to="/LM-admin/add/subcat" class="text-icon link-like"><img src="../assets/imgs/cats.svg"><span>زیردسته جدید</span></router-link></li><li><router-link to="/LM-admin/add/category" class="text-icon link-like"><img src="../assets/imgs/add.svg"><span>افزودن</span></router-link></li></ul></li>
			<li id="articles-li"><img v-if="showmenu" @click="liopener('articles-li')" class="left-float" src="../assets/imgs/down.svg"><router-link to="/LM-admin/articles" class="text-icon link-like"><img src="../assets/imgs/article.svg"><span>نوشته ها</span></router-link><ul v-if="showmenu"><li><router-link to="/LM-admin/add/article" class="text-icon link-like"><img src="../assets/imgs/add.svg"><span>افزودن</span></router-link></li></ul></li>
			<li id="comments-li"><img v-if="showmenu" @click="liopener('comments-li')" class="left-float" src="../assets/imgs/down.svg"><router-link to="/LM-admin/comments" class="text-icon link-like"><img src="../assets/imgs/comment.svg"><span>کامنت ها</span></router-link></li>
			<li id="tags-li"><img v-if="showmenu" @click="liopener('tags-li')" class="left-float" src="../assets/imgs/down.svg"><router-link to="/LM-admin/tags" class="text-icon link-like"><img src="../assets/imgs/tag.svg"><span>تگ ها</span></router-link><ul v-if="showmenu"><li><router-link to="/LM-admin/add/tag" class="text-icon link-like"><img src="../assets/imgs/add.svg"><span>افزودن</span></router-link></li></ul></li>
			<li id="images-li"><img v-if="showmenu" @click="liopener('images-li')" class="left-float" src="../assets/imgs/down.svg"><router-link to="/LM-admin/images" class="text-icon link-like"><img src="../assets/imgs/image.svg"><span>تصاویر</span></router-link><ul v-if="showmenu"><li><router-link to="/LM-admin/add/image" class="text-icon link-like"><img src="../assets/imgs/add.svg"><span>افزودن</span></router-link></li></ul></li>
			<li id="users-li"><img v-if="showmenu" @click="liopener('users-li')" class="left-float" src="../assets/imgs/down.svg"><router-link to='/LM-admin/users' class="text-icon link-like"><img src="../assets/imgs/group.svg"><span>کاربران</span></router-link><ul v-if="showmenu"><li><router-link to="/LM-admin/add/user" class="text-icon link-like"><img src="../assets/imgs/add.svg"><span>افزودن</span></router-link></li></ul></li>
			<li><router-link to='/LM-admin/settings' class="text-icon link-like"><img src="../assets/imgs/settings.svg"><span>تنظیمات</span></router-link></li>
			<li><a href="https://light-mag.ir" class="text-icon link-like" target="_blank"><img src="../assets/imgs/webpage.svg"><span>نمایش اپ</span></a></li>
		</ul>
	</aside>
</template>
<script>
	import {ref} from 'vue';
	export default{
		name: "lm-nav",
		setup(){
			const showmenu = ref(true);
			const largescreen = ref(window.innerWidth>775);
			const smallscreen = ref(window.innerWidth<=775);
			function resize(){
				if(window.innerWidth>1050){
					showmenu.value = true;
					smallscreen.value = false;
					largescreen.value = true;
					document.getElementById('app').classList = 'sidenav-large';
				}else if(window.innerWidth>775){
					smallscreen.value = false;
					largescreen.value = true;
					document.getElementById('app').classList = 'sidenav-medium';
					showmenu.value = false;
				}else{
					largescreen.value = false;
					smallscreen.value = true;
					document.getElementById("app").classList = '';
					showmenu.value = false;
				}				
			}
			resize()
			window.addEventListener('resize', resize);
			function menu(){
				showmenu.value = !showmenu.value;
				if(showmenu.value&&window.innerWidth>775){
					document.getElementById("app").classList = "sidenav-large";
				}else if(showmenu.value&&window.innerWidth<776){
					document.body.classList.add('freeze');
				}else if(!showmenu.value&&window.innerWidth<776){
					document.body.classList.remove('freeze');
				}else{
					document.getElementById("app").classList = "sidenav-medium";
				}				
			}
			function exit(){
				if(smallscreen.value){
					showmenu.value = false;
				}
			}
			function liopener(id){
				const li = document.getElementById(id)
				if(li.classList!=''){
					li.classList = '';
				}else{
					li.classList = 'openli';
				}
			}
			return{menu, exit, showmenu, largescreen, smallscreen, liopener}
		}
	};
</script>
<style>
	@import '../assets/topnav.css';
	@import '../assets/lm-nav.css';
</style>