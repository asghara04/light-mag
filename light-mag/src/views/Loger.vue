<template>
	<div id="Loger" class="center-parent">
		<div class="centered">
			<span class="text-icon"><img src="../assets/imgs/light.svg" alt="مجله نور"><h1>مجله نور</h1></span>
			<h2>ورود</h2>
			<form id="login-form">
				<label for="email">ایمیل</label>
				<input type="email" name="email" class="data-field" required="" placeholder="ایمیل" maxlength="30">
				<label>پسوورد</label>
				<input type="password" name="password" class="data-field" required="" placeholder="پسوورد" maxlength="30">
				<button class="sub-button">ورود</button>
			</form>
			<div id="login-or">
				<p>یا</p>
				<img class="google" src="../assets/imgs/google.svg" alt="گوگل">
			</div>
		</div>
	</div>
<!-- 	<div id="Loger">
		<span class="login-page-header">
			<img src="../assets/imgs/light.svg"><h1>مجله نور</h1>
		</span>
		<div id="loginWays">
			<h3>ورود</h3>
			<form id="loginForm">
				<input type="email" name="email" placeholder="ایمیل..." class="data-field">
				<input type="password" name="password" placeholder="پسوورد..." class="data-field">
			</form>
		</div>
		<p @click.prevent="showpas">نمایش پسوورد</p>
		<br>
		footer should not show up here !
	</div> -->
</template>
<script>
	export default{
		name: "Loger",
		methods:{
			showpas(){
				document.getElementById("loginForm")["password"].type = "text";
			}
		}
	};
</script>
<style>
	@import '../assets/Loger.css';
	@import '../assets/form.css';
</style>