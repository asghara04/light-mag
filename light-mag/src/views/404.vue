<template>
	<p class="err-code">404</p>
	<p class="err-description">اوه! صفحه مورد نظرتون وجود نداره، <router-link to="/">صفحه اصلی</router-link></p>
</template>
<script>
	export default{
		name: "not found"
	};
</script>
<style>
	@import '../assets/err-page.css';
</style>