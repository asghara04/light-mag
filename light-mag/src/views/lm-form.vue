<template>
	<div class="page">
		<div class="ed-bk lm-page">
			<router-view :key="this.$route.path"/>
		</div>
	</div>
</template>
<script>
	export default{
		name: "Add",
		setup(){document.querySelector("head meta[name='robots']").setAttribute("content","noindex, nofollow")
}
	};
</script>