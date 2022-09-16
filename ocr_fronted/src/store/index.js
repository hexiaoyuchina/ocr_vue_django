import Vue from 'vue'
import Vuex from 'vuex'
//导入模块
import reg_img_state from './modules/reg_image'
import getters from '@/store/getters' // 全局getters
// 注入插件
Vue.use(Vuex);
//创建实例
const store = new Vuex.Store({
    modules:{
        reg_img_state
    },
    getters
})

export default store