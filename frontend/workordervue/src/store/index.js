import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import VueAxios from 'vue-axios'

/* eslint no-undef: "error" */
axios.defaults.baseURL = 'https://owncloud.northriverboats.com/workorder/api/'

Vue.use(Vuex)
Vue.use(VueAxios, axios)

export default new Vuex.Store({
  state: {
    debug: true,
    loadCount: 0
  },
  getters: {
    debug: state => state.debug,
    isLoading: state => state.loadCount
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
    }
  }
})
