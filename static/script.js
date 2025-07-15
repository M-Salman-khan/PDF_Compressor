const form = document.querySelector("form");
const loadingModal = document.getElementById("loadingModal");
if (form) {
  form.addEventListener("submit", () => {
    loadingModal.style.display = "flex";
  });
}
