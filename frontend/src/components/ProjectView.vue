<template lang="pug">
b-container(fluid style='height: 100%')
  b-row(style='height: 100%')
    b-col(:cols="2").noborder.scroll-col
      b-list-group
        b-list-group-item(v-for='scene in scenes').selector
          h3 {{scene.number}}
          p {{scene.name}}
    b-col(:cols="3").noborder.scroll-col.splitter
      b-list-group
        b-list-group-item(v-for='shot in selectedScene.shots').selector
          h3 {{shot.number}}
            small {{shot.angle}}
          p {{shot.notes}}
    b-col(:cols="7" style='padding: 15px').scroll-col
      .stat-view
        .stat-cell
          h5 Shot
          p {{selectedScene.number}} - {{selectedShot.number}}
        .stat-cell
          h5 Angle
          p {{selectedShot.angle}}
        .stat-cell
          h5 Shot ID
          p {{selectedShot._id}}
      .note
        p {{selectedShot.notes}}
      .note
        h3 Storyboards
        .image-list(v-viewer)
          img(src='https://image.shutterstock.com/image-photo/mountains-during-sunset-beautiful-natural-260nw-407021107.jpg')
          img(src='https://image.shutterstock.com/image-photo/mountains-during-sunset-beautiful-natural-260nw-407021107.jpg')
      .note
        h3 Dialogue
        pre {{selectedShot.dialogue}}
      .note
        h3 Action
        pre {{selectedShot.action}}
      .note
        h3 Takes
        .take-list
          .take
            .take-thumbnail
              fa-icon(icon='plus')
            .take-big-actions
              h3 New shot
          .take
            .take-thumbnail
              img(src='https://image.shutterstock.com/image-photo/mountains-during-sunset-beautiful-natural-260nw-407021107.jpg')
            .take-metadata
              h3 Take 1
                b-badge(variant='danger') NG
                b-badge(variant='primary') Virtual
              p Cam: 1
              p TC 00:46:21:05
            .take-actions
              b-button(variant='tool')
                fa-icon(icon='sync')
                | Synchronize
              b-button(variant='tool')
                fa-icon(icon='edit')
                | Edit
              b-button(variant='tool')
                fa-icon(icon='trash')
                | Delete


</template>

<style lang="sass" scoped>
@import '@/wagglenet-theme.scss'
.stat-view
  display: flex
  width: 100%
  .stat-cell
    display: block
    flex-grow: 1
    h5
      text-transform: uppercase
      color: #999
      margin-bottom: 0
    p
      font-size: 36px

.image-list
  width: 100%
  overflow-x: auto
  img
    display: inline-block
    height: 160px
    width: auto
    margin-right: 20px
    cursor: pointer

.take
  display: flex
  margin-bottom: 10px
  padding: 10px
  &:hover
    background-color: $bg-color-highlight
  .take-thumbnail
    margin-right: 10px
    flex-grow: 0
    height: 90px
    width: 160px
    img
      height: 100%
      width: 100%
    svg
      font-size: 24px
      text-align: center
      width: 100%
      height: 100%
      padding: 10%
      vertical-align: middle
  .take-metadata
    display: block
    flex-grow: 1
    h3
      font-size: 22px
      span.badge
        margin-left: 5px
    p
      margin-bottom: 0
      margin-top: 5px
  .take-actions
    flex-grow: 0
    max-width: 180px
  .take-big-actions
    flex-grow: 1
    h3
      font-size: 20px
      padding-top: 30px
      padding-bottom: 10px
      white-space: nowrap
      vertical-align: top


.noborder
  padding-left: 0
  padding-right: 0

.scroll-col
  height: 100%
  overflow-y: auto

.splitter
  border-left: 1px solid rgba(0, 0, 0, 0.125);
  border-right: 1px solid rgba(0, 0, 0, 0.125);

.btn svg
  margin-right: 5px

.btn.btn-tool
  &:hover
    background-color: #333
  color: $text-color

.list-group
  border-radius: 0
  .list-group-item
    border-right: none
    border-left: none
    border-radius: 0
    padding: 10px 10px
    h3
      font-size: 24px
    h3 small
      color: #888
      margin-left: 5px
    p
      margin-bottom: 0
      font-size: 13px
</style>

<script>
import mockData from '@/test_data.json'
export default {
  data: () => ({
    scenes: mockData
  }),
  computed: {
    selectedScene () {
      return this.$data.scenes[2];
    },
    selectedShot () {
      return this.$data.scenes[2].shots[2];
    }
  }
}
</script>

