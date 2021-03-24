<template>
	<div class="lm-page">
		<div class="lm-page-head ed-bk">
			<h2>مقالات</h2>
			<router-link to="/LM-admin/add/article" class="text-icon lm-link lm-blue"><img src="../assets/imgs/add.svg">جدید</router-link>
		</div>
		<div class="page-halfer ed-bk">
			<p class="link-like half">کل: {{count}}</p>
		</div>
		<div ref="paginate" class="spcial-list" v-if="APIData!=false">
			<article class="article" v-for="(art,i) in APIData" :key="i" :class="{'yay-sider':art.image}">
				<router-link v-if="art.image" class="sider" :rel="art.name" :to="'#'"><img :src="art.image.image" :alt="art.image.alt" :name="art.image.name"></router-link>
				<div class="high-content">
					<h2><router-link :rel="art.name" :name='art.name' to="#">{{art.name}}</router-link></h2>
					<hr>

					<div class="page-halfer">
						<router-link :to="'#'" class="text-icon half lm-link lm-green"><img src="../assets/imgs/edit.svg">تغییر</router-link>
						<a class="text-icon half lm-link lm-red" @click.prevent="rm(art.id,i)"><img src="../assets/imgs/delete.svg">حذف</a>
					</div>
				</div>
			</article>
		</div>
	</div>
</template>
<script>
	import {computed,ref} from 'vue';
	import {useStore} from 'vuex';
	import {getAPI} from '@/axios.js';
	export default{
		name: "lm-articles",
		setup(){
			const store = useStore();
			const APIData = computed(()=>store.state.APIData);
			const endpoint = ref("articles/mapi/v1/");
			const count = ref(0);

			async function get_arts(end){
				try{
					const res = await getAPI.get(end,{headers:{Authorization:`JWT ${store.state.accessToken}`}});
					store.state.APIData = res.data.results;
					endpoint.value = res.data.next;
					count.value = res.data.count;
				}catch(err){
					console.log(err);
					console.log(err.response);
				}
			}
			get_arts(endpoint.value);
			return{APIData,count}
		}
	};
</script>
<style>
	@import '../assets/page-halfer.css';
	@import '../assets/lm-page.css';
	@import '../assets/home-spcial-list.css';
</style>