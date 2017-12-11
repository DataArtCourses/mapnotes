import { BASE_API_URL, service } from '../../utils/fetch'

import {
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
  centerMap: [Number(sessionStorage.getItem('centerMapLat')) || 46.444226, Number(sessionStorage.getItem('centerMapLng')) || 30.727262],
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
  [SET_PINS] (state, pins) { state.pins = pins },
  [SET_PIN_INFO] (state, {id, comments, hover}) {
    state.pinInfo = state.pins.filter(data => data.pinId === id)[0]
    state.pinInfo['comments'] = comments
    state.pinInfo['hover'] = hover
  },
  [ADD_PIN] (state, pin) { state.pins.push(pin) },
  [ADD_PIN_COMMENT] (state, comment) { state.pinInfo.comments.unshift(comment) },
  [SET_PIN_PHOTOS] (state, photos) { state.pinGallery = photos },
  [ADD_PHOTO] (state, photo) { state.pinGallery.unshift(photo) },
  [SET_PHOTO_INFO] (state, photo) { state.photoInfo = photo },
  [ADD_PHOTO_COMMENT] (state, comment) { state.photoInfo.comments.unshift(comment) }
}

const actions = {
  async recivePins ({ commit }) {
    let pins = await service.get(`${BASE_API_URL}/pins`)
    commit(SET_PINS, pins.data)
  },
  async addPin ({ commit, getters }, pinInfo) {
    if (pinInfo) {
      let pinId = await service.post(`${BASE_API_URL}/pins`, pinInfo)
      pinInfo['totalComments'] = 1
      pinInfo['totalPhotos'] = 0
      pinInfo['pinStatus'] = 0
      pinInfo['pinId'] = pinId.data.pinId
      commit(ADD_PIN, pinInfo)
    }
  },
  async recivePinInfo ({ commit, getters }, id) {
    if (id) {
      let comments = await service.get(`${BASE_API_URL}/pins/${id}/comments`)
      let photos = await service.get(`${BASE_API_URL}/pins/${id}/photos`)
      commit(SET_PIN_INFO, { 'id': id, 'comments': comments.data, 'hover': photos.data.slice(0, 3) })
      commit(SET_PIN_PHOTOS, photos.data)
    }
  },
  async recivePhotoInfo ({ commit }, id) {
    if (id) {
      let photo = await service.get(`${BASE_API_URL}/photos/${id}`)
      console.log(photo)
      commit(SET_PHOTO_INFO, photo.data)
    }
  },
  async sendComment ({ commit }, pinInfo) {
    let forSend = {body: pinInfo.comment.commentBody}
    if (pinInfo.comment.photoId === 0) {
      forSend['pin_id'] = pinInfo.pin_id
      let post = await service.post(`${BASE_API_URL}/comments`, forSend)
      pinInfo.comment['commentId'] = post.data.commentId
      pinInfo.comment['created'] = post.data.created
      commit(ADD_PIN_COMMENT, pinInfo.comment)
    } else {
      forSend['photo_id'] = pinInfo.comment.photoId
      let post = await service.post(`${BASE_API_URL}/comments`, forSend)
      pinInfo.comment['commentId'] = post.data.commentId
      pinInfo.comment['created'] = post.data.created
      commit(ADD_PHOTO_COMMENT, pinInfo.comment)
    }
  },
  async sendPhoto ({ commit }, photo) {
    let post = await service.post(`${BASE_API_URL}/photos`, photo)
    photo['photoId'] = post.data.photoId
    photo['created'] = post.data.created
    commit(ADD_PHOTO, photo)
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
