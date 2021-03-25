<template v-if="APIData">
	<h2 class="cen">تغییر مقاله</h2>
	<form class="form" @submit.prevent="sub(pk)">
		<label for="title">عنوان: </label>
		<span v-if="errs.title!=false"><p v-for="(err,i) in errs.title" :key="i" class="red-text">* {{err}}</p></span>
		<input type="text" name="name" class="data-field" maxlength="120" v-model="title" required="">
		<label for="slug">اسلاگ: </label>
		<span v-if="errs.slug!=false"><p v-for="(err,i) in errs.slug" :key="i" class="red-text">* {{err}}</p></span>
		<input type="text" name="slug" class="data-field" maxlength="120" v-model="slug" required="">
		<div v-if="imgAddress" class="form-img-div"><img :src="imgAddress"></div>
		<label for="image">تصویر: </label>
		<span v-if="errs.image!=false"><p v-for="(err,i) in errs.image" :key="i" class="red-text">* {{err}}</p></span>
		<choseImg @selected="set_img"/>
		<label for="description">توضیحات: </label>
		<span v-if="errs.description!=false"><p v-for="(err,i) in errs.description" :key="i" class="red-text">* {{err}}</p></span>
		<textarea name="description" class="data-field" maxlength="200" required="" v-model="description"></textarea>
		<label for="body">بدنه: </label>
		<span v-if="errs.body!=false"><p v-for="(err,i) in errs.body" :key="i" class="red-text">* {{err}}</p></span>
		<textarea name="body" class="data-field" maxlength="360000" required="" v-model="body"></textarea>
		<label for="category">دسته: </label>
		<span v-if="errs.category!=false"><p v-for="(err,i) in errs.category" :key="i" class="red-text">* {{err}}</p></span>
		<select name="category" class="data-field" v-model="category" size="4" @change.prevent="set_subs()">
			<option v-for="(cat,i) in cats" :key="i">{{cat.name}}</option>
		</select>
		<label for="subcat">زیردسته: </label>
		<span v-if="errs.subcat!=false"><p class="red-text" v-for="(err,i) in errs.subcat" :key="i">* {{err}}</p></span>
		<select name="subcat" class="data-field" v-model="subcat">
			<option v-for="(sub,i) in subs" :key="i">{{sub.name}}</option>
		</select>
		<label for="tags">تگ ها: </label>
		<p class="field-description">کلمات کلیدی را با , از هم جدا کنید.</p>
		<span v-if="errs.tags!=false"><p v-for="(err,i) in errs.tags" :key="i" class="red-text">* {{err}}</p></span>
		<input type="text" name="tags" v-model="ts" class="data-field" maxlength="250">
		<label for="status">وضعیت: </label>
		<span v-if="errs.status!=false"><p v-for="(err,i) in errs.status" :key="i" class="red-text">* {{err}}</p></span>
		<select class="data-field" required="" name="status" v-model="status">
			<option>عمومی</option>
			<option>پیشنویس</option>
		</select>
		<label for="author">نویسنده: </label>
		<span v-if="errs.author!=false"><p v-for="(err,i) in errs.author" :key="i" class="red-text">* {{err}}</p></span>
		<select name="author" class="data-field" required="" v-model="author">
			<option v-for="(user,i) in users" :key="i">{{user.username}}</option>
		</select>
		<button class="sub-button">ثبت</button>
	</form>
</template>
<script>
	import {ref,watch} from 'vue';
	import {getAPI} from '@/axios.js';
	import {useStore} from 'vuex';
	import {useRoute} from 'vue-router';
	import choseImg from '@/components/choseImg.vue';
	export default{
		name:"lmChangeArticle",
		props: ['pk'],
		components:{choseImg},
		setup(props){
			const title = ref(null);
			const slug = ref(null);
			const image = ref(null);
			const imgAddress = ref(null);
			const description = ref(null);
			const body = ref(null);
			const category = ref(null);
			const subcat = ref(null);
			const tags = ref(null);
			const status = ref(null);
			const author = ref(null);
			const ts = ref('');
			const errs = {'title':["hello"],'slug':["slug","bye"],'image':["image"],'description':["description"],'body':["body"],'category':["category"],'subcat':["subcat"],'tags':["tags"],'status':["status"],'author':["author"]}
			const store = useStore()
			async function get_art(pk){
				try{
					const res = await getAPI.get("articles/mapi/v1/"+pk,{headers:{Authorization:`JWT ${store.state.accessToken}`}});
					title.value = res.data.title;
					slug.value = res.data.slug;
					if(res.data.image){
						image.value = res.data.image.name;
						imgAddress.value = res.data.image.image;
					}
					description.value = res.data.description;
					body.value = res.data.body;
					if(res.data.category){
						category.value = res.data.category.name;
					}
					if(res.data.subcat){
						subcat.value = res.data.subcat.name;
					}
					if(res.data.tags){
						tags.value = res.data.tags;
						for(var i=0;i<tags.value.length;i++){
							ts.value += tags.value[i].name+','
						}
					}
					status.value = res.data.status;
					author.value = res.data.author.username;
				}catch(err){
					alert("خطایی در دریافت اطلاعات مقاله رخ داد لطفا کنسول را چک کنید.")
					console.log(err);
					console.log(err.response);
				}
			}
			get_art(props.pk)
			const route = useRoute();
			watch(
				()=>route.params.pk,
				newPk=>{
					if(route.name==="change-article"){
						get_art(newPk)
					}
				}
			)
			async function set_img(name,address){
				if(name.length<=25){
					image.value = name;
					imgAddress.value = address;
				}
			}
			const cats = ref(null);
			(async function(){
				try{
					const res = await getAPI.get("categories/all/api/v1/",{headers:{Authorization:`JWT ${store.state.accessToken}`}});
					cats.value = res.data;
					set_subs();
				}catch(err){
					console.log(err);
					console.log(err.response);
				}
			})()
			const subs = ref(null);
			async function set_subs(){
				for(var i=0;i<cats.value.length;i++){
					if(cats.value[i].name===category.value){
						subs.value = cats.value[i].subcats;
					}
				}
			}
			const users = ref(null);
			(async function(){
				try{
					const res = await getAPI.get("users/acts/mapi/v1/",{headers:{Authorization:`JWt ${store.state.accessToken}`}})
					users.value = res.data;
				}catch(err){
					console.log(err);
					console.log(err.response);
				}
			})();
			return{title,slug,set_img,imgAddress,description,body,category,subcat,ts,status,author,cats,errs,set_subs,subs,users}
		}
	};
</script>
<style>
	@import '../assets/form.css';
</style>