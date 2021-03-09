<template>
	<div class="overlay" @click="close()" v-if="imgs!=false"></div>
	<p align="center" class="data-field link-like" @click.prevent="get_imgs()">انتخاب تصویر</p>
	<div v-if="imgs!=false" class="center-all">
		<button @click="close()" class="closer"><img src="../assets/imgs/exit.svg" alt="بستن"></button>
		<div class="medium-list selecting" v-if="imgs.results">
			<article v-for="(img,i) in imgs.results" @click="select(i,img.name)" :key="i" class="art" :class="{'selected':img.select}">
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
			const current = ref(1);
			const store = useStore();
			const img = ref(null);
			async function get_imgs(){
				try{
					const res = await getAPI.get("images/mapi/v1/?page="+current.value, {headers: {Authorization: `JWT ${store.state.accessToken}`}});
					for(var i=0;i<res.data.results.length;i++){
						if(!res.data.results[i].select){
							res.data.results[i]["select"] = false;
						}
					}
					imgs.value = res.data;
					document.body.classList.add("freeze");
				}catch(err){
					alert("خطایی رخ داد.");
					console.log(err);
				}
			}
			async function close(){
				imgs.value = [];
				document.body.classList.remove("freeze");
			}
			async function select(i,name){
				for(var n=0;n<imgs.value.results.length;n++){
					imgs.value.results[n].select = false;
				}
				imgs.value.results[i].select = true;
				img.value = name;
			}
			async function subback(){
				emit('selected',img.value);
				if(img.value){
					imgs.value = [];
				}
			}

			return{imgs,get_imgs,select,close,subback}
		}
	};
</script>
<style>
	@import '../assets/form.css';
	@import '../assets/center-all.css';
	@import '../assets/medium-list.css';
</style>