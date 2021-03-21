<template>
	<h2 class="cen">کاربر جدید</h2>
	<form @submit.prevent="sub()" class="form" id="user-form">
		<div v-if="imgAddress" class="form-img-div"><img :src="imgAddress"></div>
		<label for="prof_picture">تصویر پروفایل: </label>
		<span v-if="errs.prof_picture!=false"><p v-for="(err,i) in errs.prof_picture" :key="i" class="red-text">* {{err}}</p></span>
		<choseImg @selected="set_img"/>
		<label for="email">ایمیل: </label>
		<span v-if="errs.email!=false"><p v-if="(err,i) in errs.email" :key="i" class="red-text">* {{err}}</p></span>
		<input type="email" name="email" maxlength="30" class="data-field" v-model="email">
		<label for="password">پسورد: </label>
		<span v-if="errs.password!=false"><p v-for="(err,i) in errs.password" :key="i" class="red-text">* {{err}}</p></span>
		<input type="password" name="password" class="data-field" v-model="password">
		<p class="link-like" @click="show_pass()">نمایش پسورد</p>
		<label for="username">نام کاربری: </label>
		<span v-if="errs.username!=false"><p v-for="(err,i) in errs.username" :key="i" class="red-text">* {{err}}</p></span>
		<input type="text" name="username" maxlength="30" class="data-field" v-model="username">
		<label for="name">نام: </label>
		<span v-if="errs.name!=false"><p v-for="(err,i) in errs.name" :key="i" class="red-text">* {{err}}</p></span>
		<input type="text" name="name" maxlength="35" class="data-field" v-model="name">
		<label for="is_active">فعال: </label>
		<span v-if="errs.is_active!=false"><p v-for="(err,i) in errs" :key="i" class="red-text">* {{err}}</p></span>
		<input type="checkbox" name="is_active" class="data-field" v-model="is_active">
		<label for="is_staff">دسترسی کامل باشد?</label>
		<span v-if="errs.is_staff!=false"><p v-for="(err,i) in errs.is_staff" :key="i" class="red-text">* {{err}}</p></span>
		<input type="checkbox" name="is_staff" class="data-field" v-model="is_staff">
		<label for="pubmail">ایمیل عمومی: </label>
		<span v-if="errs.pubmail!=false"><p v-for="(err,i) in errs.pubmail" :key="i" class="red-text">* {{err}}</p></span>
		<input type="email" name="pubmail" maxlength="30" class="data-field" v-model="pubmail">
		<label for="bio">بایوگرافی: </label>
		<span v-if="errs.bio!=false"><p v-for="(err,i) in errs" :key="i" class="red-text">* {{err}}</p></span>
		<textarea name="bio" class="data-field" maxlength="400" v-model="bio"></textarea>
		<label for="about">درباره: </label>
		<span v-if="errs.about!=false"><p v-for="(err,i) in errs.about" :key="i" class="red-text">* {{err}}</p></span>
		<textarea name="about" class="data-field" maxlength="400" v-model="about"></textarea>
		<label for="favorite_cat">دسته موردعلاقه: </label>
		<span v-if="errs.favorite_cat!=false"><p v-for="(err,i) in errs.favorite_cat" :key="i" class="red-text">* {{err}}</p></span>
		<select name="favorite_cat" class="data-field" v-model="favorite_cat">
			<option v-for="(cat,i) in cats" :key="i">{{cat.name}}</option>
		</select>
		<label for="instagram_link">صفحه اینستاگرام: </label>
		<span v-if="errs.instagram_link!=false"><p v-for="(err,i) in errs.instagram_link" :key="i" class="red-text">* {{err}}</p></span>
		<input type="url" name="instagram_link" class="data-field" maxlength="35" v-model="instagram_link">
		<label for="facebook_link">صفحه فیسبوک: </label>
		<span v-if="errs.facebook_link!=false"><p v-for="(err,i) in errs.facebook_link" :key="i" class="red-text">* {{err}}</p></span>
		<input type="url" name="facebook_link" class="data-field" maxlength="35" v-model="facebook_link">
		<label for="github_link">صفحه گیتهاب : </label>
		<span v-if="errs.github_link!=false"><p v-for="(err,i) in errs.github_link" :key="i" class="red-text">* {{err}}</p></span>
		<input type="url" name="github_link" class="data-field" maxlength="35" v-model="github_link">
		<label for="birthday">تاریخ تولد: </label>
		<span v-if="errs.birthday!=false"><p v-for="(err,i) in errs.birthday" :key="i" class="red-text">* {{err}}</p></span>
		<input type="date" name="birthday" class="data-field" v-model="birthday">
		<button class="sub-button">ثبت</button>
	</form>
