import {
  SET_CENTER,
  SET_PINS,
  SET_PIN_INFO,
  ADD_PIN,
  SET_PIN_PHOTOS,
  SET_PHOTO_INFO,
  ADD_PHOTO,
  ADD_PIN_COMMENT,
  ADD_PHOTO_COMMENT

} from '../mutation-types'

const state = {
  centerMap: [46.444226, 30.727262],
  pins: [],
  pinInfo: {},
  pinGallery: [],
  photoInfo: {}
}

const getters = {
  getPins: (state) => state.pins,
  getCenter: (state) => state.centerMap,
  getPinInfo: (state) => { if (state.pinInfo) { return state.pinInfo } },
  getPinGallery: (state) => state.pinGallery,
  getPhotoInfo: (state) => state.photoInfo
}

const mutations = {
  [SET_CENTER] (state, center) { state.centerMap = center },
  [SET_PINS] (state, pins) { state.pins = pins },
  [SET_PIN_INFO] (state, pin) { state.pinInfo = pin },
  [ADD_PIN] (state, pin) { state.pins = state.pins.push(pin) },
  [ADD_PIN_COMMENT] (state, comment) { state.pinInfo.comments.push(comment) },
  [SET_PIN_PHOTOS] (state, photos) { state.pinGallery = photos },
  [ADD_PHOTO] (state, photo) { state.pinGallery.unshift(photo) },
  [SET_PHOTO_INFO] (state, photo) { state.photoInfo = photo },
  [ADD_PHOTO_COMMENT] (state, comment) { state.photoInfo.comments.push(comment) }
}

const actions = {
  async setCenter ({ commit }, center) {
    if (center) {
      let lonLat = [center.lat, center.lng]
      commit(SET_CENTER, lonLat)
    }
  },
  async recivePins ({ commit }) {
    let pins = await require('../../../mocks/_pins')
    commit(SET_PINS, pins)
  },
  async addPin ({ commit }, pinInfo) {
    if (pinInfo) {
      commit(ADD_PIN, pinInfo)
    }
  },
  async recivePinInfo ({ commit, getters }, id) {
    if (id) {
      let pinInfo = await require(`../../../mocks/_pinInfo${id}.json`)[0]
      commit(SET_PIN_INFO, pinInfo)
    }
  },
  async recivePinPhotos ({ commit, getters }, id) {
    if (id) {
      let photos = await require(`../../../mocks/_gallery${id}.json`)
      commit(SET_PIN_PHOTOS, photos)
    }
  },
  async recivePhotoInfo ({ commit, getters }, id) {
    if (id) {
      let photo = getters.getPinGallery.filter(data => data.photoId === id)[0]
      commit(SET_PHOTO_INFO, photo)
    }
  },
  async sendComment ({ commit }, pinInfo) {
    if (pinInfo.comment.photoId === 0) {
      commit(ADD_PIN_COMMENT, pinInfo.comment)
    } else {
      commit(ADD_PHOTO_COMMENT, pinInfo.comment)
    }
  },
  async sendPhoto ({ commit }, photo) {
    commit(ADD_PHOTO, photo.photoInfo)
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
