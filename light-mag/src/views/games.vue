<template>
	<div class="page" id="page">
		<div class="right">
			<h1 class="cen"><span class="like-h2">بازی های لایت مگ</span></h1>
			<div class="medium-list">
				<article class="art">
					<h2>2048</h2>
				</article>
				<article class="art">
					<h2>snake</h2>
				</article>
				<article class="art">
					<h2>archry</h2>
				</article>
				<article class="art">
					<h2>biliard</h2>
				</article>
				<article class="art">
					<h2>2048</h2>
				</article>
				<article class="art">
					<h2>2048</h2>
				</article>
			</div>
		</div>
		<sidebar/>
	</div>
	<topslider/>
</template>
<script>
	import sidebar from '@/components/sidebar.vue';
	import topslider from '@/components/topslider.vue';
	export default{
		name: "Games",
		components:{
			sidebar,
			topslider
		}
	};
</script>
<style>
	@import '../assets/medium-list.css';
</style>