<template lang="pug">
b-container
  b-row
    .project
      .project-thumbnail
        fa-icon(icon='film')
      .project-metadata
        h3 WaggleNetNet Showoff
        p
          span.project-path /work/Cinesquad/123
        p
          | Ingest path:
          span.project-path /work/Cinesquad/raw/wnnrover
        p
          | Transcoded path:
          span.project-path /work/Cinesquad/wnnrover
      .project-actions
        b-button(variant='tool')
          fa-icon(icon='sync')
          | Synchronize
        b-button(variant='tool' @click='handleOpenProject("123")')
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
export default {
  data: () => ({
    'projects': {}
  }),
  methods: {
    handleOpenProject(id) {
      this.$router.push({name: 'project', params: {id}})
    }
  }
}
</script>

