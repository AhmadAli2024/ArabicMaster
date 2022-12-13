#!/usr/bin/env node

points = 0

var wordInput = document.getElementById("word-input");
const xhr = new XMLHttpRequest()

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
	const cars = ["اس","اسوان","اسوة","ماسة"];
	for(let i =0;i<4;i++){
		if(cars[i] == word){
			return true;
		}
	}
	return false;
}


function getCheckAppend() {
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
  if(points == 40){
	  let rootLetters = document.getElementById("root-letter-list");
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
