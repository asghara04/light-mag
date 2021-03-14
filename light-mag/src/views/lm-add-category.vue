<template>
	<h2 class="cen">دسته جدید</h2>
	<form class="form" @submit.prevent="sub()">
		<div v-if="imgAddress" class="form-img-div"><img :src="imgAddress"></div>
		<label for="image">تصویر دسته: </label>
		<span v-if="errs.image!=false"><p v-for="(err,i) in errs.image" :key="i" class="red-text">* {{err}}</p></span>
		<ChoseImg @selected="set_img"/>
		<label for="name">نام دسته: </label>
		<span v-if="errs.name!=false"><p v-for="(err,i) in errs.name" :key="i" class="red-text">* {{err}}</p></span>
		<input type="text" name="name" maxlength="25" class="data-field" v-model="name">
		<label for="slug">اسلاگ دسته: </label>
		<span v-if="errs.slug!=false"><p v-for="(err,i) in errs.slug" :key="i" class="red-text">* {{err}}</p></span>
		<input type="slug" name="slug" maxlength="25" class="data-field" v-model="slug">
		<button class="sub-button" name="submit">ثبت</button>
	</form>
</template>
<script>
	import {ref} from 'vue';
	import ChoseImg from '@/components/choseImg.vue';
	import {useStore} from 'vuex';
	import {getAPI} from '@/axios.js';
	import {useRouter} from 'vue-router';
	export default{
		name: "LmAddCategory",
		setup(){
			const image = ref(null);
			const name = ref(null);
			const slug = ref(null);
			const errs = ref({'image':[],'name':[],'slug':[]});
			const imgAddress = ref(null);
			function set_img(name,address){
				if(name.length<=25){
					image.value = name;
					imgAddress.value = address;
				}
			}
			const store = useStore();
			const router = useRouter();
			async function sub(){
				errs.value.image = [];
				errs.value.name = [];
				errs.value.slug = [];
				if(image.value&&image.value.length<=25&&name.value&&name.value.length<=25&&slug.value&&slug.value.length<=25){
					try{
						const res = await getAPI.post("categories/api/v1/", {
						image: {name: image.value},
						name: name.value,
						slug: slug.value
						},{headers: {Authorization: `JWT ${store.state.accessToken}`}})
						if(res.status===201){
							router.push({name: "lm-categories"})
						}else{
							console.log(res);
						}
					}catch(err){
						if(err.response.status===400){
							if(err.response.data.image){
								for(var i=0;i<err.response.data.image.length;i++){
									errs.value.image.push(err.response.data.image[i]);
								}
							}
							if(err.response.data.name){
								for(var n=0;n<err.response.data.name.length;n++){
									errs.value.name.push(err.response.data.name[n]);
								}
							}
							if(err.response.data.slug){
								for(var x=0;x<err.response.data.slug.length;x++){
									errs.value.slug.push(err.response.data.slug[x]);
								}
							}
							if(!err.response.data.image&&!err.response.data.name&&!err.response.data.slug){
								console.log(err);
								alert("خطایی رخ داد. لطفا دوباره امتحان کنید.");
							}
						}else{
							console.log(err)
						}
					}
				}else{
					if(!image.value){
						errs.value.image = ["لطفا تصویری انتخاب کنید."];
					}else if(image.value.length>25){
						errs.value.image = ["لطفا تصویر معتبری انتخاب کنید."];
					}
					if(!name.value){
						errs.value.name = ["لطفا نام دسته را وارد کنید."];
					}else if(name.value.length>25){
						errs.value.name = ["نام تصویر باید حداکثر ۲۵ حرف باشد. اکنون "+name.value.length+" تا است."]
					}
					if(!slug.value){
						errs.value.slug = ["لطفا اسلاگ دسته را وارد کنید."]
					}else if(slug.value.length>25){
						errs.value.slug = ["اسلاگ تصویر باید حداکثر ۲۵ حرف باشد. اکنون "+name.value.length+" تا است."]
					}
				}
			}

			return{name,slug,set_img,sub,errs,imgAddress}
		},
		components:{
			ChoseImg
		}
	};
</script>
<style>
	@import '../assets/form.css';
</style>