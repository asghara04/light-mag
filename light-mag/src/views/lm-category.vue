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
			<div v-if="subcats!=false" ref="paginate">
				<p class="link-like">کل: {{count}}</p>
				<div id="scrollpagination" class="medium-list">
					<article v-for="(sub,i) in subcats" :key="i" :id="sub.slug" class="art">
						<h2>{{sub.name}}</h2>
						<img v-if="sub.image" :src="sub.image.image" :alt="sub.image.alt" :name="sub.name">
					</article>
				</div>
			</div>
			<div class="page-halfer">
				<router-link :to="{name: 'change-category',params:{catslug: APIData.slug}}" class="half lm-link lm-green text-icon"><img src="../assets/imgs/edit.svg">تغییر</router-link>
				<a class="text-icon half lm-link lm-red" @click.prevent="rm()"><img src="../assets/imgs/delete.svg">حذف</a>
			</div>
		</div>
	</div>
</template>
<script>
	import {computed,watch,ref} from 'vue';
	import {getAPI} from '@/axios.js';
	import {useStore} from 'vuex';
	import {useRoute,useRouter} from 'vue-router';
	export default{
		name: "LmCategory",
		setup(){
			const route = useRoute();
			const store = useStore();
			const APIData = computed(() => store.state.APIData);
			const endpoint = ref(null);
			const paginate = ref(null);
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
			let more = false;
			async function get_subcats(end){
				if(endpoint.value&&end){
					try{
						const res = await getAPI.get(end,{headers: {Authorization: `JWT ${store.state.accessToken}`}});
						for(var i=0;i<res.data.results.length;i++){
							subcats.value.push(res.data.results[i]);
						}
						count.value = res.data.count;
						endpoint.value = res.data.next;
						more = true
						window.addEventListener('scroll',()=>pagination(endpoint.value));
					}catch(err){
						console.log(err.response);
					}
				}
			}
			function pagination(end){
				let bottom = (window.scrollY+window.innerHeight)>=(paginate.value.offsetTop+paginate.value.offsetHeight-20)&&(window.scrollY+window.innerHeight)<(paginate.value.offsetTop+paginate.value.offsetHeight);
				if(more&&end&&end===endpoint.value&&bottom===true){
					more = false;
					get_subcats(end);
				}
			}
			const router = useRouter();
			async function rm(){
				if(confirm(`آیا قصد حذف دسته ${APIData.value.name} را دارید؟\nاگر دسته را پاک کنید تمام زیردسته ها پاک و تمام مقلات این دسته بدون دسته میشوند.`)){
					try{
						const res = await getAPI.delete("categories/api/v1/"+APIData.value.slug, {headers: {Authorization: `JWT ${store.state.accessToken}`}});
						if(res.status===204){
							router.push({name: "lm-categories"})
						}else{
							console.log(res.data)
							alert('حذف با خطا مواجه شد.')
						}
					}catch(err){
						console.log(err);
					}
				}
			}
			return{APIData,get_subcats,subcats,count,paginate,endpoint,rm}
		}
	};
</script>
<style>
	@import '../assets/light-mag.css';
	@import '../assets/medium-list.css';
	@import '../assets/page-halfer.css';
	@import '../assets/lm-page.css';
</style>