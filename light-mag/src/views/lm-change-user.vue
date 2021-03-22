<template>
	<h2 class="cen">تغییر اطلاعات {{usern}}</h2>
	<form class="form">
		<div v-if="imgAddress" class="form-img-div"><img :src="imgAddress"></div>
		<label for="prof_picture">تصویر پروفایل: </label>
		<span v-if="errs.prof_picture!=false"><p v-for="(err,i) in errs.prof_picture" :key="i" class="red-text">* {{err}}</p></span>
		<choseImg @selected="set_img"/>
		<label for="email">ایمیل: </label>
		<span v-if="errs.email!=false"><p v-if="(err,i) in errs.email" :key="i" class="red-text">* {{err}}</p></span>
		<input type="email" name="email" maxlength="30" required="" class="data-field" v-model="email">
		<label for="password">پسورد: </label>
		<span v-if="errs.password!=false"><p v-for="(err,i) in errs.password" :key="i" class="red-text">* {{err}}</p></span>
		<input type="password" name="password" class="data-field" required="" v-model="password">
		<p class="link-like" @click="show_pass()">نمایش پسورد</p>
		<label for="username">نام کاربری: </label>
		<span v-if="errs.username!=false"><p v-for="(err,i) in errs.username" :key="i" class="red-text">* {{err}}</p></span>
		<input type="text" name="username" required="" maxlength="30" class="data-field" v-model="username">
		<label for="name">نام: </label>
		<span v-if="errs.name!=false"><p v-for="(err,i) in errs.name" :key="i" class="red-text">* {{err}}</p></span>
		<input type="text" name="name" maxlength="35" required="" class="data-field" v-model="name">
		<label for="is_active">فعال: </label>
		<span v-if="errs.is_active!=false"><p v-for="(err,i) in errs" :key="i" class="red-text">* {{err}}</p></span>
		<input type="checkbox" name="is_active" class="data-field" v-model="is_active">
		<label for="is_staff">دسترسی کامل: </label>
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
	import {useStore} from 'vuex';
	import {getAPI} from '@/axios.js';
	import choseImg from '@/components/choseImg.vue';
	export default{
		name: "lmChangeUser",
		props: ['usern'],
		components:{choseImg},
		setup(props){
			const store = useStore();
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
			async function get_user(usern){
				try{
					const res = await getAPI.get("users/mapi/v1/"+usern,{headers:{Authorization:`JWT ${store.state.accessToken}`}});
					email.value = res.data.email;
					password.value = res.data.password;
					username.value = res.data.username;
					name.value = res.data.name;
					prof_picture.value = res.data.prof_picture.name;
					imgAddress.value = res.data.prof_picture.image;
					is_active.value = res.data.is_active;
					is_staff.value = res.data.is_staff;
					pubmail.value = res.data.pubmail;
					bio.value = res.data.bio;
					about.value = res.data.about;
					favorite_cat.value = res.data.favorite_cat;
					instagram_link.value = res.data.instagram_link;
					facebook_link.value = res.data.facebook_link;
					github_link.value = res.data.github_link;
					birthday.value = res.data.birthday;
				}catch(err){
					console.log(err);
					console.log(err.response);
					alert("خطایی در دریافت اطلاعات کاربر رخ داد. کنسول را چک کنید.");
				}
			}
			get_user(props.usern);
			function set_img(name,address){
				if(name.value.length<=25){
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
			return{email,password,username,name,prof_picture,imgAddress,is_active,is_staff,pubmail,bio,about,favorite_cat,instagram_link,facebook_link,github_link,birthday,show_pass,errs,set_img,cats}
		}
	};
</script>
<style>
	@import '../assets/form.css';
</style>