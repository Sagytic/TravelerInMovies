<template>
  <div>
    <section>
			<button type="button" name="button" class="ac-sub-go-top"><i class="fas fa-arrow-up"></i></button>
			<div class="clearboth"></div>
		</section>

		<!-- <section>
			<div class="container">
				<div class="project-head">
					<div class="head-info">
						<div class="row">
							<div class="col-md-4">
                <a :href="movie.poster_path" target="_blank">
                <img class="projectimg" :src="movie.poster_path" style="width:300px;">
                
                </a>
							</div>
							<div class="col-md-8">
								<div class="fundding-info" v-bind="movie">
									<div class="item-moneybar"></div>
									<div class="fundding-amount mt10">
                    <h1 class="">{{movie.title}}</h1>
                    <span class="fundding-stat">개봉중</span>
                  </div>
									<div class="mt40">
										<span class="info-text">평점</span> 
                    <br>
										<span class="info-now mr5">{{ movie.vote_avg }}/10</span> 
                    <br>
										<span class="info-goal">{{ movie.vote_count }} Ratings</span>
									</div>
									<div class="mt20">
										<span class="info-text">줄거리</span> 
                    <br>
										<span class="info-now mr5">{{ movie.overview}}</span> 
										<br>
                    <span class="info-goal">2021.11.25종료</span>
									</div>
									<div class="mt40 btn-warp">
										<button type="button" class="like-btn"><i class="fas fa-heart"></i> 121</button>
										<a class="massege-btn" href="">찜하기</a>
										<a class="share-btn" href="">공유하기</a>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section> -->
		<section>
			<div class="project-bar">
			</div>
		</section>
    <section class="content-section">
      <div class="container">
        <div class="row">
          <div class="col-md-8">
            <div class="project-content mt40">
							<div class="PostEditTitle">게시글 작성하기</div>
              <form action="" id="review-form">
                <input type="text" v-model="review.title" />
                <input type="number" v-model="review.rank" min="0" max="100"/>
                <editor ref="toastuiEditor" />
              </form>
							<div class="PostEditLast">
								<div class="pull-right">
									<a class="register-btn" @click="createAction">등록 <i class="fas fa-check"></i></a>
								</div>
								<div class="clearfix"></div>
							</div>
						</div>
          </div>
          <div class="col-md-4">
            <div class="writer-info mt40">
              <div class="writer-card">
                <div class="hello">소개</div>
                <div class="mt10"><img class="user-photo" src="../../assets/user-account.png" >감독</div>
                <div class="mt10">
                  <p>소개글 입니다~~~</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import 'codemirror/lib/codemirror.css'; 
import '@toast-ui/editor/dist/toastui-editor.css'; 
import { Editor } from '@toast-ui/vue-editor';

export default {
  name: 'Moviedetail',
  components: { 
    Editor, 
  },
  data: function () {
    return {
      movie: null,
      tokenHeader: null,
      review: {
        title: '',
        content: '',
        movie_id: null,
      }
    }
  },
  methods: {
    createAction() {
      this.review.movie_id = this.movie.id
      var content = this.$refs.toastuiEditor.invoke("getHTML");
      this.review.content = content
      // content를 저장하는 액션 처리
      console.log(JSON.stringify(this.review))
      axios({
        // axios는 JSON.stringify를 자체적으로 해준다. 즉 data로 
        // 넘기는 값은 JSON.stringify를 해줄 필요가 없다.
        method: 'post',
        url: 'http://127.0.0.1:8000/movies/' + this.movie_pk + '/reviews',
        headers: this.tokenHeader,
        data: this.review
      })
        .then(res => {
          console.log(res)
          this.$router.push({ name: 'Moviedetail' })
        })
        .catch(err => {
          // 에러출력
          console.log(err)
        })
    }
  },
  props: {
    movie_pk: {
      type: String,
    }
  },
  created: function () {
    let token = localStorage.getItem('jwt')
    this.tokenHeader = {}
    const currentUser = localStorage.getItem("username");
    console.log(currentUser)
    if (token) {
      this.tokenHeader['Authorization'] = `JWT ${token}`
      this.isLogin = true
    } else {
      this.isLogin = false
    }
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/' + this.movie_pk,
      headers: this.tokenHeader,
    })
      .then(res => {
        console.log(res.data)
        this.movie = res.data
        this.username = currentUser
      })
      .catch(err => {
        console.log(err)
      })
  },
}
</script>