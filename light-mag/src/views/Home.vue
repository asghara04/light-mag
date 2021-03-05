<template>
	<div id="home">
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
				<pagination :key="current" :current="current" :all="APIData.count" :size="10"/>
			</div>
			<sidebar/>
		</div>
	</div>
</template>
<script>
	import {getAPI} from '@/axios.js';
	import {ref, watch, computed} from 'vue';
	import {useStore} from 'vuex';
	import {useRoute} from 'vue-router';
	import topslider from '@/components/topslider.vue';
	import sidebar from '@/components/sidebar.vue';
	import pagination from '@/components/pagination.vue';
	export default{
		name: 'Home',
		props: ["page"],
		setup(props){
			const current = ref(1);
			const size = ref(10);

			function set_current(){
				getAPI.get('articles/api/v1/count/')
				.then(res=> {
					if((props.page)<=parseInt((res.data.count+size.value-1)/size.value)){
						current.value = props.page||1;
					}
				})
				.catch(err => console.log(err))
			}
			set_current();

			const store = useStore();
			const APIData = computed(() => store.state.APIData);

			function get_arts(current){
				getAPI.get("articles/api/v1/?page="+current)
				.then(res => store.state.APIData = res.data)
				.catch(err => console.log(err))
			}
			get_arts(current.value);

			const route = useRoute();
			watch(
				() => route.query.page,
				newPage => {
					set_current();
					get_arts(newPage);
				}
			)

			return{APIData ,current}
		},
		components: {
			topslider,
			sidebar,
			pagination
		}
	};
</script>
<style>
	@import '../assets/home-spcial-list.css';
</style>