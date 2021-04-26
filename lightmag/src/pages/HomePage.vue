<template>
	<base-layout>
		<template v-slot:main-content>
			<articles-list></articles-list>
		</template>
	</base-layout>
</template>
<script>
	import {defineComponent} from 'vue';
	import ArticlesList from '@/components/Articles/Lg/ArticlesList.vue';
	export default defineComponent({
		name: "HomePage",
		components:{
			ArticlesList
		}
	});
</script>