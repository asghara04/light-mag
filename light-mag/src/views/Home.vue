<template>
	<div id="home">
		<Lheader/>
		<topslider/>
		<div id="page" class="page" v-if="APIData">
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
	import pagination from '@/components/pagination.vue';
	import {ref,computed} from 'vue';
	import {useStore} from 'vuex';
	import {useRoute} from 'vue-router';
	export default{
		name: "Home",
		components:{
			Lheader,
			sidebar,
			topslider,
			pagination
		},
		props:{"num": Number},
		setup(props){
			const page = ref(props.num||1);
			const route = useRoute();
			route.query.page = page.value;
			const store = useStore();
			const APIData = computed(()=>store.state.APIData);

			async function get_arts(){
				await getAPI.get("articles/api/v1/?page="+page.value)
				.then(res => store.state.APIData = res.data)
				.catch(err => console.log(err))
			}
			get_arts();

			return{APIData}
		}
	};
</script>
<style>
	@import '../assets/home-spcial-list.css';
</style>