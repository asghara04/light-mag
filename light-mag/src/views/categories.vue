<template>
	<div v-if="APIData" id="categories">
		<div class="medium-list page">
			<article v-for="(cat, i) in APIData.results" :key="i" :title="cat.name" class="art">
				<router-link :to="'/categories/'+cat.slug">
					<h2>{{cat.name}}</h2>
					<img v-if="cat.image" :src="cat.image.image" :name="cat.image.name" :alt="cat.image.alt">
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
			async function set_current(){
				try{
					const res = await getAPI.get("categories/all/api/v1/count/")
					if(props.page<=parseInt((res.data.count+size.value-1)/size.value)){
						current.value = props.page||1;
					}
					get_cats(current.value);
				}catch(err){
					console.log(err);
				}
			}
			set_current();

			const store = useStore();
			const APIData = computed(() => store.state.APIData);
			async function get_cats(current){
				try{
					const res = await getAPI.get("categories/api/v1/?page="+current);
					store.state.APIData = res.data;
				}catch(err){
					console.log(err)
				}
			}

			watch(
				() => props.page,
				() => {
					set_current();
				}
			)

			return{APIData ,current}
		}
	};
</script>
<style>
	@import '../assets/medium-list.css';
</style>