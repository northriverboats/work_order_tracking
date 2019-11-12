import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import VueAxios from 'vue-axios'

/* eslint no-undef: "error" */
axios.defaults.baseURL = 'https://workordertracking.northriverboats.com/api/'

Vue.use(Vuex)
Vue.use(VueAxios, axios)

export default new Vuex.Store({
  state: {
    debug: true,
    loadCount: 0,
    backgroundColor: ['lightskyblue', 'lightgreen'],
    userId: 1
  },
  getters: {
    debug: state => state.debug,
    isLoading: state => state.loadCount,
    backgroundColor: state => state.backgroundColor[state.userId - 1],
    userId: state => state.userId

  },
  mutations: {
    // load screen releated
    LOADCOUNT (state, count) {
      state.loadCount = count
    },
    DECLOAD (state, count) {
      state.loadCount = Math.max(state.loadCount - count, 0)
    },
    INCLOAD (state, count) {
      state.loadCount = state.loadCount + count
    },
    SETUSERID (state, userid) {
      document.documentElement.style.backgroundColor = (userid === 1 ? 'lightskyblue' : 'lightgreen')
      state.userId = userid
    }
  },
  actions: {
    setLoadCount ({ commit, state }, count) {
      commit('LOADCOUNT', count)
    },
    decreaseLoadCount ({ commit, state }, count) {
      commit('DECLOAD', count)
    },
    increaseLoadCount ({ commit, state }, count) {
      commit('INCLOAD', count)
    },
    loadUserId ({ commit, state }) {
      var userid = 1
      if (localStorage.getItem('userid')) {
        try {
          userid = JSON.parse(localStorage.getItem('userid'))
        } catch (e) {
          localStorage.removeItem('userid')
          userid = 1
        }
      }
      commit('SETUSERID', userid)
    },
    saveUserId ({ commit, state }, userid) {
      const parsed = JSON.stringify(userid)
      localStorage.setItem('userid', parsed)
      commit('SETUSERID', userid)
    }
  }
})
