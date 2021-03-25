<template>
	<div id="page" class="page" v-if="APIData">
		<div class="right ed-bk">
			<div class="page-halfer">
				<h2 class="half">مقالات <router-link :to="{name:'user-posts',params:{username:username}}">{{APIData.name}}</router-link></h2>
			</div>
			<tabbednav :key="username" ths="مقالات" :ps="'articles/user/api/v1/'+username" ls="/article/"/>
		</div>
		<sidebar/>
	</div>
	<topslider/>
</template>
<script>
	import sidebar from '@/components/sidebar.vue';
	import topslider from '@/components/topslider.vue';
	import {useStore} from 'vuex';
	import {useRoute} from 'vue-router';
	import {computed,watch} from 'vue';
	import {getAPI} from '@/axios.js';
	import tabbednav from '@/components/tabbednav.vue';
	export default{
		name: "userPosts",
		props: ['username'],
		setup(props){
			const store = useStore()
			const APIData = computed(()=>store.state.APIData);
			async function get_user(uname){
				try{
					const res = await getAPI.get("users/api/v1/"+uname+'/')
					store.state.APIData = res.data;
				}catch(err){
					console.log(err);
					console.log(err.response);
				}
			}
			get_user(props.username);
			const route = useRoute();
			watch(
				()=>route.params.username,
				newUname=>{
					get_user(newUname);
				}
			);
			return{APIData}
		},
		components:{sidebar,tabbednav,topslider}
	};
</script>
<style>
	@import '../assets/page-halfer.css';
</style>