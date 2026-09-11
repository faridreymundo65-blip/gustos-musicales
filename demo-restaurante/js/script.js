/* =========================================================
   Mar Bravo — demo de cevichería
   Para adaptar a un cliente real, cambia solo estas 3 cosas:
     1. WHATSAPP  -> el celular del negocio (formato 51 + 9 digitos)
     2. HORARIO   -> sus horas de atencion
     3. CARTA     -> sus platos y precios
   ========================================================= */

const WHATSAPP = "51987654321";

// 0 = domingo ... 6 = sabado.  null = cerrado
const HORARIO = {
  0: { abre: "11:00", cierra: "17:00" },
  1: null,
  2: { abre: "12:00", cierra: "17:00" },
  3: { abre: "12:00", cierra: "17:00" },
  4: { abre: "12:00", cierra: "22:00" },
  5: { abre: "12:00", cierra: "23:00" },
  6: { abre: "11:00", cierra: "23:00" },
};

const DIAS = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"];

const CARTA = [
  { cat: "Ceviches", nombre: "Ceviche Mar Bravo", precio: 42, badge: "El clásico", hot: true,
    desc: "Lenguado del día, ají limo, cebolla morada, choclo y camote glaseado." },
  { cat: "Ceviches", nombre: "Ceviche mixto", precio: 46,
    desc: "Pescado, pulpo, langostinos y calamar en leche de tigre de la casa." },
  { cat: "Ceviches", nombre: "Ceviche de conchas negras", precio: 54, badge: "Según pesca",
    desc: "Conchas de Tumbes, limón, culantro y ají limo. Solo cuando llegan frescas." },
  { cat: "Ceviches", nombre: "Tiradito al rocoto", precio: 38,
    desc: "Láminas finas de lenguado en crema de rocoto arequipeño." },
  { cat: "Ceviches", nombre: "Leche de tigre", precio: 22,
    desc: "Vaso de leche de tigre con trozos de pescado, chicharrón y cancha." },

  { cat: "Entradas", nombre: "Causa de cangrejo", precio: 28, badge: "Favorito",
    desc: "Papa amarilla prensada, cangrejo fresco y palta." },
  { cat: "Entradas", nombre: "Choritos a la chalaca", precio: 24,
    desc: "Seis choritos con sarsa de cebolla, choclo y limón." },
  { cat: "Entradas", nombre: "Pulpo al olivo", precio: 34,
    desc: "Pulpo tierno en mayonesa de aceituna botija." },
  { cat: "Entradas", nombre: "Chicharrón de calamar", precio: 30,
    desc: "Anillos apanados en chuño, con sarsa criolla y crema de rocoto." },

  { cat: "Platos de fondo", nombre: "Jalea mixta", precio: 58, badge: "Para 2-3", hot: true,
    desc: "Chicharrón de pescado y mariscos con yuca frita y sarsa." },
  { cat: "Platos de fondo", nombre: "Arroz con mariscos", precio: 44,
    desc: "Arroz meloso con langostinos, calamar, choritos y culantro." },
  { cat: "Platos de fondo", nombre: "Sudado de tramboyo", precio: 48,
    desc: "Caldo corto con chicha de jora, tomate y ají amarillo. Con arroz blanco." },
  { cat: "Platos de fondo", nombre: "Chita a la parrilla", precio: 52,
    desc: "Chita entera al carbón, ensalada fresca y papa nativa." },
  { cat: "Platos de fondo", nombre: "Arroz chaufa de mariscos", precio: 42,
    desc: "Chaufa al wok con langostinos, calamar y tortilla." },

  { cat: "Bebidas", nombre: "Chicha morada de la casa", precio: 10,
    desc: "Jarra chica, sin azúcar añadida." },
  { cat: "Bebidas", nombre: "Limonada frozen", precio: 12, desc: "Vaso de 400 ml." },
  { cat: "Bebidas", nombre: "Pisco sour", precio: 24, desc: "Pisco quebranta, limón y amargo de angostura." },
  { cat: "Bebidas", nombre: "Chilcano de maracuyá", precio: 22, desc: "Pisco acholado, ginger ale y maracuyá." },
  { cat: "Bebidas", nombre: "Cerveza nacional", precio: 14, desc: "Cusqueña, Pilsen o Cristal." },
  { cat: "Bebidas", nombre: "Inca Kola / gaseosa", precio: 8, desc: "Vaso de 500 ml." },

  { cat: "Postres", nombre: "Suspiro a la limeña", precio: 18, desc: "Manjar blanco y merengue al oporto." },
  { cat: "Postres", nombre: "Picarones", precio: 16, desc: "Seis unidades con miel de chancaca." },
  { cat: "Postres", nombre: "Mazamorra con arroz con leche", precio: 16, desc: "El clásico combinado." },
];

