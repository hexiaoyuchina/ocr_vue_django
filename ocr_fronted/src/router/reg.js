// 路由懒加载

const ShowRegImage = () => import('@/views/reg_img/ShowImage.vue')
const regImageRoutes = {
    path:"/reg",
    component: () => import ('@/views/reg_img/upload_img.vue'),
    children:[ // 子路由
        {
            path:'show',
            component: ShowRegImage
        }
    ]
}

export default regImageRoutes