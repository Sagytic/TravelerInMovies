<template>
  <div>
		<section>
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
		</section>
		<section>
			<div class="project-bar">
			</div>
		</section>
    <section class="content-section">
      <div class="container">
        <div class="row">
          <div class="col-md-8">
            <!-- 리뷰 목록 -->
            <div id="project-content" class="project-content mt40">
              <div class="community-card">
                <div class="community-card-head">
                  <span>
                    <img class="user-photo" src="../../assets/user-account.png" >
                  </span>
                  <div class="commu-write">
                    <span class="commu-writer">제목: {{review.title}}</span><br/>
                    <span class="commu-writer">작성자: {{review.user.nickname}}</span><br/>
                    <span class="commu-writedate">작성일: {{review.created_at.substr(0,10)}} / {{review.created_at.substr(11,8)}}</span>
                    <br>
                    <span class="commu-rank">평점: {{review.rank}}%</span>

                  </div>
                </div>
                <div class="community-card-body-review">
                  <div class="commu-content" v-html="review.content">
                  </div>
                  <div class="gmflrp"></div>
                </div>
              </div>
              <div class="community-card-foot mt10">
                <i class="fas fa-comment"></i>&nbsp;{{commentlength}}
              </div>
              <div class="">
								<div class="comment-writer" v-if="isLogin">
									<div class="comment-inbox">
										<em class="comment-inbox-name">{{username}}</em>
										<textarea class="comment-inbox-text" placeholder="댓글을 남겨주세요" 
                    rows="3" cols="30" type="text" v-model="commentval"></textarea>
									</div>
									<div class="commnet-btns">
										<div class="pull-right">
											<a class="pointer comment-register" @click="createComment">등록</a>
										</div>
										<div class="clearfix"></div>
									</div>
								</div>
                <div class="comment-writer" v-else>
									<div class="comment-inbox">
										<em class="comment-inbox-name">{{username}}</em>
										<textarea class="comment-inbox-text" placeholder="로그인 후 이용 가능합니다" rows="3" cols="30" readonly></textarea>
									</div>
									<div class="commnet-btns">
										<div class="pull-right">
										</div>
										<div class="clearfix"></div>
									</div>
								</div>
							</div>
							<div><!-- 댓글창 -->
              <div class="border-bottom"></div>
								<div class="user-comment mt20" v-for="comment in comments" v-bind:key='comment.id'>
									<div class="pull-left">
										<img class="user-photo" src="../../assets/user-account.png" >
									</div>
									<div class="pull-left comment-content">
										<p>{{comment.user.nickname}}</p>
										<p>{{comment.content}}</p>
									</div>
									<div class="pull-right">
										<span>{{comment.created_at.substr(0,10)}} / {{comment.created_at.substr(11,5)}}</span>
									</div>
									<div class="clearfix"></div>
									<div class="commnet-btns">
										<div class="pull-right">
											<a class="pointer comment-register" @click="deleteComment(comment)">삭제</a>
										</div>
										<div class="clearfix"></div>
									</div>
								</div>
							</div><!-- 댓글창 -->
            </div>
            <div v-if="review.user.username === username">
              <router-link :to="{ name: 'Moviereviewsupdate', params: { movie_pk:movie.id } }" >
                <button>수정하기</button>
              </router-link>
              <button @click="deleted()" >삭제하기</button>
              <router-link :to="{ name: 'Moviedetail', params: { movie_pk:movie.id } }" >
                <button>리뷰목록</button>
              </router-link>
            </div>
            <div v-else>
              <router-link :to="{ name: 'Moviedetail', params: { movie_pk:movie.id } }" >
                <button>리뷰목록</button>
              </router-link>
            </div>
            <!--  -->
          </div>
          <div class="col-md-4">
            <div class="writer-info mt40">
              <div class="writer-card">
                <div class="hello"></div>
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
import {mapGetters} from 'vuex'

