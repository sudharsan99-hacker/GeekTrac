import { url, EPleetcode, EPcodechef, EPupdatestats, EPunames } from "./endpoints.js";
import { loginL } from "./locations.js";
//const leetcodeStat = document.getElementById("leetcodeStat");
//const codechefStat = document.getElementById("codechefStat");
var usernamedisplay=document.getElementById("i4jn1p");
usernamedisplay.textContent=localStorage.getItem("username");
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

        console.log("hihguthgjtbgtub")
        console.log(data);
        const leetcoderank = document.getElementById("leetrating");
        const rank = data["profile"]["ranking"];
        leetcoderank.textContent = rank;
        const allproblems = document.getElementById("leetproblems");
        const allcount = data["submission"][0]["count"];
        allproblems.textContent = allcount;
        const easyproblems = document.getElementById("leeteasy");
        const easycount = data["submission"][1]["count"];
        easyproblems.textContent = easycount;
        const mediumproblems = document.getElementById("leetmedium");
        const mediumcount = data["submission"][2]["count"];
        mediumproblems.textContent = mediumcount;
        const hardproblems = document.getElementById("leethard");
        const hardcount = data["submission"][3]["count"];
        hardproblems.textContent = hardcount;
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
        const codeglobalrank = document.getElementById("globalrating");
        codeglobalrank.textContent = data["rank"]["global_rank"];
        const codecountryrank = document.getElementById("countryrating");
        codecountryrank.textContent = data["rank"]["country_rank"];
        const rating = document.getElementById("coderating");
        rating.textContent = data["rating"];
        const stars = document.getElementById("codestars");
        stars.textContent = data["stars"];
    });

    asyncCodechef.catch((res) => {
        codechefStat.innerHTML = "stats not found";
    });
}

get_leetcode_data()
get_codechef_data() 

const refreshButton = document.getElementById('iqx3z1');

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
            //alert('failed to update');
            return;
        }
        
        get_leetcode_data()
        get_codechef_data()
        alert('updated');
    });

    asyncCodechef.catch((res) => {
        //alert('failed to update');
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
        alert('fetched user names');
    });

    asyncCodechef.catch((res) => {
        alert('failed to fetch unames');
    });
};
get_unames();