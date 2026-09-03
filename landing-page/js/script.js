// ---------- Data ----------
const origins = [
  {
    country: "Huila, Colombia",
    farm: "Finca La Esperanza",
    altitude: "1,750 msnm",
    process: "Lavado",
    notes: "Panela, ciruela y cacao. El lote insignia de esta temporada.",
  },
  {
    country: "Yirgacheffe, Etiopía",
    farm: "Cooperativa Konga",
    altitude: "2,050 msnm",
    process: "Natural",
    notes: "Jazmín, durazno y té negro. Perfil floral muy marcado.",
  },
  {
    country: "Huehuetenango, Guatemala",
    farm: "Finca El Injerto",
    altitude: "1,900 msnm",
    process: "Honey",
    notes: "Caramelo, manzana roja y un final a almendra tostada.",
  },
  {
    country: "Tarrazú, Costa Rica",
    farm: "Finca Santa Teresa",
    altitude: "1,600 msnm",
    process: "Lavado",
    notes: "Cítricos, miel de abeja y cuerpo cremoso.",
  },
];

const plans = [
  {
    name: "Esencial",
    desc: "Una bolsa de 340 g. Ideal si tomas café solo por las mañanas.",
    basePrice: 16,
    weight: "340 g",
    featured: false,
    features: ["1 bolsa de 340 g por envío", "Molienda a tu método", "Ficha de origen incluida"],
  },
  {
    name: "Pareja",
    desc: "Dos bolsas de 340 g. El plan que más se repite en casas de dos.",
    basePrice: 28,
    weight: "2 × 340 g",
    featured: true,
    features: [
      "2 bolsas de 340 g por envío",
      "Molienda a tu método",
      "Ficha de origen incluida",
      "Acceso anticipado a lotes limitados",
    ],
  },
  {
    name: "Oficina",
    desc: "Cinco bolsas de 340 g para equipos de hasta 10 personas.",
    basePrice: 52,
    weight: "5 × 340 g",
    featured: false,
    features: [
      "5 bolsas de 340 g por envío",
      "Molienda a tu método",
      "Ficha de origen incluida",
      "Factura para tu empresa",
    ],
  },
];

const faqs = [
  {
    q: "¿Puedo pausar o cancelar cuando quiera?",
    a: "Sí. Desde tu cuenta puedes pausar un envío, saltarlo o cancelar la suscripción en cualquier momento, sin costos ni permanencia mínima.",
  },
  {
    q: "¿Cómo eligen los lotes de cada temporada?",
    a: "Catamos cada lote antes de confirmarlo con la finca. Solo entra al catálogo el café que supera 84 puntos en nuestra tabla de catación interna.",
  },
  {
    q: "¿Puedo cambiar el método de molienda entre envíos?",
    a: "Claro. Puedes actualizar tu método (grano entero, filtrado, espresso o prensa francesa) hasta 48 horas antes de que se prepare tu pedido.",
  },
  {
    q: "¿A qué países envían?",
    a: "Por ahora entregamos en Colombia, México, Argentina, Chile y Costa Rica. Estamos sumando nuevos países cada trimestre.",
  },
];

// ---------- Render origins ----------
const originGrid = document.getElementById("originGrid");
origins.forEach((o) => {
  const card = document.createElement("div");
  card.className = "origin-card";
  card.innerHTML = `
    <span class="origin-country">${o.country}</span>
    <h3>${o.farm}</h3>
    <div class="origin-meta">
      <div><strong>${o.altitude}</strong><span>Altitud</span></div>
      <div><strong>${o.process}</strong><span>Proceso</span></div>
    </div>
    <p class="origin-notes">${o.notes}</p>
  `;
  originGrid.appendChild(card);
});

// ---------- Render plans ----------
const planGrid = document.getElementById("planGrid");
const toggleBtns = document.querySelectorAll(".toggle-btn");
let currentFreq = "2";

function renderPlans(freq) {
  planGrid.innerHTML = "";
  const discount = freq === "2" ? 0.95 : 1;
  const freqLabel = freq === "2" ? "cada 2 semanas" : "cada 4 semanas";

  plans.forEach((p) => {
    const price = (p.basePrice * discount).toFixed(2);
    const card = document.createElement("div");
    card.className = `plan-card${p.featured ? " featured" : ""}`;
    card.innerHTML = `
      ${p.featured ? '<span class="plan-badge">Más elegido</span>' : ""}
      <h3>${p.name}</h3>
      <p class="plan-desc">${p.desc}</p>
      <div class="plan-price">$${price}<span> USD</span></div>
      <p class="plan-per">${p.weight} · entregado ${freqLabel}</p>
      <ul class="plan-features">
        ${p.features.map((f) => `<li>${f}</li>`).join("")}
      </ul>
      <a href="#inicio" class="btn ${p.featured ? "btn-primary" : "btn-ghost"}">Elegir ${p.name}</a>
    `;
    planGrid.appendChild(card);
  });
}

toggleBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    toggleBtns.forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    currentFreq = btn.dataset.freq;
    renderPlans(currentFreq);
  });
});

renderPlans(currentFreq);

// ---------- Render FAQ ----------
const faqList = document.getElementById("faqList");
faqs.forEach((item) => {
  const el = document.createElement("div");
  el.className = "faq-item";
  el.innerHTML = `
    <button class="faq-question">
      ${item.q}
      <span class="faq-icon">+</span>
    </button>
    <div class="faq-answer">
      <p>${item.a}</p>
    </div>
  `;
  faqList.appendChild(el);
});

faqList.addEventListener("click", (e) => {
  const btn = e.target.closest(".faq-question");
  if (!btn) return;
  const item = btn.closest(".faq-item");
  const answer = item.querySelector(".faq-answer");
  const isOpen = item.classList.contains("open");

  faqList.querySelectorAll(".faq-item.open").forEach((openItem) => {
    openItem.classList.remove("open");
    openItem.querySelector(".faq-answer").style.maxHeight = null;
  });

  if (!isOpen) {
    item.classList.add("open");
    answer.style.maxHeight = `${answer.scrollHeight}px`;
  }
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
