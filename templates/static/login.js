baseUrl = 'http://127.0.0.1:8000/'


const username = document.getElementById('username')
const password = document.getElementById('password')
const submitButton = document.getElementById('submit')

function loginHandler() {
    if (!username.value || !password.value){
        alert('Please fill the form! ')
        return
    }
    var data = new FormData();
    data.append('username', username.value);
    data.append('password', password.value);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', baseUrl+'api/usermanagement/login/', true);
    xhr.onload = function () {
        console.log(this.response)
    };
    xhr.send(data);
    
}


submitButton.addEventListener('click',loginHandler)


// let loginForm = document.getElementById("loginForm");

// loginForm.addEventListener("submit", (e) => {
//     e.preventDefault();
  
//     let username = document.getElementById("username");
//     let password = document.getElementById("password");
  
//     if (username.value == "" || password.value == "") {
//         alert('Please fill the form! ')
//         return
//     } else {
//         var data = new FormData();
//         data.append('username', username.value);
//         data.append('password', password.value);

//         var xhr = new XMLHttpRequest();
//         xhr.open('POST', baseUrl+'api/usermanagement/login/', true);
//         xhr.onload = function () {
//             // do something to response
//             console.log(this.responseText);
//         };
//         xhr.send(data);
//     }
//   });