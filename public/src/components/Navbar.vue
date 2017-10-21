<template>
  <section>
    <el-header>
      <el-menu class="el-menu-demo" mode="horizontal" :router="true">
        <el-menu-item index="1" :route="{name: 'registration'}">Registration</el-menu-item>
        <el-menu-item index="2" :route="{name: 'login'}">Login</el-menu-item>
      </el-menu>
    </el-header>
  </section>
</template>

<script>
import ElContainer from '../../node_modules/element-ui/packages/container/src/main.vue';

export default {
  components: {ElContainer}
}
</script>
