<template>
	<div v-if="APIData" id="categories">
		<Lheader/>
		<div class="medium-list page">
			<article v-for="cat in APIData.results" :key="cat.id" class="art">
				<h2>{{cat.name}}</h2>
				<img :src="cat.image.image" :name="cat.image.name" :alt="cat.image.alt">
			</article>
		</div>
		<pagination path="/categories" :all="APIData.count" :size="10"/>
	</div>
</template>

<script>
	import Lheader from '@/components/Lheader.vue';
	import {mapState} from 'vuex';
	import {getAPI} from '@/axios.js';
	import pagination from '@/components/pagination.vue';

	export default{
		name: "categories",
		components:{
			Lheader,
			pagination
		},
		computed: mapState(["APIData"]),
		props:{"num": Number},
		data(){
			return{
				page: this.num||parseInt("1")
			}
		},
		created(){
			this.$route.query.page = this.page
			getAPI.get("categories/api/v1/?page="+this.page)
			.then(res => {
				this.$store.state.APIData = res.data
			})
			.catch(err => {
				console.log(err)
			})
		}
	};
</script>

<style>
	@import '../assets/medium-list.css';
</style>