<template>
  <section>
    <b-button @click="gotoAdd" :type="Main" >Add WO</b-button>
    <b-button @click="gotoView" :type="List">View WOs</b-button>
    <b-switch :rounded="false"
      :outlined="false"
      size="is-large"
      v-model="workorderSwitch"
      @input="changeWorkorderType"
    >{{ workorderType }}</b-switch>
    <p>&nbsp;</p>
  </section>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Navbar',
  data () {
    return {
      workorderSwitch: false
    }
  },
  computed: {
    ...mapGetters([
      'userId'
    ]),
    Main () {
      return (this.$route.name === 'MainPage' ? 'is-primary' : '')
    },
    List () {
      return (this.$route.name === 'ListPage' ? 'is-primary' : '')
    },
    workorderType () {
      return (this.userId === 1 ? 'Recreational' : 'Commercial')
    }
  },
  methods: {
    gotoView () {
      if (this.$route.name !== 'ListPage') {
        this.$router.push({ name: 'ListPage' })
      }
    },
    gotoAdd () {
      if (this.$route.name !== 'MainPage') {
        this.$router.push({ name: 'MainPage' })
      }
    },
    changeWorkorderType () {
      this.$store.dispatch('saveUserId', (this.workorderSwitch ? 2 : 1))
    }
  },
  created () {
    this.$store.dispatch('loadUserId')
      .then(() => {
        this.workorderSwitch = (this.userId === 2)
      })
  }
}
</script>

<style>
</style>
