<template>
	<base-layout>
		<template v-slot:main-content>
			<popular-articles></popular-articles>
			<articles-list></articles-list>
		</template>
	</base-layout>
</template>
<script>
	import {defineComponent} from 'vue';
	import ArticlesList from '@/components/Articles/Lg/ArticlesList.vue';
	import PopularArticles from '@/components/Dynamic/PopularArticles.vue';
	export default defineComponent({
		name: "HomePage",
		components:{
			PopularArticles,
			ArticlesList
		}
	});
</script>