<template lang="pug">
  el-main.map-wrapper
    v-map#map(ref="leafletMap" :minZoom="minZoom" :maxZoom="maxZoom" :center="center" :zoom="zoom")
      v-tilelayer(url="http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", :attribution="attribution")  // for https -> https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png
      v-marker-cluster
        v-marker(v-for="(c, index) in pins" v-if="c !== null" :lat-lng="[c.location.lat, c.location.lng]" :key="index" :icon='icon')
          v-popup(:content="`<a href='/map/${c.pinId}'>PinInfo</a><br><b>Comments: ${c.totalComments}</b><br><b>Photos: ${c.totalPhotos}</b>`")
    el-button(@click="addPin" type="danger" icon="el-icon-plus")
    el-dialog(title="Add pin" width="50%" top="40vh" :visible.sync="enterPin" v-if="enterPin")
      el-form
        el-form-item(lable="Pin Info" prop="info")
          el-input(v-model="pinInfo.comment" type="textarea")
        el-form-item
          el-button(type="primary" @click="sendPin") Add
          el-button(type="default" @click="enterPin = false; pinInfo = {location: {}, comment: ''}") Cansel
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
      map: {},
      minZoom: 3,
      maxZoom: 18,
      zoom: 12,
      attribution: `&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors`,
      addPinOn: false,
      enterPin: false,
      pinInfo: {
        location: {},
        comment: ''
      }
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
    // for remember centerMap location
    this.map = this.$refs.leafletMap.mapObject
    this.map.on('drag', (e) => {
      let center = this.map.getCenter()
      sessionStorage.setItem('centerMapLat', center.lat)
      sessionStorage.setItem('centerMapLng', center.lng)
    })
    // for catch coordinates of the pin
    this.map.on('click', (e) => {
      if (this.addPinOn) {
        this.pinInfo.location = {
          lat: e.latlng.lat,
          lng: e.latlng.lng
        }
        this.enterPin = true
      }
    })
  },
  methods: {
    addPin () {
      this.addPinOn = !this.addPinOn
    },
    sendPin () {
      // checking if all info entered and commit Pin
      if (this.enterPin && this.pinInfo) {
        this.$store.dispatch('addPin', this.pinInfo)
        this.pinInfo = {location: {}, comment: ''}
        this.enterPin = false
      }
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
