<template>
	<div id="light-mag">
		<topnav/>
		<router-view/>
		<Lfooter/>
	</div>
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

<style scoped>
	@import 'assets/light-mag.css'
</style>