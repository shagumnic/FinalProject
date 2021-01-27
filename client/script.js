/* jshint esversion: 8*/
'use strict';

const KEY_NAME = ['steam_id', 'name', 'release_date', 'languages', 'genres'];

async function fetchData() {
    let name = document.querySelector('#name').value;
    let div = document.getElementById("form");
    let errorMsg = document.createElement("h3");
    if (name == "") {
        errorMsg.innerText = "Please enter a game";
        errorMsg.setAttribute("class", "alert alert-warning text-center");
        div.appendChild(errorMsg);
    }

    else {
        div.removeChild(errorMsg);
        let data = await fetch(`http://127.0.0.1:5000/api/v1/?name=${name}`).then(response => response.json());
        let tbody = document.querySelector('#tblList > tbody');
        for (let result of data.results) {
            let tr = document.createElement('tr');
            for (let key of KEY_NAME) {
                let th = document.createElement('td');
                th.innerText = result[key];
                tr.append(th);
            }
            tbody.append(tr);
        }

    }
} 