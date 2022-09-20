const reg_img_state ={
    state:{
        file_uuid:''
    },
    mutations:{
        file_uuid(state, file_uuid){
            console.log(file_uuid);
            state.file_uuid = file_uuid
        }
    },
    actions:{},
    getters:{
        get_file_uuid: state=>state.file_uuid
    }
}

export default reg_img_state