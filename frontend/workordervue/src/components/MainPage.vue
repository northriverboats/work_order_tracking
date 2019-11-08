<template>
  <section>
    <b-field>
      <b-upload
        v-model="dropFiles"
        native multiple
        drag-drop
        @input="submitFile"
      >
        <section class="section">
          <div class="content has-text-centered">
            <p>
              <b-icon
                icon="upload"
                size="is-large">
              </b-icon>
            </p>
            <p>Drop your Work Order here or click to upload</p>
          </div>
        </section>
      </b-upload>
    </b-field>

    <b-message title="Status" :closable=false>
      <span style="white-space: pre;">{{ status }}</span>
    </b-message>
  </section>
</template>

<script>
export default {
  name: 'MainPage',
  data () {
    return {
      dropFiles: [],
      polling: null,
      pollCount: 0,
      job: '',
      status: '',
      statusOld: ''
    }
  },
  methods: {
    pollingTimer () {
      this.axios
        .post('file/status', {'job': this.job})
        .then((response) => {
          var stat = response.data.status
          if (this.statusOld !== stat) {
            this.status += stat + '\n'
            this.statusOld = stat
          }
          this.pollCount += 1
          if (stat === 'Done' || this.pollCount > 240) {
            clearInterval(this.polling)
          }
        })
    },
    submitFile (file) {
      this.status = ''
      this.statusOld = ''
      this.pollingCount = 0
      console.log(file[0]['name'])
      this.axios
        .post('file', {'name': file[0]['name']})
        .then((response) => {
          this.job = response.data.job
          this.polling = setInterval(this.pollingTimer, 100)
        })
    }
  },
  beforeDestroy () {
    clearInterval(this.polling)
  }
}
</script>

<style>
</style>
