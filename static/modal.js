const openButton = document.getElementById("open-modal");
const modal = document.querySelector(".modal");
const overlay = modal.querySelector(".modal__overlay");
const closeBtn = modal.querySelector("button");
const openModal = () => {
    modal.classList.remove("hidden-modal1");
}
const closeModal = () => {
    modal.classList.add("hidden-modal1");
}
overlay.addEventListener("click", closeModal);
closeBtn.addEventListener("click", closeModal);
openButton.addEventListener("click", openModal);