<template>
	<div class="page" id="page">
		<div class="right ed-bk">
			<p>در صورت درخواست ارتباط با مدیریت لایت مگ میتونید به ایمیل <a href="mailto:asghar3140@gmail.com">asghar3140@gmail.com</a> مراجعه کنید. یا به پروفایل نویسنده ها برید و از راه های ارتباطی استفاده کنید.</p>
		</div>
		<sidebar/>
	</div>
	<topslider/>
</template>

<script>
	import topslider from '@/components/topslider.vue';
	import sidebar from '@/components/sidebar.vue';
	export default{
		name: 'contact',
		components:{topslider,sidebar},
		setup(){
			document.querySelector("head title").textContent = "ارتباط با لایت مگ";
			document.querySelector("head meta[name='description']").setAttribute("content","ارتباط با مجله آنلاین لایت مگ")
			document.querySelector("head meta[name='keywords']").setAttribute("content","لایت مگ,مجلع آنلاین,ارتباط,درباره لایت مگ,لایت مگ مجله آنلاین")
		}
	};
</script>