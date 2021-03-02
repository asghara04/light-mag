<template>
	<div v-if="data[0]" id="tabbed-nav">
		<button v-for="tab in len" :key="tab-1" @click.prevent="get_data(tab-1)" class='tab-head' :class="{'active':data[tab-1].active}">{{tabheads[tab-1]}}</button>
	</div>
	<div class="tab-body" v-for="tab in data" :key="tab.data">
		<div v-if='tab.active'>
			{{tab.data}}
			<div v-if="tab.data" class="medium-list">
				<article v-for="art in tab.data" :key="art.id" class="art">
					<router-link :to="tab.link+art.slug">
						<h2>{{art.name}}{{art.title}}</h2>
						<img :src="art.image.image" :alt="art.image.alt" :name="art.image.art">
					</router-link>
				</article>
			</div>
			<div v-else class="center-parent">
				<p class="centered like-h2">متاسفیم! اطلاعاتی برای نمایش وجود ندارد.</p>
			</div>
		</div>
	</div>
</template>
<script>
	import {ref} from 'vue';
	import {getAPI} from '@/axios.js';
	export default{
		name: "tabbed-nav",
		props:["ths", "ps", "tns", "ls"],
		setup(props){
			const tabheads = ref(props.ths.split("|"));
			const tabnames = ref(props.tns.split("|"));
			const endpoints = ref(props.ps.split("|"));
			const datas = ref([]);
			const len = ref(tabheads.value.length);
			const data = ref([]);
			const links = ref(props.ls.split("|"));

			for(var i=0;i<len.value;i++){
				datas.value.push({title: tabheads.value[i], name: tabnames.value[i], endpoint: endpoints.value[i], active: false, api_data: null})
			}

			function set_data(){
				for(var i=0;i<len.value;i++){
					data.value[i] = {active: datas.value[i].active, data: datas.value[i].api_data, link: links.value[i]}
				}
			}

			async function get_data(i){
				await getAPI.get(datas.value[i].endpoint)
				.then(res => {
					datas.value[i].api_data = res.data.results;
					for(var n=0;n<len.value;n++){
						datas.value[n].active = false;
					}
					datas.value[i].active = true;
					set_data();
				})//pagination needed a button down there to show more...
				.catch(err => console.log(err))
			}
			get_data(0)

			return{data, len, tabheads, links, get_data}
		}
	};
</script>
<style>
	@import '../assets/tabbed-nav.css';
	@import '../assets/medium-list.css';
</style>