<template>
	<div id="page" class="page">
		<div class="right">
			<div class="search-div ed-bk">
				<h2 class="cen">جستوجو در لایت مگ</h2>
				<form class="q-form">
					<input type="search" name="q" class="q-field" maxlength="100" autofocus="" v-model="q">
					<button class="q-button"><img src="../assets/imgs/search.svg"></button>
				</form>
			</div>
			<div class="part" v-if="q">
				<tabbednav v-if="q" :key="q" ths="نوشته ها|دسته ها" :ps="'articles/api/v1/?q='+q+'|categories/api/v1/?q='+q" ls="/article/|/categories/"/>
			</div>
		</div>
		<sidebar/>
	</div>
	<topslider/>
</template>
<script>
	import sidebar from '@/components/sidebar.vue';
	import {ref,watch} from 'vue';
	import {useRoute} from 'vue-router';
	import tabbednav from '@/components/tabbednav.vue';
	import topslider from '@/components/topslider.vue';
	export default{
		name: "Search",
		setup(){
			const route = useRoute();
			const q = ref(route.query.q);

			document.querySelector("head title").textContent = "جستوجو - لایت مگ";
			document.querySelector("head meta[name='description']").setAttribute("content","جستوجو در لایت مگ")
			document.querySelector("head meta[name='keywords']").setAttribute("content","لایت مگ,مجله آنلاین,جستوجو,درباره لایت مگ,لایت مگ مجله آنلاین")
			watch(
				()=>route.query.q,
				newQ=>{
					if(route.name==="search"){
						q.value = newQ;
					}
				}
			)
			return{q}
		},
		components:{sidebar,tabbednav,topslider}
	};
</script>
<style>
	@import '../assets/search.css';
	@import '../assets/light-mag.css';
	@import '../assets/topnav.css';
</style>