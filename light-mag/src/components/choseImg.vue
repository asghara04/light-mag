<template>
	<div class="overlay" @click="close()" v-if="imgs!=false"></div>
	<p align="center" class="data-field link-like" @click.prevent="get_imgs(endpoint)">انتخاب تصویر</p>
	<div v-if="imgs!=false" ref="paginate" @scroll="pagination(endpoint)" class="center-all">
		<button @click="close()" class="closer"><img src="../assets/imgs/exit.svg" alt="بستن"></button>
		<div class="medium-list selecting" v-if="imgs">
			<article v-for="(img,i) in imgs" @click="select(i,img.name)" :key="i" class="art" :class="{'selected':img.select}">
				<h2>{{img.name}}</h2>
				<img :src="img.image" :alt="img.alt">
			</article>
		</div>
		<button @click="subback" class="sub-button subber">انتخاب</button>
	</div>
</template>
<script>
	import {ref} from 'vue';
	import{useStore} from 'vuex';
	import {getAPI} from '@/axios.js';
	export default{
		name: "ChoseImg",
		emits: {
			selected: (name) => {
				if(!name||name.length>25){
					alert("لطفا ابتدا تصیوری انتخاب کنید.");
					return false;
				}else{
					return true;
				}
			}
		},
		setup(props,{emit}){
			const imgs = ref([]);
			const store = useStore();
			const img = ref(null);
			const endpoint = ref("images/mapi/v1/?page=1");
			const cuont = ref(null);
			const paginate = ref(null);
			let more = false;
			async function get_imgs(end){
				try{
					const res = await getAPI.get(end, {headers: {Authorization: `JWT ${store.state.accessToken}`}});
					for(var i=0;i<res.data.results.length;i++){
						res.data.results[i]['select'] = false;
						imgs.value.push(res.data.results[i]);
					}
					cuont.value = res.data.count;
					endpoint.value = res.data.next;
					more = true;
					document.body.classList.add("freeze");
				}catch(err){
					alert("خطایی رخ داد.");
					console.log(err);
				}
			}
			async function close(){
				imgs.value = [];
				endpoint.value = "images/mapi/v1/?page=1";
				document.body.classList.remove("freeze");
			}
			async function select(i,name){
				for(var n=0;n<imgs.value.length;n++){
					imgs.value[n].select = false;
				}
				imgs.value.[i].select = true;
				img.value = name;
				endpoint.value = "images/mapi/v1/?page=1";
			}
			async function subback(){
				document.body.classList.remove("freeze");
				emit('selected',img.value);
				if(img.value){
					imgs.value = [];
				}
			}
			function pagination(end){
				let bottom = (paginate.value.scrollTop+paginate.value.offsetHeight-20===paginate.value.scrollHeight-20);
				if(more&&end&&endpoint.value===end&&bottom===true){
					more = false;
					return get_imgs(end);
				}
			}
			return{imgs,get_imgs,select,close,subback,pagination,paginate,endpoint}
		}
	};
</script>
<style>
	@import '../assets/form.css';
	@import '../assets/center-all.css';
	@import '../assets/medium-list.css';
</style>