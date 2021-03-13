<template>
	<div v-if="APIData.username===this.$route.params.username" id="page" class="page">
		<div class="right page-content">
			<span>
				<router-link to="/" rel="مجله نور">صفحه اصلی</router-link> > <span>کاربران</span> > <router-link :to="{name: 'userprofile', params:{username: APIData.username}}">{{APIData.name}}</router-link>
			</span>
			<div class="third-part">
				<div class="third-one dashed">
					<img :src="APIData.prof_picture.image" :alt="APIData.prof_picture.alt" :name="APIData.prof_picture.name">
					<p><span class="blue-text">نام: </span>{{APIData.name}}</p>
					<p v-if="APIData.pubmail"><span class="blue-text">ایمیل: </span><a class="link-like" :href="'mailto:'+APIData.pubmail" target="_blank" :rel="'ایمیل '+APIData.name">{{APIData.pubmail}}</a></p>
				</div>
				<div class="third-two dashed">
					<div class="page-halfer">
						<p v-if="APIData.birthday" class="half"><span class="blue-text">تاریخ تولد: </span>{{APIData.birthday}}</p>
						<p v-if="APIData.favorite_cat" class="half"><span class="blue-text">دسته موردعلاقه: </span><router-link :to="{name: 'category', params: {catslug: APIData.favorite_cat.slug}}" :rel="APIData.favorite_cat.name" class="link-like">{{APIData.favorite_cat.name}}</router-link></p>					
					</div>
					<div class="page">
						<div v-if="APIData.bio">
							<span class="blue-text">بایوگرافی: </span><p class="pre-formatted">{{APIData.bio}}</p>
						</div>
						<div v-if="APIData.about">
							<span class="blue-text">درباره: </span><p class="pre-formatted">{{APIData.about}}</p>
						</div>
					</div>
				</div>
			</div>
			<div class="dashed" align="center">
				<p class="like-h2">ارتباط</p>
				<div class="small-medium-list">
					<a class="item" target="_blank" :href="APIData.instagram_link"><img src="../assets/imgs/instagram.png" alt="اینستاگرام"></a>
					<a :href="APIData.facebook_link" class="item" target="_blank"><img src="../assets/imgs/facebook.png"></a>
					<a :href="APIData.github_link" class="item" target="_blank"><img src="../assets/imgs/github.png" alt="گیت هاب"></a>
					<a :href="'mailto:'+APIData.pubmail" class="item" target="_blank"><img src="../assets/imgs/email.png" alt="ایمیل"></a>
				</div>
			</div>
		</div>
		<sidebar/>
	</div>
	<topslider/>
</template>
<script>
	import {computed, watch} from 'vue';
	import {useStore} from 'vuex';
	import {getAPI} from '@/axios.js';
	import {useRoute} from 'vue-router';
	import sidebar from '@/components/sidebar.vue';
	import topslider from '@/components/topslider.vue';
	export default{
		name: "Userprofile",
		props: ['username'],
		setup(props){
			const store = useStore();
			const APIData = computed(()=> store.state.APIData);

			async function get_user(username){
				await getAPI.get("users/api/v1/"+username+'/')
				.then(res => store.state.APIData = res.data)
				.catch(err => console.log(err))
			}
			get_user(props.username);

			const route = useRoute();
			watch(
				()=> route.params.username,
				newUsername=>{
					get_user(newUsername);
				}
			)

			return{APIData}
		},
		components:{
			sidebar,
			topslider
		}
	};
</script>
<style>
	@import '../assets/third-part.css';
	@import '../assets/dashed.css';
	@import '../assets/page-halfer.css';
	@import '../assets/small-medium-list.css';
</style>