// Quiz a scelta multipla con correzione immediata.
// Markup: <div class="quiz"><p>Domanda</p>
//           <button data-ok data-why="perché">Risposta giusta</button>
//           <button data-why="perché no">Risposta sbagliata</button></div>
document.querySelectorAll(".quiz").forEach((quiz) => {
  const esito = document.createElement("div");
  esito.className = "esito";
  quiz.appendChild(esito);
  quiz.querySelectorAll("button").forEach((b) => {
    b.addEventListener("click", () => {
      const giusta = b.hasAttribute("data-ok");
      b.classList.add(giusta ? "giusta" : "sbagliata");
      esito.textContent = (giusta ? "✔ Giusto. " : "✘ No. ") + (b.dataset.why || "");
    });
  });
});
