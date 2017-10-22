
export function setToken (token, remember) {
  remember ? localStorage.setItem('jwtToken', token) : sessionStorage.setItem('jwtToken', token)
}

export function getToken () {
  return localStorage.getItem('jwtToken') || sessionStorage.getItem('jwtToken');
}

export function delToken () {
  localStorage.removeItem('jwtToken');
  sessionStorage.removeItem('jwtToken');
}
