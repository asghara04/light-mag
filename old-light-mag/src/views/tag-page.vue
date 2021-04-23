<template>
	<topslider/>
	<div id="page" class="page" v-if="APIData">
		<div class="right ed-bk">
			<div class="page-halfer">
				<h2><router-link :to="{name:'tag-page',params:{tagslug:APIData.slug}}">{{APIData.name}}</router-link></h2>
				<div class="add"></div>
			</div>
			<tabbednav v-if="this.$route.name==='tag-page'" :key="tagslug" ths="مقالات" :ps="'articles/tag/api/v1/'+tagslug" ls="/article/"/>
		</div>
		<sidebar/>
	</div>
</template>
<script>
	import {computed,watch} from 'vue';
	import {getAPI} from '@/axios.js';
	import {useStore} from 'vuex';
	import {useRoute}from 'vue-router';
	import sidebar from '@/components/sidebar.vue';
	import tabbednav from '@/components/tabbednav.vue';
	import topslider from '@/components/topslider.vue';
	export default{
		name: "tagPage",
		components:{sidebar,tabbednav,topslider},
		props:['tagslug'],
		setup(props){
			const store = useStore();
			const APIData = computed(()=>store.state.APIData);
			async function get_tag(slug){
				try{
					const res = await getAPI.get("tags/api/v1/"+slug+'/');
					store.state.APIData = res.data;
					document.querySelector("head title").textContent = APIData.value.name+" - لایت مگ";
					document.querySelector("head meta[name='description']").setAttribute("content","تگ "+APIData.value.name);
					document.querySelector("head meta[name='keywords']").setAttribute("content",APIData.value.name);
				}catch(err){
					console.log(err)
					alert("خطایی رخ داد.")
				}
			}
			get_tag(props.tagslug)
			const route = useRoute();
			watch(
				()=>route.params.tagslug,
				newTagslug=>{
					if(route.name==="tag-page"){
						get_tag(newTagslug);
					}
				}
			);
			return{APIData}
		}
	};
</script>
<style>
	@import '../assets/page-halfer.css';
</style>