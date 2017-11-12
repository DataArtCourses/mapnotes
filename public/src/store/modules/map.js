import {
  SET_PINS,
  SET_PIN_INFO,
  ADD_PIN,
  ADD_PIN_COMMENT,
  SET_PIN_PHOTOS,
  SET_PHOTO_INFO

} from '../mutation-types'

const state = {
  coordinate: [],
  pins: [],
  pinInfo: {},
  pinGallery: [],
  photoInfo: {}
}

const getters = {
  getPins: (state) => state.pins,
  getPinInfo: (state) => { if (state.pinInfo) { return state.pinInfo } },
  getPinGallery: (state) => state.pinGallery,
  getPhotoInfo: (state) => state.photoInfo
}

const mutations = {
  [SET_PINS] (state, pins) { state.pins = pins },
  [SET_PIN_INFO] (state, pin) { state.pinInfo = pin },
  [ADD_PIN] (state, pin) { state.pins = state.pins.push(pin) },
  [ADD_PIN_COMMENT] (state, comment) {
    state.pinInfo.comments = state.pinInfo.comments.push(comment)
  },
  [SET_PIN_PHOTOS] (state, photos) {
    state.pinGallery = photos
  },
  [SET_PHOTO_INFO] (state, photo) { state.photoInfo = photo }
}

const actions = {
  async recivePins ({ commit }) {
    let pins = await require('../../../mocks/_pins')
    commit(SET_PINS, pins)
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
  async addPin ({ commit }, pinInfo) {
    if (pinInfo) {
      commit(ADD_PIN, pinInfo)
    }
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
