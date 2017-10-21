<template>
  <el-main>
    <el-row>
      <el-col :span="8" :offset="7">
        <el-form label-width="150px">
          <el-form-item prop="email" label="Email">
            <el-input type="email" id="email" placeholder="e-mail"></el-input>
          </el-form-item>
          <el-form-item prop="password" label="Password">
            <el-input type="password" id="password" placeholder="password"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="">Login</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </el-main>
</template>
<script>
export default {
  name: 'login',
  methods: {
    // todo Login method
  },
  data () {
    return {
      email: '',
      password: ''
    }
  }
}
</script>
