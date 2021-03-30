const requestURL = 'http://127.0.0.1:8000/api/lab3'

function sendRequest(method, url,) {
    var body = {
        input_value: document.getElementById('number').value
    }

    const xhr = new XMLHttpRequest()

    xhr.open(method, url)

    xhr.onload = function() {
        console.log(JSON.parse(xhr.response))
        document.getElementById('output').innerHTML = JSON.parse(xhr.response).output_value
    }

    xhr.send(JSON.stringify(body))
}