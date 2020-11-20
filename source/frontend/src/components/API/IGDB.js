export function connectWithAPI() {
    const url = 'https://id.twitch.tv/oauth2/token'
    return fetch(url, {
        method:'POST',
        headers:{
            "client_id": "h35ubEPmmZqqQk7bdMPVcj1pWDqC25ZJYe8",
            "client_secret": "y8er95djjzq89lvqzrvpzf0ap6gxaq",
            "grant_type": "client_credentials"
        },
    }).then((response => response.json()))
    .then(data => data)
    .catch((error) => console.log(error))
}