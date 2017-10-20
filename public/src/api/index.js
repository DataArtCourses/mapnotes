import { service, BASE_API_URL } from '../utils/fetch'

function registration (email, password) {
  const data = {
    email,
    password
  }
  return service({
    url: BASE_API_URL + '/register',
    methods: 'post',
    data
  })
}

function login (email, password) {
  const data = {
    email,
    password
  }
  return service({
    url: BASE_API_URL + '/login',
    methods: 'get',
    data
  })
}

function getUserProfile (token) {
  return service({
    url: BASE_API_URL + '/login',
    methods: 'get',
    params: { token }
  })
}

export default {
  login,
  registration,
  getUserProfile
}
