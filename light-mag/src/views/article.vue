<template>
	<div>
	<topslider></topslider>
	<div id="page" class="page">
		<article class="right page-content" v-if="APIData">
			<span>
				<router-link to="/" name="لایت مگ" rel="لایت مگ">صفحه اصلی</router-link> > <span v-if="APIData.category"><router-link :to="'/categories/'+APIData.category.slug" :rel="APIData.category.name">{{APIData.category.name}}</router-link> > </span><span v-if="APIData.subcat"><span v-if="!APIData.category">{{APIData.subcat.category}} > </span><router-link :to="'/categories/'+APIData.category.slug+'/'+APIData.subcat.slug" :rel="APIData.subcat.name">{{APIData.subcat.name}}</router-link> > </span><router-link :to="'/article/'+APIData.slug">{{APIData.title}}</router-link>
			</span>
			<h1 class="art-h"><router-link :to="'/article/'+APIData.slug">{{APIData.title}}</router-link></h1>
			<div v-if="APIData.image" class="art-pic">
				<img :src="APIData.image.image" :name="APIData.image.name" :alt="APIData.image.alt">
			</div>
			<p class="body pre-formatted">
				{{APIData.body}}
			</p>

			<hr>
				<router-link v-if="APIData.author" :to="{name: 'userprofile', params: {username: APIData.author.username}}">{{APIData.author.name}}</router-link>
			<hr>

			<div id="comments">
				<!-- other comments -->
					<p class="like-h2">کامنت جدید:</p>
					<form class="form" @submit.prevent="commentsub(APIData.id)" method="post">
						<p v-if="errs.message" class="red-text">* {{errs.message}}</p>
						<textarea class="data-field" name="message" placeholder="نظر..." @focus="focused" maxlength="350" v-model="message"></textarea>
						<p v-if="errs.name" class="red-text">* {{errs.name}}</p>
						<input v-if="focus" type="text" name="name" placeholder="نام..." class="data-field" maxlength="30" v-model="name">
						<p v-if="errs.email" class="red-text">* {{errs.email}}</p>
						<input v-if="focus" type="email" name="email" maxlength="30" class="data-field" placeholder="ایمیل..." v-model="email">
						<label v-if="focus" for="personal">ارسال خصوصی:</label>
						<input v-if="focus" type="checkbox" name="personal" v-model="personal">
						<br>
						<button class="sub-button">ثبت</button>
					</form>
			</div>
			<!-- related article like a card slider or like movie websites top -->
		</article>
		<sidebar></sidebar>
	</div>
</div>
</template>
<script>
	import topslider from '@/components/topslider.vue';
	import {getAPI} from '@/axios.js';
	import sidebar from '@/components/sidebar.vue';
	import {ref,computed,watch} from 'vue';
	import {useStore} from 'vuex';
	import {useRoute} from 'vue-router';
	export default{
		name: "Article",
		components:{
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
			const errs = ref({});

			function focused(){
				if(!focus.value){
					focus.value = true;					
				}
			}
			function commentsub(artid){
				if(!name.value||!email.value||!message.value||name.value.length>30||email.value.length>30||message.value.length>350){
					if(!name.value){
						errs.value['name'] = "لطفا نام را وارد کنید.";
					}else if(name.value.length>30){
						errs.value['name'] = "نام وارد شده بیش از حداکثرمقدا است.";
					}
					if(!email.value){
						errs.value['email'] = "لطفا ایمیل را وارد کنید."
					}else if(email.value.length>30){
						errs.value['email'] = "ایمیل وارد شده بیش از حداکثرمقدا است.";
					}
					if(!message.value){
						errs.value['message'] = "لطفا کامنت را وارد کنید.";
					}else if(message.value.length>350){
						errs.value['message'] = "کامنت وارد شده بیش از حداکثرمقدا است.";
					}
				}else{
					getAPI.post("comments/api/v1/"+artid+'/', {
						name: name.value,
						email: email.value,
						message: message.value,
						personal: personal.value
					})
					.then((res)=> {
						if(res.status===201){
							alert("نظرتون با موفقیت ثبت شد.\nپس از تایید نمایش داده میشود.");
							name.value = '';
							email.value = '';
							message.value = '';
							personal.value = false;
						}else{
							console.log(res)
						}
					})
					.catch((err) => {console.log(err);alert("خطایی رخ داد! لطفا دوباره امتحان کنید.")})
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

			return{APIData, focus, name, email, message, personal, focused, commentsub, errs}
		}
	};
</script>
<style>
	@import '../assets/article.css';
	@import '../assets/form.css';
</style>