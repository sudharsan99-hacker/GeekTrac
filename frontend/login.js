import { url, EPsignup, EPlogin } from "./endpoints.js";
import { dashboardL } from "./locations.js"
import { platformL } from "./locations.js";


const wrapper = document.querySelector('.wrapper');
const registerLink = document.querySelector('.register-link');
const loginLink = document.querySelector('.login-link');

registerLink.onclick = () => {
    wrapper.classList.add('active');
}

loginLink.onclick = () => {
    wrapper.classList.remove('active');
}

// function getData()
// {
//     //gettting the values
//     var signupusername= document.getElementById("signupusername").value; 
//     var signupemail = document.getElementById("signupemail").value;
//     var signuppassword= document.getElementById("signuppassword").value; 
//     //saving the values in local storage
//     localStorage.setItem("signupusername", susername);  
//     localStorage.setItem("signupemail", semail);
//     localStorage.setItem("signuppassword", spassword); 
//     console.log(localStorage.getItem(susername));
//     localStorage.setItem('test','test1');
// }

// const form = document.getElementById('signup-form');
// const signupusername = document.getElementById('signupusername');
// const signupemail = document.getElementById('signupemail');

// form.addEventListener('submit', function(e){
//     e.preventDefault();

//     const signupusernameValue = signupusername.value;
//     const signupemailValue = signupemail.value;

//     localStorage.setItem('signupusername', signupusernameValue);
//     localStorage.setItem('signupemail', signupemailValue);

//     window.location.href="uploadimage.html";
// })

const loginform = document.getElementById('login-form')
const signupform = document.getElementById('signup-form')

loginform.addEventListener("submit", (e) => {
    e.preventDefault()

    const inputs = loginform.elements;
    // const userinfo = {
    //     username: inputs["username"].value,
    //     password: inputs["password"].value,
    // };
    localStorage.setItem("username",inputs["username"].value);
    const form = new FormData(loginform)

    let asyncLogin = fetch(url + EPlogin, {
        method: "POST",
        body: form,

    })

    asyncLogin.then(
        (res) => {
            if (res.status != 200) {
                console.log(res);
                return "";
            }
            return res.json();
        }
    ).then((data) => {
        if (data === "") {
            alert("token not found");
            return;
        }
        localStorage.setItem("token", data);
        window.location.href = dashboardL;
    })

    asyncLogin.catch(
        (res) => {
            console.log(res)
            alert("login failed");
        }
    )
});

signupform.addEventListener("submit", (e) => {
    e.preventDefault()

    const inputs = signupform.elements;
    const userinfo = {
        username: inputs["username"].value,
        password: inputs["password"].value,
        email: inputs["email"].value,
    };
    localStorage.setItem("username",inputs["username"].value);
    const form = new FormData(signupform)

    let asyncSignup = fetch(url + EPsignup, {
        method: "POST",
        body: form,

    })

    asyncSignup.then(
        (res) => {
            if (res.status != 200) {
                console.log(res);
            }
            return res.json();
        }
    ).then((data) => {
        console.log(data)
        localStorage.setItem("token", data);
        window.location.href = platformL;
    })

    asyncSignup.catch(
        (res) => {
            alert("signup failed");
        }
    )
});