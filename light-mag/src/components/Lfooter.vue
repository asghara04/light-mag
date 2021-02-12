<template>
	<div id="Lfooter" class="ed-color">
		<div v-if="pub">
			<router-link to="/about">درباره</router-link> - 
			<router-link to="/contact">ارتباط</router-link>
			<p>develped by asghar ale 2021</p>
		</div>
		<p>&#169; copyright 2021</p>
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