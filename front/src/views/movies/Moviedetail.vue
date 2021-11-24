<template>
  <div>
    <!-- <section>
			<button type="button" name="button" class="ac-sub-go-top"><i class="fas fa-arrow-up"></i></button>
			<div class="clearboth"></div>
		</section> -->

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
            <div class="project-content mt40">
              <div class="rmfTmrldiv">
                <div class="pull-left">
                  <img class="user-photo" src="../../assets/user-account.png" >
                  <span v-if="isLogin">{{username}} 님 댓글을 작성해주세요!</span>
                  <span v-else>로그인한 유저만 글을 쓸 수 있습니다</span>
                </div>
                <div class="pull-right">
                  <router-link :to="{ name: 'Moviereviewswrite', params: { movie_pk:movie.id, username:getusernamei } }" >
                    <button type="button" class="btn btb-default">글쓰기</button>
                  </router-link>
                </div>
                <div class="clearfix"></div>
              </div>
            </div>
            <!-- 리뷰 목록 -->
            <div id="project-content" class="project-content mt40" v-for="review in reviews" v-bind:key="review">
              <div class="community-card">
                <div class="community-card-head">
                  <span>
                    <img class="user-photo" src="../../assets/user-account.png" >
                  </span>
                  <div class="commu-write">
                    <span class="commu-writer">제목: {{review.title}}</span><br/>
                    <span class="commu-writedate">작성일: {{review.created_at}}</span>
                    <br>
                    <span class="commu-rank">평점: {{review.rank}}%</span>

                  </div>
                </div>
                <div class="community-card-body">
                  <div class="commu-content" v-html="review.content">
                  </div>
                  <div class="gmflrp"></div>
                </div>
              </div>
              <div class="more-content mt20">
                <router-link :to="{ name: 'Moviereviews' }">더 보기</router-link>
              </div>
              <div class="community-card-foot mt10">
                <i class="fas fa-comment"></i>&nbsp;55
              </div>
            </div>
            <div>
              <!-- <div class="mt-3">
                <b-pagination
                  v-model="currentPage"
                  :total-rows="pageall.total_pages"
                  :per-page="1"
                  first-number
                  last-number
                  aria-controls="project-content"
                ></b-pagination>
              </div> -->
              <div class="overflow-auto">
                <b-pagination-nav :link-gen="linkGen" :number-of-pages="pageall.total_pages" use-router></b-pagination-nav>
              </div>
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
  name: 'Moviedetail',
  data: function () {
    return {
      movie: null,
      username: '',
      reviews: null,
      pageall: null,
    }
  },
  props: {
    movie_pk: {
      type: String,
    }
  },
  methods: {
      linkGen(pageNum) {
        return pageNum === 1 ? '?' : `?page_num=${pageNum}`
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
    let url = 'http://127.0.0.1:8000/movies/' + this.movie_pk + '/reviews/'
    if (this.$route.query.page_num) {
      url += '?page_num=' + this.$route.query.page_num
    }
    axios({
      method: 'get',
      url: url,
      headers: tokenHeader,
    })
      .then(res => {
        console.log(res.data.length),
        this.pageall = res.data[res.data.length - 1],
        res.data.pop(),
        this.reviews = res.data
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
      let url = 'http://127.0.0.1:8000/movies/' + this.movie_pk + '/reviews/'
      if (this.$route.query.page_num) {
        url += '?page_num=' + this.$route.query.page_num
      }
      axios({
        method: 'get',
        url: url,
        headers: tokenHeader,
      })
        .then(res => {
          console.log(res.data.length),
          this.pageall = res.data[res.data.length - 1],
          res.data.pop(),
          this.reviews = res.data
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