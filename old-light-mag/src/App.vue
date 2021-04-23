<template>
	<topnav v-if="wich()!=='admin'"/>
	<Lheader v-if="wich()!=='admin'"/>
	<lmnav :key="this.$store.getters.logedIn" v-if="wich()==='admin'&&this.$store.getters.logedIn"/>
	<router-view/>
	<Lfooter :key="wich()" :wich="wich()"/>
</template>
<script>
import topnav from '@/components/topnav.vue';
import Lfooter from '@/components/Lfooter.vue';
import lmnav from "@/components/lm-nav.vue";
import Lheader from '@/components/Lheader.vue';
export default {
	name: 'App',
	components: {
		topnav,
		Lfooter,
		Lheader,
		lmnav
	},
	setup(){
		function wich(){
			return window.location.host.split('.')[0]
		}
		return{wich}
	}
};
</script>
<style>
	@import './assets/light-mag.css';
</style>