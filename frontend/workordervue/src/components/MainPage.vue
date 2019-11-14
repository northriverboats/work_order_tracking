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
      status: ''
    }
  },
  methods: {
    pollingTimer () {
      this.axios
        .get('file/status/' + this.job)
        .then((response) => {
          var lines = response.data.status.split('\n').slice(-20)
          if (lines[lines.length - 2] === 'Error') {
            lines[lines.length - 2] = 'Done'
          }
          this.status = lines.join('\n')
          this.pollCount += 1
          if (lines[lines.length - 2] === 'Done' || this.pollCount > 90) {
            this.job = ''
            this.pollCount = 0
            clearInterval(this.polling)
          }
        })
    },
    submitFile (file) {
      if (this.job !== '') return
      this.status = ''
      this.statusOld = ''
      this.pollingCount = 0
      this.axios
        .post('file', {'name': file[0]['name'], 'userid': this.$store.getters.userId})
        .then((response) => {
          this.job = response.data.job
          this.polling = setInterval(this.pollingTimer, 500)
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
