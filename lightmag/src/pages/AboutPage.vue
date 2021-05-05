<template>
	<base-layout BackLink="/">
		<template v-slot:main-content>
			some about text
		</template>
	</base-layout>
</template>
<script>
	import {defineComponent} from 'vue';

	export default defineComponent({
		name: "About"
	});
</script>