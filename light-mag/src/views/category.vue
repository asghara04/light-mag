<template>
	<Lheader/>
	<topslider/>
	<div v-if="APIData" id="page" class="page">
		<div class="right page-content">
			<router-view/>
			<article class="page-halfer">
				<div class="half img-sider">
					<img :src="APIData.image.image" class="side-img">
					<h2>{{APIData.name}}</h2>
				</div>
				<div class="half"></div>
			</article>
			<tabbednav ths="زیردسته ها|نوشته ها" :ps="'categories/subs/api/v1/'+APIData.id+'|articles/cat/api/v1/'+APIData.id" tns='subcat|article' :ls="'/categories/'+APIData.slug+'/|/article/'"/>
		</div>
		<sidebar/>
	</div>
</template>
<script>
	import Lheader from '@/components/Lheader.vue';
	import topslider from '@/components/topslider.vue';
	import sidebar from '@/components/sidebar.vue';
	import tabbednav from '@/components/tabbed-nav.vue';
	import {useStore} from 'vuex';
	import {computed, watch} from 'vue';
	import {getAPI} from '@/axios.js';
	import {useRoute} from 'vue-router';
	export default{
		name: "category",
		props: ["slug"],
		components:{
			Lheader,
			topslider,
			sidebar,
			tabbednav
		},
		setup(props){
			const store = useStore();
			const APIData = computed(()=> store.state.APIData);

			function get_cat(slug){
				getAPI.get("categories/api/v1/"+slug)
				.then(res => store.state.APIData = res.data)
				.catch(err => console.log(err))
			}
			get_cat(props.slug)

			const route = useRoute()

			watch(
				()=> route.params.slug,
				newSlug => {
					get_cat(newSlug)
				}
			)

			return {APIData}
		}
	};
</script>
<style>
	@import '../assets/page-halfer.css';
	@import '../assets/img-sider.css';
</style>