<template>
  <div id="app">
    <div>
      <b-navbar toggleable="lg" type="dark" variant="dark">
        <b-navbar-nav>
          <b-nav-item :to="{ name: 'Home' }"><span style="color:pink"> Traveler in Movies </span></b-nav-item>
        </b-navbar-nav>
          <!-- Right aligned nav items -->
          <span v-if="isLogin">
            <b-navbar-nav class="ml-auto">
                <b-nav-item :to="{ name: 'Profile' }">Profile</b-nav-item>
                <b-nav-item @click="logout" to="#">Logout</b-nav-item>
            </b-navbar-nav>
          </span>
          <span v-else>
            <b-navbar-nav class="ml-auto">
              <li class="nav-item"><a href="http://localhost:8080/accounts/signup" aria-current="page" class="nav-link router-link-exact-active router-link-active" target="_self">Signup</a></li>
              <!-- <b-nav-item :to="{ name: 'Signup' }">Signup</b-nav-item> -->
              <b-nav-item :to="{ name: 'Login' }">Login</b-nav-item>
            </b-navbar-nav>
          </span>
            <b-navbar-nav class="ml-auto">
              <b-nav-item :to="{ name: 'Movielist' }">Movielist</b-nav-item>
            </b-navbar-nav>
      <div v-if="isLogin" style="color:white; margin-left:auto; margin-right:20px;">
        {{username}} 님 반갑습니다~
      </div>
      </b-navbar>
    </div>

    <!-- 로그인이 되었을 때 물리적인 렌더링도 변경 -->
    <router-view @login="isLogin=true"/>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
      username: null,
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      localStorage.removeItem("username")
      this.username = null
      this.$router.push({ name: 'Login' })
      // 로그아웃하며 토큰 삭제
    },
  },
  created: function () {
    // 로그인하며 토큰 저장
    const token = localStorage.getItem('jwt')
    const currentUser = localStorage.getItem("username")

    if (token) {
      this.isLogin = true
      this.username = currentUser
    }
  },
  updated: function () {
    // 로그인하며 토큰 저장
    const token = localStorage.getItem('jwt')
    const currentUser = localStorage.getItem("username")

    if (token) {
      this.isLogin = true
      this.username = currentUser
    }
  },
  computed: {
    ...mapGetters([
      'getusernamei', 
    ])
  },
}
</script>


<style>
/* 전체 */
html {
  font-size: 16px;
  background: #37373d;
}
body {
  background: #37373d;
}
.containers {
  background: #1e1e1e;
  color:white;
}
.container {
  background: #1e1e1e;
  color:white;
}
section {
  background: #1e1e1e;
}
input {
  color:black;
}
a {
  text-decoration: npne;
}
#app {
  font-family: 'Roboto' ,'Noto Sans KR', 'sans-serif';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  /* background: #1e1e1e; */
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

section {
  background:#37373d;
}
/* 로그인&회원가입 */

  body {
    font-family: 'Roboto' ,'Noto Sans KR', 'sans-serif';
  }	
  .pointer{
    cursor:pointer;
  }
  .logindiv{
    width: 450px;
      border: 1px solid #dbdbdb;
      border-radius: 5px;
      padding: 32px;
      margin: 100px auto 80px;
  }
  .logindiv h3{
    font-size:24px;
    margin-bottom:36px;
  }

  .login-info-div{
    border:1px solid #dbdbdb;
    border-radius:5px;
    background:#fff;
    width:100%;
    height:44px;
    margin-bottom:24px;
    font-size:14px;
    padding:0px 20px;
  }
  .login-info-div input{
    width:100%;
    border:0px;
    height:100%;
    outline:none;
  }
  .login-submit-div a{
    display:inline-block;
    width:100%;
    text-align: center;
    padding:10px 0px;
    background:#ff9696;
    border-radius:5px;
    color:#fff;
    font-size:16px;
  }
  .small-join {
    text-align: center;
  }
  .small-join span{
    font-size: 11px;
    color:#c7c7c7;
  }
  .small-join span a{
    color:#27a3ff;
  }
  .the_line{
    border:1px solid #dbdbdb;
    margin:15px 0px;
  }
  .join-uptext{
    margin-bottom:10px;
  }

  .join-checkbox-label input{
    width:16px;
    height:16px;
  }
  .join-checkbox-label span{
    font-weight:400;
    margin-left:10px;
    font-size:13px;
    vertical-align:3px;
  }
  .join-checkbox ul li div a{
    font-size:11px;
    color:#27a3ff;
    vertical-align:-2px;
  }



