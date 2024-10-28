import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from "axios"
import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";
import PrimeVue from 'primevue/config';

axios.default.baseURL = "http://127.0.0.1:8000/"

const app = createApp(App)

app.component("v-select", vSelect);
app.use(createPinia())
app.use(PrimeVue);
app.use(router)
app.use(axios)

app.mount('#app')
