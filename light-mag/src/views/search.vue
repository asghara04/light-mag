<template>
	<div id="page" class="page">
		<div class="right">
			<div class="search-div ed-bk">
				<h2 class="cen">جستوجو در لایت مگ</h2>
				<form class="q-form">
					<input type="search" name="q" class="q-field" maxlength="100" required="">
					<button class="q-button">جستوجو</button>
				</form>
			</div>
		</div>
		<sidebar/>
	</div>
</template>
<script>
	import sidebar from '@/components/sidebar.vue';
	export default{
		name: "Search",
		setup(){
		},
		components:{sidebar}
	};
</script>
<style>
	@import '../assets/search.css';
	@import '../assets/light-mag.css';
	@import '../assets/topnav.css';
</style>