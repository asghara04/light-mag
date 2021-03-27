<template>
	<h2 class="cen">تغییر کامنت</h2>
	<form class="form" @submit.prevent="sub(pk)">
		<label for="name">نام: </label>
		<span v-if="errs.name!=false"><p v-for="(err,i) in errs.name" :key="i" class="red-text">* {{err}}</p></span>
		<input type="text" name="name" class="data-field" required="" v-model="name" maxlength="30">
		<label for="email">ایمیل: </label>
		<span v-if="errs.email!=false"><p v-for="(err,i) in errs.email" :key="i" class="red-text">* {{err}}</p></span>
		<input type="email" name="email" class="data-field" required="" v-model="email" maxlength="30">
		<label for="message">متن: </label>
		<span v-if="errs.message!=false"><p v-for="(err,i) in errs.message" :key="i" class="red-text">* {{err}}</p></span>
		<textarea name="message" class="data-field" required="" maxlength="350" v-model="message"></textarea>
		<label for="status">وضعیت: </label>
		<span v-if="errs.status!=false"><p v-for="(err,i) in errs.status" :key="i" class="red-text">* {{err}}</p></span>
		<input type="checkbox" name="status" class="data-field" v-model="status">
		<label for="personal">شخصی: </label>
		<span v-if="errs.personal!=false"><p v-for="(err,i) in errs.personal" :key="i" class="red-text">* {{err}}</p></span>
		<input type="checkbox" name="personal" class="data-field" v-model="personal">
		<label for="readed">خوانده شده: </label>
		<span v-if="errs.readed!=false"><p v-for="(err,i) in errs.readed" :key="i" class="red-text">* {{err}}</p></span>
		<input type="checkbox" name="readed" class="data-field" v-model="readed">
		<button class="sub-button">ثبت</button>
	</form>
</template>
<script>
	import {ref} from 'vue';
	import {useStore} from 'vuex';
	import {getAPI} from '@/axios.js';
	export default{
		name: "lmChangeComment",
		props: ["compk"],
		setup(props){
			const article = ref(null);
			const name = ref(null);
			const email = ref(null);
			const message = ref(null);
			const status = ref(null);
			const personal = ref(null);
			const readed = ref(true);
			const errs = {'article':[],'name':[],'email':[],"message":[],"status":[],"personal":[],"readed":[]};
			const store = useStore();
			async function get_comment(pk){
				try{
					const res = await getAPI.get("comments/mapi/v1/"+pk+'/',{headers:{Authorization:`JWT ${store.state.accessToken}`}});
					article.value = res.data.article
					name.value = res.data.name;
					email.value = res.data.email;
					message.value = res.data.message;
					status.value = res.data.status;
					personal.value = res.data.personal;
					readed.value = res.data.readed;
				}catch(err){
					console.log(err)
					alert("خطایی در دریافت اطلاعات کامنت رخ داد.")
					console.log(err.response)
				}
			}
			get_comment(props.compk)
			return{name,email,message,status,personal,readed,errs}
		}
	};
</script>
<style>
	@import '../assets/form.css';
</style>