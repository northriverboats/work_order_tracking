<template>
  <section>
    <b-field>
      <b-upload
        v-model="dropFiles"
        native multiple
        drag-drop
        @input="test"
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

    <div class="tags">
      <span v-for="(file, index) in dropFiles"
        :key="index"
        class="tag is-primary"
      >
        {{ file.name }}
        <button class="delete is-small"
          type="button"
          @click="deleteDropFile(index)"
        >
        </button>
      </span>
    </div>
  </section>
</template>

<script>
export default {
  name: 'MainPage',
  data () {
    return {
      dropFiles: []
    }
  },
  methods: {
    test (file) {
      console.log(file[0]['name'])
    },
    deleteDropFile (index) {
      this.dropFiles.splice(index, 1)
    }
  }
}
</script>

<style>
</style>
