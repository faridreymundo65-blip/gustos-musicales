// ---------- Data ----------
const genres = [
  {
    id: "rock",
    icon: "🎸",
    name: "Rock",
    description: "Energía, guitarras eléctricas y actitud rebelde desde los años 50.",
    artists: ["Queen", "Soda Stereo", "Led Zeppelin", "Foo Fighters"],
  },
  {
    id: "pop",
    icon: "🎤",
    name: "Pop",
    description: "Melodías pegajosas y producción brillante para todo el mundo.",
    artists: ["Taylor Swift", "Shakira", "Dua Lipa", "Bruno Mars"],
  },
  {
    id: "reggaeton",
    icon: "🔥",
    name: "Reggaetón",
    description: "Ritmo perreo, dembow y fiesta latina sin parar.",
    artists: ["Bad Bunny", "Karol G", "Daddy Yankee", "Rauw Alejandro"],
  },
  {
    id: "jazz",
    icon: "🎷",
    name: "Jazz",
    description: "Improvisación, swing y sofisticación con raíces afroamericanas.",
    artists: ["Miles Davis", "Ella Fitzgerald", "John Coltrane", "Nina Simone"],
  },
  {
    id: "electronica",
    icon: "🎧",
    name: "Electrónica",
    description: "Sintetizadores, beats programados y euforia de pista de baile.",
    artists: ["Daft Punk", "Calvin Harris", "ODESZA", "Bicep"],
  },
  {
    id: "hiphop",
    icon: "🎙️",
    name: "Hip-Hop",
    description: "Rimas, flow y beats que narran historias urbanas.",
    artists: ["Kendrick Lamar", "Nicki Minaj", "J. Cole", "Residente"],
  },
  {
    id: "clasica",
    icon: "🎻",
    name: "Clásica",
    description: "Orquestas y composiciones atemporales, de Bach a Williams.",
    artists: ["Beethoven", "Mozart", "Vivaldi", "Hans Zimmer"],
  },
  {
    id: "salsa",
    icon: "💃",
    name: "Salsa",
    description: "Percusión caribeña y baile en pareja lleno de sabor.",
    artists: ["Héctor Lavoe", "Celia Cruz", "Marc Anthony", "Gilberto Santa Rosa"],
  },
];

const quizQuestions = [
  {
    question: "¿Qué plan prefieres para un sábado por la noche?",
    options: [
      { text: "Concierto en vivo con mucha energía", scores: { rock: 2, hiphop: 1 } },
      { text: "Fiesta y baile hasta el amanecer", scores: { reggaeton: 2, electronica: 1 } },
      { text: "Cena tranquila con buena música de fondo", scores: { jazz: 2, clasica: 1 } },
      { text: "Karaoke cantando tus éxitos favoritos", scores: { pop: 2, salsa: 1 } },
    ],
  },
  {
    question: "Elige un instrumento",
    options: [
      { text: "Guitarra eléctrica", scores: { rock: 2 } },
      { text: "Sintetizador", scores: { electronica: 2, pop: 1 } },
      { text: "Piano", scores: { jazz: 1, clasica: 2 } },
      { text: "Percusión", scores: { salsa: 2, reggaeton: 1 } },
    ],
  },
  {
    question: "¿Qué valoras más en una canción?",
    options: [
      { text: "La letra y el mensaje", scores: { hiphop: 2, rock: 1 } },
      { text: "El ritmo para bailar", scores: { reggaeton: 2, salsa: 1 } },
      { text: "La producción y los sonidos", scores: { electronica: 2, pop: 1 } },
      { text: "La técnica y la armonía", scores: { jazz: 2, clasica: 1 } },
    ],
  },
  {
    question: "Tu película o serie favorita probablemente tiene...",
    options: [
      { text: "Una banda sonora orquestal épica", scores: { clasica: 2 } },
      { text: "Escenas de fiesta con mucho beat", scores: { electronica: 2, reggaeton: 1 } },
      { text: "Un soundtrack lleno de clásicos del rock", scores: { rock: 2 } },
      { text: "Momentos con salsa o ritmos latinos", scores: { salsa: 2, pop: 1 } },
    ],
  },
  {
    question: "Si pudieras aprender un baile, elegirías...",
    options: [
      { text: "Salsa o bachata", scores: { salsa: 2 } },
      { text: "Perreo / reggaetón", scores: { reggaeton: 2 } },
      { text: "Breakdance", scores: { hiphop: 2 } },
      { text: "Ninguno, prefiero escuchar sentado", scores: { jazz: 1, clasica: 1 } },
    ],
  },
];

