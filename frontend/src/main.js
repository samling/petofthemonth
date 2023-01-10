import { createApp } from 'vue'
import axios from 'axios'
import App from './App.vue'
import router from './router'

import './assets/main.css'

const app = createApp(App)

axios.defaults.withCredentials = true
axios.defaults.baseURL = 'http://localhost:8000/'

app.use(router)

app.mount('#app')
