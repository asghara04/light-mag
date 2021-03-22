<template>
	<div class="page">
		<div class="lm-page">
			<div class="lm-page-head ed-bk">
				<h2>کاربران</h2>
				<router-link to="/LM-admin/add/user" class="text-icon lm-link lm-blue"><img src="../assets/imgs/add.svg">جدید</router-link>
			</div>
			<div ref="paginate" class="spcial-list" v-if="APIData!=false">
				<article class="article" v-for="(user,i) in APIData" :key="i" :class="{'yay-sider':user.prof_picture}">
					<router-link v-if="user.prof_picture" class="sider" :rel="user.name" :to="'#'"><img :src="user.prof_picture.image" :alt="user.prof_picture.alt" :name="user.prof_picture.name"></router-link>
					<div class="high-content">
						<h2><router-link :rel="user.name" :name='user.name' to="#">{{user.name}}</router-link></h2>
						<hr>
						<p v-if="user.bio" class="pre-formatted">{{user.bio}}</p>
						<details>
							<summary>اطلاعات بیشتر از {{user.name}}</summary>
							<p><span class="blue-text">تاریخ عضویت: </span>{{user.jjoin}}</p>
							<p><span class="blue-text">نام کاربری: </span>{{user.username}}</p>
						</details>
						<div class="page-halfer">
							<router-link :to="{name: 'change-user',params:{usern: user.username}}" class="text-icon half lm-link lm-green"><img src="../assets/imgs/edit.svg">تغییر</router-link>
							<a class="text-icon half lm-link lm-red" @click.prevent="rm(user.id, i)"><img src="../assets/imgs/delete.svg">حذف</a>
						</div>
					</div>
				</article>
			</div>
		</div>
	</div>
</template>
<script>
	import {ref,computed,onBeforeUnmount} from 'vue';
	import {getAPI} from '@/axios.js';
	import {useStore} from 'vuex';
	export default{
		name: "lmArticles",
		setup(){
			const store = useStore();
			const APIData = computed(()=>store.state.APIData);
			const endpoint = ref("users/mapi/v1/");
			const paginate = ref(null);
			store.state.APIData = [];
			const count = ref(null);
			let more = false;
			let bottom = false;
			async function get_users(end){
				try{
					const res = await getAPI.get(end,{headers:{Authorization:`JWT ${store.state.accessToken}`}});
					for(var i=0;i<res.data.results.length;i++){
						store.state.APIData.push(res.data.results[i])
					}
					count.value = res.data.count;
					endpoint.value = res.data.next;
					more = true;
					window.addEventListener("scroll",CaP);
				}catch(err){
					console.log(err);
					console.log(err.response);
					alert("خطایی رخ داد.");
				}
			}
			get_users(endpoint.value);

			function CaP(){
				return pagination(endpoint.value);
			}
			function pagination(end){
				if(paginate.value){
					bottom = (window.scrollY+window.innerHeight)>=(paginate.value.offsetTop+paginate.value.offsetHeight-20)&&(window.scrollY+window.innerHeight)<(paginate.value.offsetTop+paginate.value.offsetHeight);
					if(bottom&&more&&end&&end===endpoint.value){
						more = false;
						get_users(end);
					}
				}
			}
			onBeforeUnmount(()=>{
				window.removeEventListener("scroll",CaP);
			})
			async function rm(id,i){
				if(confirm("آیا از حذف "+APIData.value[i].name+" اطمینان دارد؟ در صورت حذف تمامی نوشته های این کاربر حذف میشوند.")){
					try{
						await getAPI.delete("users/mapi/v1/"+id+'/',{headers:{Authorization:`JWT ${store.state.accessToken}`}})
						get_users(endpoint.value);
					}catch(err){
						console.log(err);
						console.log(err.response);
						alert("خطایی رخ داد، لطفا کنسول را چک کنید");
					}
				}
			}
			return{paginate,APIData,rm}
		}
	};
</script>
<style>
	@import '../assets/lm-page.css';
	@import '../assets/home-spcial-list.css';
	@import '../assets/page-halfer.css';
</style>