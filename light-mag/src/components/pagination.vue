<template>
	<div class="pagination-com">
		<a v-if="current>2" :href="path+'?page='+(current-1)" rel="مجله نور">1</a>
		<p v-if="current>3">...</p>
		<a v-if="current>1" :href="path+'?page='+(current-1)" rel="مجله نور">{{current-1}}</a>

		<p class="router-link-exact-active">{{current}}</p>

		<a v-if="current<parseInt((all+size-1)/size)" :href="path+'?page='+(current+1)" rel="مجله نور">{{current+1}}</a>
		<p v-if="current+2<parseInt((all+size-1)/size)">...</p>
		<a v-if="current+1<parseInt((all+size-1)/size)" :href="path+'?page='+parseInt((all+size-1)/size)" rel="مجله نور">{{parseInt((all+size-1)/size)}}</a>
	</div>
</template>
<script>
	export default{
		name: "pagination",
		props:{
			path: String,
			all: Number,
			size: Number
		},
		data(){
			return{
				current: this.$route.query.page||1
			}
		},
	};
</script>
<style>
	@import '../assets/pagination.css';
</style>