/* 영화 목록&상세페이지&리뷰댓글 */
.user-photo{
	width:38px;
	height:38px;
	margin-right: 10px;
}
/* .ac-sub-go-top{
  width: 30px;
  height: 30px;
  bottom:calc(50% - 35px);
  position: fixed;
  right: calc((100% - 1200px)/ 2 - 80px);
  display: inline-block;
  background:rgba(255,255,255,0.7);
  border: none;
  background-size: 50%;
  display: none;
} */

.categorydiv{
	margin:14px auto;
	width: 832px;
	text-align: center;
	
}
.categorydiv a{
	color:#555;
}
.category-part{
	display:inline-block;
	width: 80px;
	height:60px;
	font-size:13px;
	text-align:center;
	margin-right: 30px;
}
.category-1{
	display:block;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  margin: 0 auto;
  background-size: cover;
}
.category-2{
	display:block;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  margin: 0 auto;
  background-size: cover;
}
.category-3{
	display:block;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  margin: 0 auto;
  background-size: cover;
}
.category-4{
	display:block;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  margin: 0 auto;
  background-size: cover;
}
.category-5{
	display:block;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  margin: 0 auto;
  background-size: cover;
}
.category-6{
	display:block;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  margin: 0 auto;
  background-size: cover;
}
.category-7{
  display: block;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  margin: 0 auto;
  background-size: cover;
}

.procount {
	font-size:16px;
}
.procount > span{
	color:#ff9696;
}

.listdiv{
	margin-top:24px;
  background:#1e1e1e;
}
.item-h{
	margin-top:50px;
	position:relative;
}

.item-image{
	border-radius:4px;
	position:relative;
	overflow:hidden;
	width: 250px;
  height: 170px;
}
.item-image a img:hover{
	transform: scale(1.2);
}
.item-image a img{
	width:100%;
	position:relative;
	transition:all 0.3s ease-out;
}

.item-view{
	margin-top: 15px;
  min-height: 150px;
}

