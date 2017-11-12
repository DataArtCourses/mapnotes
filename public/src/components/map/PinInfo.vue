<template lang="pug">
  el-aside(width="450px" style="background-color: rgb(238, 241, 246)" v-if="this.$route.params.pin_id")
    h1 Pin Info: {{ getPinInfo.pinInfo }}
    el-carousel(height="150px" trigger="click")
      el-carousel-item(v-for="item in getPinGallery.slice(0,3)" :key="item.photoId")
        a(@click="dialogGalleryVisible = true")
          img(:src="item.photoUrl")
    span Photos: {{ getPinGallery.length }} 
    span Comments: {{ getPinComments.length }}
    el-main.scroll
      ul.comments
        li(v-for="comment in getPinComments" :key="comment.author.userId")
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
        button(@click="") Send
    el-dialog(title="Photos Gallery" width="90%" top="1vh" :visible.sync="dialogGalleryVisible" v-if="dialogGalleryVisible")
      el-main
        el-row(:gutter="20")
          el-col(:span="4" v-for="item in getPinGallery" :key="item.photoId")
            el-card(:body-style="{ padding: '0px' }")
              a(@click="")
                img(:src="item.photoUrl" width="200px")
      

</template>
<script>
import { mapGetters } from 'vuex'

export default {
  data () {
    return {
      commentBody: '',
      dialogGalleryVisible: false,
      dialogPhotoVisible: false
    }
  },
  computed: {
    ...mapGetters([
      'getPinInfo',
      'getUserId',
      'getPinComments',
      'getPinGallery'
    ])
  },
  methods: {
    openGallery () {
      this.dialogGalleryVisible = !this.dialogGalleryVisible
    }
  },
  created () {
    this.$store.dispatch('recivePinInfo', +this.$route.params.pin_id)
  }
}
</script>

<style lang="scss" scoped>
.comments {
  list-style-type: none;
}
.scroll {
  height: 300px;
  overflow-y: scroll;
}
.circle {
    border-radius: 40px;
  }
</style>

