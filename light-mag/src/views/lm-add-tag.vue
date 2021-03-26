<template>
	<h2 class="cen">تگ جدید</h2>
	<form class="form" @submit.prevent="sub()">
		<label for="name">تگ: </label>
		<span v-if="errs.name!=false"><p v-for="(err,i) in errs.name" :key="i" class="red-text">* {{err}}</p></span>
		<input type="text" name="name" maxlength="25" v-model="name" class="data-field">
		<button class="sub-button">ثبت</button>
	</form>
</template>
<script>
	import {ref} from 'vue';
	import {getAPI} from '@/axios.js';
	import {useStore} from 'vuex';
	import {useRouter} from 'vue-router';
	export default{
		name: "lmAddTag",
		setup(){
			const name = ref(null);
			const errs = ref({'name':[]});
			const store = useStore();
			const router = useRouter();
			async function sub(){
				errs.value.name = [];
				if(name.value&&name.value.length<=25){
					try{
						const fd = {}
						fd['name'] = name.value;
						fd['slug'] = name.value.replace(" ","-");
						const res = await getAPI.post("tags/mapi/v1/",fd,{headers:{Authorization:`JWT ${store.state.accessToken}`}})
						if(res.status===201){
							router.push({name:"lm-tags"})
						}
					}catch(err){
						console.log(err)
						if(err.response.status===400){
							if(err.response.data.name||err.response.data.slug){
								for(var i=0;i<err.response.data.name.length;i++){
									errs.value.name.push(err.response.data.name[i]);
								}
								for(var x=0;x<err.response.data.slug.length;x++){
									errs.value.slug.push(err.response.data.slug[x]);
								}
							}
						}
					}
				}else{
					if(!name.value){
						errs.value.name.push("لطفا تگ را وارد کنید")
					}else if(name.value.length>25){
						errs.value.name.push("حداکثر طول تگ ۲۵ حرف است، تگ وارد شده "+name.value.length+" حرف دارد.")
					}
				}
			}
			return{name,errs,sub}
		}
	};
</script>
<style>
	@import '../assets/form.css';
</style>