<template>
	<h2 class="cen" v-if="id">تغییر تصویر {{name}}</h2>
	<form v-if="id" class="form" enctype="multipart/form-data" @submit.prevent="sub(id)">
		<div v-if="imgAddress" class="form-img-div"><img :src="imgAddress"></div>
		<label for="image">تصویر: </label>
		<span v-if="errs.image!=false"><p v-for="(err, i) in errs.image" class="red-text" :key="i">* {{err}}</p></span>
		<input type="file" name="image" @change.prevent="img_selected" accept="image/png, image/jpeg, image/gif" class="data-field">
		<label for="name">نام: </label>
		<span v-if="errs.name!=false"><p v-for="(err, i) in errs.name" class="red-text" :key="i">* {{err}}</p></span>
		<input type="text" name="name" class="data-field" v-model="name" maxlength="25" required="">
		<label for="alt">آلترناتیو: </label>
		<span v-if="errs.alt!=false"><p v-for="(err, i) in errs.alt" class="red-text" :key="i">* {{err}}</p></span>
		<input type="text" name="alt" class="data-field" v-model="alt" maxlength="25" required="">
		<button class="sub-button">ثبت</button>
	</form>
</template>
<script>
	import {getAPI} from '@/axios.js';
	import {useStore} from 'vuex';
	import {ref,watch} from 'vue';
	import {useRoute,useRouter} from 'vue-router';
	export default{
		name: "LmChangeImage",
		props: ['id'],
		setup(props){
			const image = ref(null);
			const name = ref(null);
			const alt = ref(null);
			const imgAddress = ref(null);
			const errs = ref({'image':[],'name':[],'alt':[]});
			const store = useStore();
			async function get_img(id){
				errs.value.image = [];
				errs.value.name = [];
				errs.value.alt = [];
				try{
					const res = await getAPI.get("images/mapi/v1/"+id,{headers:{Authorization:`JWT ${store.state.accessToken}`}});
					imgAddress.value = res.data.image;
					name.value = res.data.name;
					alt.value = res.data.alt;
				}catch(err){
					console.log(err+"now validation should be image validation should be firent!"+errs.value)
				}
			}
			async function img_selected(e){
				if(e.target.files&&(e.target.files[0]['type']==='image/jpeg'||e.target.files[0]['type']==='image/png'||e.target.files[0]['type']==='image/gif')){
					image.value = e.target.files[0];
					imgAddress.value = null;
				}else{
					errs.value.image = ["لطفا تصویر معتبری انتخاب کنید."]
				}
			}
			get_img(props.id);
			const router = useRouter();
			const fd = new FormData();
			async function sub(id){
				errs.value.image = [];
				errs.value.name = [];
				errs.value.alt = [];
				if(id&&name.value&&name.value.length<=25&&alt.value&&alt.value.length<=25){
					if(image.value){
						fd.append("image",image.value);
					}
					fd.append("name",name.value);
					fd.append("alt",alt.value);
					try{
						const res = await getAPI.patch("images/mapi/v1/"+id+'/',fd,{headers:{Authorization:`JWT ${store.state.accessToken}`}});
						if(res.status===200){
							router.push({name:"lm-images"});
						}else{
							console.log(res.data)
						}
					}catch(err){
						if(err.response.status===400){
							if(err.response.data.image){
								for(var i=0;9<err.response.data.image.length;i++){
									errs.value.image.push(err.response.data.image[i])
								}
							}
							if(err.response.data.alt){
								for(var x=0;x<err.response.data.alt.length;x++){
									errs.value.alt.push(err.response.data.alt[x])
								}
							}
							if(err.response.data.name){
								for(var y=0;y<err.response.data.name.length;y++){
									errs.value.name.push(err.response.data.name[y])
								}
							}
							if(!err.response.data.image&&!err.response.data.alt&&!err.response.data.name){
								console.log(err);
								console.log(err.response);
								alert("خطایی رخ داد! کنسول را چک کنید.")
							}
						}else{
							console.log(err.response.status);
							console.log(err.response);
						}
					}
				}else{
					if(!id){
						window.reload();
					}
					if(!alt.value){
						errs.value.alt.push("آلترناتیو تصویر را وارد کنید.");
					}else if(alt.value.length>25){
						errs.value.alt.push("آلترناتیو تصویر باید حداکثر ۲۵ حرف باشد. اکنون "+alt.value.length+" تا است.");
					}
					if(!name.value){
						errs.value.name.push("نام تصویر را وارد کنید.");
					}else if(name.value.length>25){
						errs.value.name.push("نام تصویر باید حداکثر ۲۵ حرف باشد. اکنون "+name.value.length+" تا است.");
					}
				}
			}
			const route = useRoute();
			watch(
				()=>route.params.id,
				newId=>{
					if(route.name==="change-image"){
						get_img(newId);
					}
				}
			)

			return{image,name,alt,imgAddress,sub,errs,img_selected}
		}
	};
</script>
<style>
	@import '../assets/form.css';
</style>