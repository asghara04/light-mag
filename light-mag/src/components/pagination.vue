<template>
	<div class="pagination-com">
		<router-link v-if="current>2" target="_blank" :to="{query: {page: 1}}" rel="مجله نور صفحه 1">1</router-link>
		<p v-if="current>3">...</p>
		<router-link v-if="current>1" target="_blank" :to="{query: {page: current-1}}" :rel="'مجله نور صفحه '+(current-1)">{{current-1}}</router-link>

		<p class="page-active">{{current}}</p>

		<router-link target="_blank" v-if="current<parseInt((all+size-1)/size)" :to="{query: {page: current+1}}" :rel="'مجله نور صفحه '+(current+1)">{{current+1}}</router-link>
		<p v-if="current+2<parseInt((all+size-1)/size)">...</p>
		<router-link v-if="current+1<parseInt((all+size-1)/size)" :to="{query: {page: parseInt((all+size-1)/size)}}" :rel="'مجله نور صفحه '+parseInt((all+size-1)/size)" target="_blank">{{parseInt((all+size-1)/size)}}</router-link>
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