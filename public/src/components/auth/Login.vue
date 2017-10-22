<template>
  <el-main>
    <el-row>
      <el-col :span=8 :offset=7>
        <el-form :model="LoginForm" ref="LoginForm" labelWidth="150px">
          <el-form-item prop="email" label="Email" :rules="rules">
            <el-input v-model="LoginForm.email" placeholder="e-mail"></el-input>
          </el-form-item>
          <el-form-item prop="password" label="Password" :rules="[{required: true}]">
            <el-input type="password" v-model="LoginForm.password" placeholder="password"></el-input>
          </el-form-item>
          <el-form-item>
            <el-checkbox v-model="LoginForm.checked">Remember me</el-checkbox>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('LoginForm')">Log in</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </el-main>
</template>
<script>
import axios from 'axios'
import ElFormItem from '../../../node_modules/element-ui/packages/form/src/form-item.vue';
import ElInput from '../../../node_modules/element-ui/packages/input/src/input.vue';
import ElCheckbox from '../../../node_modules/element-ui/packages/checkbox/src/checkbox.vue';

export default {
  components: {
    ElCheckbox,
    ElInput,
    ElFormItem},
  name: 'login',
  data () {
    return {
      LoginForm: {
        email: '',
        password: '',
        checked: false
      },
      rules: [
        { required: true, message: 'Please input email address', trigger: 'blur' },
        { type: 'email', message: 'Please input correct email address', trigger: 'blur,change' }
      ]
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          axios.post('http://localhost:8000/api/login', { email: this.LoginForm.email, password: this.LoginForm.password }).then(response => {
            console.log(response);
            if (response.status === 200) {
              this.$store.dispatch('login', {token: response.data.token, ch: this.LoginForm.checked})
              this.$router.push({path: '/hello'})
            }
          }).catch(e => {
            this.$message({
              type: 'error',
              message: `${e.response ? e.response.data.error : e}`
            })
          })
        } else {
          this.$message({
            type: 'error',
            message: 'Oops! Something went wrong..'
          });
          return false
        }
      })
    }
  }
}
</script>

