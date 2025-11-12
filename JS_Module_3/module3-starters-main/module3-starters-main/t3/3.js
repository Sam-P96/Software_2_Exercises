'use strict';
const names = ['John', 'Paul', 'Jones'];
const ulGetter = document.querySelector("#target")

for (name of names) {
    let liMaker = document.createElement("li")
    liMaker.innerText = name
    ulGetter.appendChild(liMaker)
}