<template>
	<div class="page">
		<div class="page-content lm-page">
			<router-view :key="this.$route.path"/>
		</div>
	</div>
</template>
<script>
	export default{
		name: "Add"
	};
</script>