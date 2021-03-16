<template>
	<div id="Loger" class="center-parent">
		<div class="centered">
			<a href="https://light-mag.ir" class="text-icon oc-color"><img src="../assets/imgs/light.svg" alt="مجله نور"><h1>مجله نور</h1></a>
			<h2>ورود</h2>
			<form id="login-form" class="form" @submit.prevent="login" method="post">
				<span v-if="errs.email"><p v-for="(err, i) in errs.email" :key="i" class="red-text">* {{err}}</p></span>
				<label for="email">ایمیل</label>
				<input type="email" name="email" v-model="email" class="data-field" maxlength="30">
				<span v-if="errs.password"><p v-for="(err, i) in errs.password" :key="i" class="red-text">* {{err}}</p></span>
				<label for="password">پسورد</label>
				<input type="password" name="password" v-model="password" class="data-field" maxlength="30">
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
			const errs = ref({'email':[], 'password':[]});

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
				errs.value.email = [];
				errs.value.password = [];
				const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
				if(!email.value||!password.value||email.value.length>30||password.value.length>30||!re.test(email.value)){
					alert("لطفا فیلد های مشخص شده را چک کنید.");
					if(!email.value){
						errs.value.email.push('لطفا ایمیلتان را وارد کنید.');
					}else if(email.value>30){
						errs.value.push('ایمیل وارد شده بزگتر از حداکثر مقدار است.');
					}else if(!re.test(email.value)){
						errs.value.email.push("لطفا ایمیل معتبری وارد کنید.");
						email.value = '';
					}
					if(!password.value){
						errs.value.password.push('لطفا پسورد را وارد کنید.');
					}else if(password.value.length>30){
						errs.value.password.push('پسورد وارد شده بزگتر از حداکثر مقدار است.');
						password.value = '';
					}
				}else{
					store.dispatch("loginUser", {
						email: email.value,
						password: password.value
					})
					.then(() => {
						if(store.getters.logedIn){
							alert("خوش آمدید.");
							router.push("/LM-admin");
						}
					})
					.catch(err => {
						alert("مشخصات وارد شده نادرست است.\nدر صورت تلاش برای ورود غیرقانونی مورد پیگرد قرار میگیرید.")
						console.log(err)
					})
					.finally(function(){
						email.value = '';
						password.value = '';
					})
				}
			}
			return {email, password, showpass, login, errs};
		},
	};
</script>
<style>
	@import '../assets/Loger.css';
	@import '../assets/form.css';
</style>