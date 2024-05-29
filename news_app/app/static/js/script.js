// Fetch articles based on search keyword and language
async function searchNews() {
  const keyword = document.getElementById("search").value;
  const language = document.getElementById("language").value;
  try {
    const response = await fetch(
      `/search?query=${keyword}&language=${language}`,
    );
    const data = await response.json();
    displayArticles(data);
  } catch (error) {
    console.error("Error fetching articles:", error);
  }
}

// Display articles in the DOM
function displayArticles(articles) {
  const articlesContainer = document.getElementById("articles");
  articlesContainer.innerHTML = "";
  articles.forEach((article) => {
    const articleElement = document.createElement("div");
    articleElement.innerHTML = `
            <h3>${article.title}</h3>
            <p>${article.description}</p>
            <button onclick="saveArticle('${article.title}', '${article.description}', '${article.url}')">Save</button>
        `;
    articlesContainer.appendChild(articleElement);
  });
}

// Save article to local storage
function saveArticle(title, description, url) {
  let savedArticles = JSON.parse(localStorage.getItem("savedArticles")) || [];
  savedArticles.push({ title, description, url });
  localStorage.setItem("savedArticles", JSON.stringify(savedArticles));
  displaySavedArticles();
}

// Display saved articles from local storage
function displaySavedArticles() {
  const savedArticles = JSON.parse(localStorage.getItem("savedArticles")) || [];
  const savedArticlesContainer = document.getElementById("saved-articles");
  savedArticlesContainer.innerHTML = "";
  savedArticles.forEach((article) => {
    const articleElement = document.createElement("div");
    articleElement.innerHTML = `
            <h3>${article.title}</h3>
            <p>${article.description}</p>
            <a href="${article.url}" target="_blank">Read more</a>
            <button onclick="removeArticle('${article.title}')">Remove</button>
        `;
    savedArticlesContainer.appendChild(articleElement);
  });
}

// Remove article from local storage
function removeArticle(title) {
  let savedArticles = JSON.parse(localStorage.getItem("savedArticles")) || [];
  savedArticles = savedArticles.filter((article) => article.title !== title);
  localStorage.setItem("savedArticles", JSON.stringify(savedArticles));
  displaySavedArticles();
}

// Initial display of saved articles
document.addEventListener("DOMContentLoaded", displaySavedArticles);
