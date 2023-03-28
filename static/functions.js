function notInList() {
    var checkBox = document.getElementById("stream10");
    var text = document.getElementById("streamText");
    if (checkBox.checked == true){
      text.style.display = "block";
    } else {
       text.style.display = "none";
    }
}