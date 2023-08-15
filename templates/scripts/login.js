baseUrl = 'http://127.0.0.1:8000/'


const userName = document.getElementById('username')
const passWord = document.getElementById('password')
const submitButton = document.getElementById('submit')

function loginHandler() {
    if (!userName.value || !passWord.value){
        alert('Please fill the form! ')
        return
    }
    var data = new FormData();
    data.append('username', userName.value);
    data.append('password', passWord.value);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', baseUrl+'api/login/', true);
    xhr.onload = function () {
        // do something to response
        console.log(this.responseText);
    };
    xhr.send(data);
    
}






submitButton.addEventListener('click',loginHandler)

