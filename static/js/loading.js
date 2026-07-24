const form = document.querySelector(".search-form");
const loading = document.getElementById("loading-screen");
const button = form.querySelector("button");

form.addEventListener("submit", function () {

    button.disabled = true;

    button.innerText = "Loading...";

    loading.style.display = "flex";

});