<template>
	<h1>hi</h1>
</template>
<script>
	export default{
		name: "lmSettings",
		setup(){
			document.querySelector("head meta[name='robots']").setAttribute("content","noindex, nofollow");
			document.querySelector("head title").textContent = "تنظیمات - لایت مگ";
		}
	};
</script>