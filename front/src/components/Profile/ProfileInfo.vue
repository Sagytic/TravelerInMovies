<template>
  <div>
    <div class="background" v-if="background_image===`${SERVER_URL}null`" :style="{ 'background-image': 'url(' + 'https://picsum.photos/600/200' + ')' }"></div>
    <div class="background" v-else :style="{ 'background-image': 'url(' + background_image + ')' }"></div>
    <header id="header">
      <h2 style="font-size: 30px; text-align: center; margin-top:2rem">{{ nickname }}님의 프로필 페이지</h2>
      <div class="container-fluid">
        <div class="row">
          <div class="col-sm d-flex justify-content-center">
            <span class="avatar">
              <el-tooltip content="프로필을 수정하시겠습니까?" effect="dark" placement="top-start">
                <a data-bs-toggle="modal" data-bs-target="#profileModal" @click="initModal">
                  <img v-if="profile_image === `${SERVER_URL}null`" src='@/assets/user-account.png' alt="">
                  <img v-else :src="profile_image" alt="">
                </a>
              </el-tooltip>
              <span>
                <button class="btn btn-primary" @click.prevent="pickRandomCountry">'오늘 떠나볼 곳은?'<span class="glyphicon glyphicon-hand-right"></span></button>
                <i style="font-size:1.5rem;" class="fas fa-plane-departure"><span>{{min_random_country}}</span></i>
              </span>
            </span>
            
          </div>
          <div class="col-sm-6 d-flex justify-content-center">
            <div class='my-5'>
              <i style="font-size:2rem; font-weight: bold;" class="el-icon-video-camera-solid px-3">대표 장르: <span v-for="g in max_reviews_genre" :key=g.id>{{g}}</span></i>
              <i style="font-size:2rem;" class="fas fa-plane-arrival px-3">대표 지역: <span v-for="g in max_reviews_country" :key=g.id>{{g}}</span></i>
            </div>
          </div>
          <div class="col-sm-3">
            
          </div>
        </div>
      </div>


      <!-- 프로필 수정 Modal -->
      <div class="modal fade" id="profileModal" tabindex="-1" aria-labelledby="profileModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title fw-bold" id="profileModalLabel">프로필 수정</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <el-form
              :model="credentials"
              :rules="rules"
              ref="form"
              style="margin: 1rem;"
            >
              <el-form-item prop="nickname" label="닉네임">
                <el-input v-model="credentials.newNickname" placeholder="닉네임을 적어주세요!" prefix-icon="fas fa-user"></el-input>
              </el-form-item>
              <el-form-item prop="profile_image" label="프로필 이미지">
                <el-input
                  @change.native='getProfileImage'
                  type="file"
                  accept="image/*"
                  v-model="credentials.newProfileImage"
                  placeholder="profile_image"
                  prefix-icon="el-icon-picture-outline"
                  class="mt-2"
                ></el-input>
              </el-form-item>
              <el-form-item prop="background_image" label="배경 이미지">
                <el-input
                  @change.native='getBackgroundImage'
                  type="file"
                  accept="image/*"
                  v-model="credentials.newBackgroundImage"
                  placeholder="background_image"
                  prefix-icon="el-icon-picture-outline"
                  class="mt-2"
                ></el-input>
              </el-form-item>
              <el-form-item>
                <el-button
                  id="profile-button"
                  type="primary"
                  native-type="submit"
                  @click.native.prevent="sendDataToServer"
                  block
                  class="mb-2"
                  data-bs-dismiss="modal"
                ><span style="color: black;">프로필 수정</span></el-button>
              </el-form-item>
            </el-form>
          </div>
        </div>
      </div>
    </header>
    <div>
      <span class="avatar">
        <el-tooltip content="티어표 확인?!" effect="dark" placement="top-start">
          <a data-bs-toggle="modal" data-bs-target="#tierModal">
            <img :src="rankImage" alt="@/assets/rank1.jpg" class="d-inline">
          </a>
        </el-tooltip>
      </span>

      <!-- 티어표 확인 Modal -->
      <div class="modal fade" id="tierModal" tabindex="-1" aria-labelledby="tierModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title fw-bold" id="tierModalLabel">유저 리뷰점수 티어표</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <img class="img-responsive" src="@/assets/rank_tiers.png" alt="here?!">
            </div>
          </div>
        </div>
      </div>

      <h4>현재: {{myTier}} -> {{nextTier}} 승급까지 {{rankPoint.remain}}pt</h4>
      <el-progress :text-inside="true" :stroke-width="30" :percentage="rankPoint.current"></el-progress>
    </div>

    <h3 style="margin-top:2rem">리뷰한 영화 장르별 대시보드</h3>
    <radar-chart
      :dataset="genres_cnt" class="genre-radar-chart"
    ></radar-chart>

    <h3 style="margin-top:2rem">리뷰한 영화 나라별 대시보드</h3>
    <radar-chart
      :dataset="countries_cnt" class="country-radar-chart"
    >
    </radar-chart>
    <p>{{review_movies[0]}}</p>
    <div class="infinite-list-wrapper" style="overflow:auto">
      <ul
        class="list"
        v-infinite-scroll="load"
        infinite-scroll-disabled="disabled">
        <!-- 유저가 작성한 리뷰 목록 스크롤링 -->
        <div class=container>
          <div class="row">
            <div class="card h-100" v-for="c in count" :key="c.id">
              <div class="card-front text-white bg-dark">
                <!-- <img :src="" alt=""> -->
              </div>
              
            </div>
          </div>

        </div>
        <!-- <li v-for="review in reviews" :key="review.id" class="list-item">{{ review.title }}</li> -->
      </ul>
      <p v-if="loading">Loading...</p>
      <p v-if="noMore">No more</p>
    </div>

  </div>
