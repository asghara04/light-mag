<template>
	<topslider/>
	<div v-if="APIData.slug==this.$route.params.catslug" id="page" class="page">
		<div class="right ed-bk">
			<router-view :key="this.$route.params.catslug"/>
			<span>
				<router-link to="/" rel="مجله نور">صفحه اصلی</router-link> > <router-link :to="{name: 'category', params: {catslug: APIData.slug}}">{{APIData.name}}</router-link>
			</span>
			<article class="page-halfer">
				<div class="half img-sider">
					<router-link v-if="APIData.image" :to="{name: 'category', params: {catslug: APIData.slug}}" :rel="APIData.name" class="side">
						<img :src="APIData.image.image" :alt="APIData.image.alt" :name="APIData.image.name" class="side-img">
					</router-link>
					<h2><router-link :to="{name: 'category', params:{catslug: APIData.slug}}">{{APIData.name}}</router-link></h2>
				</div>
				<div class="half"></div>
			</article>
			<tabbednav :key="this.$route.params.catslug" ths="زیردسته ها|نوشته ها" :ps="'categories/subs/api/v1/'+APIData.id+'|articles/cat/api/v1/'+APIData.id" :ls="'/categories/'+APIData.slug+'/|/article/'"/>
		</div>
		<sidebar/>
	</div>
</template>
<script>
	import topslider from '@/components/topslider.vue';
	import sidebar from '@/components/sidebar.vue';
	import tabbednav from '@/components/tabbednav.vue';
	import {useStore} from 'vuex';
	import {computed, watch} from 'vue';
	import {getAPI} from '@/axios.js';
	import {useRoute} from 'vue-router';
	export default{
		name: "Category",
		props: ["catslug"],
		components:{
			topslider,
			sidebar,
			tabbednav
		},
		setup(props){
			const store = useStore();
			const APIData = computed(()=> store.state.APIData);
			async function get_cat(slug){
				try{
					const res = await getAPI.get("categories/api/v1/"+slug);
					store.state.APIData = res.data;
					document.querySelector("head title").textContent = APIData.value.name+" - لایت مگ";
					document.querySelector("head meta[name='description']").setAttribute("content","توضیحات درباره دسته "+APIData.value.name)
					document.querySelector("head meta[name='keywords']").setAttribute("content",APIData.value.name)

				}catch(err){
					console.log(err);
				}
			}
			get_cat(props.catslug);
			const route = useRoute();
			watch(
				()=> route.params.catslug,
				newSlug => {
					if(route.name==="category"){
						get_cat(newSlug);
					}
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