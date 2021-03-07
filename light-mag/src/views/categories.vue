<template>
	<div v-if="APIData" id="categories">
		<div class="medium-list page">
			<article v-for="cat in APIData.results" :key="cat.id" :title="cat.name" class="art">
				<router-link :to="'/categories/'+cat.slug">
					<h2>{{cat.name}}</h2>
					<img :src="cat.image.image" :name="cat.image.name" :alt="cat.image.alt">
				</router-link>
			</article>
		</div>
		<pagination :key="current" :current="current" :all="APIData.count" :size="10"/>
	</div>
</template>
<script>
	import {getAPI} from '@/axios.js';
	import pagination from '@/components/pagination.vue';
	import {ref,computed,watch} from 'vue';
	import {useRoute} from 'vue-router';
	import {useStore} from 'vuex';
	export default{
		name: "categories",
		components:{
			pagination
		},
		props:{"page": Number},
		setup(props){
			const current = ref(1);
			const size = ref(10);

			function set_current(){
				getAPI.get('categories/all/api/v1/count/')
				.then(res=> {
					if(props.page<=parseInt((res.data.count+size.value-1)/size.value)){
						current.value = props.page||1;
					}
				})
				.catch(err => console.log(err))
			}
			set_current();

			const store = useStore();
			const APIData = computed(() => store.state.APIData);

			function get_cats(current){
				getAPI.get("categories/api/v1/?page="+current)
				.then(res => store.state.APIData = res.data)
				.catch(err => console.log(err))
			}
			get_cats(current.value);


			const route = useRoute();
			watch(
				() => route.query.page,
				() => {
					set_current();
					get_cats(current.value);
				}
			)

			return{APIData ,current}
		}
	};
</script>
<style>
	@import '../assets/medium-list.css';
</style>