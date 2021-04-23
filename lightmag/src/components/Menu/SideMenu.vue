<template>
	<ion-menu side="start" menu-id="custom" class="custom-menu" content-id="main">
		<ion-header>
			<ion-toolbar color="tertiary">
				<ion-title>light mag</ion-title>
			</ion-toolbar>
		</ion-header>
		<ion-content>
			<ion-list>
				<ion-item>Light Theme</ion-item>
				<ion-item>Item 1</ion-item>
				<ion-item>Item 2</ion-item>
				<ion-item>Item 3</ion-item>
			</ion-list>
		</ion-content>
	</ion-menu>

<!-- 	<ion-menu side="start" menu-id="first" content-id="main">
		<ion-header>
			<ion-toolbar color="primary">
				<ion-title>light mag</ion-title>
			</ion-toolbar>
		</ion-header>
		<ion-content>
			<ion-list>
				<ion-item>Dark Theme</ion-item>
				<ion-item>Item 1</ion-item>
				<ion-item>Item 2</ion-item>
				<ion-item>Item 3</ion-item>
			</ion-list>
		</ion-content>
	</ion-menu>

	<ion-menu side="end" type="push" content-id="main">
		<ion-header>
			<ion-toolbar color="danger">
				<ion-title>light mag</ion-title>
			</ion-toolbar>
		</ion-header>
		<ion-content>
			<ion-list>
				<ion-item>Midnight Theme</ion-item>
				<ion-item>Item 1</ion-item>
				<ion-item>Item 2</ion-item>
				<ion-item>Item 3</ion-item>
			</ion-list>
		</ion-content>
	</ion-menu> -->
	<ion-router-outlet id='main'/>
</template>
<script>
import {IonMenu, IonHeader, IonToolbar, IonTitle, IonContent, IonList, IonItem, menuController, IonRouterOutlet } from '@ionic/vue';
import { defineComponent } from 'vue';

export default defineComponent({
	name: 'App',
	components: {
		IonMenu,
		IonHeader,
		IonToolbar,
		IonTitle,
		IonContent,
		IonList,
		IonItem,
		IonRouterOutlet
	},
	methods:{
		openFirst(){
			menuController.enable(true, 'first');
			menuController.open('first');
		},
		openEnd(){
			menuController.open("end");
		},
		openCustom(){
			menuController.enable(true, 'custom');
			menuController.open('custom');
		}
	}
});
</script>
<style>
	.custom-menu{
		--width: 500px;
	}
</style>