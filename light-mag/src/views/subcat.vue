<template>
	<div v-if="subcat">
		<article class="page-halfer">
			<div class="half img-sider">
				<img :src="subcat.image.image" :alt="subcat.image.alt" :name="subcat.image.name" class="side-img">
				<h2>{{subcat.name}}</h2>
			</div>
			<div class="half"></div>
		</article>
		<tabbednav ths="نوشته ها" :ps="'articles/cat/sub/api/v1/'+subcat.id" tns="article" ls="/article/"/>
		<hr>
		<p class="like-h2">در دسته :</p>		
	</div>
</template>
<script>
	import {ref, watch} from 'vue';
	import {useRoute} from 'vue-router';
	import {getAPI} from '@/axios.js';
	import tabbednav from '@/components/tabbed-nav.vue';
	export default{
		name: "subcat",
		props: ['slug', "name"],
		setup(props){
			const subcat = ref(null);

			function get_subcat(slug){
				getAPI.get("categories/sub/api/v1/"+slug)
				.then(res => subcat.value = res.data)
				.catch(err => console.log(err))
			}
			get_subcat(props.name)

			const route = useRoute();
			watch(
				()=> route.params.name,
				newName => {
					get_subcat(newName)
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