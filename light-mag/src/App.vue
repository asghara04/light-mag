<template>
	<topnav/>
	<router-view :key="$route.path"/>
	<Lfooter/>
</template>

<script>
import topnav from '@/components/topnav.vue';
import Lfooter from '@/components/Lfooter.vue';
export default {
	name: 'App',
	components: {
		topnav,
		Lfooter
	}
};
</script>

<style>
	@import 'assets/light-mag.css';
</style>