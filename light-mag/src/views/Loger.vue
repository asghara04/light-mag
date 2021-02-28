<template>
	<div id="Loger" class="center-parent">
		<div class="centered">
			<a href="https://light-mag.ir" class="text-icon oc-color"><img src="../assets/imgs/light.svg	" alt="مجله نور"><h1>مجله نور</h1></a>
			<h2>ورود</h2>
			<form id="login-form" @submit.prevent="login">
				<label for="email">ایمیل</label>
				<input type="email" name="email" v-model="email" class="data-field" required="" placeholder="ایمیل" maxlength="30">
				<label>پسورد</label>
				<input type="password" name="password" v-model="password" class="data-field" required="" placeholder="پسورد" maxlength="30">
				<p @click.prevent="showpass" class="link-like">نمایش پسورد</p>
				<button class="sub-button">ورود</button>
			</form>
			<div id="login-or">
				<p>یا</p>
				<img class="google" src="../assets/imgs/google.svg" alt="گوگل">
			</div>
			<p class="link-like">فراموشی پسورد</p>
		</div>
	</div>
</template>
<script>
	import {ref} from 'vue';
	import {useStore} from 'vuex';
	import {useRouter} from 'vue-router';
	export default{
		name: "Loger",
		setup(){
			const email = ref(null);
			const password = ref(null);
			const store = useStore();
			const router = useRouter();
			const passfieldtype = ref(true);

			function showpass(){
				passfieldtype.value = !passfieldtype.value;
				const passfield = document.getElementById("login-form")["password"]
				if(passfieldtype.value){
					passfield.type = "password";
				}else{
					passfield.type = "text";
				}
			}
			
			function login(){
				store.dispatch("loginUser", {
					email: email.value,
					password: password.value
				})
				.then(() => {
					if(store.getters.logedIn){
						router.push({name: "admin-panel"})
					}
				})
				.catch(err => {
					alert("مشخصات وارد شده نادرست است.\n در صورت تلاش برای ورود غیرقانونی مورد پیگرد قرار میگیرید.")
					console.log(err)
				})
			}
			return {email, password, showpass, login};
		},
	};
</script>
<style>
	@import '../assets/Loger.css';
	@import '../assets/form.css';
</style>