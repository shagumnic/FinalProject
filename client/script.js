/* jshint esversion: 8*/
'use strict';

const KEY_NAME = ['steam_id', 'name', 'release_date', 'languages', 'genres'];

async function fetchData() {
    let name = document.querySelector('#name').value;
    let div = document.getElementById("form");
    let errorMsg = document.getElementById("message");
    if (name == "") {
        errorMsg.innerText = "Please enter a game";
        errorMsg.setAttribute("class", "alert alert-warning text-center");
    }

    else {
        let data = await fetch(`https://thomso03.pythonanywhere.com/api/v1/?name=${name}`).then(response => response.json());
        if (data.results=="") {
            errorMsg.innerText = "No game with this title";
            errorMsg.setAttribute("class", "alert alert-warning text-center");
        }
        else {
            errorMsg.innerText = "Game(s) have been fetched";
            errorMsg.setAttribute("class", "alert alert-primary text-center");
        }
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