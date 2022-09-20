// 路由懒加载
const RegImage = ()=>import('@/views/reg_img/upload_img')
const ShowRegImage = () => import('@/views/reg_img/ShowImage.vue')
const regImageRoutes = {
    path:"/reg",
    component: () => import ('@/views/reg_img/reg_home'),
    children:[ // 子路由
        {
            path:'show',
            component: ShowRegImage
        },
        {
            path:'upload',
            component: RegImage
        }
    ]
}

export default regImageRoutes