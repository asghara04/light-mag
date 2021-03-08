<template>
	<h2>دسته جدید</h2>
	<form class="form">
		<label for="image">تصویر دسته: </label>
		<label for="name">نام دسته: </label>
		<input type="text" name="name" maxlength="25" class="data-field" v-model="name">
		<label for="slug">اسلاگ دسته: </label>
		<input type="slug" name="slug" maxlength="25" class="data-field" v-model="slug">
	</form>
</template>
<script>
	import {ref} from 'vue';
	export default{
		name: "lm-add-category",
		setup(){
			const image = ref(null);
			const name = ref(null);
			const slug = ref(null);

			return{image,name,slug}
		}
	};
</script>
<style>
	@import '../assets/form.css';
</style>