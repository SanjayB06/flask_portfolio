function checkMode() {
    const currentTheme = localStorage.getItem("theme");
    if (currentTheme == "light") {
        document.body.className = 'light-theme'
    }
    if (currentTheme=="dark") {
        document.body.className = 'dark-theme'
    }
    if (document.getElementsByTagName('link')[0].getAttribute('href') == '/static/dark.css') {
        document.body.className = 'dark-theme'

    } else {
        document.body.className = 'light-theme'
    }
}

