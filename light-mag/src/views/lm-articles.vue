<template>
	<div class="lm-page">
		<div class="lm-page-head ed-bk">
			<h2>مقالات</h2>
			<router-link to="/LM-admin/add/article" class="text-icon lm-link lm-blue"><img src="../assets/imgs/add.svg">جدید</router-link>
		</div>
		<div class="page-halfer ed-bk">
			<p class="link-like half">کل: {{count}}</p>
		</div>
		<br>
		<div ref="paginate" class="spcial-list" v-if="APIData!=false">
			<article class="article" v-for="(art,i) in APIData" :key="i" :class="{'yay-sider':art.image}">
				<router-link v-if="art.image" class="sider" :rel="art.name" to="#"><img :src="art.image.image" :alt="art.image.alt" :name="art.image.name"></router-link>
				<div class="high-content">
					<h2><router-link :rel="art.title" to="#">{{art.title}}</router-link></h2>
					<hr>
					<p><span class="blue-text">توضیحات: </span>{{art.description}}</p>
					<p><span class="blue-text">وضعیت: </span>{{art.status}}</p>
					<details>
						<summary>اطلاعات بیشتر از مقاله {{art.title}}</summary>
						<p><span class="blue-text">نوشته شده در: </span>{{art.jdate}}</p>
						<p><span class="blue-text">نویسنده: </span>{{art.author.name}}</p>
					</details>
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
	import {computed,ref,onBeforeUnmount} from 'vue';
	import {useStore} from 'vuex';
	import {getAPI} from '@/axios.js';
	export default{
		name: "lm-articles",
		setup(){
			const store = useStore();
			const APIData = computed(()=>store.state.APIData);
			const endpoint = ref("articles/mapi/v1/?page=1");
			const count = ref(0);
			store.state.APIData = [];
			const paginate = ref(null);
			let more = false;
			let bottom = false;
			async function get_arts(end){
				try{
					const res = await getAPI.get(end,{headers:{Authorization:`JWT ${store.state.accessToken}`}});
					for(var i=0;i<res.data.results.length;i++){
						store.state.APIData.push(res.data.results[i])
					}
					endpoint.value = res.data.next;
					count.value = res.data.count;
					more = true;
					window.addEventListener("scroll",CaP);
				}catch(err){
					console.log(err);
					console.log(err.response);
				}
			}
			function CaP(){
				return pagination(endpoint.value);
			}
			function pagination(end){
				if(paginate.value){
					bottom = (window.scrollY+window.innerHeight)>=(paginate.value.offsetTop+paginate.value.offsetHeight-20)&&(window.scrollY+window.innerHeight)<(paginate.value.offsetTop+paginate.value.offsetHeight);
					if(bottom&&more&&end&&end===endpoint.value){
						more = false;
						get_arts(end);
					}				}
			}
			onBeforeUnmount(()=>{
				window.removeEventListener("scroll",CaP);
			})
			get_arts(endpoint.value);
			async function rm(id,i){
				if(confirm("آیا از حذف مقاله "+APIData.value[i].title+" اطمینان دارد؟ در صورت حذف تمام کامنت ها و پاسخ ها حذف میشوند، میتواند در حالت پیشنویس قرار دهید.")){
					try{
						getAPI.delete("articles/mapi/v1/"+id+"/",{headers:{Authorization:`JWT ${store.state.accessToken}`}});
					}catch(err){
						console.log(err)
						console.log(err.response)
						alert("حذف با خطا مواجه شد، کنسول را چک کنید.")
					}
				}
			}
			return{APIData,count,rm,paginate}
		}
	};
</script>
<style>
	@import '../assets/page-halfer.css';
	@import '../assets/lm-page.css';
	@import '../assets/home-spcial-list.css';
</style>