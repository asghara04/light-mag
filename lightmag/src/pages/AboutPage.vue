<template>
	<base-layout>
		<template v-slot:main-content>
			About Page - holla!
		</template>
	</base-layout>
</template>
<script>
	import {defineComponent} from 'vue';

	export default defineComponent({
		name: "About"
	});
</script>