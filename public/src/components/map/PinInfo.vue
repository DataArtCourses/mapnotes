<template lang="pug">
  el-aside(width="450px" style="background-color: rgb(238, 241, 246)" v-if="this.$route.params.pin_id && getPinInfo.comments")
    h1 Pin Info: {{ getPinInfo.pinInfo }}
    el-carousel(height="150px" trigger="click")
      el-carousel-item(v-for="item in getPinInfo.hover" :key="item")
        a(@click="getPhotos")
          img(:src="item")
    span Photos: {{ getPinInfo.totalPhotos }} 
    span Comments: {{ getPinInfo.comments.length }}
    el-main
      ul.comments
        li(v-for="comment in getPinInfo.comments.slice(0, 3)" :key="comment.author.userId")
          router-link(:to="`/profile/${comment.author.userId}`")
            img.circle(:src="comment.author.avatarUrl" width="40px")
            span {{ comment.author.userName }} 
          el-button(type="text" v-if="comment.author.userId === getUserId")
            i(class="el-icon-edit")
          el-button(type="text" v-if="comment.author.userId === getUserId")
            i(class="el-icon-delete")
          p {{ comment.commentBody }}
          time
            small {{ Date.parse(comment.time) | moment("from", "now", true) }}  
          span Likes: {{ comment.likes }}  
          a(@click="" v-if='comment.liked') Unlike
          a(@click="" v-else) Like
      el-button(type="text" @click="dialogCommentsVisible = true") All comments
    el-footer
        textarea(rows="2" cols="40" v-model="commentBody"  @keyup.enter="" placeholder="Enter text...")
        el-button(@click="") Send
    
    el-dialog(title="Photos Gallery" width="90%" top="1vh" :visible.sync="dialogGalleryVisible" v-if="dialogGalleryVisible")
      el-main
        el-row(:gutter="20")
          el-col(:span="4" v-for="item in getPinGallery" :key="item.photoId")
            el-card(:body-style="{ padding: '0px' }")
              a(@click="getPhoto(item.photoId)")
                img(:src="item.photoUrl" width="200px")
    el-dialog(title="Photo" width="80%" top="2vh" :visible.sync="dialogPhotoVisible" v-if="dialogPhotoVisible")
      el-main.scroll
        img(:src="photo.photoUrl")
        ul.comments
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
            small {{ Date.parse(comment.time) | moment("from", "now", true) }}  
          span Likes: {{ comment.likes }}  
          a(@click="" v-if='comment.liked') Unlike
          a(@click="" v-else) Like
      el-footer
          textarea(rows="2" cols="40" v-model="commentBody"  @keyup.enter="" placeholder="Enter text...")
          el-button(@click="") Send
    el-dialog(title="Comments" width="90%" top="1vh" :visible.sync="dialogCommentsVisible" v-if="dialogCommentsVisible")
      el-main.scroll
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
            small {{ Date.parse(comment.time) | moment("from", "now", true) }}  
          span Likes: {{ comment.likes }}  
          a(@click="" v-if='comment.liked') Unlike
          a(@click="" v-else) Like
      el-footer
          textarea(rows="2" cols="40" v-model="commentBody"  @keyup.enter="" placeholder="Enter text...")
          el-button(@click="") Send
      

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
      photoId: 0
    }
  },
  computed: {
    ...mapGetters([
      'getPinInfo',
      'getUserId',
      'getPinGallery'
    ]),
    photo () {
      return this.getPinGallery.filter(data => data.photoId === this.photoId)[0]
    }
  },
  methods: {
    getPhoto (event) {
      this.photoId = event
      this.dialogPhotoVisible = true
    },
    getPhotos () {
      this.$store.dispatch('recivePinPhotos', +this.$route.params.pin_id)
      this.dialogGalleryVisible = true
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

