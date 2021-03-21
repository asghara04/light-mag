<template>
	<div class="page">
		<div class="ed-bk lm-page" v-if="APIData">
			<div class="lm-page-head">
				<h2>دسته ها</h2>
				<router-link to="/LM-admin/add/category" class="text-icon lm-link lm-blue"><img src="../assets/imgs/add.svg">جدید</router-link>
			</div>
			<hr>
			<div class="page-halfer">
				<p @click.prevent="get_cats(current)" class="half link-like">تازه سازی</p>
				<p class="half link-like">کل: {{APIData.count}}</p>
			</div>
			<div v-if="APIData.results!=false" class="medium-list">
				<article v-for="(cat, i) in APIData.results" :key="i" class="art">
					<h2>{{cat.name}}</h2>
					<img v-if="cat.image" :src="cat.image.image" :alt="cat.image.alt" :name="cat.image.name">
					<div class="page-halfer">
						<router-link :to="{name: 'change-category',params:{catslug:cat.slug}}" class="text-icon half lm-link lm-green"><img src="../assets/imgs/edit.svg">تغییر</router-link>
						<router-link class="link-like" :to="{name: 'lm-category', params:{slug: cat.slug}}">نمایش</router-link>
						<a class="text-icon half lm-link lm-red" @click.prevent="rm(cat.slug,i)"><img src="../assets/imgs/delete.svg">حذف</a>
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
		name: "lm-articles",
		props: {"page":Number},
		setup(props){
			const current = ref(1);
			const size = ref(10);
			const store = useStore();

			async function set_current(){
				try{
					const res = await getAPI.get("categories/all/api/v1/count/", {headers: {Authorization: `JWT ${store.state.accessToken}`}});
					if((props.page)<=parseInt((res.data.count+size.value-1)/size.value)){
						current.value = props.page||1;
					}
					get_cats(current.value);
				}catch(err){
					console.log(err);
				}
			}
			set_current();

			const APIData = computed(()=> store.state.APIData);
			async function get_cats(current){
				try{
					const res = await getAPI.get("categories/api/v1/?page="+current, {headers: {Authorization: `JWT ${store.state.accessToken}`}});
					store.state.APIData = res.data;
				}catch(err){
					console.log(err);
					console.log(err.response);
				}
			}

			async function rm(catslug, i){
				if(confirm(`آیا قصد حذف دسته ${APIData.value.results[i].name} را دارید؟\nاگر دسته را پاک کنید تمام زیردسته ها پاک و تمام مقلات این دسته بدون دسته میشوند.`)){
					try{
						const res = await getAPI.delete("categories/api/v1/"+catslug, {headers: {Authorization: `JWT ${store.state.accessToken}`}});
						if(res.status===204){
							get_cats(current.value)
						}else{
							console.log(res.data)
							alert('حذف با خطا مواجه شد.')
						}
					}catch(err){
						console.log(err);
					}
				}
			}

			watch(
				()=> props.page,
				()=> {
					set_current();
				}
			);

			return{APIData, current, get_cats, rm}
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