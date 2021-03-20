<template>
	<div class="pagination-com">
		<router-link v-if="current>2" class="link-like" :to="{query: {page: 1}}" rel="لایت مگ، صفحه 1">1</router-link>
		<p v-if="current>3">...</p>
		<router-link v-if="current>1" class="link-like" :to="{query: {page: (current-1)}}" :rel="'لایت مگ، صفحه '+(current-1)">{{(current-1)}}</router-link>

		<p class="page-active">{{current}}</p>

		<router-link v-if="current<parseInt((all+size-1)/size)" class="link-like" :to="{query: {page: (current+1)}}" :rel="'لایت مگ، صفحه '+(current+1)">{{(current+1)}}</router-link>
		<p v-if="current+2<parseInt((all+size-1)/size)">...</p>
		<router-link v-if="current+1<parseInt((all+size-1)/size)" class="link-like" :to="{query: {page: parseInt((all+size-1)/size)}}" :rel="'لایت مگ، صفحه '+parseInt((all+size-1)/size)">{{parseInt((all+size-1)/size)}}</router-link>
	</div>
</template>
<script>
	export default{
		name: "pagination",
		props:{
			current: Number,
			all: Number,
			size: Number
		},
	};
</script>
<style>
	@import '../assets/pagination.css';
</style>