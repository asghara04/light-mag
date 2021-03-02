<template>
	<div v-if="APIData" id="categories">
		<Lheader/>
		<div class="medium-list page">
			<article v-for="cat in APIData.results" :key="cat.id" class="art">
				<router-link :to="'/categories/'+cat.slug">
					<h2>{{cat.name}}</h2>
					<img :src="cat.image.image" :name="cat.image.name" :alt="cat.image.alt">
				</router-link>
			</article>
		</div>
		<pagination path="/categories" :all="APIData.count" :size="10"/>
	</div>
</template>
<script>
	import Lheader from '@/components/Lheader.vue';
	import {getAPI} from '@/axios.js';
	import pagination from '@/components/pagination.vue';
	import {ref,computed} from 'vue';
	import {useRoute} from 'vue-router';
	import {useStore} from 'vuex';

	export default{
		name: "categories",
		components:{
			Lheader,
			pagination
		},
		props:{"num": Number},
		setup(props){
			const page = ref(props.num||1);
			const route = useRoute();
			route.query.param = page.value;
			const store = useStore();
			const APIData = computed(()=>store.state.APIData)

			function get_cats(){
				getAPI.get("categories/api/v1/?page="+page.value)
				.then(res => store.state.APIData = res.data)
				.catch(err => console.log(err))
			}
			get_cats();

			return{APIData}
		}
	};
</script>
<style>
	@import '../assets/medium-list.css';
</style>