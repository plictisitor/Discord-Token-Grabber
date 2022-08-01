// use this script to login using the token. execute it in the browser console (f12 / ctrl+shift+i)

token = "INSERT"

function login(token) {
    setInterval(() => {
        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
    }, 50);
    setTimeout(() => {
        location.reload();
    }, 2500);
}

login(token);