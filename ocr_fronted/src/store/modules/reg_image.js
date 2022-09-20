const reg_img_state ={
    state:{
        file_uuid: '',
        file_name:''
    },
    mutations:{
        updateFileUuid(state, file_uuid) {
            console.log(file_uuid);
            state.file_uuid = file_uuid
        },
        updateFileName(state, file_name){
            state.file_name = file_name
}
    },
    actions:{},
    getters:{
        getFileUuid: state=>state.file_uuid,
        getFileName: state=>state.file_name
    }
}

export default reg_img_state