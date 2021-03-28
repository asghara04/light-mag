<template>
	<h2 class="cen">زیردسته جدید</h2>
	<form @submit.prevent="sub()" class="form">
		<div v-if="imgAddress" class="form-img-div"><img :src="imgAddress"></div>
		<label for="image">تصویر: </label>
		<span v-if="errs.image!=false"><p class="red-text" v-for="(err,i) in errs.image" :key="i">* {{err}}</p></span>
		<choseImg @selected="set_img"/>
		<label for="category">دسته: </label>
		<span v-if="errs.category!=false"><p class="red-text" v-for="(err,i) in errs.category" :key="i">* {{err}}</p></span>
		<select class="data-field" required="" v-model="category">
			<option v-for="(cat,i) in cats" :key="i" :value="i">{{cat.name}}</option>
		</select>
		<label for="name">نام: </label>
		<span v-if="errs.name!=false"><p class="red-text" v-for="(err,i) in errs.name" :key="i">* {{err}}</p></span>
		<input type="text" name="name" class="data-field" v-model="name" maxlength="25">
		<label for="slug">اسلاگ: </label>
		<span v-if="errs.slug!=false"><p class="red-text" v-for="(err,i) in errs.slug" :key="i">* {{err}}</p></span>
		<input type="slug" name="slug" class="data-field" v-model="slug" maxlength="25">
		<button class="sub-button">ثبت</button>
	</form>
</template>
<script>
	import {ref} from 'vue';
	import {getAPI} from '@/axios.js';
	import {useStore} from 'vuex';
	import choseImg from '@/components/choseImg.vue';
	import {useRouter} from 'vue-router';
	export default{
		name: "LmAddSubcat",
		setup(){
			document.querySelector("head title").textContent = "زیردسته جدید - لایت مگ";
			document.querySelector("head meta[name='robots']").setAttribute("content","noindex, nofollow")
			const category = ref(null);
			const image = ref(null);
			const name = ref(null);
			const slug = ref(null);
			const cats = ref([]);
			const store = useStore();
			const errs = ref({"category":[],"image":[],"name":[],"slug":[]})
			async function get_cats(){
				try{
					const res = await getAPI.get("categories/all/api/v1/", {headers: {Authorization: `JWT ${store.state.accessToken}`}});
					cats.value = res.data;
				}catch(err){
					console.log(err);
				}
			}
			get_cats()
			const imgAddress = ref(null);
			function set_img(name,address){
				if(name.length<=25){
					image.value = name;
					imgAddress.value = address;
				}
			}
			const router = useRouter();
			async function sub(){
				errs.value.category = [];
				errs.value.image = [];
				errs.value.name = [];
				errs.value.slug = [];
				if(category.value&&image.value&&image.value.length<=25&&name.value&&name.value.length<=25&&slug.value&&slug.value.length<=25){
					try{
						const res = await getAPI.post("categories/subs/api/v1/"+cats.value[category.value].id+'/', {
							category: cats.value[category.value].name,
							image: {name: image.value},
							name: name.value,
							slug: slug.value
						}, {headers: {Authorization: `JWT ${store.state.accessToken}`}});
						if(res.status===201){
							router.push({name: "lm-category",params:{slug:cats.value[category.value].slug}});
						}else{
							console.log(res);
							alert('خطایی رخ داد به ادمین اطلاع دهید یا کنسول را چک کنید.');
						}
					}catch(err){
						if(err.response.status==400){
							if(err.response.data.category){
								for(var i=0;i<err.response.data.category.length;i++){
									errs.value.category.push(err.response.data.category[i]);
								}
							}
							if(err.response.data.image){
								for(var n=0;n<err.response.data.image.length;n++){
									errs.value.image.push(err.response.data.image[n]);
								}
							}
							if(err.response.data.name){
								for(var x=0;x<err.response.data.name.length;x++){
									errs.value.name.push(err.response.data.name[x]);
								}
							}
							if(err.response.data.slug){
								for(var y=0;y<err.response.data.slug.length;y++){
									errs.value.slug.push(err.response.data.slug[y]);
								}
							}
							console.log(err.response.data);
						}else{
							alert('خطایی دریافت شد.')
							console.log(err.response.status);
						}
					}
				}else{
					if(!cats.value[category.value].name){
						errs.value.category.push("لطفا ابتدا دسته ای را انتخاب کنید.");
					}else if(cats.value[category.value].name.length>25){
						errs.value.category.push("دسته معتبری را انتخاب کنید.");
					}
					if(!image.value){
						errs.value.image.push("لطفا ابتدا تصویر زیردسته را انتخاب کنید.");
					}else if(image.value.length>25){
						errs.value.image.push("تصویر معتبری را انتخاب کنید.");
					}
					if(!name.value){
						errs.value.name.push("لطفا ابتدا نام زیردسته را وارد کنید.")
					}else if(name.value.length>25){
						errs.value.name.push('حداکثر طول نام زیردسته 25 است اکنون '+name.value.length+' وارد شده است.');
					}
					if(!slug.value){
						errs.value.slug.push("لطفا ابتدا اسلاگ زیردسته را وارد کنید.");
					}else if(slug.value.length>25){
						errs.value.slug.push('حداکثر طول اسلاگ زیردسته 25 است اکنون '+name.value.length+' وارد شده است.');
					}
				}
			}
			return{category,set_img,name,slug,cats,sub,errs,imgAddress}
		},
		components:{choseImg}
	};
</script>
<style>
	@import '../assets/form.css';
</style>