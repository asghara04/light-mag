import { createApp } from 'vue'

/* Components */
import App from './App.vue'
import BaseApp from './components/Base/BaseApp.vue';
import BaseLayout from './components/Base/BaseLayout.vue';
import MainRefresher from './components/Refresher/MainRefresher.vue';

import router from './router';

/* store */
import store from './store/index.js';

import { IonicVue } from '@ionic/vue';

/* meta manager for vue-meta 3.0.0-alpha.5 */
import {createMetaManager} from 'vue-meta';

/* Core CSS required for Ionic components to work properly */
import '@ionic/vue/css/core.css';

/* Basic CSS for apps built with Ionic */
import '@ionic/vue/css/normalize.css';
import '@ionic/vue/css/structure.css';
import '@ionic/vue/css/typography.css';

/* Optional CSS utils that can be commented out */
import '@ionic/vue/css/padding.css';
import '@ionic/vue/css/float-elements.css';
import '@ionic/vue/css/text-alignment.css';
import '@ionic/vue/css/text-transformation.css';
import '@ionic/vue/css/flex-utils.css';
import '@ionic/vue/css/display.css';

/* Theme variables */
import './theme/variables.css';
import './theme/lightmag.css';

const app = createApp(App)
  .use(IonicVue)
  .use(router)
  .use(store)
  .use(createMetaManager)

/* goobal components */
app.component("base-app", BaseApp);
app.component('base-layout', BaseLayout);
app.component('main-refresher', MainRefresher);

router.isReady().then(() => {
  app.mount('#app');
});