<template>
	<div class="page" id="page">
		<div class="right ed-bk">
			<h2 class="cen">لایت مگ</h2>
			<p>لایت مگ یه مجله آنلاینه و از شنبه، ۷ فروردین ۱۴۰۰ شروع به فعالیت کرده و کل ایده لایت مگ هم اینه که قالب مقالاتش آموزنده، فان، اخبار جالب،.. باشه. و تو زمینه های مختلف موضوعات زیادی رو پوشش میده از جمله:</p>
			<ul>
				<li>فناوری</li>
				<li>فیلم و سریال</li>
				<li>توسعه و برنامه نویسی</li>
				<li>هوش مصنوعی</li>
				<li>اخبار</li>
				<li>سرگرمی</li>
				<li>و...</li>
			</ul>
			<p>در صورت درخواست ارتباط با مدیریت به <router-link to="/contact" class="link-like" ref="لایت مگ">این صفحه</router-link> مرجعه کنید.</p>
		</div>
		<sidebar/>
	</div>
	<topslider/>
</template>

<script>
	import topslider from '../components/topslider.vue';
	import sidebar from '../components/sidebar.vue';
	export default{
		name: "about",
		components:{topslider,sidebar},
		setup(){
			document.querySelector("head title").textContent = "لایت مگ - درباره";
			document.querySelector("head meta[name='description']").setAttribute("content","دربار لایت مگ ،مجله آنلاین")
			document.querySelector("head meta[name='keywords']").setAttribute("content","لایت مگ,مجله آنلاین,اصغر اله,درباره لایت مگ,لایت مگ مجله آنلاین")
		}
	};
</script>
<style>
	@import '../assets/light-mag.css';
</style>