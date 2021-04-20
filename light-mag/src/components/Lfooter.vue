<template>
	<footer id="footer" class="ed-color">
		<div v-if="wich!=='admin'" class="footer-details">
			<div class="page-halfer">
				<div class="half">
					<p></p>
					<router-link to="/about" class="link-like" rel="درباره لایت مگ">درباره لایت مگ</router-link>
				</div>
				<div class="half">
					<router-link class="link-like" to="/contact" rel="ارتباط با لایت مگ">ارتباط با لایت مگ</router-link>
				</div>
			</div>
			<p>توسعه دهنده و برنامه نویس <strong>اصغر اله</strong></p>
		</div>
		<p class="name">&#169; <strong>لایت مگ</strong> 2021</p>
		<div id='mediaad-wGUw'></div>
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
	@import '../assets/page-halfer.css';
</style>