import { fetch, BASE_API_URL } from '../utils/fetch'

export function registration (email, password) {
  const data = {
    email,
    password
  }
  return fetch({
    url: BASE_API_URL + '/register',
    methods: 'post',
    data
  })
}

export function login (email, password) {
  const data = {
    email,
    password
  }
  return fetch({
    url: BASE_API_URL + '/login',
    methods: 'post',
    data
  })
}
