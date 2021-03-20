<template>
	<div v-if="data[0]" id="tabbednav">
		<button v-for="(tab, i) in data" :key="tab.active" @click="reset_call(i)" class='tab-head' :class="{'active':tab.active}">{{tabheads[i]}}</button>
	</div>
	<div class="tab-body" v-for="(tab,i) in data" :key="i">
		<div v-if='tab.active!=false' ref="paginate">
			<p>کل: {{tab.count}}</p>
			<div v-if="tab.data!=false" class="medium-list">
				<article v-for="art in tab.data" :key="art.id" class="art">
					<router-link :to="tab.link+art.slug">
						<h2>{{art.name}}{{art.title}}</h2>
						<img v-if="art.image" :src="art.image.image" :alt="art.image.alt" :name="art.image.art">
					</router-link>
				</article>
			</div>
			<div v-else class="center-parent">
				<p class="cen like-h2">متاسفیم! اطلاعاتی برای نمایش وجود ندارد.</p>
			</div>
		</div>
	</div>
</template>
<script>
	import {ref,onBeforeUnmount} from 'vue';
	import {getAPI} from '@/axios.js';
	import {useRouter} from 'vue-router';
	export default{
		name: "Tabbednav",
		props:["ths", "ps", "ls"],
		setup(props){
			const tabheads = ref([]);
			const endpoints = ref();
			const datas = ref([]);
			const data = ref([]);
			const links = ref();
			const paginate = ref(null);
			const activet = ref(0);
			async function set_props(){
				tabheads.value = props.ths.split("|");
				endpoints.value = props.ps.split("|");
				links.value = props.ls.split("|");
			}
			set_props();
			function set_datas(){
				for(var i=0;i<endpoints.value.length;i++){
					datas.value.push({title: tabheads.value[i], endpoint: endpoints.value[i], active: false, api_data: [],count: 0})
				}
			}
			set_datas();
			function set_data(){
				for(var i=0;i<endpoints.value.length;i++){
					data.value[i] = {active: datas.value[i].active, data: datas.value[i].api_data, link: links.value[i],count: datas.value[i].count}
				}
			}
			function reset_call(i){
				datas.value[i].endpoint = endpoints.value[i];
				datas.value[i].api_data = [];
				return get_data(i);
			}
			const router = useRouter();
			let more = false;
			async function get_data(i){
				if(datas.value[i].endpoint){
					try{
						const res = await getAPI.get(datas.value[i].endpoint);
						for(var n=0;n<res.data.results.length;n++){
							datas.value[i].api_data.push(res.data.results[n]);
						}
						for(var x=0;x<endpoints.value.length;x++){
							datas.value[x].active = false;
						}
						datas.value[i].active = true;
						datas.value[i].endpoint = res.data.next;
						datas.value[i].count = res.data.count;
						more = true;
						activet.value = i;
						set_data();
						window.addEventListener("scroll",pagination);
					}catch(err){
						console.log(datas.value[i].endpoint)
					}
				}else{
					router.go();
				}
			}
			get_data(activet.value);
			function pagination(){
				if(paginate.value){
					let bottom = ((window.scrollY+window.innerHeight)>=(paginate.value.offsetTop+paginate.value.offsetHeight-20)&&(window.scrollY+window.innerHeight)<(paginate.value.offsetTop+paginate.value.offsetHeight));
					if(more&&datas.value[activet.value].endpoint&&bottom===true){
						more = false;
						get_data(activet.value);
					}
				}
			}
			onBeforeUnmount(()=>{
				window.removeEventListener('scroll', pagination);
			});
			return{data,tabheads,links,get_data,paginate,reset_call}
		}
	};
</script>
<style>
	@import '../assets/tabbednav.css';
	@import '../assets/medium-list.css';
</style>