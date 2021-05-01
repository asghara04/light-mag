<template>
	
</template>
<script>
	import {defineComopnent} from 'vue';

	export default defineComopnent({
		name: "ArticleList",
		props:{
			type:{
				type: String,
				required: false,
				default: "all"
			},
			author:{
				type: String,
				required: false
			},
			category:{
				type: String,
				required: false
			},
			subcat:{
				type: String,
				required: false
			}
		}
	});
</script>