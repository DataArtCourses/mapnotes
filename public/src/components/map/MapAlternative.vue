<template lang="pug">
  el-main.map-wrapper
    v-map#map(ref="leafletMap" :minZoom="minZoom" :maxZoom="maxZoom" :center="center" :zoom="zoom")
      v-tilelayer(url="http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", :attribution="attribution")  // for https -> https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png
      v-marker-cluster
        v-marker(v-for="(c, index) in pins" v-if="c !== null" :lat-lng="[c.location.lat, c.location.lng]" :key="index" :icon='icon')
          v-popup(:content="`<a href='/map/${c.pinId}'>PinInfo</a><br><b>Comments: ${c.totalComments}</b><br><b>Photos: ${c.totalPhotos}</b>`")
    el-button(@click="addPin" type="danger" icon="el-icon-plus")
    el-dialog
</template>
<script>
import Vue2Leaflet from 'vue2-leaflet'
import Vue2LeafletMarkerCluster from 'vue2-leaflet-markercluster'
// icons
import iconUrl from '../../assets/marker-icon.png'
import shadowUrl from '../../assets/marker-shadow.png'
import iconRetinaUrl from '../../assets/marker-icon-2x.png'

export default {
  components: {
    'v-map': Vue2Leaflet.Map,
    'v-tilelayer': Vue2Leaflet.TileLayer,
    'v-marker': Vue2Leaflet.Marker,
    'v-marker-cluster': Vue2LeafletMarkerCluster,
    'v-popup': Vue2Leaflet.Popup
  },
  data () {
    let icon = window.L.icon(Object.assign({},
        window.L.Icon.Default.prototype.options,
        {iconUrl, shadowUrl, iconRetinaUrl}
      ))
    return {
      icon,
      minZoom: 3,
      maxZoom: 18,
      zoom: 12,
      attribution: `&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors`,
      addPinOn: false,
      enterPin: false,
      pinComment: '',
      pinLatLng: []
    }
  },
  computed: {
    pins () {
      return this.$store.getters.getPins
    },
    center () {
      return this.$store.getters.getCenter
    }
  },
  mounted () {
    this.$refs.leafletMap.mapObject.on('drag', (e) => {
      let center = this.$refs.leafletMap.mapObject.getCenter()
      this.$store.dispatch('setCenter', center)
    })
    this.$refs.leafletMap.mapObject.on('click', (e) => {
      if (this.addPinOn) console.log(e.latlng)
    })
  },
  methods: {
    addPin () {
      this.addPinOn = !this.addPinOn
    }
  },
  beforeCreate () {
    // pins loader
    this.$store.dispatch('recivePins')
  }
}
</script>
<style  lang="scss" scoped>
@import "~leaflet/dist/leaflet.css";
@import "~leaflet.markercluster/dist/MarkerCluster.css";
@import "~leaflet.markercluster/dist/MarkerCluster.Default.css";

.map-wrapper {
    position: relative;
    #map {
      width: 100%;
      height: 630px;
  }
}
</style>