</template>
<script>
	import {ref} from 'vue';
	import choseImg from '@/components/choseImg.vue';
	import {getAPI} from '@/axios.js';
	import {useStore} from 'vuex';
	import {useRouter} from 'vue-router';
	export default{
		name: "lmAddUser",
		components:{choseImg},
		setup(){
			const email = ref(null);
			const password = ref(null);
			const username = ref(null);
			const name = ref(null);
			const prof_picture = ref(null);
			const imgAddress = ref(null);
			const is_active = ref(null);
			const is_staff = ref(null);
			const pubmail = ref(null);
			const bio = ref(null);
			const about = ref(null);
			const favorite_cat = ref(null);
			const instagram_link = ref(null);
			const facebook_link = ref(null);
			const github_link = ref(null);
			const birthday = ref(null);
			const errs = ref({'email':[],'password':[],'username':[],'name':[],'prof_picture':[],'is_active':[],'is_staff':[],'pubmail':[],'bio':[],'about':[],'favorite_cat':[],'instagram_link':[],'facebook_link':[],'github_link':[],'birthday':[]});

			function set_img(name,address){
				if(name.length<=25){
					prof_picture.value = name;
					imgAddress.value = address;
				}
			}
			const passfieldtype = ref(true);
			function show_pass(){
				passfieldtype.value = !passfieldtype.value;
				const passfield = document.getElementById("user-form")["password"]
				if(passfieldtype.value){
					passfield.type = "password";
				}else{
					passfield.type = "text";
				}
			}
			const store = useStore();
			const cats = ref(null);
			async function get_cats(){
				try{
					const res = await getAPI.get("categories/all/api/v1/",{headers:{Authorization: `JWT ${store.state.accessToken}`}});
					cats.value = res.data;
				}catch(err){
					console.log(err);
					console.log(err.response);
					alert("مشکلی در دریافت دسته ها پیش آمد.");
				}
			}
			get_cats();
			const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
			const router = useRouter();
			async function sub(){
				errs.value.email = [];
				errs.value.password = [];
				errs.value.username = [];
				errs.value.name = [];
				errs.value.prof_picture = [];
				errs.value.is_active = [];
				errs.value.is_staff = [];
				errs.value.pubmail = [];
				errs.value.bio = [];
				errs.value.about = [];
				errs.value.favorite_cat = [];
				errs.value.instagram_link = [];
				errs.value.facebook_link = [];
				errs.value.github_link = [];
				errs.value.birthday = [];
				if(email.value&&email.value.length<=30&&re.test(email.value)&&username.value&&username.value.length<=30&&name.value&&name.value.length<=35&&prof_picture.value&&prof_picture.value.length<=25&&((pubmail.value&&pubmail.value.length<=30&&re.test(pubmail.value))||!pubmail.value)&&((bio.value&&bio.value.length<=400)||!bio.value)&&((about.value&&about.value.length<=400)||!about.value)&&((favorite_cat.value&&favorite_cat.value.length<=25)||!favorite_cat.value)&&((instagram_link.value&&instagram_link.value.length<=35&&instagram_link.value.includes("https://instagram.com/"))||!instagram_link.value)&&((facebook_link.value&&facebook_link.value.length<=35&&facebook_link.value.includes("https://facebook.com/"))||!facebook_link.value)&&((github_link.value&&github_link.value.length<=35&&github_link.value.includes("https://github.com/"))||!github_link.value)){
					try{
						const res = await getAPI.post("users/mapi/v1/",{
							email: email.value,
							password: password.value,
							username: username.value,
							name: name.value,
							prof_picture: {name: prof_picture.value},
							is_active: is_active.value,
							is_staff: is_staff.value,
							pubmail: pubmail.value,
							bio: bio.value,
							about: about.value,
							favorite_cat: {name: favorite_cat.value},
							instagram_link: instagram_link.value,
							facebook_link: facebook_link.value,
							github_link: github_link.value,
							birthday: birthday.value
						},{headers:{Authorization:`JWT ${store.state.accessToken}`}});
						if(res.status===201){
							alert(res.data.message);
							router.push({name: "lm-users"});
						}else{
							console.log(res.status);
							console.log(res)
							alert("خطایی ره داد، کنسول را چک کنید.")
						}
					}catch(err){
						console.log(err.response.status);
						console.log(err.response);
						console.log(err);
					}
				}else{
					if(!email.value){
						errs.value.email.push("لطفا ابتاد ایمیل را وارد کنید.");
					}else if(email.value.length>30){
						errs.value.email.push("حداکثر طول ایمیل ۳۰ حرف است، ایمیل وارد شده "+email.value.length+" حرف دارد.");
					}else if(!re.test(email.value)){
						errs.value.email.push("لطفا ایمیل معتبری وارد کنید.");
					}
					if(!password.value){
						errs.value.password.push("لطفا ابتدا پسورد را وارد کنید.");
					}
					if(!username.value){
						errs.value.username.push("لطفا ابتدا نام کاربری را وارد کنید.");
					}else if(username.value.length>30){
						errs.value.username.push("حداکثر طول نام کاربری ۳۰ حرف است، نام کاربری وارد شده "+username.value.length+" حرف دارد.");
					}
					if(!name.value){
						errs.value.name.push("لطفا ابتدا نام را وارد کنید.");
					}else if(name.value.length>35){
						errs.value.name.push("حداکثر طول نام ۳۵ حرف است، نام وارد شده "+name.value.length+" حرف دارد.");
					}
					if(!prof_picture.value){
						errs.value.prof_picture.push("لطفا ابتدا تصویر پروفایل را انتخاب کنید.");
					}else if(prof_picture.value.length>25){
						errs.value.prof_picture.push("لطفا تصویر معتبری انتخاب کنید.");
					}
					if(pubmail.value&&pubmail.value.length>30){
						errs.value.pubmail.push("حداکثر طول ایمیل عمومی ۳۰ حرف است، ایمیل عمومی وارد شده "+pubmail.value.length+" حرف دارد.");
					}else if(pubmail.value&&!re.test(pubmail.value)){
						errs.value.pubmail.push("لطفا ایمیل عمومی معتبری وارد کنید.");
					}
					if(bio.value&&bio.value.length>400){
						errs.value.bio.push("حداکثر طول بایوگرافی ۴۰۰ حرف است، بایوگرافی وارد شده "+bio.value.length+" حرف دارد.");
					}
					if(about.value&&about.value.length>400){
						errs.value.about.push("حداکثر طول درباره ۴۰۰ حرف است، درباره وارد شده "+about.value.length+" حرف دارد.");
					}
					if(instagram_link.value&&instagram_link.value.length>35){
						errs.value.instagram_link.push("حداکثر طول آدرس اینستاگرام ۳۵ حرف است، آدرس وارد شده "+instagram_link.value.length+" حرف دارد.");
					}else if(instagram_link.value&&!instagram_link.value.includes("https://instagram.com/")){
						errs.value.instagram_link.push("لطفا آدرس اینستاگرام معتبری وارد کنید.");
					}
					if(facebook_link.value&&facebook_link.value.length>35){
						errs.value.facebook_link.push("حداکثر طول آدرس فیسبوک ۳۵ حرف است، آدرس وارد شده "+facebook_link.value.length+" حرف دارد.");
					}else if(facebook_link.value&&!facebook_link.value.includes("https://facebook.com/")){
						errs.value.facebook_link.push("لطفا آدرس فیسبوک معتبری وارد کنید.");
					}
					if(github_link.value&&github_link.value.length>35){
						errs.value.github_link.push("حداکثر طول آدرس گیتهاب ۳۵ حرف است، آدرس وارد شده "+github_link.value.length+" حرف است.");
					}else if(github_link.value&&!github_link.value.includes("https://github.com/")){
						errs.value.github_link.push("لطفا آدرس گیتهاب معتبری وارد کنید.");
					}
				}
			}
			return{email,password,username,name,imgAddress,set_img,is_active,is_staff,pubmail,bio,about,favorite_cat,instagram_link,facebook_link,github_link,birthday,errs,show_pass,cats,sub}
		}
	};
</script>
<style>
	@import '../assets/form.css';
</style>