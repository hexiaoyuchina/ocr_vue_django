
<template>
  <div>
    <el-upload
      class="upload-demo"
      action="#" 
      :on-preview="handlePreview"
      :on-remove="handleRemove"
      :file-list="fileList"
      :http-request="uploadFile"
      :before-upload="beforeUpload"
      list-type="picture">
      <el-button size="small" type="primary">点击上传</el-button>
      <div class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
    </el-upload>
</div>
</template>

<script>

import httpServer from '@/service/reg_service'
export default {
  name: 'App',
  data(){
    return {
      fileList:[]
    }
  },
  methods:{
    beforeUpload(file){
      let types = ['image/jpeg', 'image/jpg', 'image/png'];
      const isImage = types.includes(file.type);
      if (!isImage) {
        this.$message.error('上传图片只能是 JPG、JPEG、PNG 格式!');
        return false;
      }
      return true
    },
    handleRemove(file, fileList) {
        //文件列表移除文件时的钩子
        console.log(file, fileList);
    },
    handlePreview(file) {
        //点击文件列表已上传的文件时的钩子
        console.log(file);
    },

    uploadFile(params) {
      console.log("uploadFile", params);
      const _file = params.file;
      // 通过 FormData 对象上传文件
      var formData = new FormData();
      formData.append("file", _file);

      // 发起请求
      httpServer.upload_img(true,formData).then(res=>{

        console.log(res.file_uuid)
        this.$store.reg_img_state.file_uuid = res.file_uuid
        this.$router.push('reg/show')
      })
    }
  },
  computed:{
    
  }
}
</script>