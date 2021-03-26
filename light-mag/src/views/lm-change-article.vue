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
	import {useRoute,useRouter} from 'vue-router';
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
			const errs = ref({'title':[],'slug':[],'image':[],'description':[],'body':[],'category':[],'subcat':[],'tags':[],'status':[],'author':[]})
			const store = useStore()
			async function get_art(pk){
				try{
					const res = await getAPI.get("articles/mapi/v1/"+pk+'/',{headers:{Authorization:`JWT ${store.state.accessToken}`}});
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
							ts.value += tags.value[i].name
							if(i<tags.value.length-1){
								ts.value += ',';
							}
						}
					}
					status.value = res.data.status;
					author.value = res.data.author.username;
					get_cats();
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
			async function get_cats(){
				try{
					const res = await getAPI.get("categories/all/api/v1/",{headers:{Authorization:`JWT ${store.state.accessToken}`}});
					cats.value = res.data;
					set_subs();
				}catch(err){
					console.log(err);
					console.log(err.response);
				}
			}
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
			const router = useRouter();
			async function sub(pk){
				errs.value.title = [];
				errs.value.slug = [];
				errs.value.image = [];
				errs.value.description = [];
				errs.value.body = [];
				errs.value.category = [];
				errs.value.subcat = [];
				errs.value.tags = [];
				errs.value.status = [];
				errs.value.author = [];
				if(title.value&&title.value.length<=120&&slug.value&&slug.value.length<=120&&(!image.value||(image.value&&image.value.length<=25))&&description.value&&description.value.length<=200&&body.value&&body.value.length<=360000&&(!category.value||(category.value&&category.value.length<=25))&&(!subcat.value||(subcat.value&&subcat.value.length<=25))&&(!ts.value||(ts.value&&ts.value.length<=250))&&(!status.value||(status.value&&status.value.length<=8))&&(!author.value||(author.value&&author.value.length<=30))){
					try{
						const fd = {};
						fd['title'] = title.value;
						fd['slug'] = slug.value;
						fd['image'] = {name: image.value};
						fd['description'] = description.value;
						fd['body'] = body.value;
						if(category.value){
							fd['category'] = {name: category.value}
						}
						if(subcat.value){
							fd['subcat'] = {name: subcat.value}
						}
						if(ts.value!=false){
							tags.value = ts.value.split(",");
							for(var i=0;i<tags.value.length;i++){
								tags.value[i] = {name: tags.value[i], slug: tags.value[i].replace(" ","-")}
							}
							fd['tags'] = tags.value;
						}
						fd['status'] = status.value;
						fd['author'] = {username: author.value};
						const res = await getAPI.patch("articles/mapi/v1/"+pk+'/',fd,{headers:{Authorization:`JWT ${store.state.accessToken}`}});
						if(res.status===200){
							router.push({name: "lm-articles"});
						}
					}catch(err){
						console.log(err)
						if(err.response.status===400){
							if(err.response.data.title!=false){
								for(var a=0;a<err.response.data.title.length;a++){
									errs.value.title.push(err.response.data.title[a]);
								}
							}
							if(err.response.data.slug!=false){
								for(var s=0;s<err.response.data.slug.length;s++){
									errs.value.slug.push(err.response.data.slug[s]);
								}
							}
							if(err.response.data.image){
								for(var g=0;g<err.response.data.image.length;g++){
									errs.value.image.push(err.response.data.image[g]);
								}
							}
							if(err.response.data.description){
								for(var h=0;h<err.response.data.description.length;h++){
									errs.value.description.push(err.response.data.description[h]);
								}
							}
							if(err.response.data.body){
								for(var d=0;d<err.response.data.body.length;d++){
									errs.value.body.push(err.response.data.body[d]);
								}
							}
							if(err.response.data.category){
								for(var k=0;k<err.response.data.category.length;k++){
									errs.value.category.push(err.response.data.category[k]);
								}
							}
							if(err.response.data.subcat){
								for(var m=0;m<err.response.data.subcat.length;m++){
									errs.value.subcat.push(err.response.data.subcat[m]);
								}
							}
							if(err.response.data.tags){
								for(var n=0;n<err.response.data.tags.length;n++){
									errs.value.tags.push(err.response.data.tags[n]);
								}
							}
							if(err.response.data.status){
								for(var b=0;b<err.response.data.status.length;b++){
									errs.value.status.push(err.response.data.status[b]);
								}
							}
							if(err.response.data.author){
								for(var c=0;c<err.response.data.author.length;c++){
									errs.value.author.push(err.response.data.author[c]);
								}
							}
						}else{
							console.log(err.response);
							alert("خطایی رخ داد، کنسول را چک کنید.");
						}
					}
				}else{
					alert(0)
					if(!title.value){
						errs.value.title.push("لطفا عنوان مقاله را وارد کنید.");
					}else if(title.value.length>120){
						errs.value.title.push("حداکثر طول عنوان مقاله ۱۲۰ حرف است، عنوان وارد شده "+title.value.length+" حرف دارد.");
					}
					if(!slug.value){
						errs.value.slug.push("لطفا اسلاگ مقاله را وارد کنید.");
					}else if(slug.value.length>120){
						errs.value.slug.push("حداکثر طول اسلاگ مقاله ۱۲۰ حرف است، اسلاگ وارد شده"+slug.value.length+" حرف دارد.");
					}
					if(image.value&&image.value.length>25){
						errs.value.image.push("لطفا تصویر معتبری انتخاب کنید.");
					}
					if(!description.value){
						errs.value.description.push("لطفا توضیحات معتبری وارد کنید.");
					}else if(description.value.length>200){
						errs.value.description.push("حداکثر طول توضیحات ۲۰۰ حرف است، توضیحات وارد شده "+description.value.length+" حرف دارد.");
					}
					if(!body.value){
						errs.value.body.push("لطفا بدنه مقاله را وارد کنید.");
					}else if(body.value.length>360000){
						errs.value.body.push("حداکثر طول بدنه ۳۶۰۰۰۰ حرف است، بدنه وارد شده "+body.value+" حرف دارد.");
					}
					if(category.value&&category.value.length>25){
						errs.value.category.push("لطفا دسته معتبری انتخاب کنید.");
					}
					if(subcat.value&&subcat.value.length>25){
						errs.value.subcat.push("لطفا زیردسته معتبری انتخاب کنید.");
					}
					if(ts.value&&ts.value.length>250){
						errs.value.tags.push("تگ ها زیادی وارد شده است.");
					}
					if(!status.value){
						errs.value.status.push("لطفا وضعیت مقاله را انتخاب کنید.");
					}else if(status.value.length>8){
						errs.value.status.push("لطفا وضعیت معتبری انتخاب کنید.");
					}
					if(!author.value){
						errs.value.author.push("لطفا نویسنده مقاله را انتخاب کنید.");
					}else if(author.value.length>30){
						errs.value.author.push("لطفا کاربر معتبری انتخاب کنید");
					}
				}
			}
			return{title,slug,set_img,imgAddress,description,body,category,subcat,ts,status,author,cats,errs,set_subs,subs,users,sub}
		}
	};
</script>
<style>
	@import '../assets/form.css';
</style>