const FAQS = [
  { q: "¿Hacen delivery?",
    a: "Sí, con repartidor propio en Barranco, Miraflores y Chorrillos. El ceviche sale en empaque térmico con la leche de tigre aparte para que llegue en su punto. Pedido mínimo S/ 45." },
  { q: "¿Necesito reservar?",
    a: "De martes a jueves no hace falta. Viernes, sábado y domingo de 12 a 3 conviene reservar por WhatsApp — es cuando se llena." },
  { q: "¿Qué pasa si se acaba el pescado del día?",
    a: "Lo avisamos en la puerta y por WhatsApp apenas se acaba. Preferimos decirte que no hay antes que servirte algo congelado." },
  { q: "¿Tienen opciones sin pescado?",
    a: "Sí: causa de verduras, arroz chaufa de vegetales y papa a la huancaína. Avísanos si hay alergia a mariscos y preparamos en sartén aparte." },
  { q: "¿Qué medios de pago aceptan?",
    a: "Yape, Plin, efectivo y todas las tarjetas. Para delivery se puede pagar por Yape al confirmar el pedido." },
  { q: "¿Se puede ir con niños?",
    a: "Claro. Hay sillas altas y media porción de arroz con mariscos o chaufa a mitad de precio." },
];

/* ---------- utilidades ---------- */
const $ = (id) => document.getElementById(id);
const soles = (n) => `S/ ${n}`;
const minutos = (hhmm) => {
  const [h, m] = hhmm.split(":").map(Number);
  return h * 60 + m;
};

/* ---------- estado abierto / cerrado ---------- */
function pintarEstado() {
  const ahora = new Date();
  const hoy = HORARIO[ahora.getDay()];
  const dot = $("statusDot");
  const txt = $("statusText");
  if (!dot || !txt) return;

  if (!hoy) {
    dot.classList.add("closed");
    txt.textContent = "Hoy cerrado · Barranco, Lima";
    return;
  }

  const min = ahora.getHours() * 60 + ahora.getMinutes();
  if (min >= minutos(hoy.abre) && min < minutos(hoy.cierra)) {
    dot.classList.add("open");
    txt.textContent = `Abierto ahora · cierra ${hoy.cierra}`;
  } else {
    dot.classList.add("closed");
    txt.textContent = min < minutos(hoy.abre)
      ? `Cerrado · abre hoy ${hoy.abre}`
      : "Cerrado por hoy · Barranco, Lima";
  }
}

/* ---------- tabla de horarios ---------- */
function pintarHorario() {
  const tabla = $("hoursTable");
  if (!tabla) return;
  const hoy = new Date().getDay();
  const orden = [1, 2, 3, 4, 5, 6, 0];            // empieza en lunes

  tabla.innerHTML = orden.map((d) => {
    const h = HORARIO[d];
    const rango = h ? `${h.abre} – ${h.cierra}` : "Cerrado";
    return `<tr class="${d === hoy ? "today" : ""}"><td>${DIAS[d]}</td><td>${rango}</td></tr>`;
  }).join("");
}

/* ---------- carta + carrito ---------- */
const carrito = new Map();                        // nombre -> cantidad
let categoriaActiva = "Ceviches";

function categorias() {
  return [...new Set(CARTA.map((p) => p.cat))];
}

function pintarTabs() {
  const cont = $("menuTabs");
  cont.innerHTML = categorias().map((c) =>
    `<button class="tab${c === categoriaActiva ? " active" : ""}" data-cat="${c}" role="tab">${c}</button>`
  ).join("");
}

function pintarPlatos() {
  const cont = $("menuGrid");
  const platos = CARTA.filter((p) => p.cat === categoriaActiva);

  cont.innerHTML = platos.map((p) => {
    const cant = carrito.get(p.nombre) || 0;
    const controles = cant > 0
      ? `<button class="qty-btn" data-accion="quitar" data-plato="${p.nombre}" aria-label="Quitar uno">−</button>
         <span class="qty-num">${cant}</span>
         <button class="qty-btn add" data-accion="agregar" data-plato="${p.nombre}" aria-label="Agregar uno">+</button>`
      : `<button class="qty-btn add" data-accion="agregar" data-plato="${p.nombre}" aria-label="Agregar ${p.nombre}">+</button>`;

    return `
      <article class="dish${cant > 0 ? " in-cart" : ""}">
        <div class="dish-body">
          <div class="dish-top">
            <h3 class="dish-name">${p.nombre}</h3>
            ${p.badge ? `<span class="dish-badge${p.hot ? " hot" : ""}">${p.badge}</span>` : ""}
          </div>
          <p class="dish-desc">${p.desc}</p>
          <span class="dish-price">${soles(p.precio)}</span>
        </div>
        <div class="dish-controls">${controles}</div>
      </article>`;
  }).join("");
}

