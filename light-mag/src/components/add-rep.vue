<template>
	<p v-if="!form" class="red-text" @click.prevent="form=true">پاسخ دادن</p>
	<form v-if="form" class="form" @submit.prevent="sub(id)">
		<label for="name">نام: </label>
		<span v-if="errs.name"><p v-for="(err,i) in errs.name" :key="i" class="red-text">* {{err}}</p></span>
		<input type="text" name="name" maxlength="30" class="data-field" v-model="name">
		<label for="email">ایمیل: </label>
		<span v-if="errs.email"><p v-for="(err,i) in errs.email" :key="i" class="red-text">* {{err}}</p></span>
		<input type="email" name="email" maxlength="30" class="data-field" v-model="email">
		<label for="message">پاسخ: </label>
		<span v-if="message"><p v-for="(err,i) in errs.message" :key="i" class="red-text">* {{err}}</p></span>
		<textarea maxlength="250" name="message" class="data-field" v-model="message"></textarea>
		<button class="sub-button">ثبت</button>
	</form>
</template>
<script>
	import {ref} from 'vue';
	import {getAPI} from '@/axios.js';
	export default{
		name: "Addrep",
		props:['id'],
		setup(){
			const form = ref(false);
			const name = ref(null);
			const email = ref(null);
			const message = ref(null);
			const errs = ref({'name':[],'email':[],'message':[]});
			const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
			async function sub(id){
				errs.value.name = [];
				errs.value.email = [];
				errs.value.message = [];
				if(name.value&&name.value.length<30&&email.value&&email.value.length<=30&&re.test(email.value)&&message.value&&message.value.length<=250){
					try{
						const res = await getAPI.post("comments/reply/api/v1/"+id+'/',{
							comment: id,
							name: name.value,
							email: email.value,
							message: message.value
						});
						if(res.status===201){
							alert(res.data.message)
							name.value = null;
							email.value = null;
							message.value = null;
							form.value = false;
						}else{
							alert("یه مشکلی پیش اومد! لطفا دوباره امتحان کنید.")
						}
					}catch(err){
						if(err.response.stats===400){
							if(err.response.data.name){
								for(var x=0;x<err.response.data.name.length;x++){
									errs.value.name.push(err.response.data.name[x]);
								}
							}
							if(err.response.data.email){
								for(var y=0;y<err.response.data.email.length;y++){
									errs.value.email.push(err.response.data.email[y]);
								}
							}
							if(err.response.data.message){
								for(var z=0;z<err.response.data.message.length;z++){
									errs.value.message.push(err.response.data.message[z]);
								}
							}
						}else{
							alert("یه مشکلی ویش اومد. لطفا دوباره امتحان کنید.");
							console.log(err)
						}
					}
				}else{
					if(!name.value){
						errs.value.name.push("لطفا نام تون رو وارد کنید.");
					}else if(name.value.length>30){
						errs.value.name.push('حداکثر طول نام 30 حرف است، اکنون '+name.value.length+' حرف وارد شده است.');
					}
					if(!email.value){
						errs.value.email.push("لطفا ایمیل تون رو وارد کنید.");
					}else if(email.value.length>30){
						errs.value.name.push('حداکثر طول ایمیل 30 حرف است، اکنون '+email.value.length+' حرف وارد شده است.');
					}else if(!re.test(email.value)){
						errs.value.email.push("لطفا ایمیلمعتبری وارد کنید.");
					}
					if(!message.value){
						errs.value.email.push("لطفا پاسخ تون رو وارد کنید.");
					}else if(message.value.length>250){
						errs.value.message.push('حداکثر طول پاسخ 250 حرف است، اکنون '+message.value.length+' حرف وارد شده است.');
					}
				}
			}

			return{form,name,email,message,sub,errs}
		}
	};
</script>
<style>
	@import '../assets/form.css';
</style>