fetch("http://127.0.0.1:8000/articles")
  .then((res) => res.json())
  .then((data) => {
    const container = document.getElementById("articles");
    container.innerHTML = "";
    data.forEach((article) => {
      const div = document.createElement("article");
      div.innerHTML = `<h2>${article.title}</h2><div>${article.html}</div>`;
      container.appendChild(div);
    });
  })
  .catch((err) => {
    document.getElementById("articles").textContent = "Erreur : " + err;
  });
