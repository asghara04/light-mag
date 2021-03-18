<template>
	<p v-if="comments==false" class="cen link-like" @click.prevent="get_coms(endpoint)">نمایش کامنت ها</p>
	<div v-else class="com-box" ref="paginte">
		<div v-for="(com,i) in comments" :key="i" class="com">
			<h4>{{com.name}}</h4>
			<time class="s-size">{{com.jdate}}</time>
			<p class="message">{{com.message}}</p>
			<!-- <p class="red-text">پاسخ دادن</p>    component    -->
			<!-- <div v-if="com.reps">
				<p v-if="!replies" @click.prevent="get_reps(com.id,i)" class=" cen link-like">{{com.reps}} پاسخ، نمایش</p>
				<div v-else>
					
				</div>
			</div> -->
		</div>
	</div>
</template>
<script>
	import {ref} from 'vue';
	import {getAPI} from'@/axios.js';
	import {onBeforeUnmount} from 'vue';
	import {useRoute} from 'vue-router';
	export default{
		name: "Comments",
		props:['id'],
		setup(props){
			const comments = ref([]);
			const endpoint = ref("comments/api/v1/"+props.id);
			let more = false;
			let bottom = false;
			const paginte = ref(null);
			async function get_coms(end){
				if(endpoint.value&&end){
					try{
						const res = await getAPI.get(end);
						for(var i=0;i<res.data.results.length;i++){
							res.data.results[i]['replies'] = {next:null,reps:[]};
							comments.value.push(res.data.results[i]);
						}
						endpoint.value = res.data.next;
						console.log(endpoint.value);
						more = true;
						window.addEventListener('scroll',CaP);
					}catch(err){
						console.log(err)
					}
				}
			}
			function CaP(){
				return pagination(endpoint.value)
			}
			const route = useRoute();
			async function pagination(end){
				if(paginte.value){
					bottom = (window.scrollY+window.innerHeight)>=(paginte.value.offsetTop+paginte.value.offsetHeight-20)&&(window.scrollY+window.innerHeight)<(paginte.value.offsetTop+paginte.value.offsetHeight);
					console.log(bottom)
					if(bottom&&more&&end&&route.name==="article"){
						more = false;
						get_coms(end);
					}
				}
			}
			// async function get_reps(pk,i){
			// 	try{
			// 		const res = await getAPI.get("comments/reply/api/v1/"+pk);
			// 		comments.value[i].replies = res.data.results;
			// 	}catch(err){
			// 		console.log(err)
			// 	}
			// }
			onBeforeUnmount(()=>window.removeEventListener('scroll',CaP))
			return{get_coms,comments,endpoint,paginte}
		}
	};
</script>
<style>
	@import '../assets/com-box.css';
</style>