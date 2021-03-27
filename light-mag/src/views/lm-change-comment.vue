<template>
	<h2 class="cen">تغییر کامنت</h2>
	<form class="form" @submit.prevent="sub(compk)">
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
	import {useRouter} from 'vue-router';
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
			const errs = ref({'article':[],'name':[],'email':[],"message":[],"status":[],"personal":[],"readed":[]});
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
			const router = useRouter();
			async function sub(pk){
				errs.value.name = [];
				errs.value.email = [];
				errs.value.message = [];
				errs.value.status = [];
				errs.value.personal = [];
				errs.value.readed = [];
				if(article.value&&name.value&&name.value.length<=30&&email.value&&email.value.length<=30&&message.value&&message.value.length<=350){
					try{
						await getAPI.put("comments/mapi/v1/"+pk+'/',{
							article: article.value,
							name: name.value,
							email: email.value,
							message: message.value,
							status: status.value,
							personal: personal.value,
							readed: readed.value
						},{headers:{Authorization:`JWT ${store.state.accessToken}`}});
						router.push({name: 'lm-comments'})
					}catch(err){
						console.log(err)
						if(err.response.status===400){
							if(err.response.data.name){
								for(var i=0;i<err.response.data.name.length;i++){
									errs.value.name.push(err.response.data.name[i]);
								}
							}
							if(err.response.data.email){
								for(var x=0;x<err.response.data.email.length;x++){
									errs.value.email.push(err.response.data.email[x]);
								}
							}
							if(err.response.data.message){
								for(var h=0;h<err.response.data.message.length;h++){
									errs.value.message.push(err.response.data.message[h]);
								}
							}
							if(err.response.data.status){
								for(var n=0;n<err.response.data.status.length;n++){
									errs.value.status.push(err.response.data.status[n])
								}
							}
							if(err.response.data.personal){
								for(var t=0;t<err.response.data.personal.length;t++){
									errs.value.personal.push(err.response.data.personal[n])
								}
							}
							if(err.response.data.readed){
								for(var c=0;c<err.response.data.readed.length;c++){
									errs.value.readed.push(err.response.data.readed[c])
								}
							}
						}else{
							alert("somthing went wrong chwck thw console")
						}
					}
				}else{
					if(!name.value){
						errs.value.name.push("لطفا نام را وارد کنید.");
					}else if(name.value.length>30){
						errs.value.name.push("حداکثر طول نام ۳۰ حرف است، نام وارد شده "+name.value.length+" حرف دارد.");
					}
					if(!email.value){
						errs.value.email.push("لطفا ایمیل را وارد کنید.");
					}else if(email.value.length>30){
						errs.value.email.push("حداکثر طول ایمیل ۳۰ حرف است، ایمیل وارد شده "+email.value.length+" حرف دارد.");
					}
					if(!message.value){
						errs.value.message.push("متن را وارد کنید.");
					}else if(message.value.length>350){
						errs.value.message.push("حداکثر طول متن ۳۵۰ حرف است، متن وارد شده "+message.value.length+" حرف دارد.");
					}
				}
			}
			return{name,email,message,status,personal,readed,sub,errs}
		}
	};
</script>
<style>
	@import '../assets/form.css';
</style>