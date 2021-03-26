<template>
	<h2 class="cen">تغییر تگ</h2>
	<form class="form" @submit.prevent="sub(tagslug)">
		<label for="name"></label>
		<span v-if="errs.name!=false"><p v-for="(err,i) in errs.name" :key="i" class="red-text">* {{err}}</p></span>
		<input type="text" name="name" class="data-field" v-model="name" required="" maxlength="25">
		<button class="sub-button">ثبت</button>
	</form>
</template>
<script>
	import {getAPI} from '@/axios.js';
	import {useStore} from 'vuex';
	import {useRouter,useRoute} from 'vue-router';
	import {ref,watch} from 'vue';
	export default{
		name: "lmChangeTag",
		props:['tagslug'],
		setup(props){
			const name = ref(null);
			const store = useStore();
			const router = useRouter();
			const route = useRoute();
			const errs = ref({'name':[]});
			async function get_tag(slug){
				try{
					const res = await getAPI.get("tags/api/v1/"+slug+'/',{headers:{Authorization:`JWT ${store.state.accessToken}`}});
					name.value = res.data.name;
				}catch(err){
					console.log(err)
					console.log(err.response)
				}
			}
			get_tag(props.tagslug)
			watch(
				()=>route.params.tagslug,
				newTag=>{
					if(route.name==="change-tag"){
						get_tag(newTag);
					}
				}
			)
			async function sub(tagslug){
				errs.value.name = [];
				if(name.value&&name.value.length<=25){
					try{
						const fd = {}
						fd['name'] = name.value;
						fd['slug'] = name.value.replace(" ","-");
						const res = await getAPI.put("tags/api/v1/"+tagslug+'/',fd,{headers:{Authorization:`JWT ${store.state.accessToken}`}})
						if(res.status===200){
							router.push({name:"lm-tags"})
						}
					}catch(err){
						console.log(err);
						if(err.response.status===400){
							if(err.response.data.name||err.response.data.slug){
								for(var i=0;i<err.response.data.name.length;i++){
									errs.value.name.push(err.response.data.name[i]);
								}
								for(var x=0;x<err.response.data.slug.length;x++){
									errs.value.name.push(err.response.data.slug[x]);
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