</template>

<script>
import SERVER from '@/api/server.js'
import RadarChart from '@/components/Profile/RadarChart'
import { mapActions, mapState } from 'vuex'
import swal from 'sweetalert'
import _ from 'lodash'


export default {
  name: 'ProfileInfo',
  components: {
    RadarChart,
  },
  data: function () {
    return {
      max_reviews_genre: null,
      max_reviews_country: null,
      min_random_country: '',
      rankImage: '',
      tiers: ['실버','에메랄드','골드','플레티넘','사파이어','마스터'],
      mytier: '',
      nextTier: '',
      rankPoint: {
        current: 0,
        remain: 0,
      },
      // user_reviews: {},
      // genres_cnt: {},
      SERVER_URL: SERVER.URL,
      credentials: {
        newNickname: '',
        newProfileImage: '',
        newBackgroundImage: '',
      },
      rules: {
        newNickname: [
          {
            required: true,
            message: "닉네임을 적어주세요",
            trigger: "blur"
          },
        ],
      },
      count: 0,
      loading: false,
    }
  },
  methods: {


    load () {
      this.loading = true
      setTimeout( () => {
        this.count += 1
        this.loading = false
      }, 2000)
    },
    initModal: function () {
      this.credentials.newNickname = this.nickname
      this.credentials.newProfileImage = ''
      this.credentials.newBackgroundImage = ''
    },
    getProfileImage (event) {
      this.credentials.newProfileImage = event.target.files[0] // cat.jpg file로 담김
    },
    getBackgroundImage (event) {
      this.credentials.newBackgroundImage = event.target.files[0]

    },
    sendDataToServer () {
      if (this.credentials.newNickname === '') {
        swal ('닉네임을 적어주세요.', {
          dangerMode: true,
        })
      } else if (this.credentials.newProfileImage === '') {
        swal ('프로필 이미지를 넣어주세요', {
          dangerMode: true,
        })
      } else if (this.credentials.newBackgroundImage === '') {
        swal ('배경 이미지를 넣어주세요', {
          dangerMode: true,
        })
      } else {
        const formData = new FormData()
        formData.append('nickname', this.credentials.newNickname)
        formData.append('profile_image', this.credentials.newProfileImage)
        formData.append('background_image', this.credentials.newBackgroundImage)
        formData.append('rank_point', this.rank_point)
        this.profileUpdate(formData)
      }
    },
    ...mapActions([
      'profileUpdate',
    ]),
    countMaxReviewGenres () {
      const max_cnt = _.max(Object.values(this.genres_cnt))
      const result = _.filter(_.map(this.genres_cnt, (v,k) => {
        if (v===max_cnt) return k}))
      this.max_reviews_genre = result
    },
    countMaxReviewCountries () {
      const max_cnt = _.max(Object.values(this.countries_cnt))
      const result = _.filter(_.map(this.countries_cnt, (v,k) => {
        if (v===max_cnt) return k}))
      this.max_reviews_country = result
    },
    pickRandomCountry () {
      const min_cnt = _.min(Object.values(this.countries_cnt))
      const result = _.filter(_.map(this.countries_cnt, (v,k) => {
        if (v===min_cnt) return k}))
      this.min_random_country = _.sample(result)
    },
    bindImageToRank () {
      const point = this.rank_point
      let step = 0
      if (point >= 500) {
        step = 6
      } else if (point < 500 && point >=400) {
        step = 5
      } else if (point < 400 && point >=300) {
        step = 4 
      } else if (point < 300 && point >= 200) {
        step = 3 
      } else if (point < 200 && point >= 100) {
        step = 2
      } else {
        step = 1
      }
      this.rankImage = require(`@/assets/rank${step}.jpg`)
      this.myTier = this.tiers[step-1]
      if (step === 6) {
        this.nextTier = this.tiers[step-1]
      } else {
        this.nextTier = this.tiers[step]
      }
      this.rankPoint.current = point % 100
      this.rankPoint.remain = 100 - this.rankPoint.current
    }
  },

  computed: {
    ...mapState([
      'nickname',
      'profile_image',
      'background_image',
      'rank_point',
      'userid',
      'reviews',
      'genres_cnt',
      'countries_cnt',
      'review_movies',
    ]),
    noMore () {
      return this.count >=20
    },
    disabled () {
      return this. loading || this.noMore
    },

  },

  created () {
    this.countMaxReviewGenres()
    this.countMaxReviewCountries()
    this.bindImageToRank()
  }


}
</script>

