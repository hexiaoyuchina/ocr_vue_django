import Fetch from '@/utils/fetch.js'

export default {
    upload_img(state,data){
        return Fetch({
            method: 'post',
            url:'/api/reg_img/reg_image/',
            data:data,
            loadingStatus:state
        })
    },
    get_res_image(state, data){
        return Fetch({
            method: 'post',
            url: '/api/re_img/show_res/',
            data:data,
            loadingStatus:state
        })
    }
}