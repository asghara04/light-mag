<template>
	<div id="Loger" class="center-parent">
		<div class="centered">
			<span class="text-icon"><img src="../assets/imgs/light.svg" alt="مجله نور"><h1>مجله نور</h1></span>
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
	export default{
		name: "Loger",
		data(){
			return{
				email: null,
				password: null
			}
		},
		methods:{
			showpass(){
				document.getElementById("login-form")["password"].type = "text";
			},
			login(){
				this.$store.dispatch('loginUser', {
					email: this.email,
					password: this.password
				})
				.then(res => {
					this.$router.push({name: 'admin-panel'})
					console.log(res)
				})
				.catch(err => {
					alert("مشخصات وارد شده نادرست است.\n در صورت تلاش برای ورود غیرقانونی مورد پیگرد قرار میگیرید.")
					console.log(err)
				})
			}
		}
	};
</script>
<style>
	@import '../assets/Loger.css';
	@import '../assets/form.css';
</style>