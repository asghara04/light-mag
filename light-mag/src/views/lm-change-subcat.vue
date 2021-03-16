<template>
	<h2 class="cen" v-if="cat&&sub">تغییر زیردسته {{sub}} در دسته {{cat}}</h2>
	<form class="form" @submit.prevent="subber(cat,sub)" v-if="cat&&sub">
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
		<input type="text" name="name" class="data-field" required="" v-model="name" maxlength="25">
		<label for="slug">اسلاگ: </label>
		<span v-if="errs.slug!=false"><p class="red-text" v-for="(err,i) in errs.slug" :key="i">* {{err}}</p></span>
		<input type="slug" name="slug" class="data-field" v-model="slug" required="" maxlength="25">
		<button class="sub-button">ثبت</button>
	</form>
</template>
<script>
	import {ref,watch} from 'vue';
	import {getAPI} from '@/axios.js';
	import {useStore} from 'vuex';
	import choseImg from '@/components/choseImg.vue';
	import {useRoute,useRouter} from 'vue-router';
	export default{
		name: "LmChangeSubcat",
		props:['cat','sub'],
		setup(props){
			const category = ref(null);
			const image = ref(null);
			const imgAddress = ref(null);
			const name = ref(null);
			const slug = ref(null);
			const errs = ref({'category':[],'image':[],'name':[],'slug':[]});
			const store = useStore();
			async function get_subcat(cat,sub){
				try{
					const res = await getAPI.get(`categories/sub/api/v1/${cat}/${sub}/`,{headers:{Authorization:`JWT ${store.state.accessToken}`}});
					category.value = res.data.category;
					if(res.data.image){
						image.value = res.data.image.name;
						imgAddress.value = res.data.image.image;
					}
					name.value = res.data.name;
					slug.value = res.data.slug;
				}catch(err){
					console.log(err.response)
					alert("خطایی در دریافت دسته ها رخ داد!");
				}
			}
			get_subcat(props.cat,props.sub);
			const cats = ref(null);
			async function get_cats(){
				try{
					const res = await getAPI.get("categories/all/api/v1/",{headers:{Authorization:`JWT ${store.state.accessToken}`}});
					cats.value = res.data;
				}catch(err){
					console.log(err.response);
					alert("خطایی در دریافت دسته ها رخ داد!");
				}
			}
			get_cats();
			const router = useRouter();
			async function subber(cat,sub){
				errs.value.image = [];
				errs.value.category = [];
				errs.value.name = [];
				errs.value.slug = [];
				if(image.value&&image.value.length<=25&&cats.value[category.value]&&cats.value[category.value].name.length<=25&&name.value&&name.value.length<=25&&slug.value&&slug.value.length<=25){
					try{
						const res = await getAPI.patch('categories/sub/api/v1/'+cat+'/'+sub+'/',{
							category: cats.value[category.value].name,
							image:{name:image.value},
							name: name.value,
							slug: slug.value
						}, {headers:{Authorization:`JWT ${store.state.accessToken}`}});
						if(res.status===200){
							router.push({name: "lm-category",params: {slug: cats.value[category.value].slug}})
						}
					}catch(err){
						if(err.response.status===400){
							if(err.response.data.image){
								for(var i=0;i<err.response.data.image.length;i++){
									errs.value.image.push(err.response.data.image[i]);
								}
							}
							if(err.response.data.category){
								for(var x=0;x<err.response.data.category.length;x++){
									errs.value.category.push(err.response.data.category[x]);
								}
							}
							if(err.response.data.name){
								for(var y=0;y<err.response.data.name.length;y++){
									errs.value.name.push(err.response.data.name[y]);
								}
							}
							if(err.response.data.slug){
								for(var z=0;z<err.response.data.slug.length;z++){
									errs.value.slug.push(err.response.data.slug[z]);
								}
							}
							if(!err.response.data.image&&!!err.response.data.category&&!!err.response.data.name&&!!err.response.data.slug){
								console.log(err.response);
							}
						}else{
							console.log(err.response);
							alert("ثبت با خطا مواجه شد. کنسول را چک کنید.")
						}
					}
				}else{
					if(!image.value){
						errs.value.image.push("لطفا ابتدا تصویری انتخاب کنید.");
					}else if(image.value.length>25){
						errs.value.image.push("تصویر معتبری را انتخاب کنید.");
					}
					if(!cats.value[category.value]){
						errs.value.category.push("لطفا ابتدا دسته ای انتخاب کنید.");
					}else if(cats.value[category.value].name.length>25){
						errs.value.category.push("دسته معتبری انتخاب کنید.");
					}
					if(!name.value){
						errs.value.name.push("نام زیردسته را وارد کنید.")
					}else if(name.value.length>25){
						errs.value.name.push("نام زیردسته باید حداکثر ۲۵ حرف باشد. اکنون "+name.value.length+" تا است.")
					}
					if(!slug.value){
						errs.value.slug.push("اسلاگ زیردسته را وارد کنید.");
					}else if(slug.value.length>25){
						errs.value.slug.push("اسلاگ زیردسته باید حداکثر ۲۵ حرف باشد. اکنون "+name.value.length+" تا است.");
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
				()=>(route.params.cat,route.params.sub),
				(newCat,newSub)=>{
					if(route.name==="change-subcat"&&newSub&&newCat){
						category.value = null;
						image.value = null;
						imgAddress.value = null;
						name.value = null;
						slug.value = null;
						get_subcat()
					}
				}
			)
			return{category,image,imgAddress,name,slug,errs,cats,set_img,subber}
		},
		components:{choseImg}
	};
</script>
<style>
	@import '../assets/form.css';
</style>