<template>
	<div v-if="APIData" class="page">
		<div class="page-content lm-page cen">
			<h1>{{APIData.name}}</h1>
			<div v-if="APIData.image" class="art-pic">
				<img :src="APIData.image.image" :alt="APIData.image.alt" :name="APIData.image.name">
			</div>
			<hr v-else>
			<p class="like-h2" v-if="subcats!=false">زیردسته ها</p>
			<button v-if="subcats==false" @click="get_subcats()" class="lm-link lm-blue">نمایش زیردسته ها</button>
			<div v-if="subcats!=false">
				<p class="link-like">کل: {{subcats.count}}</p>
				<div class="medium-list">
					<article v-for="(sub,i) in subcats.results" :key="i" :id="sub.slug" class="art">
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

			async function get_cat(slug){
				try{
					const res = await getAPI.get("categories/api/v1/"+slug, {headers:{Authorization: `JWT ${store.state.accessToken}`}});
					store.state.APIData = res.data;
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
			async function get_subcats(){
				try{
					const res = await getAPI.get("categories/subs/api/v1/"+APIData.value.id,{headers: {Authorization: `JWT ${store.state.accessToken}`}});
					subcats.value = res.data;
				}catch(err){
					console.log(err);
				}
			}

			return{APIData,get_subcats,subcats}
		}
	};
</script>
<style>
	@import '../assets/light-mag.css';
	@import '../assets/medium-list.css';
</style>