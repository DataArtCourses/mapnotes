<template lang="pug">
  el-aside(width="450px" style="background-color: rgb(238, 241, 246)" v-if="this.$route.params.pin_id")
    h1 Pin Info: {{ getPinInfo.pinInfo }}
    el-carousel(height="150px" trigger="click")
      el-carousel-item(v-for="item in getPinInfo.hover" :key="item.photoId")
        a(@click="getPhotos")
          img(:src="item.photoUrl")
    span Photos: {{ getPinInfo.totalPhotos }} 
    el-button(type="primary" @click="dialogAddPhoto=true") Add photo
      i(class="el-icon-upload el-icon-right")
    span Comments: {{ getPinInfo.totalComments }}
    el-main
      ul.comments
        li(v-for="(comment, index) in pinComments" :key="index")
          router-link(:to="`/profile/${comment.author.userId}`")
            img.circle(:src="comment.author.avatarUrl ||'http://dsi-vd.github.io/patternlab-vd/images/fpo_avatar.png'" width="40px")
            span {{ comment.author.userName }} 
          el-button(type="text" v-if="comment.author.userId === getUserId")
            i(class="el-icon-edit")
          el-button(type="text" v-if="comment.author.userId === getUserId")
            i(class="el-icon-delete")
          p {{ comment.commentBody }}
          time
            small {{ Date.parse(comment.created) | moment("calendar") }}  
          span Likes: {{ comment.likes }}  
          a(@click="" v-if='comment.liked') Unlike
          a(@click="" v-else) Like
      el-button(type="text" @click="dialogCommentsVisible = true") All comments
    el-footer
        el-input(type="textarea" :rows="2" v-model.trim="commentBody"  @keyup.enter="sendComment" placeholder="Enter text...")
        el-button(@click="sendComment") Send
    el-dialog(title="Photos Gallery" width="90%" top="1vh" :visible.sync="dialogGalleryVisible" v-if="dialogGalleryVisible")
      el-header
        el-button(type="primary" @click="dialogAddPhoto=true") Add photo
          i(class="el-icon-upload el-icon-right")
      el-main
        el-row(:gutter="20")
          el-col(:span="4" v-for="item in getPinGallery" :key="item.photoId")
            el-card(:body-style="{ padding: '0px' }")
              a(@click="getPhoto(item.photoId)")
                img(:src="item.photoUrl" width="200px")
    el-dialog(title="Photo" width="80%" top="2vh" :visible.sync="dialogPhotoVisible" v-if="dialogPhotoVisible")
      el-main
        el-card(:body-style="{ padding: '0px' }")
          img(:src="photo.photoUrl")
          br
          router-link(:to="`/profile/${photo.author.userId}`")
            img.circle(:src="photo.author.avatarUrl || 'http://dsi-vd.github.io/patternlab-vd/images/fpo_avatar.png'" width="40px")
            span {{ photo.author.userName }}    
          span Likes: {{ photo.likes }}    
          a(@click="" v-if='photo.liked') Unlike   
          a(@click="" v-else) Like   
          time
            small {{ Date.parse(photo.created) | moment("calendar") }}
          el-button(type="text" v-if="photo.author.userId === getUserId")
            i(class="el-icon-delete")
          br
          span {{ photo.photoInfo }}
        el-card
          span Comments
          ul.comments.scroll
            li(v-for="(comment, index) in photo.comments" :key="index")
              router-link(:to="`/profile/${comment.author.userId}`")
                img.circle(:src="comment.author.avatarUrl || 'http://dsi-vd.github.io/patternlab-vd/images/fpo_avatar.png'" width="40px")
                span {{ comment.author.userName }} 
              el-button(type="text" v-if="comment.author.userId === getUserId")
                i(class="el-icon-edit")
              el-button(type="text" v-if="comment.author.userId === getUserId")
                i(class="el-icon-delete")
              p {{ comment.commentBody }}
              time
                small {{ Date.parse(comment.created) | moment("calendar") }}  
              span Likes: {{ comment.likes }}  
              a(@click="" v-if='comment.liked') Unlike
              a(@click="" v-else) Like
        el-footer
            el-input(type="textarea" :rows="2" v-model.trim="commentBody"  @keyup.enter="" placeholder="Enter text...")
            el-button(@click="sendComment") Send
    el-dialog(title="Comments" width="90%" top="1vh" :visible.sync="dialogCommentsVisible" v-if="dialogCommentsVisible")
      el-main
        ul.comments
        li(v-for="(comment, index) in getPinInfo.comments" :key="index")
          router-link(:to="`/profile/${comment.author.userId}`")
            img.circle(:src="comment.author.avatarUrl || 'http://dsi-vd.github.io/patternlab-vd/images/fpo_avatar.png'" width="40px")
            span {{ comment.author.userName }} 
          el-button(type="text" v-if="comment.author.userId === getUserId")
            i(class="el-icon-edit")
          el-button(type="text" v-if="comment.author.userId === getUserId")
            i(class="el-icon-delete")
          p {{ comment.commentBody }}
          time
            small {{ Date.parse(comment.created) | moment("calendar") }}  
          span Likes: {{ comment.likes }}  
          a(@click="" v-if='comment.liked') Unlike
          a(@click="" v-else) Like
        el-footer
          el-input(type="textarea" :rows="2" v-model.trim="commentBody"  @keyup.enter="sendComment" placeholder="Enter text...")
          el-button(@click="sendComment") Send
    el-dialog(title="Add photo" width="50%" top="40vh" :visible.sync="dialogAddPhoto" v-if="dialogAddPhoto")
      el-form
        el-form-item(lable="Photo Url" prop="url")
          el-input(v-model.trim="photoUrl")
        el-form-item(lable="Photo Info" prop="info")
          el-input(v-model.trim="photoInfo" type="textarea")
        el-form-item
          el-button(type="primary" @click="sendPhoto") Add
          el-button(type="default" @click="dialogAddPhoto = false; photoUrl = ''") Cansel
