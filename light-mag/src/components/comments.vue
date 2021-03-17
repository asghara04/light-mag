<template>
	<p v-if="!comments" class="cen link-like" @click.prevent="get_coms()">نمایش کامنت ها</p>
	<div v-else class="com-box">
		<div v-for="(com,i) in comments" :key="i" class="com">
			<h4>{{com.name}}</h4>
			<time class="s-size">{{com.jdate}}</time>
			<p class="message">{{com.message}}</p>
			<!-- <p class="red-text">پاسخ دادن</p>    component    -->
			<div v-if="com.reps">
				<p v-if="!replies" @click.prevent="get_reps(com.id,i)" class=" cen link-like">{{com.reps}} پاسخ، نمایش</p>
				<div v-else>
					
				</div>
			</div>
		</div>
	</div>
</template>
<script>
	import {ref} from 'vue';
	import {getAPI} from'@/axios.js';
	export default{
		name: "Comments",
		props:['id'],
		setup(props){
			const comments = ref(null);
			async function get_coms(){
				try{
					const res = await getAPI.get("comments/api/v1/"+props.id);
					comments.value = res.data.results;
					for(var i=0;i<comments.value.length;i++){
						comments.value[i]['replies'] = [];// sould be a {}
					}
				}catch(err){
					console.log(err)
				}
			}
			async function get_reps(pk,i){
				try{
					const res = await getAPI.get("comments/reply/api/v1/"+pk);
					comments.value[i].replies = res.data.results;
				}catch(err){
					console.log(err)
				}
			}
			return{get_coms,comments}
		}
	};
</script>
<style>
	@import '../assets/com-box.css';
</style>