<style>
.background {
  width: 100%;
  height: 300px;
  background-repeat: no-repeat;
  background-position: center;
}
#profile_main > div > div > div > div {
  width: 70%;
}
/* .el-progress-bar {
  width: 70%;
} */

/* .background-img {
  width: 100%;
  height: 20vh;
} */

.avatar {
  border-radius: 100%;
  display: inline-block;
  margin: 0 0 0 0;
  padding: 0.5rem;
  border: solid 1px rgba(255, 255, 255, 0.25);
  background-color: rgba(255, 255, 255, 0.075);
}
#header .avatar img {
  border-radius: 100%;
  display: block;
  width: 10em;
  cursor: pointer;
  transition: 0.3s;
}
.avatar img:hover {
  filter: brightness(1.2);
  transform: translateY(1.5px) rotate(-10deg);
}
@media screen and (max-width: 1280px) {
  #header {
    padding: 0 0 1em 0;
  }
}
#header {
  padding: 0 0 0 0;
}
.modal{
opacity:1;    
}
#header > a > img {
  width: 15%;
  height: 15%;
}
.modal-open { 
  padding-right: 0px !important;
}

#profile-button {
  width: 100%;
  margin-top: 40px;
  padding: 14px 20px;
  border: none;
  cursor: pointer;
  width: 100%;
  transition: 0.5s;
  font-size: 16px;
  color: rgba(26, 28, 168, 0.82);
}

.genre-radar-chart {
  width: 30%;
  height: 30%;
}

.country-radar-chart {
  width: 30%;
  height: 30%;
}
</style>