.item-title {
	width:100%;
	font-size:20px;
	margin-bottom:10px; 
	overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.item-info{
	font-size: 13px;
	padding:10px;
	color:#9e9e9e;
}

.item-content{
	margin:0px 0px 16px;
	overflow:hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.wait-coment{
	text-align: center;
	border: 1px solid #dbdbdb;
	padding: 6px 0px;
	border-radius: 5px;
	color: #555;
}

.item-moneybar{
	width:100%;
	margin:0px;
	overflow:hidden;
	background:#d0d0d0;
	height:2px;
	position:relative;
}
.item-moneybar-ss{
	content:"";
	display: block;
	height:100%;
	background:#ff9696;
}

.inqtext{
	resize:none;
	width: 550px;
	height:60px;
	font-size:16px;
}
.inqusend-btn a{
	display:inline-block;
	background: #ff9696;
  color: #fff;
  padding: 3px 10px;
  margin-top: 10px;
  border-radius: 5px;
}

.item-funddingstat{
	margin:0px;
	align-items: flex-end;
	height:35px;
}
.fundding-amount{
	line-height:27px;
	color:#ff9696;
	font-size:30px;
	font-weight:700;
	margin-top:18px;
	letter-spacing:2px;
}

.fundding_contents{
	width: 300px;
  height: 145px;
  margin-top: 35px;
  background: #37373d;
  padding: 20px;
}
.fundding_contents h5{
  font-size: 20px;
  color: #969696;
}
    
.fundding_contents p{
  color: #969696;
}
 
.percent{
	color:#ff9696;
	margin-left:6px;
}
.rest-day{
	margin-left:auto;
	color:#9e9e9e;
}

.mt40 {
  margin-top: 40px;
}

.mt20 {
  margin-top: 20px;
}

.user-photo {
  width: 38px;
  height: 38px;
  margin-right: 10px;
}
.sitelogo {
  width: 100%;
}

.fundding-amount {
  line-height: 27px;
  color: #ff9696;
  font-size: 30px;
  font-weight: 700;
  margin-top: 18px;
  letter-spacing: 2px;
}

.fundding_contents {
  width: 300px;
  height: 145px;
  margin-top: 35px;
  background: #37373d;
  padding: 20px;
}
.fundding_contents h5 {
  font-size: 20px;
  color: #969696;
}

.fundding_contents p {
  color: #969696;
}

.percent {
  color: #ff9696;
  margin-left: 6px;
}
.rest-day {
  margin-left: auto;
  color: #9e9e9e;
}

.project-head {
  padding-bottom: 30px;
}
.head-info {
  width: 100%;
  margin: 0 auto;
  position: relative;
  height: auto;
  padding: 0;
}
.head-title {
  height: 180px;
  padding-bottom: 0;
  align-items: center;
  justify-content: center;
}
.title-div {
  text-align: center;
  margin: 0 auto;
  padding: 10px;
  margin-top: 50px;
}

.projectimg {
  width: 100%;
}
.fundding-info {
  padding: 0 15px 30px 30px;
}

.fundding-stat {
  font-size: 14px;
  font-weight: 700;
}
.info-text {
  font-size: 14px;
  min-width: 50px;
  line-height: 30px;
  display: inline-block;
  color: #969696;
}
.info-now {
  font-size: 20px;
}
.info-goal {
  font-size: 12px;
  color: #969696;
  line-height: 28px;
}

.btn-warp {
  width: 100%;
}
.btn-warp a {
  display: inline-block;
  padding: 8px 14px;
  border: 1px solid #dbdbdb;
}
.like-btn {
  display: inline-block;
  padding: 8px 14px;
  border: 1px solid #dbdbdb;
  color: #ff9696;
  background: #fff;
}
.project-bar {
  border-top: 1px solid #dbdbdb;
  border-bottom: 1px solid #dbdbdb;
  box-shadow: rgb(0 0 0 / 10%) 0 2px 3px;
}
.project-bar div a {
  display: inline-block;
  font-size: 14px;
  padding: 20px;
}

.content-section {
  height:100%;
  background: #37373d;
}

.project-content,
.reward-list,
.writer-info {

  padding: 30px;
  background: #fff;
  border: 1px solid #dbdbdb;
}

.project_content_image {
  width: 630px;
}

.project-content img {
  max-width: 100%;
}

.project-content {
  margin-bottom: 60px;
}
.community-card {
  position: relative;
}
.community-card-head {
  vertical-align: bottom;

}
.commu-write {
  display: inline-block;
  vertical-align: -12px;
}
.community-card-body {
  min-height: 30px;
  max-height: 500px;
  overflow: hidden;
}
.commu-content {
  padding: 21px 0;
}
.gmflrp {
  position: absolute;
  display: block;
  bottom: 0;
  left: 0;
  right: 0;
  height: 50px;
  z-index: 200;
  background: linear-gradient(rgba(255, 255, 255, 0), rgba(255, 255, 255, 0.5) 45%, rgb(255, 255, 255));
  content: "";
}
.more-content {
  width: 100%;
}
.more-content a {
  border-radius: 5px;
  padding: 10px;
  display: inline-block;
  width: 100%;
  text-align: center;
  background: rgba(255,150,150,0.2);
  font-weight: 700;
}

.community-card-foot {
  width: 100%;
  padding-top: 10px;
  border-top: 1px solid #dbdbdb;
}

.comment-inbox {
  position: relative;
  margin-bottom: 10px;
}

.user-comment {
  border-bottom: 1px solid #dbdbdb;
  padding-bottom: 20px;
}

.comment-inbox-name {
  display: block;
  margin-bottom: 10px;
  font-weight: 500;
  font-size: 13px;
}

.comment-inbox-text {
  overflow: hidden;
  min-height: 17px;
  width: 100%;
  border: 0;
  font-size: 13px;
  resize: none;
}

.comment-writer {
  margin: 12px 0 29px;
  padding: 16px 10px 10px 18px;
  border: 1px solid #efefef;
  border-radius: 3px;

}
.comment-delete-btn {
  display: inline-block;
  background: #ff9696;
  color: #fff;
  padding: 1px 5px;
  border-radius: 5px;
}
.commu-write {
  margin-bottom: 20px;
}

.rmfTmrldiv span {
  margin-left: 10px;
  margin-top: 10px;
  display: inline-block;
}

.button_p {
  color: #fff;
  background: #FF9696;
  border: none;
  padding: 10px 50px;
  margin: 10px;
  font-size: 17px;
}

.register-btn {
  color: #FF9696;
  background: #ffffff;
  border: 1px solid #FF9696;
  padding: 15px 40px;
  margin: 20px 0;
  font-size: 16px;
  display: inline-block;
}

.community_wb {
  color: #fff;
  background: #FF9696;
  border: none;
  padding: 10px 20px;
  margin: 10px;
  font-size: 15px;
}

.community_b a {
  border: 1px solid #dbdbdb;
  padding: 10px;
}

.comment_b {
  border: 1px solid #FF9696;
  padding: 5px 10px;
  color: #FF9696;
}

.s-size-photo {
  height: 150px;
  margin-right: 30px;
}

.order-check {
  border-top: 1px solid #dbdbdb;
  padding: 24px;
}

.order-state-head {
  font-size: 16px;
  color: #333;
  font-weight: 500;
}
.order-state-body input {
  border: 1px solid #dbdbdb;
  height: 35px;
}
.order-state-body {
  border: 1px solid #dbdbdb;
  border-radius: 5px;
  padding: 10px;
}

.precautions {
  font-size: 11px;
  padding: 8px;
}

.order-last-pay div:first-child {
  color: #ff9696;
  font-size: 16px;
}

.order-state-table tr th {
  padding: 4px 0 4px 20px;
  vertical-align: top;
  text-align: left;
}

.order-state-text {
  padding: 4px 0 4px 20px;
  font-size: 12px;
}

.order-state-table {
  width: 100%;
  margin: 16px 0;
}

.order-last-pay {
  padding: 10px;
}

.perinfo-check div a {
  margin: 3px 0 0 10px;
  display: inline-block;
  color: #27a3ff;
  text-decoration: underline;
}

.more-info {
  margin: 3px 0 0 10px;
}

.project-order-submit a {
  display: inline-block;
  background: #ff9696;
  color: #fff;
  font-size: 16px;
  border-radius: 3px;
  padding: 10px 30%;
}

.project-order-submit {
  text-align: center;
}
.precautions span {
  color: #ff9696;
  font-weight: 700;
}

.order-complete {
  text-align: center;
}

.congratu {
  margin-top: 100px;
  color: #ff9696;
}

.postNum_b {
  background: #37373d;
  color: #969696;
  padding: 10px;
  border: none;
}

.mainBack_button {
  color: #FF9696;
  background: #ffffff;
  border: 1px solid #FF9696;
  padding: 15px 60px;
  margin: 20px;
  font-size: 16px;
  display: inline-block;
  margin-bottom: 100px;
}

.project_list_button {
  background: #FF9696;
  border: none;
  padding: 15px 50px;
  margin: 20px;
  font-size: 16px;
}

.xpdlqmf {
  text-align: center;
}

.fundding-amount1 {
  line-height: 27px;
  color: #ff9696;
  font-size: 25px;
  font-weight: 700;
  margin-top: 18px;
  letter-spacing: 2px;
}

.order_radio_b {
  height: 13px;
  margin-right: 10px;
  margin-left: 100px;
}
.item-image a img{
width:100%;
}

</style>
