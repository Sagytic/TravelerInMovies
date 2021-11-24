<template>
    <div>
      <section>
			<div class="containers">
				<div class="logindiv center-block mt40">
					<h3>가입하기</h3>
					<form name="loginform">
						<div class="join-uptext">아이디</div>
						<div class="login-info-div">
							<input type="text" name="username" id="username" v-model="credentials.username" placeholder="아이디는 영문 대소문자 5~15자 이내로 생성 가능합니다." >
							<span id="msg1" style="color:#f00"></span>
						</div>
						<!-- 닉네임 추가 -->
						<div class="join-uptext">닉네임</div>
						<div class="login-info-div">
							<input type="text" name="nickname" id="nickname" v-model="credentials.nickname" placeholder="닉네임은 영문 대소문자 5~15자 이내로 생성 가능합니다." >
							<span id="msg2" style="color:#f00"></span>
						</div>
						<!--  -->
						<div class="join-uptext">비밀번호</div>
						<div class="login-info-div">
							<input type="password" name="pw" id="pw" v-model="credentials.password" placeholder="비밀번호는 영문 대소문자 8~15자 이내로 생성 가능합니다.">
							<span id="msg3" style="color:#f00"></span>
						</div>
						<div class="login-info-div">
							<input type="password" name="pw2" id="pw2" v-model="credentials.passwordConfirmation" placeholder="비밀번호를 확인합니다">
							<span id="msg4" style="color:#f00"></span>
						</div>
						<!-- 이메일 X -->
						<!-- <div class="join-uptext">이메일</div>
						<div class="login-info-div">
							<input type="email" name="email" id="email" v-model="credentials.email" placeholder="사용하실 이메일을 입력해주세요">
							<span id="msg5" style="color:#f00"></span>
						</div> -->
						<div class="">
							<label for="allcheck" class="pointer join-checkbox-label pull-left">
								<input id="allcheck" type="checkbox" name="allcheck"><span>전체 동의</span>
							</label>
							<div class="clearfix"></div>
						</div>
						<div class="the_line"></div>
						<div class="join-checkbox">
							<ul class="list-unstyled">
								<li>
									<label for="ok" class="pointer join-checkbox-label pull-left">
										<input id="ok" type="checkbox" name="ok"><span>  이용 약관 동의</span>
									</label>
									<div class="pull-right">
										<a id="ok-btn" class="pointer">내용보기</a>
									</div>
									<div class="clearfix"></div>
								</li>
								<li>
									<label for="ok2" class="pointer join-checkbox-label pull-left">
										<input id="ok2" type="checkbox" name="ok2"><span>개인 정보 수집,이용 동의</span>
									</label>
									<div class="pull-right">
										<a id="ok2-btn" class="pointer">내용보기</a>
									</div>
									<div class="clearfix"></div>
								</li>
								<li>
									<label for="ok3" class="pointer join-checkbox-label pull-left">
										<input id="ok3" type="checkbox" name="ok3"><span>만 14세 이상입니다.</span>
									</label>
									<div class="clearfix"></div>
								</li>
							</ul>
						</div>
						<div class="login-submit-div mt40">
							<a onclick="goJoin()" @click="signup" class="pointer">가입하기</a>
						</div>
					</form>
					<div class="mt10 small-join">
						<span>이미 계정이 있다면? <router-link :to="{ name: 'Login' }">로그인하러가기</router-link></span>
					</div>
				</div>
			</div>
		</section>
		
		<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
			<div class="modal-dialog" >
				<div class="modal-content">
					<div class="modal-header">
						<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
						<h4 class="modal-title" id="myModalLabel"></h4>
					</div>
					<div class="modal-body" style="overflow:hidden;">
					</div>
					<div class="modal-footer">
						<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
					</div>
				</div>
			</div>
		</div>
    </div>
</template>
<script>
import axios from 'axios'
import 'bootstrap'
// npm i vue-swal 필요
import swal from "sweetalert";

// import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
// npm update vue-template-compiler 필요

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
				nickname: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials
      })
        .then(() => {
          this.$router.push({ name: 'Login'})
        })
				// back에서 확인후 가져온 에러로 팝업창 띄우기
        .catch(err => {
          swal(err.response.data.error, {
            dangerMode: true,
          })
      })
    },
		// refreshAll() {
		// 		this.$router.go();
		// 	},
	},
	merged: function() {
		this.$router.go();
	},
}
</script>

<style scoped>
.containers {
	width:80%;
	margin:auto;
}
</style>