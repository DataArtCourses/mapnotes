import axios from 'axios'
import { Message } from 'element-ui'

import store from '../store'
import getToken from './auth'

const BASE_API_URL = 'http://localhost:8000/api';

const service = axios.create({
  baseURL: BASE_API_URL,
  timeout: 5000
});

service.interceptors.request.use(config => {
  // Do something before request is sent
  if (store.getters.isAuth) {
    config.headers['Authorization'] = getToken()
  }
  return config
}, error => {
  // Do something with request error
  console.log(error);
  Promise.reject(error)
});

service.interceptors.response.use(
  response => response,
  error => {
    console.log('err' + error);// for debug
    Message({
      message: error.message,
      type: 'error',
      duration: 5 * 1000
    });
    return Promise.reject(error)
  }
);

export {
  service,
  BASE_API_URL
}
