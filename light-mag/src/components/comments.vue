<template>
	<p class="link-like">نمایش کامنت ها</p>
</template>
<script>
	import {ref} from 'vue';
	import {getAPI} from'@/axios.js';
	export default{
		name: "Comments",
		props: ['slug'],
		setup(props){
			const comments = ref(null);

			async function get_coms(slug){
				const res = await getAPI.get("comments/")
			}
		}
	};
</script>
<style>
	
</style>