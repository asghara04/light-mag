<template>
	<h2>dashboard</h2>
</template>
<script>
	export default{
		name: 'lm-admin',
		setup(){
			document.querySelector("head title").textContent = "داشبورد - لایت مگ";
			document.querySelector("head meta[name='robots']").setAttribute("content","noindex, nofollow")

		}
	};
</script>