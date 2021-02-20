<template>
	<div id="Lfooter" class="ed-color">
		<div v-if="pub">
			<router-link to="/about">درباره</router-link> - 
			<router-link to="/contact">ارتباط</router-link>
			<p>توسعه دهنده و برنامه نویس <strong>اصغر اله</strong></p>
		</div>
		<p>&#169; <strong>مجله نور</strong> 2021</p>
	</div>
</template>

<script>
	export default{
		name: "Lfooter",
		data(){
			return{
				pub: true
			}
		}
	};
</script>

<style>
	@import '../assets/footer.css';
</style>