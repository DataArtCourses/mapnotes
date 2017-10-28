import {
  SET_PINS,
  SET_PIN_INFO,
  ADD_PIN
} from '../mutation-types'

const state = {
  pins: [],
  pin: {},
  pinSideBar: false
}

const getters = {
  getPins: (state) => state.pins,
  getPinInfo: (state) => state.pin
}

const mutations = {
  [SET_PINS] (state, pins) { state.pins = pins },
  [SET_PIN_INFO] (state, pin) { state.pin = pin },
  [ADD_PIN] (state, pin) { state.pins = state.pins.push(pin) }
}

const actions = {
  async recivePins ({ commit }) {
    let pins = await require('../../../mocks/_pins')
    commit(SET_PINS, pins)
  },
  async recivePinInfo ({ commit }, id) {
    let pins = await require('../../../mocks/_pins')
    let pin = await pins.filter(data => { return data.pinId === id })[0]
    commit(SET_PIN_INFO, pin)
  },
  async addPin ({ commit }, pinInfo) {
    commit(ADD_PIN, pinInfo)
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
