#!/usr/bin/env node

points = 0;
attempt = 0;
var wordInput = document.getElementById("word-input");
const xhr = new XMLHttpRequest();
const roots = ["بطل","ءيس","بسس","بزق","ءما"];
let children = [["أمل","تأمل"],["بزق","بزاق","بزاقة"],["بس"],["ايس","ايس"],["ابطل","بطالة","بطل","بطولة"]];
children.reverse();
let answers = [];

function addToUsedWords(word,answer) {
  let ul = document.getElementById("used-words-list");
  let li = document.createElement("li");
  if(answer){
	  li.style.background = "green";
  }
  else{
	  li.style.background = "red";
  }
  li.appendChild(document.createTextNode(word));
  ul.appendChild(li);
}


function updateClient(word){
	for(let i =0;i<4;i++){
		if(answers[i] == word){
      answers.splice(i, 1);
			return true;
		}
	}
  attempt+=1;
	return false;
}


function getRoot(){
  let idx = Math.floor(Math.random()*5);
  answers = children[idx];
  let rootLettersList = document.getElementById('root-letter-list');
  for(let i=2; i>=0; i--){
    let li = document.createElement("li");
    li.innerHTML = roots[idx][i];
    rootLettersList.appendChild(li);
  }
}

function getCheckAppend() {
  if(attempt == 5){
    document.getElementById('used-words-list').innerHTML =  '';
    document.getElementById('root-letter-list').innerHTML =  '';
    attempt = 0;
    points=0;
    document.getElementById("points").innerHTML=points;
    getRoot();
    return;
  }
  let word = wordInput.value;
  if(word===''){return;}
  // code to verify the words
  answer = updateClient(word);
  addToUsedWords(word,answer);
  if(answer){
	  points+=10;
	  document.getElementById("points").innerHTML=points;
  }
	else{
	  document.getElementById("points").innerHTML=points;
  }
  if(points == answers.length*10){
	  let rootLettersList = document.getElementById("root-letter-list");
    let rootLetters = rootLettersList.getElementsByTagName('li');
	  for(let i =0;i<3;i++){
		  rootLetters[i].style.background="green";
	  }
  }
  wordInput.value = '';
}


wordInput.addEventListener("keydown", (e)=>{
  if(e.key=="Enter"){
    getCheckAppend();
  }
});

getRoot();
