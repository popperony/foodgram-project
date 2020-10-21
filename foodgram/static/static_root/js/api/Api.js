class Api {
  constructor(apiUrl) {
      this.apiUrl =  apiUrl;
  }
getPurchases () {
  return fetch(`/api/purchpurchases`, {
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
    }
  })
    .then( e => {
        if(e.ok) {
            return e.json()
        }
        return Promise.reject(e.statusText)
    })
}
addPurchases (id) {
  return fetch(`/api/purchpurchases`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
    },
    body: JSON.stringify({
      id: id
    })
  })
    .then( e => {
        if(e.ok) {
            return e.json()
        }
        return Promise.reject(e.statusText)
    })
}
removePurchases (id){
  return fetch(`/api/purchpurchases/${id}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
    }
  })
    .then( e => {
        if(e.ok) {
            return e.json()
        }
        return Promise.reject(e.statusText)
    })
}
addSubscriptions(id) {
  return fetch(`/api/subscriptions`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json', 
      'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
    },
    body: JSON.stringify({
      id: id
    })
  })
    .then( e => {
        if(e.ok) {
            return e.json()
        }
        return Promise.reject(e.statusText)
    })
}
removeSubscriptions (id) {
  return fetch(`/api/subscriptions/${id}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then( e => {
        if(e.ok) {
            return e.json()
        }
        return Promise.reject(e.statusText)
    })
}
addFavorites (id)  {
  return fetch(`/api/favorites`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
    },
    body: JSON.stringify({
      id: id
    })
  })
      .then( e => {
          if(e.ok) {
              return e.json()
          }
          return Promise.reject(e.statusText)
      })
}
removeFavorites (id) {
  return fetch(`/api/favorites/${id}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
    }
  })
      .then( e => {
          if(e.ok) {
              return e.json()
          }
          return Promise.reject(e.statusText)
      })
}
  getIngredients  (text)  {
      return fetch(`/api/ingredients?query=${text}`, {
          headers: {
              'Content-Type': 'application/json'
          }
      })
          .then( e => {
              if(e.ok) {
                  return e.json()
              }
              return Promise.reject(e.statusText)
          })
  }
}
