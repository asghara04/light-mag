<template>
	<h2 class="cen">تغییر دسته {{name}}</h2>
	<form class="form" @submit.prevent="sub(catslug)" v-if="catslug">
		<div v-if="imgAddress" class="form-img-div"><img :src="imgAddress"></div>
		<label for="image">تصویر دسته: </label>
		<span v-if="errs.image!=false"><p v-for="(err,i) in errs.image" :key="i" class="red-text">* {{err}}</p></span>
		<ChoseImg @selected="set_img"/>
		<label for="name">نام دسته: </label>
		<span v-if="errs.name!=false"><p v-for="(err,i) in errs.name" :key="i" class="red-text">* {{err}}</p></span>
		<input type="text" name="name" maxlength="25" required="" class="data-field" v-model="name">
		<label for="slug">اسلاگ دسته: </label>
		<span v-if="errs.slug!=false"><p v-for="(err,i) in errs.slug" :key="i" class="red-text">* {{err}}</p></span>
		<input type="slug" name="slug" maxlength="25" required="" class="data-field" v-model="slug">
		<button class="sub-button" name="submit">ثبت</button>
	</form>
</template>
<script>
	import {ref,watch} from 'vue';
	import {getAPI} from '@/axios.js';
	import {useStore} from 'vuex';
	import ChoseImg from '@/components/choseImg.vue';
	import {useRouter,useRoute} from 'vue-router';
	export default{
		name: "LmChangeCategory",
		props: ['catslug'],
		setup(props){
			const image = ref(null);
			const name = ref(null);
			const slug = ref(null);
			const errs = ref({'image':[],'name':[],'alt':[]});
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
					alert('خطایی رخ داد. کنسول را چک کنید')
					console.log(err.response.status)
					console.log(err.response)
				}
			}
			get_cat(props.catslug);
			const router = useRouter();
			async function sub(catslug){
				errs.value.image = [];
				errs.value.name = [];
				errs.value.slug = [];
				if(image.value&&image.value.length<=25&&name.value&&name.value.length<=25&&slug.value&&slug.value.length<=25){
					try{
						const res = await getAPI.patch("categories/api/v1/"+catslug+'/',{
							image: {name: image.value},
							name: name.value,
							slug: slug.value
						},{headers:{Authorization:`JWT ${store.state.accessToken}`}});
						if(res.status===200){
							router.push({name:"lm-category",params: {slug: slug.value||catslug}})
						}
					}catch(err){
						if(err.response.status===400){
							if(err.response.data.image){
								for(var i=0;i<err.response.data.image.length;i++){
									errs.value.image.push(err.res.data.image[i]);
								}
							}
							if(err.response.data.name){
								for(var x=0;x<err.response.data.name.length;x++){
									errs.value.name.push(err.response.data.name[x]);
								}
							}
							if(err.response.data.slug){
								for(var y=0;y<err.response.data.slug.length;y++){
									errs.value.slug.push(err.response.data.slug[y])
								}
							}
							if(!err.response.data.image&&!err.response.data.name&&!err.response.data.slug){
								console.log(err.response);
								alert('خطایی رخ داد. کنسول را چک کنید.');
							}
						}else{
							console.log(err.response);
							alert('خطایی رخ داد. کنسول را چک کنید.');
						}
					}
				}else{
					if(!image.value){
						errs.value.image.push('لطفا ابتدا تصویر دسته را انتخاب کنید.');
					}
					else if(image.value.length>25){
						errs.value.image.push("لطفا تصویر معتبری انتخاب کنید.");
					}
					if(!name.value){
						errs.value.name.push('لطفا ابتدا نام دسته را وارد کنید.');
					}
					else if(name.value.length>25){
						errs.value.name.push("نام تصویر باید حداکثر ۲۵ حرف باشد. اکنون "+name.value.length+" تا است.");
					}
					if(!slug.value){
						errs.value.slug.push('لطفا ابتدا اسلاگ دسته را وارد کنید.');
					}
					else if(slug.value.length>25){
						errs.value.slug.push("اسلاگ تصویر باید حداکثر ۲۵ حرف باشد. اکنون "+slug.value.length+" تا است.");
					}
				}
			}
			function set_img(name,address){
				if(name.length<=25){
					image.value = name;
					imgAddress.value = address;
					errs.value.image = [];
				}
			}
			const route = useRoute();
			watch(
				()=>route.params.catslug,
				newCatslug=>{
					if(route.name==="change-category"){
						get_cat(newCatslug);
					}
				}
			)
			return{image,name,slug,imgAddress,errs,sub,set_img}
		},
		components:{ChoseImg}
	};
</script>
<style>
	@import '../assets/form.css';
</style>