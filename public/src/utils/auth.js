
export function setToken (token, id, remember) {
  if (remember) {
    localStorage.setItem('jwtToken', token)
    localStorage.setItem('userId', id)
  } else {
    sessionStorage.setItem('jwtToken', token)
    sessionStorage.setItem('userId', id)
  }
}

export function getToken () {
  return localStorage.getItem('jwtToken') || sessionStorage.getItem('jwtToken')
}

export function getuUserId () {
  return localStorage.getItem('userId') || sessionStorage.getItem('userId')
}

export function delToken () {
  localStorage.removeItem('jwtToken')
  sessionStorage.removeItem('jwtToken')
  sessionStorage.removeItem('userId')
  localStorage.removeItem('userId')
}
