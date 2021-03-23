<template>
	<h2 class="cen">تغییر اطلاعات {{usern}}</h2>
	<form class="form" @submit.prevent="sub()">
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
	import {useRouter} from 'vue-router';
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
				if(){
					try{
						
					}catch(err){
						if(err.response.status===400){
							if(err.response.data.email!=false){
								for(var a=0;a<err.response.data.email.length;a++){
									errs.value.email.push(err.response.data.email[a]);
								}
							}
							if(err.response.data.password!=false){
								for(var b=0;b<err.response.data.password.length;b++){
									errs.value.password.push(err.response.data.password[b]);
								}
							}
							if(err.response.data.username!=false){
								for(var c=0;c<err.response.data.username.length;c++){
									errs.value.username.push(err.response.data.username[c]);
								}
							}
							if(err.response.data.name!=false){
								for(var d=0;d<err.response.data.name.length;d++){
									errs.value.name.push(err.response.data.name[d]);
								}
							}
							if(err.response.data.prof_picture!=false){
								for(var e=0;e<err.response.data.prof_picture.length;e++){
									errs.value.prof_picture.push(err.response.data.prof_picture[e]);
								}
							}
							if(err.response.data.is_active!=false){
								for(var f=0;f<err.response.data.is_active.length;f++){
									errs.value.is_active.push(err.response.data.is_active[f]);
								}
							}
							if(err.response.data.is_staff!=false){
								for(var g=0;g<err.response.data.is_staff.length;g++){
									errs.value.is_staff.push(err.response.data.is_staff[g]);
								}
							}
							if(err.response.data.pubmail!=false){
								for(var h=0;h<err.response.data.pubmail.length;h++){
									errs.value.pubmail.push(err.response.data.pubmail[h]);
								}
							}
							if(err.response.data.bio!=false){
								for(var i=0;i<err.response.data.bio.length;i++){
									errs.value.bio.push(err.response.data.bio[i]);
								}
							}
							if(err.response.data.about!=false){
								for(var j=0;j<err.response.data.about.length;j++){
									errs.value.about.push(err.response.data.about[j]);
								}
							}
							if(err.response.data.favorite_cat!=false){
								for(var k=0;k<err.response.data.favorite_cat.length;k++){
									errs.value.favorite_cat.push(err.response.data.favorite_cat[k]);
								}
							}
							if(err.response.data.instagram_link!=false){
								for(var l=0;l<err.response.data.instagram_link.length;l++){
									errs.value.instagram_link.push(err.response.data.instagram_link[l]);
								}
							}
							if(err.response.data.facebook_link!=false){
								for(var m=0;m<err.response.data.facebook_link.length;m++){
									errs.value.facebook_link.push(err.response.data.facebook_link[m]);
								}
							}
							if(err.response.data.github_link!=false){
								for(var n=0;n<err.response.data.github_link.length;n++){
									errs.value.github_link.push(err.response.data.github_link[n]);
								}
							}
							if(err.response.data.birthday!=false){
								for(var o=0;o<err.response.data.birthday.length;o++){
									errs.value.birthday.push(err.response.data.birthday[o]);
								}
							}
						}else{
							alert("خطایی رخ داد. لطفا کنسول را چک کنید.");
						}
						console.log(err)
						console.log(err.response)
					}
				}else{
					// front validations
				}
			}
			return{email,password,username,name,prof_picture,imgAddress,is_active,is_staff,pubmail,bio,about,favorite_cat,instagram_link,facebook_link,github_link,birthday,show_pass,errs,set_img,cats,sub}
		}
	};
</script>
<style>
	@import '../assets/form.css';
</style>