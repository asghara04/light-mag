<template>
	<div id="home">
		<topslider/>
		<div id="page" class="page" v-if="APIData">
			<div class="right">
				<div class="spcial-list">
					<article v-for="(article, i) in APIData.results" v-bind:key="i" class="article" :class="{'yay-sider':article.image}">
						<router-link v-if="article.image" class="sider" :rel="article.title" :to="'/article/'+article.slug"><img :src="article.image.image" :alt="article.image.alt" :name="article.image.name"></router-link>
						<div class="high-content">
							<h2><router-link :rel="article.title" :name='article.title' :to="'/article/'+article.slug">{{article.title}}</router-link></h2>
							<hr>
							<p class="pre-formatted">{{article.description}} - <router-link :to="'/article/'+article.slug">ادامه...</router-link></p>
							<div class="page-halfer"><p class="half text-icon"><img src="../assets/imgs/clock.svg">{{article.jpub_date}}</p><p class="half text-icon"><img class="mar" src="../assets/imgs/coms.svg">{{article.coms}}</p></div><router-link v-if="article.author" :to="{name: 'userprofile',params:{username: article.author.username}}" class="half icon-t"><img v-if="article.author.prof_picture" :src="article.author.prof_picture.image" :alt="article.author.prof_picture.alt"><img v-else src="../assets/imgs/user.svg">{{article.author.name}}</router-link>
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
	import topslider from '@/components/topslider.vue';
	import sidebar from '@/components/sidebar.vue';
	import pagination from '@/components/pagination.vue';
	import  {useRoute} from 'vue-router';
	export default{
		name: 'Home',
		props: ["page"],
		setup(props){
			const current = ref(1);
			const size = ref(10);

			async function set_current(){
				try{
					const res = await getAPI.get("articles/api/v1/count/")
					if((props.page)<=parseInt((res.data.count+size.value-1)/size.value)){
						current.value = props.page||1;
					}
					get_arts(current.value);
				}catch(err){
					console.log(err);
				}
			}
			set_current();

			document.querySelector("head title").textContent = "لایت مگ - صفحه اصلی";
			document.querySelector("head meta[name='description']").setAttribute("content","صحه اصلی لایت مگ")

			const store = useStore();
			const APIData = computed(() => store.state.APIData);
			async function get_arts(current){
				try{
					const res = await getAPI.get("articles/api/v1/?page="+current);
					store.state.APIData = res.data;
				}catch(err){
					console.log(err);
				}
			}
			const route = useRoute();
			watch(
				() => props.page,
				() => {
					if(route.name==="Home"){
						set_current();
					}
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
	@import '../assets/page-halfer.css';
</style>