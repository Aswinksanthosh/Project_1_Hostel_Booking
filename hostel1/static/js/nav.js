const overlay = document.querySelector(".overlay");
const continueBtn = document.querySelector(".continue-btn");

continueBtn.addEventListener("click", function() {
  overlay.classList.add("hidden");
});
