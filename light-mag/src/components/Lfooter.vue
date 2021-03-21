<template>
	<footer id="footer" class="ed-color">
		<div v-if="wich!=='admin'" class="footer-details">
			<router-link to="/about">درباره</router-link> - 
			<router-link to="/contact">ارتباط</router-link>
			<p>توسعه دهنده و برنامه نویس <strong>اصغر اله</strong></p>
		</div>
		<p class="name">&#169; <strong>لایت مگ</strong> 2021</p>
	</footer>
</template>

<script>
	export default{
		name: "Lfooter",
		props:["wich"]
	};
</script>

<style>
	@import '../assets/footer.css';
</style>