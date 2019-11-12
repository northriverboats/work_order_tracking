<template>
  <section>
     <section>
      <b-button @click="gotoAdd">Add WO</b-button>
      <b-button type="is-primary">View WOs</b-button>
      <p>&nbsp;</p>
    </section>
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
    gotoAdd () {
      this.$router.push({ name: 'MainPage' })
    }
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
