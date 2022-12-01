var wordInput = document.getElementById("word-input");

function addToUsedWords(word) {
  let ul = document.getElementById("used-words-list");
  let li = document.createElement("li");
  li.appendChild(document.createTextNode(word));
  ul.appendChild(li);
}

function getCheckAppend() {
  let word = wordInput.value;
  if(word===''){return;}
  // code to verify the words
  addToUsedWords(word);
  console.log(word);
  wordInput.value = '';
}

wordInput.addEventListener("keydown", (e)=>{
  if(e.key=="Enter"){
    getCheckAppend();
  }
});
