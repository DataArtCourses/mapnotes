<template lang="pug">
  el-container
    map-alternative
    pin-info
</template>
<script>
// import MapMain from './MapMain'
import MapAlternative from './MapAlternative'
import PinInfo from './PinInfo'

export default {
  name: 'map',
  components: {
    MapAlternative,
    PinInfo
  }
}
</script>
