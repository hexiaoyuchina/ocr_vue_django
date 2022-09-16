import axios from "axios"
import store from "@/store"
import { Loading } from "element-ui"
// 创建axios实例
const service = axios.create({
    baseURL: '', // api的base_url,vue.config.js中代理成真正的
    timeout: 30000,                  // 请求超时时间
    loadingStatus: false             // 是否显示加载中
  })
let loadingInstance = null
var loadEntity = {
    lock: true,
    text: '数据正在加载中',    // lang.LOADING,
    spinner: 'el-icon-loading',
    background: 'rgba(0, 0, 0, 0.3)',
    customClass: 'loading'
}
let needLoadingRequestCount = 0
// request 拦截器
service.interceptors.request.use(
    config => {
        // 请求时间长时显示加载中
        if(config.loadingStatus){
            needLoadingRequestCount++
            loadingInstance = Loading.service(loadEntity)
        }
        // token设置header
        if (store.getters.token) {
            config.headers['Access-Token'] = store.getters.token // 让每个请求携带自定义token 请根据实际情况自行修改
            config.headers['X-Requested-With'] = 'XMLHttpRequest'
            config.headers['project-id'] = store.getters.project_id
            // config = addConfigItem(config)
          }      
        return config
    },
    error =>{
        //处理出错的请求
        return Promise.reject(error)
    }
)

//response拦截器
service.interceptors.response.use(
    response => {
        if (response.config.loadingStatus) {
            needLoadingRequestCount--
            if (needLoadingRequestCount <= 0) {
              loadingInstance.close()
            }
        }
        if (response.data.code == 401) {
            // Message.error(response.data.login_url);
            window.parent.location.href = response.data.login_url;
        } else {
            return response.data;
        }
    },
    error =>{
        if (error.response && error.response.status === 401) { //未登录

            // let href = process.env.VUE_APP_GIC_URL
            // let loginurl = error.response.data.sso_url + href
            // console.log(loginurl)
            const loginurl = window.location.origin + '/login'
            window.location.href = loginurl
        } else if (error && error.response) {
            // ElMessage({message: error.response.msg, type: 'error'})
        }
        return Promise.reject(error.response.data)
    }  
)
export default service