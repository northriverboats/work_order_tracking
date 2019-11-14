<template>
  <section>
    <b-table :data="workorders" :columns="columns"></b-table>
  </section>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'ListPage',
  data () {
    return {
      workorders: [],
      columns: [
        {
          field: 'id',
          label: 'Id',
          numeric: true
        },
        {
          field: 'hull',
          label: 'Hull'
        },
        {
          field: 'folder',
          label: 'Folder'
        },
        {
          field: 'workorder',
          label: 'Work Order'
        }
      ]
    }
  },
  computed: {
    ...mapState([
      'userId'
    ])
  },
  watch: {
    userId (newValue, oldValue) {
      this.getWorkorders(newValue)
    }
  },
  methods: {
    getWorkorders (userId) {
      this.axios
        .get('workorders/' + userId)
        .then((response) => {
          this.workorders = response.data.workorders
        })
    }
  },
  created () {
    this.getWorkorders(this.userId)
  }
}
</script>

<style>
</style>
