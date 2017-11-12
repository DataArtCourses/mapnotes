<template lang="pug">
  el-container
    map-main
    pin-info
</template>
<script>
import MapMain from './MapMain'
import PinInfo from './PinInfo'

export default {
  name: 'map',
  components: {
    MapMain,
    PinInfo
  }
}
</script>
