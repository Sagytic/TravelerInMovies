import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/main/Home.vue'
import Signup from '@/views/accounts/Signup.vue'
import Login from '@/views/accounts/Login.vue'
import Profile from '@/views/accounts/Profile.vue'
import Movielist from '@/views/movies/Movielist.vue'
import Moviedetail from '@/views/movies/Moviedetail.vue'
import Moviereviews from '@/views/movies/Moviereviews.vue'
import Moviereviewswrite from '@/views/movies/Moviereviewswrite.vue'
import MovieRecommend from '@/views/movies/MovieRecommend.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '',
    name: 'Home',
    component: Home,
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/accounts/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/movies',
    name: 'Movielist',
    component: Movielist
  },
  {
    path: '/movies/:movie_pk',
    name: 'Moviedetail',
    component: Moviedetail,
    props: true
  },
  {
    path: '/movies/:movie_pk/Moviereviews',
    name: 'Moviereviews',
    component: Moviereviews,
    props: true
  },
  {
    path: '/movies/:movie_pk/Moviereviewswrite',
    name: 'Moviereviewswrite',
    component: Moviereviewswrite,
    props: true
  },
  {
    path: '/movies/MovieRecommend',
    name: 'MovieRecommend',
    component: MovieRecommend
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
