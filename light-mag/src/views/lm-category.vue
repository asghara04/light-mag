<template>
	<div v-if="APIData" class="page">
		<div class="page-content lm-page cen">
			<h1>{{APIData.name}}</h1>
			<div v-if="APIData.image" class="art-pic">
				<img :src="APIData.image.image" :alt="APIData.image.alt" :name="APIData.image.name">
			</div>
			<hr v-else>
			<p class="like-h2" v-if="subcats!=false">زیردسته ها</p>
			<a v-if="subcats==false&&endpoint" @click="get_subcats(endpoint)" class="link-like">نمایش زیردسته ها</a>
			<div v-if="subcats!=false">
				<p class="link-like">کل: {{count}}</p>
				<div id="scrollpagination" class="medium-list">
					<article v-for="(sub,i) in subcats" :key="i" :id="sub.slug" class="art">
						<h2>{{sub.name}}</h2>
						<img v-if="sub.image" :src="sub.image.image" :alt="sub.image.alt" :name="sub.name">
					</article>
				</div>
			</div>
		</div>
	</div>
</template>
<script>
	import {computed,watch,ref} from 'vue';
	import {getAPI} from '@/axios.js';
	import {useStore} from 'vuex';
	import {useRoute} from 'vue-router';
	export default{
		name: "LmCategory",
		setup(){
			const route = useRoute();
			const store = useStore();
			const APIData = computed(() => store.state.APIData);
			const endpoint = ref(null);
			async function get_cat(slug){
				try{
					const res = await getAPI.get("categories/api/v1/"+slug, {headers:{Authorization: `JWT ${store.state.accessToken}`}});
					store.state.APIData = res.data;
					endpoint.value = "categories/subs/api/v1/"+APIData.value.id+'/?page=1';
				}catch(err){
					alert("خطایی رخ داد.")
					console.log(err)
				}
			}
			get_cat(route.params.slug);

			watch(
				()=> route.params.slug,
				(newSlug) => {
					if(route.name=="lm-category"){
						get_cat(newSlug);
					}
				}
			)
			const subcats = ref([]);
			const count = ref(null);
			
			async function get_subcats(end){
				if(endpoint.value!=false){
					try{
						const res = await getAPI.get(end,{headers: {Authorization: `JWT ${store.state.accessToken}`}});
						for(var i=0;i<res.data.results.length;i++){
							subcats.value.push(res.data.results[i]);
						}
						count.value = res.data.count;
						endpoint.value = res.data.next;
						window.addEventListener("scroll",()=>{pagination(window,endpoint.value);})
					}catch(err){
						console.log(err.response);
					}
				}
			}
			function pagination(elem,end){
				let bottom = (elem.innerHeight+elem.pageYOffset)>=(document.body.offsetHeight-20);
				if(end&&bottom===true){
					get_subcats(end);
				}
			}
			return{APIData,get_subcats,subcats,count,endpoint}
		}
	};
</script>
<style>
	@import '../assets/light-mag.css';
	@import '../assets/medium-list.css';
</style>