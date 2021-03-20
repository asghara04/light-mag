<template>
	<p class="err-code">404</p>
	<p class="err-description">اوه! صفحه مورد نظرتون وجود نداره، <router-link to="/">صفحه اصلی</router-link></p>
	<topslider/>
</template>
<script>
	import topslider from '@/components/topslider.vue';
	export default{
		name: "not found",
		components:{topslider}
	};
</script>
<style>
	@import '../assets/err-page.css';
</style>