<template>
	<h1>{{username}}</h1>
</template>
<script>
	import {computed} from 'vue';
	import {useStore} from 'vuex';
	import {getAPI} from '@/axios.js';
	export default{
		name: "Userprofile",
		props: ['username'],
		setup(props){
			const store = useStore();
			const APIData = computed(()=> store.state.APIData);

			async function get_user(username){
				await getAPI.get("users/api/v1/"+username+'/')
				.then(res => store.state.APIData = res.data)
				.catch(err => console.log(err))
			}
			get_user(props.username)

			return{APIData}
		}
	};
</script>