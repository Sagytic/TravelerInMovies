<template>
  <div id='home'>
    <!-- logo -->
    <!-- nav -->

    <!-- bg you/tube 영상이 클릭되지 투명 벽 생성 -->
    <div id='wall' style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; opacity: 0;"></div>
    <!-- autoplay / fullscreen / prevent touch / autoplay=1&mute=1 -> autoplay ex&chrome--> <!-- {{ videoUrl }} -->
    <iframe width="1920" height="1080" :src="newVid" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <!-- carousel -->
      <!-- v-for 변환 -->
      <!-- <div id="example">
        <carousel-3d :autoplay="true" :autoplay-timeout="5000" :display="5">
          <slide v-for="(slide, i) in slides" :index="i">
            <span class="title">You know</span>
            <p>You know, being a test pilot isn't always the healthiest business in the world.</p>
          </slide>
        </carousel-3d>
      </div> -->
      <!-- carousel poster -->
    <div id="carousel">
      <carousel-3d :width="150" :height="200" :display="10">
        <slide :index="0">
          <img src="https://i.ytimg.com/vi/gC37e02iu4M/movieposter_en.jpg" alt="" @click="changeSpain">
        </slide>
        <slide :index="1">
          <img src="https:/upload.wikimedia.org/wikipedia/ko/1/12/La_la_land.jpg" alt="" @click="changeBGVideo">
        </slide>
        <slide :index="2">
          <img src="https://upload.wikimedia.org/wikipedia/ko/thumb/a/a3/%EA%B7%B8%EB%85%80_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg/220px-%EA%B7%B8%EB%85%80_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg" alt="" @click="changeSpain">
        </slide>
        <slide :index="3">
          <img src="https://img2.yna.co.kr/etc/inner/KR/2020/01/10/AKR20200110125500005_01_i_P2.jpg" alt="" @click="changeBGVideo">
        </slide>
        <slide :index="4">
          <img src="http://t1.daumcdn.net/movie/e29bd40296d944288046b02dded779d41548118641846" alt="" @click="changeSpain">
        </slide>
        <slide :index="5">
          <img src="https://w.namu.la/s/476e0d65087f23733229076eb3a481c0a4e85287b0f73e895c7ce77d888953762c122896452700c7244697a8027b0a8b958bf220fc1015f9bd742b86e789a96fa6249cb376f12ad520b2ac11c4b855fdac17c8f75ef1bf5bac8297b1c81e9b94" alt="" @click="changeBGVideo">
        </slide>
        <slide :index="6">
          <img src="https://img1.daumcdn.net/thumb/C300x430/?fname=https%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Fd0235b8e9c0048e4301f8c9c74da929863e33456" alt="" @click="changeSpain">
        </slide>
        <slide :index="7">
          <img src="https://img1.daumcdn.net/thumb/C300x430/?fname=https%3A%2F%2Ft1.daumcdn.net%2Fmovie%2Fd0643e2cd42252fb6d9018173e867fcd9612c115" alt="" @click="changeBGVideo">
        </slide>
        <slide :index="8">
          <img src="https://youthassembly.or.kr/data/file/B62/thumb-3529829945_EwfyvjSH_8bbee4aeaee03b1a83a72b13f90c52c6bd0df789_805x1153.jpg" alt="" @click="changeSpain">
        </slide>
      </carousel-3d>
    </div>
    <!-- Detail Card -->
    <!-- show 태그 사용해서 처음에는 안 보이고, 포스터 클릭시 메소드 호출해서 videoURL 바꾸면서 id 넘기고 그 id 기반으로 세부내용/리뷰 출력 -->
    <div id="detailCard">
      <div class="scene scene--card">
        <div
          class="card"
          @click="cardOne == 'start' ? (cardOne = 'flipped' ) : (cardOne = 'start' )"
          v-bind:class="{ flipme: cardOne == 'flipped' }"
          style="border-radius: 5%;"
        >
          <div class="card__face card__face--front" >포스터 + 평점 + 짧은 overview</div>
          <div class="card__face card__face--back">유저 리뷰 + 리뷰 작성하러 가기</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Carousel3d, Slide } from 'vue-carousel-3d';

export default {
  name: 'home',
  data: function () {
    return {
      videoUrl: null,
      cardOne: "start",
    }
  },
  components: {
    Carousel3d,
    Slide
  },
  methods: {
    changeBGVideo: function () {
      // 선택한 영화의 도시 선택
      // const country = 'xxx'
      // videoUrl을 해당 도시에 매칭
      const autoPlay = 'autoplay=1&mute=1'
      const hideBar = '&modestbranding=1&autohide=1&showinfo=0&controls=0'
      this.videoUrl = 'https://www.youtube.com/embed/pMxgov6_5TA?'+ autoPlay + hideBar
    },
    changeSpain: function () {
      this.videoUrl = 'https://www.youtube.com/embed/0FXJUP6_O1w?'+'autoplay=1&mute=1'+'&modestbranding=1&autohide=1&showinfo=0&controls=0'
    },
    onSlideStart() {
        this.sliding = true
    },
    onSlideEnd() {
        this.sliding = false
    },
    logout: function (event) {
      console.log(event)
    }
  },
  computed: {
    newVid: function () {
      console.log(this.videoUrl)
      return this.videoUrl
    }
  },
  created: function () {
    this.videoUrl = 'https://www.youtube.com/embed/pMxgov6_5TA?autoplay=1&mute=1&modestbranding=1&autohide=1&showinfo=0&controls=0'
    console.log(this.videoUrl)
  }
}
  
</script>

<style>
#home > iframe {
  z-index: -2;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0.7;
}

#wall {
   z-index: -1;
}

#carousel {
  position: fixed;
  bottom: 0px;
  width: 100%;
  display: flex;
  justify-content: center;
}
/* flip card */
.scene {
  width: 100%;
  height: 550px;
  margin: 40px 0;
  perspective: 600px;

}

.card {
  width: 100%;
  height: 100%;
  transition: transform 0.8s;
  transform-style: preserve-3d;
  cursor: pointer;
  position: relative;
}

.card__face {
  border-radius: 5%;
  position: absolute;
  width: 100%;
  height: 100%;
  line-height: 260px;
  color: white;
  text-align: center;
  font-weight: bold;
  font-size: 10px;
  backface-visibility: hidden;
}

.card__face--front {
  background: rgb(219, 86, 77);
}

.card__face--back {
  background: rgb(89, 23, 115);
  transform: rotateY(180deg);
}

/* this style is applied when the card is clicked */
.flipme {
  transform: rotateY(180deg);
}

#detailCard {
  margin: auto;
  width: 50%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
/* end of flip card */

</style>