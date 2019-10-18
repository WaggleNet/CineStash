<template lang="pug">
b-container(fluid)
  b-row
    b-col(:cols="2")
      b-list-group
        b-list-group-item Scene 1
        b-list-group-item Scene 2
    b-col(:cols="3")
      b-list-group
        b-list-group-item Scene 1
        b-list-group-item Scene 2
    b-col(:cols="7")
      .stat-view
        .stat-cell
          h5 Shot
          p 1A
        .stat-cell
          h5 Angle
          p Wide
        .stat-cell
          h5 Shot ID
          p 3KZBP
      .note
        p This is a note
      .note
        h3 Storyboards
        .image-list(v-viewer)
          img(src='https://image.shutterstock.com/image-photo/mountains-during-sunset-beautiful-natural-260nw-407021107.jpg')
          img(src='https://image.shutterstock.com/image-photo/mountains-during-sunset-beautiful-natural-260nw-407021107.jpg')
      .note
        h3 Dialogue
        pre This is a dialogue.
      .note
        h3 Action
        pre Drop the camera to the ground.
      .note
        h3 Takes
        .take-list
          .take


</template>

<style lang="sass" scoped>

.image-list
  width: 100%
  overflow-x: auto
  img
    display: inline-block
    height: 160px
    width: auto
    margin-right: 20px
    cursor: pointer

</style>

<script>
export default {

}
</script>

