<template>
	<div v-if="data[0]" id="tabbednav">
		<button v-for="(tab, index) in data" :key="tab.active" @click="get_data(index)" class='tab-head' :class="{'active':tab.active}">{{tabheads[index]}}</button>
	</div>
	<div class="tab-body" v-for="(tab,i) in data" :key="i">
		<div v-if='tab.active!=false' ref="paginate">
			<div v-if="tab.data!=false" class="medium-list">
				<article v-for="art in tab.data" :key="art.id" class="art">
					<router-link :to="tab.link+art.slug">
						<h2>{{art.name}}{{art.title}}</h2>
						<img :src="art.image.image" :alt="art.image.alt" :name="art.image.art">
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
	import {ref} from 'vue';
	import {getAPI} from '@/axios.js';
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
			async function set_props(){
				tabheads.value = props.ths.split("|");
				endpoints.value = props.ps.split("|");
				links.value = props.ls.split("|");
			}
			set_props()

			function set_datas(){
				for(var i=0;i<tabheads.value.length;i++){
					datas.value.push({title: tabheads.value[i], endpoint: endpoints.value[i], active: false, api_data: []})
				}
			}
			set_datas()

			function set_data(){
				for(var i=0;i<tabheads.value.length;i++){
					data.value[i] = {active: datas.value[i].active, data: datas.value[i].api_data, link: links.value[i]}
				}
			}
			let more = false;
			async function get_data(i){
				try{
					const res = await getAPI.get(datas.value[i].endpoint);
					for(var n=0;n<res.data.results.length;n++){
						datas.value[i].api_data.push(res.data.results[n]);
					}
					for(var x=0;x<tabheads.value.length;x++){
						datas.value[x].active = false;
					}
					datas.value[i].active = true;
					datas.value[i].endpoint = res.data.next;
					more = true;
					set_data();
					window.addEventListener("scroll",()=>{if(datas.value[i].endpoint!=null){pagination(datas.value[i].endpoint,i);}})
				}catch(err){
					console.log(err);
				}
			}
			get_data(0);

			async function pagination(end,i){
				let bottom = ((window.scrollY+window.innerHeight)>=(paginate.value.offsetTop+paginate.value.offsetHeight-20)&&(window.scrollY+window.innerHeight)<(paginate.value.offsetTop+paginate.value.offsetHeight));
				if(more&&end&&bottom===true){
					more = false;
					get_data(i);
				}
			}

			return{data,tabheads,links,get_data,paginate}
		}
	};
</script>
<style>
	@import '../assets/tabbednav.css';
	@import '../assets/medium-list.css';
</style>