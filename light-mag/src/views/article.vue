<template>
	<div>
	<Lheader></Lheader>
	<topslider></topslider>
	<div id="page" class="page">
		<article class="right page-content" v-if="APIData">
			<span>
				<router-link to="/" name="مجله نور">صفحه اصلی</router-link> > <span v-if="APIData.category"><router-link :to="'/categories/'+APIData.category.slug" :name="APIData.category">{{APIData.category.name}}</router-link> > </span><span v-if="APIData.subcat"><span v-if="!APIData.category">{{APIData.subcat.category}} > </span><router-link :to="'/categories/'+APIData.category.slug+'/'+APIData.subcat.slug">{{APIData.subcat.name}}</router-link> > </span><router-link :to="'/article/'+APIData.slug">{{APIData.title}}</router-link>
			</span>
			<h1 class="art-h"><router-link :to="'/article/'+APIData.slug">{{APIData.title}}</router-link></h1>
			<div v-if="APIData.image" class="art-pic">
				<img :src="APIData.image.image" :name="APIData.image.name" :alt="APIData.image.alt">
			</div>
			<p class="body">
				{{APIData.body}}
			</p>

			<div id="comments">
				<!-- other comments -->
					<h3>کامنت جدید:</h3>
					<form @submit.prevent="commentsub(APIData.id)">
						<textarea class="data-field" name="message" placeholder="نظر..." required="" @focus="focused" maxlength="250" v-model="message"></textarea>
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
		<sidebar></sidebar>
	</div>
</div>
</template>
<script>
	import Lheader from '@/components/Lheader.vue';
	import topslider from '@/components/topslider.vue';
	import {getAPI} from '@/axios.js';
	import sidebar from '@/components/sidebar.vue';
	import {ref,computed,watch} from 'vue';
	import {useStore} from 'vuex';
	import {useRoute} from 'vue-router';
	export default{
		name: "Article",
		components:{
			Lheader,
			sidebar,
			topslider
		},
		props:["artslug"],
		setup(props){
			const store = useStore();
			const APIData = computed(()=>store.state.APIData);
			const route = useRoute();

			function get_art(slug){
				getAPI.get("articles/api/v1/"+slug)
				.then(res => store.state.APIData = res.data)
				.catch(err => console.log(err))
			}
			get_art(props.artslug)

			const focus = ref(false);
			const name = ref(null);
			const email = ref(null);
			const message = ref(null);
			const personal = ref(false);

			function focused(){
				if(!focus.value){
					focus.value = true;					
				}
			}
			function commentsub(artid){
				if(name.value&&email.value&&message.value){
					getAPI.post("comments/api/v1/"+artid+'/', {
						name: name.value,
						email: email.value,
						message: message.value,
						personal: personal.value
					})
					.then(() => {
						alert("نظرتون با موفقیت ثبت شد.\nپس از تایید نمایش داده میشود.");
						name.value = '';
						email.value = '';
						message.value = '';
						personal.value = false;
					})
					.catch(err => {console.log(err);alert("خطایی رخ داد! لطفا دوباره امتحان کنید یا به ادمین اطلاع دهید.")})
				}else{
					alert("لطفا فیلد های مورد نظر را پر کنید.")
				}
			}

			watch(
				() => route.params.artslug,
				newSlug => {
					if(route.name==="article"){
						get_art(newSlug)
					}
				}
			)

			return{APIData, focus, name, email, message, personal, focused, commentsub}
		}
	};
</script>
<style>
	@import '../assets/article.css';
	@import '../assets/form.css';
</style>