<template>
    <div class="hello">
      <h1> 展示 </h1>
        <el-image :src="imageUrl"></el-image>
      <router-view></router-view>
    </div>
  </template>
  
  <script>
    import httpServer from '@/service/reg_service'
    export default {
      name: 'showImage',
        data(){
          return {
              wordIndex: [],
              imageUrl:''
          }
        },
      mounted(){
        console.log('aaaa');
        var data={'file_uuid':this.$store.getters.getFileUuid, 'file_name': this.$store.getters.getFileName};


        httpServer.get_word_index(true, data).then((res)=>{
            console.log(res)
            this.wordIndex = res
        });

        this.imageUrl = 'http://36.111.131.226:8000/static/'+this.$store.getters.getFileUuid+'/'+this.$store.getters.getFileName

      }
    }
  </script>

  