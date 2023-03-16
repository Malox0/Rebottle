import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

import './assets/main.css'
import {createVuetify} from "vuetify";

const app = createApp(App)

import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import "vuetify/dist/vuetify.min.css";
import "@mdi/font/css/materialdesignicons.css";


const vuetify = createVuetify({
    components,
    directives,
})


app.use(createPinia())
app.use(vuetify)

app.mount('#app')
