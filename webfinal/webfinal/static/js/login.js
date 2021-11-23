document.querySelector('#nombre').addEventListener('keydown',()=>{
   document.querySelector(".lnombre").classList.add("show");
})
document.querySelector("#apellido").addEventListener("keydown", () => {
  document.querySelector(".lapellido").classList.add("show");
});
document.querySelector("#correo").addEventListener("keydown", () => {
  document.querySelector(".lcorreo").classList.add("show");
});
document.querySelector("#fecha").addEventListener("click", () => {
  document.querySelector(".lfecha").classList.add("show");
});
