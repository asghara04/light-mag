<template>
	<div v-if="subcat">
		<span>
			<router-link to='/' rel="مجله نور">صفحه اصلی</router-link> > <router-link :to="{name: 'category', params:{catslug: catslug}}">{{subcat.category}}</router-link> > <router-link :to="{name: 'subcat', params: {catslug: catslug, subcatname: subcat.slug}}">{{subcat.name}}</router-link>
		</span>
		<article class="page-halfer">
			<div class="half img-sider">
				<router-link :to="{name: 'subcat', params: {catslug: catslug, subcatname: subcat.slug}}" :rel="subcat.name"><img :src="subcat.image.image" :alt="subcat.image.alt" :name="subcat.image.name" class="side-img"></router-link>
				<h2><router-link :to="{name: 'subcat', params: {catslug: catslug, subcatname: subcat.slug}}" :rel="subcat.name">{{subcat.name}}</router-link></h2>
			</div>
			<div class="half"></div>
		</article>
		<tabbednav :key="this.$route.params.subcatname" ths="نوشته ها" :ps="'articles/cat/sub/api/v1/'+subcat.id" ls="/article/"/>
		<hr>
		<p class="like-h2">در دسته :</p>
	</div>
</template>
<script>
	import {ref, watch} from 'vue';
	import {useRoute} from 'vue-router';
	import {getAPI} from '@/axios.js';
	import tabbednav from '@/components/tabbednav.vue';
	export default{
		name: "Subcat",
		props: ['catslug', "subcatname", 'id'],
		setup(props){
			const subcat = ref(null);

			function get_subcat(slug){
				getAPI.get("categories/sub/api/v1/"+props.id+'/'+slug)
				.then(res => subcat.value = res.data)
				.catch(err => console.log(err))
			}
			get_subcat(props.subcatname)

			const route = useRoute();
			watch(
				()=> route.params.subcatname,
				newSubcatname => {
					if(route.name==="subcat"){
						get_subcat(newSubcatname)
					}
				}
			)

			return{subcat}
		},
		components:{
			tabbednav
		}
	};
</script>
<style>
	@import '../assets/page-halfer.css';
	@import '../assets/img-sider.css';
</style>