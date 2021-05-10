<template>
	<base-layout back-link="/">
		<template v-slot:main-content>
			<strong>Light Magazine</strong> is an Online Website and contain Technology and programming news and toturials, and first complete version will published on 2021 May 26, so this text will change soon :)
		</template>
	</base-layout>
</template>
<script>
	import {defineComponent} from 'vue';

	export default defineComponent({
		name: "About"
	});
</script>