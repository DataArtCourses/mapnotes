<template lang="pug">
  el-main.map-wrapper
    #map
    .pin-sample(v-on:mousedown="pinTrackStart" v-on:mouseup="pinTrackEnd")
      img(src='../../assets/marker-icon.png' draggable="false")
</template>

<script>
  import L from 'leaflet'
  import markerIcon from '../../assets/marker-icon.png'
  import markerShadow from '../../assets/marker-shadow.png'
  import markerIcon2X from '../../assets/marker-icon-2x.png'
  import 'leaflet/dist/leaflet.css'

  const MAP_ICON = L.icon({
    iconUrl: markerIcon,
    shadowUrl: markerShadow,
    iconRetinaUrl: markerIcon2X,
    iconSize: [25, 41], // size of the icon
    shadowSize: [41, 41], // size of the shadow
    iconAnchor: [12, 41], // point of the icon which will correspond to marker's location
    shadowAnchor: [12, 41],  // the same for the shadow
    popupAnchor: [1, -34], // point from which the popup should open relative to the iconAnchor
    tooltipAnchor: [16, -28]
  });

  export default {
    data () {
      return {
        map: false,
        pins: [],
        pinSample: null,
        pinShift: {},
        mapOffset: null
      }
    },

    mounted () {
      // pins loader
      this.$store.dispatch('recivePins')
      this.$store.dispatch('recivePinInfo', 101)

      // map settings
      this.map = L.map('map', {
        minZoom: 3,
        maxZoom: 18,
        inertia: false
      }).setView([46.444226, 30.727262], 12);

      L.tileLayer('//a.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(this.map);

      // drag and drop
      this.pinSample = document.querySelector('#map + .pin-sample');
      this.mapOffset = this.getPosition(document.getElementById('map'));
    },

    methods: {
      pinTrackStart (event) {
        let pos = this.getPosition(this.pinSample);
        this.pinShift.top = event.pageY - pos.top;
        this.pinShift.left = event.pageX - pos.left;

        this.pinSample.style.right = 'unset';
        this.pinTracking(event);
        document.onmousemove = this.pinTracking;
      },

      pinTrackEnd (event) {
        document.onmousemove = null;

        this.setMarker({
          left: parseInt(this.pinSample.style.left) + this.pinSample.clientWidth / 2,
          top: parseInt(this.pinSample.style.top) + this.pinSample.clientHeight
        });

        this.pinSample.style.right = '10px';
        this.pinSample.style.top = '10px';
        this.pinSample.style.left = 'unset';
      },

      pinTracking (event) {
        this.pinSample.style.left = event.pageX - this.mapOffset.left - this.pinShift.left + 'px';
        this.pinSample.style.top = event.pageY - this.mapOffset.top - this.pinShift.top + 'px';
      },

      getPosition (elem) {
        let box = elem.getBoundingClientRect();
        return {
          top: box.top + pageYOffset,
          left: box.left + pageXOffset
        }
      },

      setMarker (pos) {
        let pointLatlng = this.map.containerPointToLatLng(L.point(pos.left, pos.top));

        let marker = L.marker([pointLatlng.lat, pointLatlng.lng], {icon: MAP_ICON}).addTo(this.map);
        this.pins.push(marker);
      }
    }
  }
</script>

<style>
  #map {
    width: 100%;
    height: 500px;
  }
  .map-wrapper {
    position: relative;
  }
  .pin-sample {
    position: absolute;
    top: 10px;
    right: 10px;
    z-index: 1000;
    cursor: pointer;
  }
</style>
