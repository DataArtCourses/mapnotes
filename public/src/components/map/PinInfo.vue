<template lang="pug">
  el-aside(width="450px" style="background-color: rgb(238, 241, 246)" v-if="this.$route.params.pin_id && getPinInfo.comments")
    h1 Pin Info: {{ getPinInfo.pinInfo }}
    el-carousel(height="150px" trigger="click")
      el-carousel-item(v-for="item in getPinInfo.hover" :key="item")
        a(@click="getPhotos")
          img(:src="item")
    span Photos: {{ getPinInfo.totalPhotos }} 
    el-button(type="primary" @click="dialogAddPhoto=true") Add photo
      i(class="el-icon-upload el-icon-right")
    span Comments: {{ getPinInfo.comments.length }}
    el-main
      ul.comments
        li(v-for="comment in pinComments" :key="comment.author.userId")
          router-link(:to="`/profile/${comment.author.userId}`")
            img.circle(:src="comment.author.avatarUrl" width="40px")
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
        el-input(type="textarea" :rows="2" v-model="commentBody"  @keyup.enter="sendComment" placeholder="Enter text...")
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
            img.circle(:src="photo.author.avatarUrl" width="40px")
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
            li(v-for="comment in photo.comments" :key="comment.author.userId")
              router-link(:to="`/profile/${comment.author.userId}`")
                img.circle(:src="comment.author.avatarUrl" width="40px")
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
            el-input(type="textarea" :rows="2" v-model="commentBody"  @keyup.enter="" placeholder="Enter text...")
            el-button(@click="sendComment") Send
    el-dialog(title="Comments" width="90%" top="1vh" :visible.sync="dialogCommentsVisible" v-if="dialogCommentsVisible")
      el-main
        ul.comments
        li(v-for="comment in getPinInfo.comments" :key="comment.author.userId")
          router-link(:to="`/profile/${comment.author.userId}`")
            img.circle(:src="comment.author.avatarUrl" width="40px")
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
          el-input(type="textarea" :rows="2" v-model="commentBody"  @keyup.enter="sendComment" placeholder="Enter text...")
          el-button(@click="sendComment") Send
    el-dialog(title="Add photo" width="50%" top="40vh" :visible.sync="dialogAddPhoto" v-if="dialogAddPhoto")
      el-form
        el-form-item(lable="Photo Url" prop="url")
          el-input(v-model="photoUrl")
        el-form-item(lable="Photo Info" prop="info")
          el-input(v-model="photoInfo" type="textarea")
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
      return this.getPinInfo.comments.sort((a, b) => Date.parse(b.created) - Date.parse(a.created)).slice(0, 3)
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
      this.$store.dispatch('recivePinPhotos', +this.$route.params.pin_id)
      this.dialogGalleryVisible = true
    },
    sendComment () {
      if (this.commentBody) {
        let comment = {
          commentBody: this.commentBody,
          created: new Date(),
          author: this.$store.getters.getUserInfo,
          likes: 0,
          liked: false,
          photoId: this.photoId
        }
        this.$store.dispatch('sendComment', { comment: comment, pin_id: +this.$route.params.pin_id })
        this.commentBody = ''
      }
    },
    sendPhoto () {
      if (this.photoUrl && this.photoInfo) {
        let info = {
          comments: [],
          likes: 0,
          liked: false,
          created: new Date(),
          author: this.$store.getters.getUserInfo,
          photoUrl: this.photoUrl,
          photoInfo: this.photoInfo,
          photoId: this.getPinGallery.length + 1
        }
        this.$store.dispatch('sendPhoto', { photoInfo: info, pin_id: +this.$route.params.pin_id })
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

