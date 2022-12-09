#!/usr/bin/env node

var wordInput = document.getElementById("word-input");
const xhr = new XMLHttpRequest()

function addToUsedWords(word) {
  let ul = document.getElementById("used-words-list");
  let li = document.createElement("li");
  li.appendChild(document.createTextNode(word));
  ul.appendChild(li);
}

function updateClient(postData){
	xhr.open("GET","http://localhost:1000/cgi-bin/game1.py")
	xhr.setRequestHeader("Content-Type","application/json");
	xhr.send(JSON.stringify("hello"))
	xhr.upload.onprogress = function(e){
		console.log('${e.loaded}B of ${e.total}B uploaded!')
	}
	xhr.upload.onload = function(e){
		console.log('comp')
	}
	xhr.onload = function(){
		console.log(xhr.status)
	}
}

function getCheckAppend() {
  let word = wordInput.value;
  if(word===''){return;}
  // code to verify the words
  addToUsedWords(word);
  updateClient(word);
  console.log(word);
  wordInput.value = '';
}


wordInput.addEventListener("keydown", (e)=>{
  if(e.key=="Enter"){
    getCheckAppend();
  }
});
