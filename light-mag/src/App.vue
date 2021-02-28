<template>
	<topnav v-if="wich()!=='admin'"/>
	<lmnav v-if="wich()==='admin'&&this.$store.getters.logedIn"/>
	<router-view/>
	<Lfooter :wich="wich()"/>
</template>

<script>
import topnav from '@/components/topnav.vue';
import Lfooter from '@/components/Lfooter.vue';
import lmnav from "@/components/lm-nav.vue";
export default {
	name: 'App',
	components: {
		topnav,
		Lfooter,
		lmnav
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