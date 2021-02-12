<template>
	<div id="Loger">
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
		
		
		
		نمایش پسوورد
		<br>
		footer should not show up here !
	</div>
</template>
<script>
	export default{
		name: "Loger",
	};
</script>
<style>
	@import '../assets/Loger.css';
	@import '../assets/form.css';
</style>