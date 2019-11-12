<template>
  <section>
    <b-table :data="workorders" :columns="columns"></b-table>
  </section>
</template>

<script>
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
  methods: {
  },
  created () {
    this.axios
      .get('workorders')
      .then((response) => {
        this.workorders = response.data.workorders
      })
  }
}
</script>

<style>
</style>
