<template>
	<div v-if="subcat.slug==this.$route.params.subcatname">
		<span>
			<router-link to='/' rel="مجله نور">صفحه اصلی</router-link> > <router-link :to="{name: 'category', params:{catslug: catslug}}">{{subcat.category}}</router-link> > <router-link :to="{name: 'subcat', params: {catslug: catslug, subcatname: subcat.slug}}">{{subcat.name}}</router-link>
		</span>
		<article class="page-halfer">
			<div class="half img-sider">
				<router-link v-if="subcat.image" :to="{name: 'subcat', params: {catslug: catslug, subcatname: subcat.slug}}" :rel="subcat.name" class="side">
					<img :src="subcat.image.image" :alt="subcat.image.alt" :name="subcat.image.name" class="side-img">
				</router-link>
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
	import {ref,watch} from 'vue';
	import {useRoute} from 'vue-router';
	import {getAPI} from '@/axios.js';
	import tabbednav from '@/components/tabbednav.vue';
	export default{
		name: "Subcat",
		props: ['catslug', "subcatname"],
		setup(props){
			const subcat = ref({});

			async function get_subcat(slug,subslug){
				try{
					const res = await getAPI.get('categories/sub/api/v1/'+slug+'/'+subslug);
					subcat.value = res.data;
					document.querySelector("head title").textContent = subcat.value.name+" - لایت مگ";
					document.querySelector("head meta[name='description']").setAttribute("content","زیردسته "+subcat.value.name);
					document.querySelector("head meta[name='keywords']").setAttribute("content",subcat.value.name);
				}catch(err){
					console.log(err)
				}
			}
			get_subcat(props.catslug,props.subcatname)

			const route = useRoute();
			watch(
				()=> route.params.subcatname,
				(newSubcatname) => {
					if(route.name==="subcat"&&route.params.catslug===props.catslug&&newSubcatname){
						get_subcat(props.catslug,newSubcatname)
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