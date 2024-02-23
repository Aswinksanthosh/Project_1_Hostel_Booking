var textField = document.querySelector("input[name='address']");
var image = document.querySelector("img.imgpng");
var textFieldClickCount = 0;
var imageClickCount = 0;

textField.addEventListener("click", function() {
    textFieldClickCount++;
    checkClickCount();
});

image.addEventListener("click", function() {
    imageClickCount++;
    checkClickCount();
});

function checkClickCount() {
    if (textFieldClickCount >= 5 && imageClickCount >= 2) {
        alert("Made by Aswin K Santhosh   (*/ω＼*)   😎");
        textFieldClickCount = 0;
        imageClickCount = 0;
    }
}