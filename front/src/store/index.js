import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    usernamei: localStorage.getItem("username")
  },
  getters: {
    getusernamei: state => {
      return state.usernamei
    }
  },
  actions: {
  },
  modules: {
  }
})
