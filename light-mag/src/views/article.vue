<template>
	<Lheader/>
	<topslider/>
	<div id="page" class="page">
		<article class="right page-content" v-if="APIData">
			<p>
				<router-link to="/" name="مجله نور">صفحه اصلی</router-link> > <span v-if="APIData.category"><router-link :to="'/categories/'+APIData.category.slug" :name="APIData.category">{{APIData.category.name}}</router-link> > </span><span v-if="APIData.subcat"><span v-if="!APIData.category">{{APIData.subcat.category}} > </span><router-link :to="'/'">{{APIData.subcat.name}}</router-link> > </span><router-link :to="'/article/'+APIData.slug">{{APIData.title}}</router-link>
			</p>
			<h1 class="art-h"><router-link :to="'/article/'+APIData.slug">{{APIData.title}}</router-link></h1>
			<div v-if="APIData.image" class="art-pic">
				<img :src="APIData.image.image" :name="APIData.image.name" :alt="APIData.image.alt">
			</div>
			<p class="body">
				{{APIData.body}}
			</p>

			<div id="comments">
				<!-- other comments -->
					<form @submit.prevent="commentsub(APIData.id)">
						<label for="message">نظر:</label>
						<textarea class="data-field" name="message" required="" @focus="focused" maxlength="250" v-model="message"></textarea>
						<input v-if="focus" type="text" name="name" placeholder="نام..." required="" class="data-field" maxlength="30" v-model="name">
						<input v-if="focus" type="email" name="email" required="" maxlength="30" class="data-field" placeholder="ایمیل..." v-model="email">
						<label v-if="focus" for="personal">ارسال خصوصی:</label>
						<input v-if="focus" type="checkbox" name="personal" v-model="personal">
						<br>
						<button name="submit">ثبت</button>
					</form>
			</div>
			<!-- related article like a card slider or like movie websites top -->
		</article>
		<sidebar/>
	</div>
</template>

<script>
	import Lheader from '@/components/Lheader.vue';
	import topslider from '@/components/topslider.vue';
	import {getAPI} from '@/axios.js';
	import {mapState} from 'vuex';
	import sidebar from '@/components/sidebar.vue';

	export default{
		name: "article",
		components:{
			Lheader,
			sidebar,
			topslider
		},
		props:["address"],
		computed: mapState(["APIData"]),
		created(){
			getAPI.get("articles/api/v1/"+this.address)
			.then(res => {
				this.$store.state.APIData = res.data
			})
			.catch(err => {
				console.log(err)
			})
		},
		data(){
			return{
				focus: false,
				name: null,
				email: null,
				message: null,
				personal: false
			}
		},
		methods:{
			focused(){
				this.focus = true
			},
			commentsub(apiid){
				getAPI.post("comments/api/v1/"+apiid+'/', {
					name: this.name,
					email: this.email,
					message: this.message,
					personal: this.personal
				})
				.then(res => {
					console.log(res.data.message)
					alert("نظر شما با موفقیت ثبت شد.")
				})
				.catch(err => {
					alert("مشکلی رخ داد! صفحه را ریلود کنید ولی کامنتتان ثبت نشده است.")
					console.log(err)
				})
			}
		}
	};
</script>

<style>
	@import '../assets/article.css';
	@import '../assets/form.css';
</style>