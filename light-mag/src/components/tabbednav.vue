<template>
	<div v-if="data[0]" id="tabbednav">
		<button v-for="(tab, index) in data" :key="tab.active" @click.prevent="get_data(index)" class='tab-head' :class="{'active':tab.active}">{{tabheads[index]}}</button>
	</div>
	<div class="tab-body" v-for="tab in data" :key="tab.active">
		<div v-if='tab.active!=false'>
			<div v-if="tab.data!=false" class="medium-list">
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
		name: "Tabbednav",
		props:["ths", "ps", "ls"],
		setup(props){
			const tabheads = ref([]);
			const endpoints = ref();
			const datas = ref([]);
			const data = ref([]);
			const links = ref();

			async function set_props(){
				tabheads.value = props.ths.split("|");
				endpoints.value = props.ps.split("|");
				links.value = props.ls.split("|");
			}
			set_props()

			function set_datas(){
				for(var i=0;i<tabheads.value.length;i++){
					datas.value.push({title: tabheads.value[i], endpoint: endpoints.value[i], active: false, api_data: null})
				}
			}
			set_datas()

			function set_data(){
				for(var i=0;i<tabheads.value.length;i++){
					data.value[i] = {active: datas.value[i].active, data: datas.value[i].api_data, link: links.value[i]}
				}
			}

			function get_data(i){
				getAPI.get(datas.value[i].endpoint)
				.then(res => {
					datas.value[i].api_data = res.data.results;
					for(var n=0;n<tabheads.value.length;n++){
						datas.value[n].active = false;
					}
					datas.value[i].active = true;
					set_data();
				})//pagination needed a button down there to show more...
				.catch(err => console.log(err))
			}
			get_data(0);

			return{data, tabheads, links, get_data}
		}
	};
</script>
<style>
	@import '../assets/tabbednav.css';
	@import '../assets/medium-list.css';
</style>