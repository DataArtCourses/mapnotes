
export function setToken (token, remember) {
  remember ? localStorage.setItem('jwtToken', token) : sessionStorage.setItem('jwtToken', token)
}

export function getToken () {
  const storage = localStorage.getItem('jwtToken') || sessionStorage.getItem('jwtToken')
  return storage
}

export function delToken () {
  localStorage.removeItem('jwtToken')
  sessionStorage.removeItem('jwtToken')
}
