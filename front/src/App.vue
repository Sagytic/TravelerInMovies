<template>
  <div id="app">
    <div >
      <b-navbar toggleable="lg" type="dark" variant="dark">
        <b-navbar-nav>
          <b-nav-item href="#"><span style="color: rgba(140, 100, 172);">Traveler</span> <span style="color: rgba(100, 240, 160);"> In</span> Movies</b-nav-item>
        </b-navbar-nav>
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
                <b-nav-item-dropdown text="Search" right>
                  <b-dropdown-item href="#">All</b-dropdown-item>
                  <b-dropdown-item href="#">Location</b-dropdown-item>
                  <b-dropdown-item href="#">Recommend</b-dropdown-item>
                  <b-dropdown-item href="#">Genre</b-dropdown-item>
                </b-nav-item-dropdown>
                <b-nav-item-dropdown text="Account" right>
                  <b-dropdown-item href="#">Profile</b-dropdown-item>
                  <b-dropdown-item href="#">Sign Out</b-dropdown-item>
                </b-nav-item-dropdown>
          </b-navbar-nav>
      </b-navbar>
    </div>

    <!-- 로그인이 되었을 때 물리적인 렌더링도 변경 -->
    <router-view @login="isLogin=true"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
      // 로그아웃하며 토큰 삭제
    }
  },
  created: function () {
    // 로그인하며 토큰 저장
    const token = localStorage.getItem('jwt')

    if (token) {
      this.isLogin = true
    }
  }
}
</script>


<style>
</style>
