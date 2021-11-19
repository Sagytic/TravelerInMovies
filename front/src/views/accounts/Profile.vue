<template>
  <section>
			<div class="container2">
				<div class="container2-1">
					<div class="container2-1-1">
						<div class="absoluteid1">
							<a href="profile.html">
								<div class="absoluteid1-1">
									프로필 변경
								</div>
							</a>
							<a href="myproject.html">
								<div class="absoluteid1-2">
									창작자 페이지
								</div>
							</a>
						</div>
						<div class="container2-1-1-1">
							<a href="#">
								<div class="container2-1_box0">
									<div class="container2-1_box0_img">
										<img class="user-photo" src="../../assets/user-account.png" >
									</div>
									<div class="container2-1_box2">
										내 계정 
									</div>
									<div class="container2-1_box_id">
										admin
									</div>
								</div>
							</a>	
						</div>
						<div class="container2-1-1-2">
								<div class="container2-1_box2">
									마이페이지
								</div>
							<a href="mypage.html">
								<div class="container2-1_box1">
									찜 목록
								</div>
							</a>
							<a href="mypage2.html">
								<div class="container2-1_box1">
									리뷰 목록
								</div>
							</a>
							<a href="News.html">
								<div class="container2-1_box1" style="">
									댓글 목록
								</div>
							</a>	
						</div>
<!--					<div class="container2-1-1-3">
							<div class="container2-1_box2">
								주문내역
							</div>
							<a href="#">
								<div class="container2-1_box1">
									배송상황
								</div>
							</a>
							<a href="#">
								<div class="container2-1_box1">
									후원내역
								</div>
							</a>
						</div>											-->	
					</div>
					<div class="container2-1-2">
						<a href="#">
							<div class="container2-1_box1">
								이용안내
							</div>
						</a>
						<a href="#">
							<div class="container2-1_box1">
								문의사항
							</div>
						</a>	
						<a href="#">
							<div class="container2-1_box1">
								공지사항
							</div>
						</a>
					</div>
				</div>
				<div class="container2-2">
					<div class="container2-2-1">
						<div class="container2-2-1-1">
							<h4>프로필 변경</h4>
						</div>
						
					</div>
					<div class="container2-2-2">
						<div class="container2-2-2-1">
							<div class="id1-1"><strong>아이디</strong></div>
							<input class="id1-2" value=" admin"><br>
							<button class="id1-3">변경</button>
						</div>
						<div class="container2-2-2-2">
							<div class="icon1-1"><strong>프로필 이미지</strong></div>
							<div class="icon1-2">
								<img src="../../assets/user-account.png" class="icon-1-2-1"><br>
								<input type="file" class="icon1-2-2">
								<button class="icon1-2-3">프로필 아이콘 편집</button>
							</div>
							
						</div>
						<div class="container2-2-2-1">
							<div class="pw1-1"><strong>비밀번호</strong></div>
							<input class="pw1-2" value=" 12341234"><br>
							<button class="pw1-3">변경</button>
						</div>
						<div class="container2-2-2-1">
							<div class="email1-1"><strong>이메일</strong></div>
							<input class="email1-2" value="admin@naver.com"><br>
							<button class="email1-3">변경</button>
						</div>
					</div>
				</div>
			</div>
		</section>
</template>

<script>
import axios from 'axios'

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
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials
      })
        .then(res => {
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$router.push({ name: 'TodoList' })
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>
