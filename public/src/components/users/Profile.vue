<template lang="pug">
  el-main
    div(v-if="editForm")
      el-form(ref="profileForm" :model="profileForm" label-width="120px")
        el-button(type="primary" @click="editMode") Save
        el-form-item(label="Avatar")
          el-input(type="url" v-model="profileForm.avatarUrl")
        el-form-item(label="First Name")
          el-input(type="text" v-model="profileForm.firstName")
        el-form-item(label="Surname")
          el-input(type="text" v-model="profileForm.surname")
        el-form-item(label="Phone")
          el-input(type="phone" v-model="profileForm.phone")
        el-form-item(label="Bio")
          el-input(type="textarea" v-model="profileForm.bio")
    div(v-else)
      img(:src="profileForm.avatarUrl")
      el-button(type="primary" @click="saveEdit") Edit
      p First name: 
        span {{ profileForm.firstName }}
      p Surname: 
        span {{ profileForm.surname }}
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
      profileForm: {}
    }
  },
  created () {
    this.profileForm = Object.assign({}, this.$store.getters.getProfile)
  },
  destroyed () {
    this.profileForm = Object.assign({}, this.$store.getters.getProfile)
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

