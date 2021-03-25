<template>
	<topslider></topslider>
	<div id="page" class="page">
		<div class="right">
			<article class="ed-bk" v-if="APIData">
				<div><router-link to="/" name="لایت مگ" rel="لایت مگ" class="link-like">صفحه اصلی</router-link> >  <span v-if="APIData.category"><router-link :to="{name: 'category',params:{catslug:APIData.category.slug}}">{{APIData.category.name}}</router-link> > </span><span v-if="APIData.subcat"><span v-if="!APIData.category"><span>{{APIData.subcat.category}}</span> > <span>{{APIData.subcat.name}}</span></span><span v-else><router-link :to="{name:'subcat',params:{catslug:APIData.category.slug,subcatname:APIData.subcat.slug}}">{{APIData.subcat.name}}</router-link></span> > </span><router-link :to="{name:'article',params:{artslug:APIData.slug}}">{{APIData.title}}</router-link></div>
				<h1 class="art-h"><router-link :to="'/article/'+APIData.slug">{{APIData.title}}</router-link></h1>
				<div v-if="APIData.image" class="art-pic">
					<img :src="APIData.image.image" :name="APIData.image.name" :alt="APIData.image.alt">
				</div>
				<div v-html="APIData.body"></div>
				<div class="art-detail">
					<div v-if="APIData.category">
						<p><span class="blue-text">دسته: </span><router-link :to="{name:'category',params:{catslug: APIData.category.slug}}" class="link-like">{{APIData.category.name}}</router-link></p>
						<p v-if="APIData.subcat"><span class="blue-text">زیردسته: </span><router-link :to="{name:'subcat',params:{catslug:APIData.category.slug,subcatname:APIData.subcat.slug}}" class="link-like">{{APIData.subcat.name}}</router-link></p>
					</div>
					<div v-if="!APIData.category&&APIData.subcat">
						<p><span class="blue-text">دسته: </span>{{APIData.subcat.category}}</p>
						<p><span class="blue-text">زیردسته: </span>{{APIData.subcat.name}}</p>
					</div>
					<p><span class="blue-text">تاریخ انتشار: </span>{{APIData.jpub_date}}</p>
					<p><span class="blue-text">نویسنده: </span><router-link class="icon-t link-like" :to="{name:'userprofile',params:{username:APIData.author.username}}"><img :src="APIData.author.prof_picture.image" :alt="APIData.author.prof_picture.alt" :name="APIData.author.prof_picture.name">{{APIData.author.name}}</router-link></p>
				</div>
				<!-- related article like a card slider or like movie websites top -->
			</article>
			<div class="ed-bk comments">
				<comments v-if="APIData.coms" :key="artslug" :id="APIData.id"/>
				<p v-else class="cen blue-text">هنوز کامنتی ثبت نشده، میتونی اولی باشی :)</p>
				<p class="like-h2">کامنت جدید:</p>
				<form class="form" @submit.prevent="commentsub(APIData.id)" method="post">
					<label v-if="focus" for="message">نظر: </label>
					<span v-if="errs.message!=false"><p v-for="(err,i) in errs.message" :key="i" class="red-text">* {{err}}</p></span>
					<textarea class="data-field" name="message" placeholder="نظر..." @focus="focused" maxlength="350" v-model="message"></textarea>
					<label v-if="focus" for="name">نام: </label>
					<span v-if="errs.name!=false"><p v-for="(err,i) in errs.name" :key="i" class="red-text">* {{err}}</p></span>
					<input v-if="focus" type="text" name="name" placeholder="نام..." class="data-field" maxlength="30" v-model="name">
					<label v-if="focus" for="email">ایمیل: </label>
					<span v-if="errs.email!=false"><p v-for="(err,i) in errs.email" :key="i" class="red-text">* {{err}}</p></span>
					<input v-if="focus" type="email" name="email" maxlength="30" class="data-field" placeholder="ایمیل..." v-model="email">
					<label v-if="focus" for="personal">ارسال خصوصی:</label>
					<span v-if="errs.personal!=false"><p v-for="(err,i) in errs.personal" :key="i" class="red-text">* {{err}}</p></span>
					<input v-if="focus" type="checkbox" class="data-field" name="personal" v-model="personal">
					<button v-if="focus" class="sub-button">ثبت</button>
				</form>
			</div>
			<div class="ed-bk tag-island" v-if="APIData.tags!=false">
				<router-link v-for="(tag,i) in APIData.tags" :key="i" :to="{name: 'tag-page',params:{tagslug: tag.slug}}" class="tag-like">{{tag.name}}</router-link>
			</div>
		</div>
		<sidebar/>
	</div>
