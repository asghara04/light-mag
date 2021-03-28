<template>
	<h2 class="cen">تغییر پاسخ</h2>
	<form class="form" @submit.prevent="sub(reppk)">
		<label for="name">نام: </label>
		<span v-if="errs.name!=false"><p v-for="(err,i) in errs.name" :key="i" class="red-text">* {{err}}</p></span>
		<input type="text" name="name" class="data-field" v-model="name" maxlength="30" required="">
		<label for="email">ایمیل: </label>
		<span v-if="errs.email!=false"><p v-for="(err,i) in errs.email" :key="i" class="red-text">* {{err}}</p></span>
		<input type="email" name="email" class="data-field" v-model="email" maxlength="30" required="">
		<label for="message">پاسخ: </label>
		<span v-if="errs.message!=false"><p v-for="(err,i) in errs.message" :key="i" class="red-text">* {{err}}</p></span>
		<textarea class="data-field" name="message" v-model="message" maxlength="250" required=""></textarea>
		<label for="status">وضعیت: </label>
		<span v-if="errs.status!=false"><p v-for="(err,i) in errs.status" :key="i" class="red-text">* {{err}}</p></span>
		<input type="checkbox" name="status" v-model="status" class="data-field">
		<label for='readed'>خوانده شده: </label>
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
		name: "lmChangeReply",
		props:['reppk'],
		setup(props){
			document.querySelector("head title").textContent = "تغییر پاسخ - لایت مگ";
			document.querySelector("head meta[name='keywords']").setAttribute("content","noindex, nofollow")
			const comment = ref(null);
			const name = ref(null);
			const email = ref(null);
			const message = ref(null);
			const status = ref(null);
			const readed = ref(null);
			const errs = ref({"name":[],"email":[],"message":[],"status":[],"readed":[]});
			const store = useStore();
			async function get_rep(pk){
				try{
					const res = await getAPI.get("comments/reply/mapi/v1/"+pk,{headers:{Authorization:`JWT ${store.state.accessToken}`}});
					comment.value = res.data.comment;
					name.value = res.data.name;
					email.value = res.data.email;
					message.value = res.data.message;
					status.value = res.data.status;
					readed.value = res.data.readed;
				}catch(err){
					console.log(err);
					console.log(err.response)
					alert("somthing went wrong while requesting for reply data");
				}
			}
			get_rep(props.reppk)
			const router = useRouter();
			async function sub(pk){
				errs.value.name = [];
				errs.value.email = [];
				errs.value.message = [];
				errs.value.status = [];
				errs.value.readed = [];
				if(comment.value&&name.value&&name.value.length<=30&&email.value&&email.value.length<=30&&message.value&&message.value.length<=250){
					try{
						await getAPI.put("comments/reply/mapi/v1/"+pk+'/',{
							comment: comment.value,
							name: name.value,
							email: email.value,
							message: message.value,
							status: status.value,
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
					}else if(message.value.length>250){
						errs.value.message.push("حداکثر طول متن ۳۵۰ حرف است، متن وارد شده "+message.value.length+" حرف دارد.");
					}
				}
			}
			return{name,email,message,status,readed,errs,sub}
		}
	};
</script>
<style>
	@import '../assets/form.css';
</style>