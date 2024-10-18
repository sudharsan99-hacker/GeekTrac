import { url, EPleetcode, EPcodechef, EPupdatestats, EPunames } from "./endpoints.js";
import { loginL } from "./locations.js";
const leetcodeStat = document.getElementById("leetcodeStat");
const codechefStat = document.getElementById("codechefStat");

function get_leetcode_data() {
    let token = localStorage.getItem("token")
    let asyncLeetcode = fetch(url + EPleetcode,{
        headers: {
            "Authorization": token,
        }
    });
    asyncLeetcode.then((res) => {
        return res.json();
    }).then((data) => {
        console.log(data);
        leetcodeStat.innerHTML = data["username"];
    });

    asyncLeetcode.catch((res) => {
        leetcodeStat.innerHTML = "stats not found";
    });
}

function get_codechef_data() {
    let token = localStorage.getItem("token")
    let asyncCodechef = fetch(url + EPcodechef,{
        headers: {
            "Authorization": token,
        }
    });
    asyncCodechef.then((res) => {
        return res.json();
    }).then((data) => {
        console.log(data);
        codechefStat.innerHTML = data["username"];
    });

    asyncCodechef.catch((res) => {
        codechefStat.innerHTML = "stats not found";
    });
}

get_leetcode_data()
get_codechef_data() 

const refreshButton = document.getElementById('updatestat');

refreshButton.addEventListener("click", (e) => {
    let token = localStorage.getItem("token")
    let asyncCodechef = fetch(url + EPupdatestats,{
        method: "POST",
        headers: {
            "Authorization": token,
        }
    });
    asyncCodechef.then((res) => {
        if (res.status != 200) {
            alert('failed to update');
            return;
        }
        
        get_leetcode_data()
        get_codechef_data()
        alert('updated');
    });

    asyncCodechef.catch((res) => {
        alert('failed to update');
    });
})

const pnamesE = document.getElementById("pnames");

function get_unames() {
    let token = localStorage.getItem("token")
    let asyncCodechef = fetch(url + EPunames,{
        method: "GET",
        headers: {
            "Authorization": token,
        }
    });
    asyncCodechef.then((res) => {
        return res.json();
    }).then((data) => {
        console.log(data); 
        alert('fetched unames');
    });

    asyncCodechef.catch((res) => {
        alert('failed to fetch unames');
    });
};
get_unames();