</template>
<script>
	import topslider from '@/components/topslider.vue';
	import {getAPI} from '@/axios.js';
	import sidebar from '@/components/sidebar.vue';
	import {ref,computed,watch} from 'vue';
	import {useStore} from 'vuex';
	import {useRoute} from 'vue-router';
	import comments from '@/components/comments.vue';
	export default{
		name: "Article",
		components:{
			sidebar,
			topslider,
			comments
		},
		props:["artslug"],
		setup(props){
			const store = useStore();
			const APIData = computed(()=>store.state.APIData);
			const route = useRoute();

			async function get_art(slug){
				try{
					const res = await getAPI.get('articles/api/v1/'+slug)
					store.state.APIData = res.data;
				}catch(err){
					console.log(err)
				}
			}
			get_art(props.artslug)

			const focus = ref(false);
			const name = ref(null);
			const email = ref(null);
			const message = ref(null);
			const personal = ref(false);
			const errs = ref({'name':[],'email':[],'message':[],'personal':[]});

			function focused(){
				if(!focus.value){
					focus.value = true;					
				}
			}
			async function commentsub(artid){
				errs.value.name = [];
				errs.value.email = [];
				errs.value.message = [];
				errs.value.personal = [];
				focus.value = true;
				const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
				if(name.value&&name.value.length<=30&&email.value&&email.value.length<=30&&re.test(email.value)&&message.value&&message.value.length<=350){
					try{
						const res = await getAPI.post("comments/api/v1/"+artid+'/',{
							article: artid,
							name: name.value,
							email: email.value,
							message: message.value,
							personal: personal.value
						})
						if(res.status===201){
							alert(res.data.message)
							name.value = null;
							email.value = null;
							message.value = null;
							personal.value = null;
							focus.value = false;
						}else{
							console.log(res)
						}
					}catch(err){
						if(err.response.status===400){
							if(err.response.data.name){
								for(var i=0;i<err.response.data.name.length;i++){
									errs.value.name.push(err.response.data.name[i])
								}
							}
							if(err.response.data.email){
								for(var x=0;x<err.response.data.email.length;x++){
									errs.value.email.push(err.response.data.email[x])
								}
							}
							if(err.response.data.message){
								for(var y=0;y<err.response.data.message.length;y++){
									errs.value.message.push(err.response.data.message[y])
								}
							}
							if(err.response.data.personal){
								for(var z=0;z<err.response.data.personal.length;z++){
									errs.value.personal.push(err.response.data.personal[z])
								}
							}
						}else{
							alert('خطایی رخ داد، لطفا دوباره امتحان کنید.')
						}
					}
				}else{
					if(!message.value){
						errs.value.message.push('لطفا کامنتتون رو وارد کنید.');
					}else if(message.value.length>350){
						errs.value.message.push('حداکثر طول کامنت 350 است، اکنون '+message.value.length+' وارد شده است.');
					}
					if(!name.value){
						errs.value.name.push('لطفا نام تون رو وارد کنید.');
					}else if(name.value.length>30){
						errs.value.name.push('حداکثر طول نام 30 است، اکنون '+name.value.length+' وارد شده است.');
					}
					if(!email.value){
						errs.value.email.push('لطفا ایمیل تون رو وارد کنید.');
					}else if(email.value.length>30){
						errs.value.email.push('حداکثر طول ایمیل 30 است، اکنون '+email.value.length+' وارد شده است.');
					}else if(!re.test(email.value)){
						errs.value.email.push('لطفا ایمیل معتبری وارد کنید.');
					}
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