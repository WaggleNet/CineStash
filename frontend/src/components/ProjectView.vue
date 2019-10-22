<template lang="pug">
b-container(fluid style='height: 100%')
  b-modal(
    v-model='takeModal.open'
    :title='"Editing Take " + takeModal.data.takeId'
    @ok='handleTakeSubmit'
    @cancel='handleTakeCancel'
    )
      h5 Camera
      b-form-select(v-model='takeModal.data.cam' :options='{cam1: "cam1"}')
      h5 Timecode
      b-form-input(v-model='takeModal.data.timecode')
      h5 Notes
      b-form-input(v-model='takeModal.data.notes')
      h5 Other info
      .form-group
        b-button(
          pill
          :pressed='takeModal.data.meta.ng'
          variant='outline-danger'
          @click='takeModal.data.meta.ng = !takeModal.data.meta.ng'
        ) NG
        b-button(
          pill
          :pressed = 'takeModal.data.meta.mos'
          variant='outline-success'
          @click='takeModal.data.meta.mos = !takeModal.data.meta.mos'
        ) Mute
  b-row(style='height: 100%')
    b-col(:cols="2").noborder.scroll-col
      b-list-group
        b-list-group-item(
          v-for='scene, idx in scenes'
          :class='{active: idx == sceneIdx}'
          @click='sceneIdx = idx'
          ).selector
          h3 {{scene.number}}
          p {{scene.name}}
    b-col(:cols="3").noborder.scroll-col.splitter
      b-list-group
        b-list-group-item(
          v-for='shot, idx in selectedScene.shots',
          :class='{active: idx == shotIdx}'
          @click='shotIdx = idx'
          ).selector
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
          .take(@click='handleTakeCreate')
            .take-thumbnail
              fa-icon(icon='plus')
            .take-big-actions
              h3 New take
          .take(v-for='i in selectedShot.takes')
            .take-thumbnail
              img(src='https://image.shutterstock.com/image-photo/mountains-during-sunset-beautiful-natural-260nw-407021107.jpg')
            .take-metadata
              h3 Take {{i.takeId}}
                b-badge(variant='danger' v-if='i.meta.ng') NG
                b-badge(variant='primary' v-if='i.meta.virtual') Virtual
                b-badge(variant='success' v-if='i.meta.mos') Mute
              p Cam: {{i.cam}}
              p TC {{i.timecode}}
            .take-actions
              b-button(variant='tool')
                fa-icon(icon='sync')
                | Synchronize
              b-button(variant='tool' @click='handleTakeEdit(i)')
                fa-icon(icon='edit')
                | Edit
              b-button(variant='tool' @click='handleTakeDelete(i)')
                fa-icon(icon='trash')
                | Delete


</template>

<style lang="sass" scoped>
@import '@/wagglenet-theme.sass'
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
  white-space: nowrap
  img
    display: inline-block
    height: 160px
    width: auto
    margin-right: 20px
    cursor: pointer

.note
    margin-bottom: 15px

.note h3
  font-size: 22px
  text-transform: uppercase
  color: $text-color-tame

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
</style>

<script>
import mockData from '@/test_data.json'
import Vue from 'vue'
import _ from 'lodash'

const emptyTake = {
  takeId: 1,
  meta: {
    ng: false,
    virtual: true,
    mos: false
  },
  cam: '',
  timecode: '0:0:0:0'
};

export default {
  data: () => ({
    scenes: mockData,
    sceneIdx: 0,
    shotIdx: 0,
    takeModal: {
      open: false,
      data: emptyTake
    }
  }),
  computed: {
    selectedScene () {
      return this.$data.scenes[this.$data.sceneIdx]
    },
    selectedShot () {
      return this.selectedScene.shots[this.$data.shotIdx]
    }
  },
  methods: {
    handleTakeCreate () {
      // Determine the maximum take number
      let takeId = 1;
      if (!this.selectedShot.takes) {
        this.selectedShot.takes = []
      } else if (this.selectedShot.takes.length) {
        takeId = _.max(this.selectedShot.takes, 'takeId').takeId + 1
      }
      // Create the take
      const data = _.cloneDeep(emptyTake)
      data.takeId = takeId
      this.$data.takeModal.data = data
      this.$data.takeModal.open = true
    },
    handleTakeEdit (take) {
      this.$data.takeModal.data = _.cloneDeep(take)
      this.$data.takeModal.open = true
    },
    handleTakeDelete (take) {
      this.$swal({
        text: 'Really delete this scene? You cannot change it back',
        type: 'warning',
        showCancelButton: true
        }).then(res => {
        if (res.value) {
          this.selectedShot.takes = this.selectedShot.takes.filter(i => i.takeId !== take.takeId);
          this.$forceUpdate()
          console.log(this.selectedShot.takes)
        }
      })
    },
    handleTakeSubmit () {
      const take = this.$data.takeModal.data
      for (let idx = 0; idx < this.selectedShot.takes.length; idx++) {
        if (this.selectedShot.takes[idx].takeId == take.takeId) {
          this.selectedShot.takes[idx] = take
          return
        }
      }
      this.selectedShot.takes.push(take)
      this.$forceUpdate()
    },
    handleTakeCancel () {
    }
  }
}
</script>