</template>
<script>
import { mapGetters } from 'vuex'

export default {
  data () {
    return {
      commentBody: '',
      dialogCommentsVisible: false,
      dialogGalleryVisible: false,
      dialogPhotoVisible: false,
      dialogAddPhoto: false,
      photoId: 0,
      photoUrl: '',
      photoInfo: ''
    }
  },
  computed: {
    ...mapGetters([
      'getPinInfo',
      'getUserId',
      'getPinGallery',
      'getPhotoInfo'
    ]),
    photo () {
      return this.getPhotoInfo
    },
    pinComments () {
      if (this.getPinInfo && this.getPinInfo.comments) {
        return this.getPinInfo.comments.slice(0, 3)
      }
    },
    changeId () {
      if (!this.dialogPhotoVisible) {
        this.photoId = 0
      }
    }
  },
  methods: {
    getPhoto (event) {
      this.photoId = event
      this.$store.dispatch('recivePhotoInfo', event)
      this.dialogPhotoVisible = true
    },
    getPhotos () {
      this.dialogGalleryVisible = true
    },
    sendComment () {
      if (this.commentBody) {
        let comment = {
          commentBody: this.commentBody,
          author: {
            userId: this.$store.getters.getUserId,
            avatarUrl: this.$store.getters.getProfile.avatar_url,
            userName: this.$store.getters.getProfile.first_name + ' ' + this.$store.getters.getProfile.last_name
          },
          likes: 0,
          liked: false,
          photoId: this.photoId
        }
        this.$nextTick(() => {
          this.$store.dispatch('sendComment', { comment: comment, pin_id: +this.$route.params.pin_id })
          this.commentBody = ''
        })
      }
    },
    sendPhoto () {
      if (this.photoUrl && this.photoInfo) {
        this.$store.dispatch('sendPhoto', {
          photo_url: this.photoUrl,
          photo_info: this.photoInfo,
          pin_id: +this.$route.params.pin_id
        })
        this.photoUrl = ''
        this.photoInfo = ''
        this.dialogAddPhoto = false
      }
    }
  },
  beforeCreate () {
    this.$store.dispatch('recivePinInfo', +this.$route.params.pin_id)
  }
}
</script>

<style lang="scss" scoped>
.comments {
  list-style-type: none;
}
.scroll {
  height: 600px;
  overflow-y: scroll;
}
.circle {
    border-radius: 40px;
  }
</style>

