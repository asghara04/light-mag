<template>
	<nav id="topnav" class="lm-nav">
		<img src="../assets/imgs/menu.svg" class="imgbutton lm-menu" id="menu-icon" @click="menu()" alt="منو">
		<div id="topdiv">
			<h3><router-link to="/" class="text-icon ed-color" name="مجله نور"><img src="../assets/imgs/light.svg">مجله نور</router-link></h3>
			<img class="imgbutton" src="../assets/imgs/previous.svg" alt="بعد" onclick="window.history.back()">
			<img class="imgbutton" src="../assets/imgs/next.svg" onclick="window.history.forward()" alt='قبل'>
		</div>
	</nav>
	<aside id="highsidebar" :class="{'open-side':user&&showmenu&&largescreen,'close-side':user&&!showmenu&&largescreen,'open':user&&showmenu&&smallscreen}">
		<router-link :to="{name: 'admin-panel'}" class="text-icon link-like"><img src="../assets/imgs/dashboard.svg"><span>داشبورد</span></router-link>
		<router-link to="/LM-admin/categories" class="text-icon link-like"><img src="../assets/imgs/cats.svg"><span>موضوعات</span></router-link>
		<router-link to="/LM-admin/articles" class="text-icon link-like"><img src="../assets/imgs/article.svg"><span>نوشته ها</span></router-link>
		<router-link to="/LM-admin/comments" class="text-icon link-like"><img src="../assets/imgs/comment.svg"><span>کامنت ها</span></router-link>
		<router-link to="/LM-admin/tags" class="text-icon link-like"><img src="../assets/imgs/tag.svg"><span>تگ ها</span></router-link>
		<router-link to='/LM-admin/users' class="text-icon link-like"><img src="../assets/imgs/group.svg"><span>کاربران</span></router-link>
		<a class="text-icon link-like" target="_blank" href="https://light-mag.ir/games"><img src="../assets/imgs/game.svg"><span>گیم ها</span></a>
		<router-link to='/LM-admin/settings' class="text-icon link-like"><img src="../assets/imgs/settings.svg"><span>تنظیمات</span></router-link>
		<a href="https://light-mag.ir" class="text-icon link-like" target="_blank"><img src="../assets/imgs/webpage.svg"><span>نمایش اپ</span></a>
		<router-link :to="{name: 'admin-panel'}" class="text-icon link-like"><img src="../assets/imgs/dashboard.svg"><span>داشبورد</span></router-link>
		<router-link to="/LM-admin/categories" class="text-icon link-like"><img src="../assets/imgs/cats.svg"><span>موضوعات</span></router-link>
		<router-link to="/LM-admin/articles" class="text-icon link-like"><img src="../assets/imgs/article.svg"><span>نوشته ها</span></router-link>
		<router-link to="/LM-admin/comments" class="text-icon link-like"><img src="../assets/imgs/comment.svg"><span>کامنت ها</span></router-link>
		<router-link to="/LM-admin/tags" class="text-icon link-like"><img src="../assets/imgs/tag.svg"><span>تگ ها</span></router-link>
		<router-link to='/LM-admin/users' class="text-icon link-like"><img src="../assets/imgs/group.svg"><span>کاربران</span></router-link>
		<a class="text-icon link-like" target="_blank" href="https://light-mag.ir/games"><img src="../assets/imgs/game.svg"><span>گیم ها</span></a>
		<router-link to='/LM-admin/settings' class="text-icon link-like"><img src="../assets/imgs/settings.svg"><span>تنظیمات</span></router-link>
		<a href="https://light-mag.ir" class="text-icon link-like" target="_blank"><img src="../assets/imgs/webpage.svg"><span>نمایش اپ</span></a>
		<router-link :to="{name: 'admin-panel'}" class="text-icon link-like"><img src="../assets/imgs/dashboard.svg"><span>داشبورد</span></router-link>
		<router-link to="/LM-admin/categories" class="text-icon link-like"><img src="../assets/imgs/cats.svg"><span>موضوعات</span></router-link>
		<router-link to="/LM-admin/articles" class="text-icon link-like"><img src="../assets/imgs/article.svg"><span>نوشته ها</span></router-link>
		<router-link to="/LM-admin/comments" class="text-icon link-like"><img src="../assets/imgs/comment.svg"><span>کامنت ها</span></router-link>
		<router-link to="/LM-admin/tags" class="text-icon link-like"><img src="../assets/imgs/tag.svg"><span>تگ ها</span></router-link>
		<router-link to='/LM-admin/users' class="text-icon link-like"><img src="../assets/imgs/group.svg"><span>کاربران</span></router-link>
		<a class="text-icon link-like" target="_blank" href="https://light-mag.ir/games"><img src="../assets/imgs/game.svg"><span>گیم ها</span></a>
		<router-link to='/LM-admin/settings' class="text-icon link-like"><img src="../assets/imgs/settings.svg"><span>تنظیمات</span></router-link>
		<a href="https://light-mag.ir" class="text-icon link-like" target="_blank"><img src="../assets/imgs/webpage.svg"><span>نمایش اپ</span></a>
	</aside>
</template>
<script>
	export default{
		name: "lm-nav",
		created(){
			this.resize(window.innerWidth);
			window.addEventListener('resize', this.resize);
		},
		data(){
			return{
				user: this.$store.getters.logedIn,
				showmenu: true,
				largescreen: window.innerWidth>775,
				smallscreen: window.innerWidth<=775
			}
		},
		methods:{
			resize(){
				if(window.innerWidth>1050){
					this.showmenu = true;
					this.smallscreen = false;
					this.largescreen = true;
					document.getElementById('app').classList = 'sidenav-large';
				}else if(window.innerWidth>775){
					this.smallscreen = false;
					this.largescreen = true;
					document.getElementById('app').classList = 'sidenav-medium';
					this.showmenu = false;
				}else{
					this.largescreen = false;
					this.smallscreen = true;
					document.getElementById("app").classList = '';
					this.showmenu = false;
				}
			},
			menu(){
				this.showmenu = !this.showmenu;
				if(this.showmenu&&window.innerWidth>775){
					document.getElementById("app").classList = "sidenav-large";
				}else if(this.showmenu&&window.innerWidth<776){
					document.body.classList.add('freeze');
				}else if(!this.showmenu&&window.innerWidth<776){
					document.body.classList.remove('freeze');
				}else{
					document.getElementById("app").classList = "sidenav-medium";
				}
			},
			exit(){
				this.showmenu = false;
			}
		}
	};
</script>
<style>
	@import '../assets/topnav.css';
	@import '../assets/lm-nav.css';
</style>