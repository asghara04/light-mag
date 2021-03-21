<template>
	<div class="page">
		<div v-if="APIData" class="ed-bk lm-page">
			<div class="lm-page-head">
				<h2>تصاویر</h2>
				<router-link to="/LM-admin/add/image" class="text-icon lm-link lm-blue"><img src="../assets/imgs/add.svg"> جدید</router-link>
			</div>
			<hr>
			<div class="page-halfer">
				<p @click.prevent="get_imgs(current)" class="link-like half">تازه سازی</p>
				<p class="link-like half">کل: {{APIData.count}}</p>
			</div>
			<div v-if="APIData.results" class="medium-list">
				<article v-for="(img, i) in APIData.results" :key="i" class="art">
					<h2>{{img.name}}</h2>
					<img :src="img.image">
					<div class="page-halfer">
						<router-link :to="'/LM-admin/change/image/'+img.id" class="text-icon half lm-link lm-green"><img src="../assets/imgs/edit.svg">تغییر</router-link>
						<a class="text-icon half lm-link lm-red" @click.prevent="rm(img.id, i)"><img src="../assets/imgs/delete.svg">حذف</a>
					</div>
				</article>
			</div>
			<pagination :current="current" :all="APIData.count" :size="10"/>
		</div>
	</div>
</template>
<script>
	import {ref,computed,watch} from 'vue';
	import {useStore} from 'vuex';
	import {getAPI} from '@/axios.js';
	import pagination from '@/components/pagination.vue';
	export default{
		name: 'lm-images',
		props: ["page"],
		setup(props){
			const current = ref(1);
			const size = ref(10);
			const store = useStore();
			
			async function set_current(){
				try{
					const res = await getAPI.get("images/mapi/v1/count/", {headers: {Authorization: `JWT ${store.state.accessToken}`}})
					if((props.page)<=parseInt((res.data.count+size.value-1)/size.value)){
						current.value = props.page||1;
					}
					get_imgs(current.value);
				}catch(err){
					console.log(err);
				}
			}
			set_current();

			const APIData = computed(() => store.state.APIData);
			async function get_imgs(current){
				try{
					const res = await getAPI.get("images/mapi/v1/?page="+current, {headers: {Authorization: `JWT ${store.state.accessToken}`}})
					store.state.APIData = res.data;
				}catch(err){
					console.log(err);
					console.log(err.response);
				}
			}

			async function rm(imgid, i){
				if(confirm(`آیا قصد حذف تصویر ${APIData.value.results[i].name} را دارید؟\nاگر تصویر را حذف کنید تمام مدل های مرتط از جمله مقالات،دسته ها،... بدون تصویر میشوند.`)){
					try{
						await getAPI.delete("images/mapi/v1/"+imgid, {headers: {Authorization: `JWT ${store.state.accessToken}`}});
					get_imgs(current.value);
					}catch(err){
						alert("حذف با خطا مواجه شد.");
						console.log(err);
					}
				}
			}

			watch(
				()=> props.page,
				()=> {
					set_current();
				}
			)
			return{APIData, rm, get_imgs, current}
		},
		components:{
			pagination
		}
	};
</script>
<style>
	@import '../assets/lm-page.css';
	@import '../assets/medium-list.css';
	@import '../assets/page-halfer.css';
</style>