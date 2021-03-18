<template>
	<p v-if="comments==false" class="cen link-like" @click.prevent="get_coms(endpoint)">نمایش کامنت ها</p>
	<div v-else class="com-box" ref="paginate">
		<div v-for="(com,i) in comments" :key="i" class="com">
			<h4>{{com.name}}</h4>
			<time class="s-size">{{com.jdate}}</time>
			<p class="message">{{com.message}}</p>
			<Addrep :key="id" :id="com.id"/>
			<div v-if="com.reps">
				<p v-if="com.replies.reps==false" @click.prevent="get_reps(i)" class="link-like">{{com.reps}} پاسخ، نمایش</p>
				<div v-else v-for="(rep,i) in com.replies.reps" :key="i" class="sub">
					<h4>{{rep.name}}</h4>
					<time class="s-size">{{rep.jdate}}</time>
					<p class="message">{{rep.message}}</p>
				</div>
				<p v-if="com.replies.reps!=false&&com.replies.endpoint" class="link-like" @click.prevent="get_reps(i)">نمایش بیشتر...</p>
			</div>
		</div>
	</div>
</template>
<script>
	import {ref} from 'vue';
	import {getAPI} from'@/axios.js';
	import {onMounted} from 'vue';
	import {useRoute} from 'vue-router';
	import Addrep from '@/components/add-rep.vue';
	export default{
		name: "Comments",
		props:['id'],
		setup(props){
			const comments = ref([]);
			const endpoint = ref("comments/api/v1/"+props.id);
			let more = false;
			let bottom = false;
			const paginate = ref(null);
			async function get_coms(end){
				if(endpoint.value&&end){
					try{
						const res = await getAPI.get(end);
						for(var i=0;i<res.data.results.length;i++){
							res.data.results[i]['replies'] = {endpoint:"comments/reply/api/v1/"+res.data.results[i].id,reps:[]};
							comments.value.push(res.data.results[i]);
						}
						endpoint.value = res.data.next;
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
				if(paginate.value){
					bottom = (window.scrollY+window.innerHeight)>=(paginate.value.offsetTop+paginate.value.offsetHeight-20)&&(window.scrollY+window.innerHeight)<(paginate.value.offsetTop+paginate.value.offsetHeight);
					if(bottom&&more&&end&&route.name==="article"){
						more = false;
						get_coms(end);
					}
				}
			}
			async function get_reps(i){
				try{
					const res = await getAPI.get(comments.value[i].replies.endpoint)
					for(var x=0;x<res.data.results.length;x++){
						comments.value[i].replies.reps.push(res.data.results[x]);
					}
					comments.value[i].replies.endpoint = res.data.next;
				}catch(err){
					console.log(err)
				}
			}
			onMounted(()=>window.removeEventListener('scroll',CaP))
			return{get_coms,comments,endpoint,paginate,get_reps}
		},
		components:{Addrep}
	};
</script>
<style>
	@import '../assets/com-box.css';
</style>