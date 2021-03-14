<template>
	<h2></h2>
	<form v-if="name&&slug" class="form" @submit.prevent="sub()">
		<div v-if="imgAddress" class="form-img-div"><img :src="imgAddress"></div>
		<label for="image">تصویر دسته: </label>
		<span v-if="errs.image!=false"><p v-for="(err,i) in errs.image" :key="i" class="red-text">* {{err}}</p></span>
		<ChoseImg @selected="set_img"/>
	</form>
</template>
<script>
	import {ref} from 'vue';
	import {getAPI} from '@/axios.js';
	import {useStore} from 'vuex';
	import ChoseImg from '@/components/choseImg.vue';
	export default{
		name: "LmChangeCategory",
		props: ['catslug'],
		setup(props){
			const image = ref(null);
			const name = ref(null);
			const slug = ref(null);
			const errs = ref(null);
			const imgAddress = ref(null);
			const store = useStore();
			async function get_cat(catslug){
				try{
					const res = await getAPI.get("categories/api/v1/"+catslug,{headers:{Authorization:`JWT ${store.state.accessToken}`}})
					if(res.data.image){
						image.value = res.data.image.name;
						imgAddress.value = res.data.image.image;
					}
					name.value = res.data.name;
					slug.value = res.data.slug;
				}catch(err){
					console.log(err)
				}
			}
			get_cat(props.catslug);

			async function sub(){
				//pass
			}
			function set_img(name,address){
				if(name.length<=25){
					image.value = name;
					imgAddress.value = address;
				}
			}
			return{image,name,slug,imgAddress,errs,sub,set_img}
		},
		components:{ChoseImg}
	};
</script>
<style>
	@import '../assets/form.css';
</style>