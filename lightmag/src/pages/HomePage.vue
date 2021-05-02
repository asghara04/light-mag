<template>
	<base-layout>
		<template v-slot:main-content>
			<popular-articles></popular-articles>
			<ion-router-outlet/>
		</template>
		<!-- an ion-router-outlet or router-view or somthing for home children -->
	</base-layout>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonRouterOutlet} from '@ionic/vue';
	import PopularArticles from '@/components/Dynamic/PopularArticles.vue';

	export default defineComponent({
		name: "HomePage",
		components:{
			PopularArticles,
			IonRouterOutlet
		}
	});
</script>