export default {
  name: 'Moviereview',
  data: function () {
    return {
      movie: null,
      username: '',
      review: null,
      pageall: null,
      comment: null,
      commentlength: null,
    }
  },
  props: {
    movie_pk: {
      type: Number,
    },
    review_pk: {
      type: Number,
    },
    comment_pk: {
      type: Number,
    }
  },
  methods: {
    getreviews() {
      let token = localStorage.getItem('jwt')
      let tokenHeader = {}
      if (token) {
        tokenHeader['Authorization'] = `JWT ${token}`
        this.isLogin = true
      } else {
        this.isLogin = false
      }
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/reviews/' + this.review_pk + '/comments/',
        headers: tokenHeader,
      })
        .then(res => {
          console.log(res.data.length),
          this.comments = res.data
          this.commentlength = res.data.length
        })
        .catch(err => {
          console.log(err)
        })
    },
    linkGen(pageNum) {
      return pageNum === 1 ? '?' : `?page_num=${pageNum}`
    },
    deleted: function () {
      let token = localStorage.getItem('jwt')
      let tokenHeader = {}
      if (token) {
        tokenHeader['Authorization'] = `JWT ${token}`
        this.isLogin = true
      } else {
        this.isLogin = false
      }
      let url = 'http://127.0.0.1:8000/movies/' + this.movie_pk + '/reviews/' + this.review_pk +'/'
      axios({
        method: 'delete',
        url: url,
        headers: tokenHeader,
      })  
      .then(res => {
        console.log(res.data.length),
        this.review = res.data
        this.$router.push({ name: 'Moviedetail' })
      })
      .catch(err => {
        console.log(err)
      })
   },
  createComment: function () {
    let token = localStorage.getItem('jwt')
    let tokenHeader = {}
    if (token) {
      tokenHeader['Authorization'] = `JWT ${token}`
      this.isLogin = true
    } else {
      this.isLogin = false
    }
    const comment = {
      content: this.commentval,
      review_id: this.review.id,
    }
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/movies/reviews/' + this.review.id + '/comments/',
      headers: tokenHeader,
      data: comment,
    })
      .then(res => {
        console.log(res.data)
        this.comment=res.data
        this.getreviews()
      })
      .catch(err => {
        console.log(err)
      })
   },
   deleteComment: function (comment) {
    console.log(comment)
    let token = localStorage.getItem('jwt')
    let tokenHeader = {}
    if (token) {
      tokenHeader['Authorization'] = `JWT ${token}`
      this.isLogin = true
    } else {
      this.isLogin = false
    }
    axios({
      method: 'delete',
      url: 'http://127.0.0.1:8000/movies/comments/' + comment.id + '/',
      headers: tokenHeader,
    })
      .then(res => {
        console.log(res.data)
        this.getreviews()
      })
      .catch(err => {
        console.log(err)
      })
   }
  },
  created: function () {
    let token = localStorage.getItem('jwt')
    let tokenHeader = {}
    const currentUser = localStorage.getItem("username");
    console.log(currentUser)
    if (token) {
      tokenHeader['Authorization'] = `JWT ${token}`
      this.isLogin = true
    } else {
      this.isLogin = false
    }
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/' + this.movie_pk,
      headers: tokenHeader, currentUser
    })
      .then(res => {
        console.log(res.data)
        this.movie = res.data
        this.username = currentUser
      })
      .catch(err => {
        console.log(err)
      })
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/reviews/' + this.review_pk + '/comments/',
      headers: tokenHeader,
    })
      .then(res => {
        console.log(res.data.length),
        this.comments = res.data
        this.commentlength = res.data.length
      })
      .catch(err => {
        console.log(err)
      })
    let url = 'http://127.0.0.1:8000/movies/' + this.movie_pk + '/reviews/' + this.review_pk +'/'
    axios({
      method: 'get',
      url: url,
      headers: tokenHeader,
    })
      .then(res => {
        console.log(res.data.length),
        this.review = res.data
      })
      .catch(err => {
        console.log(err)
      })
  },
  watch: {
    $route() {
        let token = localStorage.getItem('jwt')
        let tokenHeader = {}
        if (token) {
          tokenHeader['Authorization'] = `JWT ${token}`
          this.isLogin = true
        } else {
          this.isLogin = false
        }
      let url = 'http://127.0.0.1:8000/movies/' + this.movie_pk + '/reviews/' + this.review_pk +'/'
      axios({
        method: 'get',
        url: url,
        headers: tokenHeader,
      })
        .then(res => {
          console.log(res.data.length),
          this.review = res.data
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  computed: {
    ...mapGetters([
      'getusernamei', 
    ])
  },
}
</script>

<style scoped>
.community-card-body-review {
    min-height: 30px;
}
.comment{
  width:100%;
  height:80px;
}
.project-content {
  height:87%;
}
.user-comment {
  padding:10px;
}
.border-bottom {
  border-bottom:1px solid #dbdbdb;
}
</style>