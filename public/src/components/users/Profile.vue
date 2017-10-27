<template lang="pug">
  div
    el-button(type="primary" @click="editMode") Edit
    div(v-if="editForm")
      el-form(ref="profileForm" :model="profileForm" label-width="120px")
        el-form-item(label="Avatar")
          el-input(type="url" v-model="profileForm.avatar_url")
        el-form-item(label="First Name")
          el-input(type="text" v-model="profileForm.firstName")
        el-form-item(label="Last Name")
          el-input(type="text" v-model="profileForm.lastName")
        el-form-item(label="Phone")
          el-input(type="phone" v-model="profileForm.phone")
        el-form-item(label="Bio")
          el-input(type="textarea" v-model="profileForm.bio")
        el-button(type="primary" @click="saveEdit") Save
    div(v-else)
      img(:src="profileForm.avatar_url")
      p First name:
        span {{ profileForm.first }}
      p Last name:
        span {{ profileForm.second }}
      p Phone:
        span {{ profileForm.phone }}
      p Info:
        span {{ profileForm.bio }}
      
</template>
<script>
export default {
  data () {
    return {
      editForm: false,
      profileForm: {
        firstName: '',
        lastName: '',
        phone: '',
        bio: '',
        avatar_url: 'http://dsi-vd.github.io/patternlab-vd/images/fpo_avatar.png'
      }
    }
  },
  methods: {
    editMode () {
      this.editForm = !this.editForm
    },
    saveEdit () {
      this.editForm = !this.editForm
    }
  }
}
</script>

