import { url, EPaddplatform } from "./endpoints.js";

const addPlatformForm = document.getElementById("platform");

addPlatformForm.addEventListener("submit", (e) => {
    e.preventDefault();


    const inputs = addPlatformForm.elements;
    const userinfo = {
        platform: inputs["platform"].value,
        username: inputs["username"].value,
    };

    console.log(userinfo);


    const form = new FormData(addPlatformForm);
    let token = localStorage.getItem("token")
    console.log(url + EPaddplatform);
    let asyncAddPlatform = fetch(url + EPaddplatform,{
        method: "POST",
        headers: {
            "Authorization": token,
        },
        body: form
    });

    asyncAddPlatform.then((res) => {
        if (res.status != 200) {
            console.log(res)
        }
        return res.json();
    }).then((data) => {
        console.log(data);
        leetcodeStat.innerHTML = data["username"];
    });
    asyncAddPlatform.catch((res) => {
        console.log(res)
        console.log("error");
    })
})