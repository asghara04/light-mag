<template>

</template>
<script>
	import {defineComopnent} from 'vue';

	// an computed method should be on "module" property
	// computed data and store map getters
	// ---- pagination ----

	export default defineComopnent({
		name: "ArticleList",
		props:{
			module:{
				type: String,
				required: true,
				default: "home"
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
		},
		components:{

		},
		setup(){

		}
	});
</script>