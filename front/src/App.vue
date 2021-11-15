<template>
  <div id="app">
    <div id="nav">
      <!-- login 여부에 따라 보여주는 카테고리 설정 -->
      <span v-if="isLogin">
        <router-link :to="{ name: 'TodoList' }">Todo List</router-link> | 
        <!-- 로그아웃은 컴포넌트가 없으니까 형식적으로 to #  -->
        <router-link @click.native="logout" to="#"> 로그아웃</router-link>
        <!-- a태그에 고유한 이벤트가 없어서 click이벤트가 실행이 안 되는중. native 추가해서 클릭 이벤트가 온전히 수행될 수 있도록 -->
        <!-- router-link가 a태그 기능은 아니니까 넣어주는 거지.. -->
      </span>
      <span v-else>
        <router-link :to="{ name: 'signup' }">Signup</router-link> |
        <router-link :to="{ name: 'login' }">Login</router-link> 
      </span>
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
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
</style>
