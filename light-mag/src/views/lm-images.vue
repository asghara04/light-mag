<template>
	<div class="page">
		<div class="page-content lm-page">
			<div class="lm-page-head">
				<h2>تصاویر</h2>
				<router-link to="/LM-admin/add/image" class="text-icon lm-link lm-blue"><img src="../assets/imgs/add.svg"> جدید</router-link>
			</div>
			<hr>
			refresh<br>
			count<br>
			pagination
			<div v-if="APIData" class="medium-list">
				<article v-for="(img, i) in APIData" :key="i" class="art">
					<h2>{{img.name}}</h2>
					<img :src="img.image">
					<div class="page-halfer">
						<a class="text-icon half lm-link lm-green"><img src="../assets/imgs/edit.svg">تغییر</a>
						<a class="text-icon half lm-link lm-red" @click.prevent="rm(img.id, i)"><img src="../assets/imgs/delete.svg">حذف</a>
					</div>
				</article>
			</div>
		</div>
	</div>
</template>
<script>
	import {computed} from 'vue';
	import {useStore} from 'vuex';
	import {getAPI} from '@/axios.js';
	export default{
		name: 'lm-images',
		setup(){
			const store = useStore();
			const APIData = computed(() => store.state.APIData);

			function get_imgs(){
				getAPI.get("images/mapi/v1", {headers: {Authorization: `JWT ${store.state.accessToken}`}})
				.then(res => store.state.APIData = res.data)
				.catch(err => console.log(err))
			}
			get_imgs();

			async function rm(imgid, i){
				await getAPI.delete("images/mapi/v1/"+imgid, {headers: {Authorization: `JWT ${store.state.accessToken}`}})
				.then(() => {
					alert("تصویر "+APIData.value[i].name+" با موفقیت حذف شد.")
					get_imgs();
				})
				.catch(err => {
					alert("حذف با خطا مواجه شد.");
					console.log(err);
				})
			}


			return{APIData, rm}
		}
	};
</script>
<style>
	@import '../assets/lm-page.css';
	@import '../assets/medium-list.css';
	@import '../assets/page-halfer.css';
</style>