// ---------- Render genres ----------
const genreGrid = document.getElementById("genreGrid");
genres.forEach((g) => {
  const card = document.createElement("div");
  card.className = "genre-card";
  card.innerHTML = `
    <div class="genre-icon">${g.icon}</div>
    <h3>${g.name}</h3>
    <p>${g.description}</p>
  `;
  genreGrid.appendChild(card);
});

// ---------- Render artist filters + grid ----------
const artistFilters = document.getElementById("artistFilters");
const artistGrid = document.getElementById("artistGrid");
const favGenreSelect = document.getElementById("favGenre");

function renderArtists(genreId) {
  artistGrid.innerHTML = "";
  const list = genreId === "all" ? genres : genres.filter((g) => g.id === genreId);
  list.forEach((g) => {
    g.artists.forEach((artist) => {
      const card = document.createElement("div");
      card.className = "artist-card";
      card.innerHTML = `
        <div class="artist-avatar">${g.icon}</div>
        <h4>${artist}</h4>
        <span>${g.name}</span>
      `;
      artistGrid.appendChild(card);
    });
  });
}

const allBtn = document.createElement("button");
allBtn.className = "filter-btn active";
allBtn.textContent = "Todos";
allBtn.dataset.genre = "all";
artistFilters.appendChild(allBtn);

genres.forEach((g) => {
  const btn = document.createElement("button");
  btn.className = "filter-btn";
  btn.textContent = `${g.icon} ${g.name}`;
  btn.dataset.genre = g.id;
  artistFilters.appendChild(btn);

  const option = document.createElement("option");
  option.value = g.id;
  option.textContent = g.name;
  favGenreSelect.appendChild(option);
});

artistFilters.addEventListener("click", (e) => {
  const btn = e.target.closest(".filter-btn");
  if (!btn) return;
  artistFilters.querySelectorAll(".filter-btn").forEach((b) => b.classList.remove("active"));
  btn.classList.add("active");
  renderArtists(btn.dataset.genre);
});

renderArtists("all");

// ---------- Quiz logic ----------
const quizQuestionEl = document.getElementById("quizQuestion");
const quizResultEl = document.getElementById("quizResult");
const quizProgress = document.getElementById("quizProgress");
const resultGenreEl = document.getElementById("resultGenre");
const resultDescEl = document.getElementById("resultDesc");
const restartBtn = document.getElementById("restartQuiz");

let currentQuestion = 0;
let scores = {};

function startQuiz() {
  currentQuestion = 0;
  scores = {};
  quizResultEl.classList.add("hidden");
  quizQuestionEl.classList.remove("hidden");
  renderQuestion();
}

function renderQuestion() {
  const q = quizQuestions[currentQuestion];
  quizProgress.style.width = `${((currentQuestion) / quizQuestions.length) * 100}%`;

  quizQuestionEl.innerHTML = `
    <h3>${q.question}</h3>
    <div class="quiz-options">
      ${q.options
        .map((opt, i) => `<button class="quiz-option" data-index="${i}">${opt.text}</button>`)
        .join("")}
    </div>
  `;

  quizQuestionEl.querySelectorAll(".quiz-option").forEach((btn) => {
    btn.addEventListener("click", () => {
      const opt = q.options[parseInt(btn.dataset.index, 10)];
      Object.entries(opt.scores).forEach(([genre, value]) => {
        scores[genre] = (scores[genre] || 0) + value;
      });
      currentQuestion++;
      if (currentQuestion < quizQuestions.length) {
        renderQuestion();
      } else {
        showResult();
      }
    });
  });
}

function showResult() {
  quizProgress.style.width = "100%";
  quizQuestionEl.classList.add("hidden");
  quizResultEl.classList.remove("hidden");

  let topGenreId = Object.keys(scores)[0];
  Object.entries(scores).forEach(([id, value]) => {
    if (value > (scores[topGenreId] || 0)) topGenreId = id;
  });

  const topGenre = genres.find((g) => g.id === topGenreId) || genres[0];
  resultGenreEl.textContent = `${topGenre.icon} ${topGenre.name}`;
  resultDescEl.textContent = topGenre.description;
}

restartBtn.addEventListener("click", startQuiz);
startQuiz();

// ---------- Contact form ----------
const contactForm = document.getElementById("contactForm");
const formFeedback = document.getElementById("formFeedback");

contactForm.addEventListener("submit", (e) => {
  e.preventDefault();
  formFeedback.classList.remove("hidden");
  contactForm.reset();
  setTimeout(() => formFeedback.classList.add("hidden"), 4000);
});

// ---------- Mobile nav ----------
const navToggle = document.getElementById("navToggle");
const navLinks = document.getElementById("navLinks");

navToggle.addEventListener("click", () => {
  navLinks.classList.toggle("open");
});

navLinks.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => navLinks.classList.remove("open"));
});

// ---------- Footer year ----------
document.getElementById("year").textContent = new Date().getFullYear();
