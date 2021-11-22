<template>
  <section>
			<div class="container">
				<div class="logindiv center-block mt40">
					<h3>로그인</h3>
					<form name="loginform" id="loginform">
						<div class="login-info-div">
							<input type="text" name="id" id="username" v-model="credentials.username" placeholder="아이디 입력" >
						</div>
						<div class="login-info-div">
							<input type="password" id="password" v-model="credentials.password" name="pw" placeholder="비밀번호 입력">
						</div>
						<div class="login-submit-div mt40">
							<a @click="login" id="login-btn" class="pointer">로그인</a>
						</div>
					</form>
					<div class="mt10 small-join">
						<span> 계정이 없다면? <router-link :to="{ name: 'Signup' }">가입하러가기</router-link></span>
					</div>
					<div class="the_line"></div>
					<div class="mt10 small-join">
						<span><a href="#">비밀번호를 찾고 계신가요?</a></span>
					</div>
				</div>
			</div>
		</section>
</template>

<script>
import axios from 'axios'
import {mapActions} from 'vuex'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
		...mapActions([
			'loginGetToken',
      'getProfile',
      'getReviewsGenre',
      'getReviewsCountry',
      'getReviews',
      'getReviewsMovieInfo',
		]),

    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials
      })
        .then(res => {
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          console.log(res.data.token)
          this.loginGetToken()
          // this.setToken()
          this.getProfile()
          this.getReviewsGenre()
          this.getReviewsCountry()
          this.getReviews()
          this.getReviewsMovieInfo()
          this.$router.push({ name: 'Home' })
          // commit("SET_TOKEN", res.data.token)
          
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  // updated: function () {
  //   this.getProfile()
  // }
}
</script>
