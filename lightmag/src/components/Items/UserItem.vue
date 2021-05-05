<template>
	<!-- should be linked to router somthing like this: /users?username=user.username -->
	<ion-item lines="none">
		<ion-avatar slot="start" v-if="user.prof_picture">
			<img :src="user.prof_picture.image" :alt="user.prof_picture.alt">
		</ion-avatar>
		<ion-label>{{user.name}}</ion-label>
	</ion-item>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonItem, IonAvatar, IonLabel} from '@ionic/vue';

	export default defineComponent({
		name: "UserItem",
		props:{
			user:{
				type: Object,
				required: true
			}
		},
		components:{
			IonItem,
			IonAvatar,
			// IonImg,
			IonLabel
		}
	});
</script>