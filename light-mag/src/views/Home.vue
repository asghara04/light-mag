<template>
	<div id="home">
		<Lheader/>
		<topslider/>
		<div id="page" class="page">
			<div class="right">
				<div class="spcial-list">
					<article v-for="article in APIData.results" v-bind:key="article.id" class="article">
						<router-link v-if="article.image" :name="article.title" :to="'/article/'+article.slug"><img :src="article.image.image" :alt="article.image.alt" :name="article.image.name"></router-link>
						<div>
							<h2><router-link :name='article.title' :to="'/article/'+article.slug">{{article.title}}</router-link></h2>
							<hr>
							<p>{{article.description}} - <router-link :to="'/article/'+article.slug">ادامه...</router-link></p>
						</div>
					</article>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>iiiiiiiiiiiiiiiooooooooooooooooooooooooooooooooohi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
					<h1>hi</h1>
				</div>
				<pagination path="/" :all="APIData.count" :size="10"/>
			</div>
			<sidebar/>
		</div>
	</div>
</template>

<script>
	import Lheader from '@/components/Lheader.vue';
	import sidebar from '@/components/sidebar.vue';
	import topslider from '@/components/topslider.vue';
	import {getAPI} from '@/axios.js';
	import {mapState} from 'vuex';
	import pagination from '@/components/pagination.vue';

	export default{
		name: "Home",
		components:{
			Lheader,
			sidebar,
			topslider,
			pagination
		},
		props:{"num": Number},
		data(){
			return{
				page: this.num||parseInt("1"),
			}
		},
		computed: mapState(['APIData']),
		created(){
			this.$route.query.page = this.page;
			getAPI.get("articles/api/v1/?page="+this.page)
			.then(response => {
				this.$store.state.APIData = response.data;
			})
			.catch(err => {
				console.log(err);
			})
		},
	};
</script>

<style>
	@import '../assets/home-spcial-list.css';
</style>