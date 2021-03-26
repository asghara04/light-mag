<template>
	<div class="page lm-page">
		<div class="lm-page-head ed-bk">
			<h2>تگ ها</h2>
			<router-link to="/LM-admin/add/tag" class="text-icon lm-link lm-blue"><img src="../assets/imgs/add.svg">جدید</router-link>
		</div>
		<div class="page-halfer ed-bk" v-if="count">
			<p class="link-like half">کل: {{count}}</p>
		</div>
		<br>
		<div ref="paginate" v-if="APIData" class="medium-list">
			<article v-for="(tag,i) in APIData" :key="i" class="art">
				<h2>{{tag.name}}</h2>
				<div class="page-halfer">
					<router-link :to="'/LM-admin/change/tag/'+tag.slug" class="text-icon half lm-link lm-green"><img src="../assets/imgs/edit.svg">تغییر</router-link>
					<a class="text-icon half lm-link lm-red" @click.prevent="rm(tag.slug,i)"><img src="../assets/imgs/delete.svg">حذف</a>
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
		name: "lm-tags",
		setup(){
			const store = useStore();
			const APIData = computed(()=>store.state.APIData);
			const paginate = ref(null)
			const endpoint = ref("tags/mapi/v1/?page=1");
			const count = ref(0);
			store.state.APIData = [];
			let more = false;
			let bottom = false;
			async function get_tags(end){
				try{
					const res = await getAPI.get(end,{headers:{Authorization: `JWT ${store.state.accessToken}`}});
					for(var i=0;i<res.data.results.length;i++){
						store.state.APIData.push(res.data.results[i])
					}
					endpoint.value = res.data.next;
					count.value = res.data.count;
					more = true;
					window.addEventListener("scroll",CaP);
				}catch(err){
					alert("خطایی در دریافت تگ ها رخ داد.")
					console.log(err)
					console.log(err.response)
				}				
			}
			function CaP(){
				return pagination(endpoint.value)
			}
			function pagination(end){
				if(paginate.value){
					bottom = (window.scrollY+window.innerHeight)>=(paginate.value.offsetTop+paginate.value.offsetHeight-20)&&(window.scrollY+window.innerHeight)<(paginate.value.offsetTop+paginate.value.offsetHeight);
					if(bottom&&more&&end&&end===endpoint.value){
						more = false;
						get_tags(end);
					}				}
			}
			onBeforeUnmount(()=>{
				window.removeEventListener("scroll",CaP);
			})
			get_tags(endpoint.value);
			async function rm(slug,i){
				if(confirm("آیا از حذف تگ "+APIData.value[i].name+" اطمینان دارید؟")){
					try{
						await getAPI.delete("tags/api/v1/"+slug+'/',{headers:{Authorization:`JWT ${store.state.accessToken}`}});
					}catch(err){
						alert("خطایی در حذف رخ داد.")
						console.log(err)
						console.log(err.response)
					}
				}
			}
			return{APIData,paginate,count,rm}
		}
	};
</script>
<style>
	@import '../assets/lm-page.css';
	@import '../assets/medium-list.css';
	@import '../assets/page-halfer.css';
</style>