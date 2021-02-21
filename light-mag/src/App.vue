<template>
	<topnav :wich="wich()"/>
	<router-view :key="$route.path"/>
	<Lfooter :wich="wich()"/>
</template>

<script>
import topnav from '@/components/topnav.vue';
import Lfooter from '@/components/Lfooter.vue';
export default {
	name: 'App',
	components: {
		topnav,
		Lfooter
	},
	methods:{
		wich(){
			return window.location.host.split('.')[0]
		}
	}
};
</script>

<style>
	@import 'assets/light-mag.css';
</style>