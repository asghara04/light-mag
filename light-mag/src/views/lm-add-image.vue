<template>
	<h2>تصویر جدید</h2>
	<form class="form" enctype="multipart/form-data" @submit.prevent="sub">
		<img src="hi">
		<label for="image">تصویر: </label>
		<span v-if="errs.image!=false"><p v-for="(err, i) in errs.image" class="red-text" :key="i">* {{err}}</p></span>
		<input type="file" name="image" @change.prevent="image_selected" accept="image/png, image/jpeg, image/gif" class="data-field" required="">
		<label for="name">نام: </label>
		<span v-if="errs.name!=false"><p v-for="(err, i) in errs.name" class="red-text" :key="i">* {{err}}</p></span>
		<input type="text" name="name" class="data-field" v-model="name" maxlength="25">
		<label for="alt">آلترناتیو: </label>
		<span v-if="errs.alt!=false"><p v-for="(err, i) in errs.alt" class="red-text" :key="i">* {{err}}</p></span>
		<input type="text" name="alt" class="data-field" v-model="alt" maxlength="25">
		<button class="sub-button">ثبت</button>
	</form>
</template>
<script>
	import {ref} from 'vue';
	import {getAPI} from '@/axios.js';
	import {useStore} from 'vuex';
	import {useRouter} from 'vue-router';
	export default{
		name: "LmAddImage",
		setup(){
			const image = ref(null);
			const name = ref(null);
			const alt = ref(null);
			const fd = new FormData();
			const errs = ref({'image':[], 'name':[], 'alt':[]});

			function image_selected(e){
				if(e.target.files&&(e.target.files[0]['type']==='image/jpeg'||e.target.files[0]['type']==='image/png'||e.target.files[0]['type']==='image/gif')){
					image.value = e.target.files[0]
				}
			}
			const store = useStore();
			const router = useRouter();
			async function sub(){
				errs.value.image = [];
				errs.value.name = [];
				errs.value.alt = [];
				if(name.value&&alt.value&&name.value.length<=25&&alt.value.length<=25&&image.value){
					fd.append("image", image.value, image.value['name']);
					fd.append("alt", alt.value);
					fd.append("name", name.value);
					try{
						const res = await getAPI.post("images/mapi/v1/", fd, {headers: {Authorization: `JWT ${store.state.accessToken}`}})
						if(res.status===201){
							router.push({name: "lm-images"})
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
							if(err.response.data.alt){
								for(var n=0;n<err.response.data.alt.length;n++){
									errs.value.alt.push(err.response.data.alt[n]);
								}
							}
							if(err.response.data.name){
								for(var e=0;e<err.response.data.name.length;e++){
									errs.value.name.push(err.response.data.name[e])
								}
							}
							if(!err.response.data.image&&!err.response.data.image&&!err.response.alert.alt){
								console.log(err)
								alert("خطایی رخ داد. لطفا دوباره امتحان کنید.");
							}
						}else{
							console.log(err);
						}
					}
				}else{
					if(!alt.value){
						errs.value.alt = ["آلترناتیو تصویر را وارد کنید."];
					}else if(alt.value.length>25){
						errs.value.alt = ["آلترناتیو تصویر باید حداکثر ۲۵ حرف باشد. اکنون "+alt.value.length+" تا است."];
					}
					if(!name.value){
						errs.value.name = ["نام تصویر را وارد کنید."];
					}else if(name.value.length>25){
						errs.value.name = ["نام تصویر باید حداکثر ۲۵ حرف باشد. اکنون "+name.value.length+" تا است."];
					}
					if(!image.value){
						errs.value.image = ["باید تصویری انتخاب کنید!"];
					}
				}
			}

			return{image, name, alt, image_selected, sub, errs}
		}
	};
</script>
<style>
	@import '../assets/form.css';
</style>