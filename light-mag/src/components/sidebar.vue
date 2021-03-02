<template>
	<aside id="sidebar">
		<p>کل نوشته ها: </p>
		<hr>
		<h3 class="down-name"><router-link class="text-icon" name='لایت مگ' to="/"><img src="../assets/imgs/light.svg" alt="LM" name="مجله نور">مجله نور</router-link></h3>
	</aside>
</template>

<script>
	export default{
		name: "sidebar"
	};
</script>

<style>
	@import '../assets/sidebar.css';
</style>