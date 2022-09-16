
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  outputDir: 'dist',

  devServer:{ // 本地解决跨域问题
    open: false,// 服务启动后是否打开浏览器
    port: 8080, // 指定监听的端口号
    proxy:{// 本地实现跨域访问后端服务，将前端的url代理到对应的后端
      'api/':{
        target: 'http://36.111.131.226:8000/',// 实际后端服务地址
        changeOrigin: true, //设置为 true 之后，就会把请求 API header 中的 origin，改成跟 target 里边的域名一样了
        pathReWrite: {
          '^/api': '/api' //后面的api为替换成的路径，将api/ 代理到http://36.111.131.226:8000/api/
        }
      }
    }
  }
})
