<template>
	<div class="page lm-page">
		<div class="lm-page-head ed-bk">
			<h2>کامنت ها</h2>
		</div>
		<div class="page-halfer ed-bk" v-if="count">
			<p>کل: {{count}}</p>
		</div>
		<br>
		<div ref="paginate" class="spcial-list" v-if="APIData!=false">
			<article class="article" v-for="(com,i) in APIData" :key="i">
				<div class="high-content">
					<h2>{{com.name}}</h2>
					<hr>
					<p><span class="blue-text">تاریخ: </span>{{com.jdate}}</p>
					<p><span class="blue-text">فعالیت: </span>{{com.status}}</p>
					<p><span class="blue-text">نظر:‌ </span>{{com.message}}</p>
					<p><span class="blue-text">پاسخ ها: </span>{{com.reps}}</p>
					<div class="page-halfer">
						<router-link :to="{name: 'change-comment',params:{compk:com.id}}" class="text-icon half lm-link lm-green"><img src="../assets/imgs/edit.svg">تغییر</router-link>
						<a class="text-icon half lm-link lm-red" @click.prevent="rm(com.id,i)"><img src="../assets/imgs/delete.svg">حذف</a>
					</div>
					<details v-if="com.reps">
						<summary>پاسخ ها</summary>	
						<div v-for="(rep,x) in com.replies" :key="x">
							<h3>{{rep.name}}</h3>
							<p><span class="blue-text">تاریخ: </span>{{rep.jdate}}</p>
							<p><span class="blue-text">فعالیت: </span>{{rep.status}}</p>
							<p><span class="blue-text">پاسخ:‌ </span>{{rep.message}}</p>
							<div class="page-halfer">
								<router-link :to="{name: 'change-article',params:{pk:com.id}}" class="text-icon half lm-link lm-green"><img src="../assets/imgs/edit.svg">تغییر</router-link>
								<a class="text-icon half lm-link lm-red" @click.prevent="rep_rm(rep.id,x)"><img src="../assets/imgs/delete.svg">حذف</a>
							</div>
							<hr v-if="com.reps+1>i">
						</div>
					</details>
				</div>
			</article>
		</div>
	</div>
</template>
<script>
	import {computed,ref,onBeforeUnmount} from 'vue';
	import {getAPI} from '@/axios.js';
	import {useStore} from 'vuex';
	export default{
		name: "lmComments",
		setup(){
			const store = useStore();
			const APIData = computed(()=>store.state.APIData);
			const count = ref(0);
			const endpoint = ref("comments/mapi/v1/");
			let more = false;
			let bottom = false;
			store.state.APIData = []
			const paginate = ref(null);
			async function get_coms(end){
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
					console.log(err)
					console.log(err.response)
					alert("خطایی در دریافت کامنت ها رخ داد.")
				}
			}
			get_coms(endpoint.value);
			function CaP(){
				return pagination(endpoint.value)
			}
			function pagination(end){
				if(paginate.value){
					bottom = (window.scrollY+window.innerHeight)>=(paginate.value.offsetTop+paginate.value.offsetHeight-20)&&(window.scrollY+window.innerHeight)<(paginate.value.offsetTop+paginate.value.offsetHeight);
					if(bottom&&more&&end&&end===endpoint.value){
						more = false;
						get_coms(end);
					}
				}
			}
			onBeforeUnmount(()=>{
				window.removeEventListener("scroll",CaP);
			})
			async function rm(id,i){
				if(confirm("آیا از حذف کامنت "+APIData.value[i].name+" در مقاله "+APIData.value[i].article+" اطمینان دارید؟(در صورت حذف تمامی پاسخ ها نیز حذف میشوند)")){
					try{
						await getAPI.delete("comments/mapi/v1/"+id+'/',{headers:{Authorization:`JWT ${store.state.accessToken}`}})
					}catch(err){
						alert("خطایی در حذف کامنت رخ داد.")
						console.log(err);
						console.log(err.response);
					}
				}
			}
			async function rep_rm(id,i){
				if(confirm("آیا از حذف پاسخ "+APIData.value[i].name+" اطمینان دارید؟")){
					try{
						await getAPI.delete("/comments/reply/mapi/v1/"+id+"/",{headers:{Authorization:`JWT ${store.state.accessToken}`}})
					}catch(err){
						alert("خطایی در حذف پاسخ رخ داد.");
						console.log(err);
						console.log(err.response);
					}
				}
			}
			return{APIData,count,paginate,rm,rep_rm}
		}
	};
</script>
<style>
	@import '../assets/home-spcial-list.css';
	@import '../assets/lm-page.css';
	@import '../assets/page-halfer.css';
</style>