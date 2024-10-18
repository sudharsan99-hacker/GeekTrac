import { url, EPaddplatform } from "./endpoints.js";
import { loginL } from "./locations.js";

const addPlatformForm = document.getElementById("platform_form");

console.log("hi");

addPlatformForm.addEventListener("submit", (e) => {
    e.preventDefault();

    console.log(addPlatformForm);

    const inputs = addPlatformForm.elements;
    console.log(inputs);
    const userinfo = {
        codechef : inputs["codechef"].value,
        leetcode : inputs["leetcode"].value
    };

    console.log(userinfo);

    let token = localStorage.getItem("token");
    const form = new FormData(addPlatformForm);
    console.log("token");
    console.log(token)
    let asyncAddPlatform = fetch(url + EPaddplatform, {
        method: "POST", // Change method to POST
        headers: {
            'Content-Type': 'application/json',
            "Authorization": token,
        },
        body: JSON.stringify(userinfo)
    });
    
    asyncAddPlatform.then((res) => {
        if (res.status != 200) {
            console.log(res)
        }
        return res.json();
    }).then((data) => {
        console.log(data);
        window.location.href = loginL;
        //leetcodeStat.innerHTML = data["username"];
    });
    asyncAddPlatform.catch((res) => {
        console.log(res)
        console.log("error");
    })
})

