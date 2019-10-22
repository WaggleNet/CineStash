<template lang="pug">
b-container
  b-modal(
    v-model='modal.open'
    :title='"Editing Project " + modal.data._id'
    @ok='handleSubmitProject'
    @cancel='handleCancel'
    )
      h5 Project Name
      b-form-input(v-model='modal.data.name')
      h5 Paths
      h6 Project Path
      b-form-input(v-model='modal.data.projectPath')
      h6 Footage Ingest
      b-form-input(v-model='modal.data.ingestPath')
      h6 Transcoded Footage
      b-form-input(v-model='modal.data.transcodedPath')
  br
  b-row
    b-col(:cols='12')
      b-button(variant='primary' @click='handleNewProject') New Project
  b-row
    .project(v-for='i in projects')
      .project-thumbnail
        fa-icon(icon='film')
      .project-metadata
        h3 {{i.name}}
        p
          span.project-path {{i.projectPath}}
        p
          | Ingest path:
          span.project-path {{i.ingestPath}}
        p
          | Transcoded path:
          span.project-path {{i.transcodedPath}}
      .project-actions
        b-button(variant='tool')
          fa-icon(icon='sync')
          | Synchronize
        b-button(variant='tool' @click='handleOpenProject(i._id)')
          fa-icon(icon='edit')
          | Open
        b-button(variant='tool')
          fa-icon(icon='trash')
          | Delete
</template>

<style lang="sass" scoped>
.project
  width: 100%
  margin-top: 20px
  display: flex
  .project-thumbnail
    width: 160px
    height: 90px
    svg
      width: 100%
      height: 100%
  .project-metadata
    margin: 0 10px
    flex-grow: 1
    h3
      margin-bottom: 0
      font-size: 18px
    p
      font-size: 14px
      margin-bottom: 0
    span.project-path
      margin-left: 5px
      color: #777
  .project-actions
    max-width: 180px
    flex-grow: 0

</style>

<script>
const sampleProjects = [{
    projectPath: '',
    ingestPath: '',
    transcodedPath: '',
    name: 'WaggleNetNet Showoff',
    _id: '123123'
  }]
export default {
  data: () => ({
    projects: [],
    modal: {
      open: false,
      data: {}
    }
  }),
  methods: {
    handleOpenProject(id) {
      this.$router.push({name: 'project', params: {id}})
    },
    handleDeleteProject(id) {

    },
    handleNewProject() {
      this.$data.modal.data = {
        name: '',
        projectPath: '',
        ingestPath: '',
        transcodedPath: '',
        _id: ''
      }
      this.$data.modal.open = true
    },
    handleEditProject(id) {

    },
    handleLoadProjects(id) {
      this.$data.projects = sampleProjects
    },
    handleSubmitProject() {

    },
    handleCancel() {

    }
  },
  created () {
    this.handleLoadProjects()
  }
}
</script>

