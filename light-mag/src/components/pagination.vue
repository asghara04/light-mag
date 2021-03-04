
<!-- <template>
	<div class="pagination-com">
		<router-link v-if="current>2" class="link-like" target="_blank" :to="{query: {page: 1}}" rel="مجله نور صفحه 1">1</router-link>
		<p v-if="current>3">...</p>
		<router-link v-if="current>1" target="_blank" class="link-like" :to="{query: {page: (current-1)}}" :rel="'مجله نور صفحه '+(current-1)">{{(current-1)}}</router-link>

		<p class="page-active">{{current}}</p>

		<router-link target="_blank" v-if="current<parseInt((all+size-1)/size)" class="link-like" :to="{query: {page: (current+1)}}" :rel="'مجله نور صفحه '+(current+1)">{{(current+1)}}</router-link>
		<p v-if="current+2<parseInt((all+size-1)/size)">...</p>
		<router-link v-if="current+1<parseInt((all+size-1)/size)" class="link-like" :to="{query: {page: parseInt((all+size-1)/size)}}" :rel="'مجله نور صفحه '+parseInt((all+size-1)/size)" target="_blank">{{parseInt((all+size-1)/size)}}</router-link>
	</div>
</template>
<script>
	import {ref} from 'vue';
	import {useRoute} from 'vue-router';
	export default{
		name: "pagination",
		props:{
			all: Number,
			size: Number
		},
		setup(){
			const route = useRoute();
			const current = ref(parseInt(route.query.page)||1)

			return{current}
		}
	};
</script>
<style>
	@import '../assets/pagination.css';
</style> -->