<template lang="pug">
  el-main
    div(v-if="editForm")
      el-form(ref="profile" :model="profile" label-width="120px")
        el-button(type="primary" @click="saveEdit") Save
        el-form-item(label="Avatar")
          el-input(type="url" v-model="profile.avatar_url")
        el-form-item(label="First Name")
          el-input(type="text" v-model="profile.first_name")
        el-form-item(label="Surname")
          el-input(type="text" v-model="profile.last_name")
        el-form-item(label="Phone")
          el-input(type="phone" v-model="profile.phone")
        el-form-item(label="Bio")
          el-input(type="textarea" v-model="profile.bio")
    div(v-else)
      img(:src="profileForm.avatar_url || 'http://dsi-vd.github.io/patternlab-vd/images/fpo_avatar.png'")
      el-button(type="primary" @click="editMode") Edit
      p First name: 
        span {{ profileForm.first_name }}
      p Surname: 
        span {{ profileForm.last_name }}
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
      profile: {
        first_name: '',
        last_name: '',
        phone: '',
        bio: '',
        avatar_url: ''
      }
    }
  },
  computed: {
    profileForm () {
      return this.$store.getters.getProfile
    }
  },
  methods: {
    editMode () {
      Object.assign(this.profile, this.$store.getters.getProfile)
      this.editForm = !this.editForm
    },
    saveEdit () {
      if (this.profileForm) this.$store.dispatch('sendProfile', this.profile)
      this.editForm = !this.editForm
    }
  }
}
</script>

