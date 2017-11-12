import {
  SET_PINS,
  SET_PIN_INFO,
  ADD_PIN,
  ADD_PIN_COMMENT

} from '../mutation-types'

const state = {
  coordinate: [],
  pins: [],
  pinInfo: {},
  pinComments: [],
  pinGallery: []
}

const getters = {
  getPins: (state) => state.pins,
  getPinInfo: (state) => state.pinInfo,
  getPinComments: (state) => state.pinComments,
  getPinGallery: (state) => state.pinGallery
}

const mutations = {
  [SET_PINS] (state, pins) { state.pins = pins },
  [SET_PIN_INFO] (state, pin) {
    state.pinInfo = pin.info
    state.pinGallery = pin.photos
    state.pinComments = pin.comments
  },
  [ADD_PIN] (state, pin) { state.pins = state.pins.push(pin) },
  [ADD_PIN_COMMENT] (state, comment) {
    state.pinComments.push(comment)
    state.pinInfo.comments = state.pinInfo.pinComments.shift().push(comment)
  }
}

const actions = {
  async recivePins ({ commit }) {
    let pins = await require('../../../mocks/_pins')
    commit(SET_PINS, pins)
  },
  async recivePinInfo ({ commit, getters }, id) {
    if (id) {
      let pins = await require('../../../mocks/_pins')
      let pin = await pins.filter(data => { return data.pinId === id })[0]
      let comments = await require(`../../../mocks/_comments${id}.json`)
      let photos = await require(`../../../mocks/_gallery${id}.json`)
      commit(SET_PIN_INFO, {'info': pin, 'comments': comments, 'photos': photos})
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
