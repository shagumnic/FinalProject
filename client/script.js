/* jshint esversion: 8*/
'use strict';

const KEY_NAME = ['steam_id', 'name', 'release_date', 'languages', 'genres'];

async function getVideoGameData() {

    //let name = document.getElementById("videogame").value;

    let videogame = await fetch(`http://127.0.0.1:5000/api/v1/?name=${name}`)
        .then(response => response.json())
        .catch(error => console.log(error));

    let table = document.getElementById("tableId");

    for (let game in videogame.results) {
        let tr = document.createElement("tr");
        
        let td_id = document.createElement("td");
        td_id.innerText = game.steam_id;
        tr.appendChild(td_id);

        let td_name = document.createElement("td");
        td_name.innerText = game.name;
        tr.appendChild(td_id);
    }
}

async function fetchData() {
    let name = document.querySelector('#name').value;
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