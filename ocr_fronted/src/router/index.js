import Vue from 'vue'
import Router  from 'vue-router'
//0.导入模块中的路由
import regImageRoutes from './reg'

//1.注入插件
Vue.use(Router )
// 2.定义路由活导入，路由与组建进行映射
const routes = [
    regImageRoutes
]
//3.创建路由实例并导出
const router =  new Router({
  routes,
  mode:'history'
})
   

export default router