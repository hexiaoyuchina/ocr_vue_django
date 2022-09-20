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

    get_word_index(state,data){
        return Fetch({
            method: 'post',
            url: '/api/reg_img/get_word_index/',
            data:data,
            loadingStatus:state
        })
    }
}