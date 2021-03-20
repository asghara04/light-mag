<template>
	<lmNav/>
	<div class="page">
		<div class="page-content lm-page">
			<router-view :key="this.$route.path"/>
		</div>
	</div>
</template>
<script>
	import lmNav from '@/components/lm-nav.vue';
	export default{
		name: "Add",
		components: {lmNav}
	};
</script>