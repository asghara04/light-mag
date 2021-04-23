<template>
	<base-layout>
		<template v-slot:main-content>
			<h1>testing ionic grid system</h1>
			<ion-grid>
				<ion-row>
					<ion-col class="ion-padding">
						<div>
							padding
						</div>
					</ion-col>
					<ion-col class="ion-padding-top">
						<div>
							padding-top
						</div>
					</ion-col>
					<ion-col class="ion-padding-start">
						<div>
							padding-start
						</div>
					</ion-col>
					<ion-col class="ion-padding-end">
						<div>
							padding-end
						</div>
					</ion-col>
				</ion-row>
				<ion-row>
					<ion-col class="ion-padding-bottom">
						<div>
							padding-bottom
						</div>
					</ion-col>
					<ion-col class="ion-padding-vertical">
						<div>
							padding-vertical
						</div>
					</ion-col>
					<ion-col class="ion-padding-horizental">
						<div>
							padding-horizental
						</div>
					</ion-col>
					<ion-col class="ion-no-padding">
						<div>
							no-padding
						</div>
					</ion-col>
				</ion-row>
			</ion-grid>
		</template>
	</base-layout>
</template>
<script>
	import {defineComponent} from 'vue';
	import {IonGrid, IonRow, IonCol} from '@ionic/vue';
	export default defineComponent({
		name: "HomePage",
		components:{
			IonGrid,
			IonRow,
			IonCol
		}
	});
</script>