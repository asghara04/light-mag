<template>
	<ion-app>
		<base-app></base-app>
	</ion-app>
</template>

<script>
import { IonApp } from '@ionic/vue';
import { defineComponent } from 'vue';

export default defineComponent({
	name: 'App',
	components: {
		IonApp,
	}
});
</script>