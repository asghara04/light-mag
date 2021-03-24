<template>
	<h2 class="cen">نوشتن مقاله جدید</h2>
	<form class="form" @submit.prevent="sub()">
		<label for="title">عنوان: </label>
		<span v-if="errs.title!=false"><p v-for="(err,i) in errs.title" :key="i" class="red-text">* {{err}}</p></span>
		<input type="text" name="title" class="data-field" maxlength="80" v-model="title">
		<label for="slug">اسلاگ: </label>
		<span v-if="errs.slug!=false"><p v-for="(err,i) in errs.slug" :key="i" class="red-text">* {{err}}</p></span>
		<input type="text" name="slug" class="data-field" maxlength="80" v-model="slug">
		<div v-if="imgAddress" class="form-img-div"><img :src="imgAddress"></div>
		<label for="image">تصویر: </label>
		<span v-if="errs.image!=false"><p v-for="(err,i) in errs.image" :key="i" class="red-text">* {{err}}</p></span>
		<choseImg @selected="set_img"/>
		<label for="description">توضیح: </label>
		<span v-if="errs.description!=false"><p v-for="(err,i) in errs.description" :key="i" class="red-text">* {{err}}</p></span>
		<textarea name="description" maxlength="200" class="data-field" v-model="description"></textarea>
		<label for="body">بدنه: </label>
		<span v-if="errs.body!=false"><p v-for="(err,i) in errs.body" :key="i" class="red-text">* {{err}}</p></span>
		<!-- tiptap2 later -->
		<textarea name="body" maxlength="360000" class="data-field" v-model="body"></textarea>
		<label for="category">دسته: </label>
		<span v-if="errs.category!=false"><p v-for="(err,i) in errs.category" :key="i" class="red-text">* {{err}}</p></span>
		<select name="category" class="data-field" v-model="category" size="4" @change.prevent="set_subs()">
			<option v-for="(cat,i) in cats" :key="i">{{cat.name}}</option>
		</select>
		<label for="subcat">زیردسته: </label>
		<span v-if="errs.subcat!=false"><p v-for="(err,i) in errs.subcat" :key="i" class="red-text">* {{err}}</p></span>
		<select name="subcat" class="data-field" v-model="subcat">
			<option v-for="(sub,i) in subs" :key="i" class="data-field">{{sub.name}}</option>
		</select>
		<label for="tags">تگ ها: </label>
		<span v-if="errs.tags!=false"><p v-for="(err,i) in errs.tags" :key="i" class="red-text">* {{err}}</p></span>
		<p class="field-description">کلمات کلیدی را با , از هم جدا کنید.</p>
		<input type="text" name="tags" v-model="tags" class="data-field" maxlength="250">
		<label for="status">وضعیت: </label>
		<span v-if="errs.status!=false"><p v-for="(err,i) in errs.status" :key="i" class="red-text">* {{err}}</p></span>
		<select name="status" required="" class="data-field" v-model="status">
			<option>عمومی</option>
			<option>پیشنویس</option>
		</select>
		<label for="author">نویسنده: </label>
		<span v-if="errs.author!=false"><p v-for="(err,i) in errs.author" :key="i" class="red-text">* {{err}}</p></span>
		<select name="author" class="data-field" v-model="author">
			<option v-for="(user,i) in users" :key="i">{{user.username}}</option>
		</select>
	</form>
</template>
<script>
	import {ref} from 'vue';
	import choseImg from '@/components/choseImg.vue';
	import {getAPI} from '@/axios.js';
	import {useStore} from 'vuex';
	export default{
		name: "lmAddArticle",
		setup(){
			const title = ref(null);
			const slug = ref(null);
			const image = ref(null);
			const imgAddress = ref(null);
			const description = ref(null);
			const body = ref(null);
			const category = ref(null);
			const subcat = ref(null);
			const tags = ref([]);
			const status = ref("عمومی");
			const author = ref(null);
			const errs = ref({'title':[],'slug':[],'image':[],'description':[],'body':[],'category':[],'subcat':[],'tags':[],'status':[],'author':[]})
			function set_img(name,address){
				if(name.length<=25){
					image.value = name;
					imgAddress.value = address;
				}
			}
			const store = useStore();
			const cats = ref(null);
			async function get_cats(){
				try{
					const res = await getAPI.get("categories/all/api/v1/",{headers:{Authorization:`JWT ${store.state.accessToken}`}});
					cats.value = res.data;
				}catch(err){
					console.log(err);
					console.log(err.response);
				}
			}
			get_cats();
			const subs = ref(null);
			function set_subs(){
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
			return{title,slug,set_img,imgAddress,description,body,category,subcat,tags,status,author,errs,cats,set_subs,subs,users}
		},
		components:{choseImg}
	};
</script>
<style>
	@import '../assets/form.css';
</style>