function precioDe(nombre) {
  const p = CARTA.find((x) => x.nombre === nombre);
  return p ? p.precio : 0;
}

function pintarPedido() {
  const barra = $("orderBar");
  const total = [...carrito].reduce((s, [n, c]) => s + precioDe(n) * c, 0);
  const items = [...carrito.values()].reduce((s, c) => s + c, 0);

  if (items === 0) {
    barra.hidden = true;
    document.body.classList.remove("has-order");
    $("orderDetail").hidden = true;
    $("orderSummary").setAttribute("aria-expanded", "false");
    return;
  }

  barra.hidden = false;
  document.body.classList.add("has-order");
  $("orderCount").textContent = items;
  $("orderTotal").textContent = soles(total);

  $("orderDetail").innerHTML = [...carrito].map(([n, c]) =>
    `<div class="order-row"><span>${c} × ${n}</span><span>${soles(precioDe(n) * c)}</span></div>`
  ).join("");

  // Mensaje de WhatsApp ya armado
  const lineas = [...carrito].map(([n, c]) => `• ${c} × ${n} — ${soles(precioDe(n) * c)}`);
  const texto =
    `Hola Mar Bravo, quiero hacer este pedido:\n\n` +
    lineas.join("\n") +
    `\n\nTotal: ${soles(total)}\n\n` +
    `¿Me confirman disponibilidad y tiempo de entrega?`;

  $("orderSend").href = `https://wa.me/${WHATSAPP}?text=${encodeURIComponent(texto)}`;
}

/* ---------- FAQ ---------- */
function pintarFaq() {
  const lista = $("faqList");
  lista.innerHTML = FAQS.map((f) => `
    <div class="faq-item">
      <button class="faq-question" aria-expanded="false">
        ${f.q}<span class="faq-icon" aria-hidden="true">+</span>
      </button>
      <div class="faq-answer"><p>${f.a}</p></div>
    </div>`).join("");
}

/* ---------- eventos ---------- */
document.addEventListener("DOMContentLoaded", () => {
  pintarEstado();
  pintarHorario();
  pintarTabs();
  pintarPlatos();
  pintarFaq();

  // cambiar de categoria
  $("menuTabs").addEventListener("click", (e) => {
    const tab = e.target.closest(".tab");
    if (!tab) return;
    categoriaActiva = tab.dataset.cat;
    pintarTabs();
    pintarPlatos();
  });

  // agregar / quitar platos
  $("menuGrid").addEventListener("click", (e) => {
    const btn = e.target.closest(".qty-btn");
    if (!btn) return;
    const nombre = btn.dataset.plato;
    const actual = carrito.get(nombre) || 0;

    if (btn.dataset.accion === "agregar") {
      carrito.set(nombre, actual + 1);
    } else if (actual <= 1) {
      carrito.delete(nombre);
    } else {
      carrito.set(nombre, actual - 1);
    }
    pintarPlatos();
    pintarPedido();
  });

  // abrir / cerrar el detalle del pedido
  $("orderSummary").addEventListener("click", () => {
    const det = $("orderDetail");
    det.hidden = !det.hidden;
    $("orderSummary").setAttribute("aria-expanded", String(!det.hidden));
  });

  // acordeon de preguntas
  const lista = $("faqList");
  lista.addEventListener("click", (e) => {
    const btn = e.target.closest(".faq-question");
    if (!btn) return;
    const item = btn.closest(".faq-item");
    const resp = item.querySelector(".faq-answer");
    const abierto = item.classList.contains("open");

    lista.querySelectorAll(".faq-item.open").forEach((otro) => {
      otro.classList.remove("open");
      otro.querySelector(".faq-answer").style.maxHeight = null;
      otro.querySelector(".faq-question").setAttribute("aria-expanded", "false");
    });

    if (!abierto) {
      item.classList.add("open");
      resp.style.maxHeight = `${resp.scrollHeight}px`;
      btn.setAttribute("aria-expanded", "true");
    }
  });

  // menu movil
  const toggle = $("navToggle");
  const links = $("navLinks");
  toggle.addEventListener("click", () => {
    const abierto = links.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(abierto));
  });
  links.querySelectorAll("a").forEach((a) =>
    a.addEventListener("click", () => {
      links.classList.remove("open");
      toggle.setAttribute("aria-expanded", "false");
    })
  );

  $("year").textContent = new Date().getFullYear();
});
