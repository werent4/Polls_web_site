function CopyToClipboard(element) {
  alert("Text has been successfully copied")

  // create a temporary textarea element to hold the text to copy
  var tempTextarea = document.createElement("textarea");

  // set the value of the textarea to the content of the specified element
  tempTextarea.value = element.innerText;

  // append the textarea to the DOM
  document.body.appendChild(tempTextarea);

  // select the text in the textarea
  tempTextarea.select();

  // copy the selected text to the clipboard
  document.execCommand("copy");

  // remove the textarea from the DOM
  document.body.removeChild(tempTextarea);
}
