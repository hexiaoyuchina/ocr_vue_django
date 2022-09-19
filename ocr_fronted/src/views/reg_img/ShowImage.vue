<template>
    <div class="hello">
      <h1>{{ 展示 }}</h1>
    </div>
  </template>
  
  <script>
    import httpServer from '@/service/reg_service'
    export default {
      name: 'showImage',
      mounted(){
        httpServer.showImage(true, this.$store.reg_img_state.file_uuid).then((res)=>{
          console.log(res);
        })
      }
    }
  </script>

  