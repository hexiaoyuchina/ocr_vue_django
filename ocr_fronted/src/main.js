
import App from './App.vue'
import Vue from 'vue'
import router  from './router'
import store from './store'
import './plugins/element.js'

new Vue({
    router, // 挂载路由
    store, // 挂载状态管理
    render: h => h(App)
  }).$mount('#app')
  
