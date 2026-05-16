<!DOCTYPE html>
<html lang="es">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1.0" />
  <title>TikTok en Salud — Presentación 2025</title>
  <link rel="preconnect" href="https://api.fontshare.com" />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=satoshi@400,500,700&display=swap"
    rel="stylesheet" />
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
  <style>
    /* ── RESET & VIEWPORT BASE ── */
    *,
    *::before,
    *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0
    }

    html {
      scroll-snap-type: y mandatory;
      scroll-behavior: smooth;
      height: 100%;
      overflow-x: hidden
    }

    body {
      height: 100%;
      overflow-x: hidden;
      font-family: 'Satoshi', sans-serif;
      background: #0a0f1c;
      color: #e8eaf6
    }

    /* ── TOKENS ── */
    :root {
      --red: #fe2c55;
      --cyan: #25f4ee;
      --purple: #9c27b0;
      --gold: #ffd700;
      --blue: #2196f3;
      --bg: #0a0f1c;
      --surface: rgba(255, 255, 255, .04);
      --border: rgba(255, 255, 255, .08);
      --glass: rgba(255, 255, 255, .06);
      --glass-border: rgba(255, 255, 255, .12);
      --text: #e8eaf6;
      --muted: #8892b0;
      --title-size: clamp(1.8rem, 5vw, 4.2rem);
      --h2-size: clamp(1.3rem, 3.2vw, 2.4rem);
      --h3-size: clamp(1rem, 2.2vw, 1.6rem);
      --body-size: clamp(.78rem, 1.4vw, 1.05rem);
      --small-size: clamp(.65rem, .9vw, .85rem);
      --pad: clamp(1.2rem, 4vw, 3.5rem);
      --gap: clamp(.5rem, 2vw, 1.5rem);
    }

    /* ── SLIDES ── */
    .slide {
      width: 100vw;
      height: 100vh;
      height: 100dvh;
      overflow: hidden;
      scroll-snap-align: start;
      display: flex;
      flex-direction: column;
      position: relative;
      padding: var(--pad)
    }

    /* Mesh background */
    .slide::before {
      content: '';
      position: absolute;
      inset: 0;
      pointer-events: none;
      background-image: linear-gradient(rgba(255, 255, 255, .02) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, .02) 1px, transparent 1px);
      background-size: 60px 60px
    }

    /* ── GLASS CARD ── */
    .glass {
      background: var(--glass);
      border: 1px solid var(--glass-border);
      border-radius: 20px;
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px)
    }

    /* ── NAV ── */
    #nav {
      position: fixed;
      bottom: 1.8rem;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      align-items: center;
      gap: .7rem;
      z-index: 100;
      background: rgba(10, 15, 28, .7);
      backdrop-filter: blur(12px);
      border: 1px solid var(--border);
      border-radius: 50px;
      padding: .45rem .9rem
    }

    .dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--muted);
      cursor: pointer;
      transition: all .3s;
      border: none
    }

    .dot.active {
      background: var(--red);
      width: 22px;
      border-radius: 4px
    }

    .nav-btn {
      background: none;
      border: none;
      color: var(--muted);
      cursor: pointer;
      font-size: 1rem;
      padding: .1rem .3rem;
      transition: color .2s
    }

    .nav-btn:hover {
      color: var(--text)
    }

    #slide-counter {
      font-size: .7rem;
      color: var(--muted);
      font-family: 'Satoshi';
      min-width: 3rem;
      text-align: center
    }



    /* ── REVEAL ANIMATIONS ── */
    .reveal {
      opacity: 0;
      transform: translateY(28px);
      transition: opacity .65s cubic-bezier(.16, 1, .3, 1), transform .65s cubic-bezier(.16, 1, .3, 1)
    }

    .reveal-left {
      opacity: 0;
      transform: translateX(-40px);
      transition: opacity .65s cubic-bezier(.16, 1, .3, 1), transform .65s cubic-bezier(.16, 1, .3, 1)
    }

    .slide.active .reveal,
    .slide.active .reveal-left {
      opacity: 1;
      transform: none
    }

    .slide.active .reveal:nth-child(2) {
      transition-delay: .1s
    }

    .slide.active .reveal:nth-child(3) {
      transition-delay: .18s
    }

    .slide.active .reveal:nth-child(4) {
      transition-delay: .26s
    }

    .slide.active .reveal:nth-child(5) {
      transition-delay: .34s
    }

    .slide.active .reveal:nth-child(6) {
      transition-delay: .42s
    }

    /* ── BADGE ── */
    .badge {
      display: inline-flex;
      align-items: center;
      gap: .4rem;
      background: rgba(254, 44, 85, .12);
      border: 1px solid rgba(254, 44, 85, .35);
      color: var(--red);
      font-size: var(--small-size);
      font-weight: 700;
      letter-spacing: .08em;
      text-transform: uppercase;
      padding: .35rem 1rem;
      border-radius: 50px;
      font-family: 'Satoshi'
    }

    .badge-cyan {
      background: rgba(37, 244, 238, .1);
      border-color: rgba(37, 244, 238, .3);
      color: var(--cyan)
    }

    /* ── GRADIENT TEXT ── */
    .gtext {
      background: linear-gradient(135deg, var(--red) 0%, var(--purple) 50%, var(--cyan) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text
    }

    /* ── KPI GRID ── */
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: var(--gap);
      margin-top: var(--gap)
    }

    .kpi-card {
      padding: 1.4rem 1rem;
      text-align: center;
      border-radius: 18px;
      cursor: default;
      transition: transform .4s cubic-bezier(.16, 1, .3, 1), box-shadow .4s;
      transform-style: preserve-3d;
      will-change: transform
    }

    .kpi-card:hover {
      transform: translateY(-6px) rotateX(-4deg) rotateY(4deg);
      box-shadow: 0 24px 48px rgba(254, 44, 85, .15)
    }

    .kpi-num {
      font-family: 'Clash Display';
      font-size: clamp(1.8rem, 3.5vw, 3rem);
      font-weight: 700;
      display: block;
      line-height: 1
    }

    .kpi-label {
      font-size: var(--small-size);
      color: var(--muted);
      margin-top: .5rem;
      line-height: 1.4
    }

    .kpi-src {
      font-size: .6rem;
      color: #333d55;
      margin-top: .4rem;
      font-style: italic
    }

    /* ── CHART CARD ── */
    .chart-card {
      padding: 1.4rem;
      border-radius: 18px;
      height: 100%;
      display: flex;
      flex-direction: column
    }

    .chart-card h3 {
      font-family: 'Clash Display';
      font-size: var(--h3-size);
      margin-bottom: .3rem
    }

    .chart-card .sub {
      font-size: var(--small-size);
      color: var(--muted);
      margin-bottom: 1rem;
      line-height: 1.5
    }

    .chart-wrap {
      flex: 1;
      position: relative;
      min-height: 0
    }

    .chart-wrap canvas {
      max-height: 100% !important
    }

    .src-tag {
      font-size: .6rem;
      color: #333d55;
      margin-top: .6rem;
      font-style: italic;
      border-top: 1px solid var(--border);
      padding-top: .4rem
    }

    /* ── GRID LAYOUTS ── */
    .g2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: var(--gap);
      flex: 1;
      min-height: 0
    }

    .g3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: var(--gap)
    }

    /* ── FACT PILLS ── */
    .fact-pill {
      display: flex;
      gap: 1rem;
      align-items: flex-start;
      padding: 1rem 1.2rem;
      border-radius: 14px
    }

    .pill-num {
      font-family: 'Clash Display';
      font-size: clamp(1.4rem, 2.8vw, 2.2rem);
      font-weight: 700;
      line-height: 1;
      white-space: nowrap
    }

    .pill-text {
      font-size: var(--small-size);
      color: var(--muted);
      line-height: 1.45
    }

    .pill-src {
      font-size: .6rem;
      color: #333d55;
      margin-top: .3rem;
      font-style: italic
    }

    /* ── PROGRESS BARS ── */
    .prog-list {
      display: flex;
      flex-direction: column;
      gap: 1rem
    }

    .prog-item label {
      display: flex;
      justify-content: space-between;
      font-size: var(--small-size);
      color: var(--muted);
      margin-bottom: .4rem
    }

    .prog-item label b {
      color: var(--text)
    }

    .prog-track {
      height: 11px;
      background: rgba(255, 255, 255, .05);
      border-radius: 99px;
      overflow: hidden
    }

    .prog-fill {
      height: 100%;
      border-radius: 99px;
      width: 0;
      transition: width 1.4s cubic-bezier(.4, 0, .2, 1)
    }

    .fill-tk {
      background: linear-gradient(90deg, #fe2c55, #ff758c)
    }

    .fill-ig {
      background: linear-gradient(90deg, #e1306c, #833ab4)
    }

    .fill-fb {
      background: linear-gradient(90deg, #1877f2, #42b0ff)
    }

    .fill-yt {
      background: linear-gradient(90deg, #ff0000, #ff6b6b)
    }

    .fill-tw {
      background: linear-gradient(90deg, #1da1f2, #0d8ecf)
    }

    /* ── INSIGHT LIST ── */
    .ins-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: .9rem
    }

    .ins-list li {
      display: flex;
      align-items: flex-start;
      gap: .9rem;
      font-size: var(--body-size);
      line-height: 1.55
    }

    .ins-list li strong {
      color: var(--text)
    }

    .ins-num {
      font-family: 'Clash Display';
      font-size: 1.6rem;
      font-weight: 700;
      color: var(--red);
      opacity: .6;
      min-width: 2rem;
      line-height: 1
    }

    /* ── CTA BUTTON ── */
    .cta-btn {
      display: inline-flex;
      align-items: center;
      gap: .5rem;
      background: linear-gradient(135deg, var(--red), var(--purple));
      color: #fff;
      font-weight: 700;
      font-family: 'Satoshi';
      padding: .75rem 1.8rem;
      border-radius: 50px;
      border: none;
      cursor: pointer;
      font-size: .9rem;
      letter-spacing: .04em;
      transition: opacity .2s, transform .2s;
      margin-top: 1rem
    }

    .cta-btn:hover {
      opacity: .85;
      transform: translateY(-2px)
    }

    /* ── SLIDE HEADINGS ── */
    .slide-title {
      font-family: 'Clash Display';
      font-size: var(--h2-size);
      font-weight: 700;
      margin-bottom: .3rem
    }

    .slide-sub {
      font-size: var(--body-size);
      color: var(--muted);
      margin-bottom: var(--gap)
    }

    /* ── RESPONSIVE ── */
    @media(max-width:860px) {
      .kpi-grid {
        grid-template-columns: repeat(3, 1fr)
      }

      .g2 {
        grid-template-columns: 1fr
      }

      .g3 {
        grid-template-columns: 1fr 1fr
      }
    }

    @media(max-width:600px) {
      .kpi-grid {
        grid-template-columns: repeat(2, 1fr)
      }

      .g3 {
        grid-template-columns: 1fr
      }
    }

    @media(max-height:620px) {
      :root {
        --title-size: clamp(1.4rem, 4vw, 2.8rem);
        --h2-size: clamp(1.1rem, 2.8vw, 2rem);
        --pad: 1rem
      }
    }

    @media(prefers-reduced-motion:reduce) {
      * {
        animation-duration: .01ms !important;
        transition-duration: .2s !important
      }

      html {
        scroll-behavior: auto
      }
    }
  </style>
</head>

<body>



  <!-- ═══ NAVIGATION ═══ -->
  <div id="nav">
    <button class="nav-btn" id="btn-prev">←</button>
    <div id="dots"></div>
    <span id="slide-counter">01 / 11</span>
    <button class="nav-btn" id="btn-next">→</button>
  </div>

  <!-- ════════════════════════════════════════
     SLIDE 1 — HERO
════════════════════════════════════════ -->
  <section class="slide" id="s1" style="justify-content:center;align-items:flex-start;
  background:radial-gradient(ellipse 70% 60% at 80% 50%,rgba(254,44,85,.18) 0%,transparent 65%),
             radial-gradient(ellipse 50% 40% at 10% 80%,rgba(37,244,238,.1) 0%,transparent 60%),
             var(--bg)">

    <div class="reveal"><span class="badge">📱 Campaña Sector Salud · 2025</span></div>

    <h1 class="reveal" style="font-family:'Clash Display';font-size:var(--title-size);
    font-weight:700;line-height:1.08;margin:1.2rem 0;max-width:14ch">
      Análisis TikTok para Campañas de Salud</br>

    </h1>

    <p class="reveal" style="font-size:var(--body-size);color:var(--muted);
    max-width:52ch;line-height:1.7;margin-bottom:1.4rem">
      Este informe demuestra, con datos verificados de 2024-2025, por qué toda campaña de salud
      que ignore TikTok deja de llegar a su audiencia más receptiva y más activa del mundo.
    </p>

    <div class="reveal" style="display:flex;gap:.7rem;flex-wrap:wrap">
      <span class="badge badge-cyan">🩺 Datos sector salud 2024 / 2025</span>
      <span class="badge">📊 10 fuentes verificadas</span>
    </div>

    <!-- decorative circle -->
    <div style="position:absolute;right:-80px;top:50%;transform:translateY(-50%);
    width:clamp(260px,35vw,520px);height:clamp(260px,35vw,520px);
    border-radius:50%;border:1px solid rgba(254,44,85,.12);pointer-events:none"></div>
    <div style="position:absolute;right:20px;top:50%;transform:translateY(-50%);
    width:clamp(160px,22vw,340px);height:clamp(160px,22vw,340px);
    border-radius:50%;border:1px solid rgba(37,244,238,.1);pointer-events:none"></div>
  </section>

  <!-- ════════════════════════════════════════
     SLIDE 2 — KPIs
════════════════════════════════════════ -->
  <section class="slide" id="s2" style="justify-content:center;
  background:radial-gradient(ellipse 60% 50% at 50% 0%,rgba(254,44,85,.12) 0%,transparent 60%),var(--bg)">

    <div class="reveal badge" style="display:inline-flex;margin-bottom:1rem">⚡ Números que cambian la conversación</div>

    <h2 class="reveal slide-title">Los 5 datos que definen la oportunidad</h2>
    <p class="reveal slide-sub">Cada cifra es una razón concreta para incluir TikTok en la campaña de salud.</p>

    <div class="kpi-grid">
      <div class="kpi-card glass reveal" id="k2">
        <span class="kpi-num" style="color:var(--red)">$32.46</span>
        <div class="kpi-label">CPL Promedio(Meta)</div>
        <div class="kpi-src">WordStream / Lima Retail 2025</div>
      </div>
      <div class="kpi-card glass reveal" id="k3">
        <span class="kpi-num" style="color:var(--purple)">4.93%</span>
        <div class="kpi-label">CTR Tráfico TikTok 2025</div>
        <div class="kpi-src">Somos Chili / Metricool 2025</div>
      </div>
      <div class="kpi-card glass reveal" id="k4">
        <span class="kpi-num" style="color:var(--gold)">$5.00</span>
        <div class="kpi-label">CPL TikTok Ads (LATAM AVG)</div>
        <div class="kpi-src">Lima Retail 2025 / Benchmarks</div>
      </div>
      <div class="kpi-card glass reveal" id="k5">
        <span class="kpi-num" style="color:var(--cyan)">$0.01</span>
        <div class="kpi-label">CPC Tráfico TikTok Ads</div>
        <div class="kpi-src">Somos Chili 2025 (Metricool)</div>
      </div>
      <div class="kpi-card glass reveal" id="k6">
        <span class="kpi-num" style="color:var(--cyan)">92%</span>
        <div class="kpi-label">Toma alguna acción<br />tras ver un video</div>
        <div class="kpi-src">TikTok for Business 2024</div>
      </div>
      <div class="kpi-card glass reveal" id="k7">
        <span class="kpi-num" style="color:var(--purple)">35%</span>
        <div class="kpi-label">Acción concreta<br />en contenido de salud</div>
        <div class="kpi-src">TikTok Health Insights 2024</div>
      </div>
      <div class="kpi-card glass reveal" id="k8">
        <span class="kpi-num" style="color:var(--gold)">75min</span>
        <div class="kpi-label">Diarios en TikTok<br />por usuario LATAM</div>
        <div class="kpi-src">ExpressoCompany / Statista 2025</div>
      </div>
      <div class="kpi-card glass reveal" id="k9">
        <span class="kpi-num" style="color:var(--cyan)">10×</span>
        <div class="kpi-label">Más interacciones<br />que en Instagram</div>
        <div class="kpi-src">SocialInsider Benchmark 2025</div>
      </div>
    </div>
  </section>

  <!-- ════════════════════════════════════════
     SLIDE 3 — AUDIENCIA LATAM
════════════════════════════════════════ -->
  <section class="slide" id="s3" style="
  background:radial-gradient(ellipse 50% 60% at 0% 50%,rgba(37,244,238,.08) 0%,transparent 60%),var(--bg)">

    <h2 class="reveal slide-title">🌍 ¿Dónde está nuestra audiencia?</h2>
    <p class="reveal slide-sub">Usuarios activos en TikTok por país — LATAM 2025. Solo 6 países suman más de 289
      millones de personas.</p>

    <div class="g2" style="flex:1;min-height:0">
      <div class="glass chart-card reveal">
        <h3>Usuarios TikTok por país (millones)</h3>
        <div class="sub">Alcance potencial disponible solo con presencia orgánica</div>
        <div class="chart-wrap"><canvas id="cLatam"></canvas></div>
        <div class="src-tag">📌 Resourcera.com / Statista / DataReportal — ene 2025</div>
      </div>
      <div class="glass chart-card reveal">
        <h3>¿Quiénes son? Distribución por edad</h3>
        <div class="sub">El grupo 25–34 es el más grande: adultos jóvenes que deciden sobre la salud familiar</div>
        <div class="chart-wrap"><canvas id="cAge"></canvas></div>
        <div class="src-tag">📌 DreamGrow / GlobalStatistics / DataReportal 2025</div>
      </div>
    </div>
  </section>

  <!-- ════════════════════════════════════════
     SLIDE 4 — COMPORTAMIENTO SALUD
════════════════════════════════════════ -->
  <section class="slide" id="s4" style="
  background:radial-gradient(ellipse 60% 50% at 100% 100%,rgba(156,39,176,.12) 0%,transparent 60%),var(--bg)">

    <h2 class="reveal slide-title">🏥 ¿Qué hace la gente con el contenido de salud?</h2>
    <p class="reveal slide-sub">No solo miran: investigan, comparten y actúan. Tasa de acción inédita en redes sociales.
    </p>

    <div class="g2" style="flex:1;min-height:0">
      <!-- fact pills -->
      <div style="display:flex;flex-direction:column;gap:.7rem">
        <div class="glass fact-pill reveal">
          <div class="pill-num gtext">67%</div>
          <div>
            <div class="pill-text">Busca más información sobre el producto o servicio de salud que vio</div>
            <div class="pill-src">TikTok for Business Health, 2024</div>
          </div>
        </div>
        <div class="glass fact-pill reveal">
          <div class="pill-num" style="color:var(--red)">35%</div>
          <div>
            <div class="pill-text">Toma una acción concreta: busca médico, compra o se registra</div>
            <div class="pill-src">TikTok Health Insights, 2024</div>
          </div>
        </div>
        <div class="glass fact-pill reveal">
          <div class="pill-num" style="color:var(--purple)">28%</div>
          <div>
            <div class="pill-text">Sigue al creador de salud que encontró confiable y útil</div>
            <div class="pill-src">TikTok for Business / Code3, 2024</div>
          </div>
        </div>
        <div class="glass fact-pill reveal">
          <div class="pill-num" style="color:var(--gold)">2.4×</div>
          <div>
            <div class="pill-text">El contenido en video corto se percibe más confiable que publicidad tradicional</div>
            <div class="pill-src">Singlegrain 2024</div>
          </div>
        </div>
      </div>
      <!-- doughnut -->
      <div class="glass chart-card reveal">
        <h3>¿Qué hace alguien tras ver contenido de salud?</h3>
        <div class="sub">9 de cada 10 personas toman algún tipo de acción — una tasa inédita</div>
        <div class="chart-wrap"><canvas id="cActions"></canvas></div>
        <div class="src-tag">📌 TikTok Health Insights 2024 · Code3 Health Report 2024</div>
      </div>
    </div>
  </section>

  <!-- ════════════════════════════════════════
     SLIDE 5 — TIEMPO EN PLATAFORMAS
════════════════════════════════════════ -->
  <section class="slide" id="s5" style="
  background:radial-gradient(ellipse 60% 50% at 60% 20%,rgba(33,150,243,.1) 0%,transparent 60%),var(--bg)">

    <h2 class="reveal slide-title">⏱ Más tiempo = más oportunidades</h2>
    <p class="reveal slide-sub">Minutos diarios por plataforma. TikTok domina en tiempo de atención — el recurso más
      escaso de 2025.</p>

    <div class="g2" style="flex:1;min-height:0">
      <div class="glass chart-card reveal">
        <h3>Tiempo diario promedio por plataforma (min)</h3>
        <div class="sub">LATAM — DataReportal / Statista / ExpressoCompany 2025</div>
        <div class="chart-wrap"><canvas id="cTime"></canvas></div>
        <div class="src-tag">📌 DataReportal 2025 · Statista 2025 · ExpressoCompany 2025</div>
      </div>
      <div style="display:flex;flex-direction:column;justify-content:center;gap:1.2rem">
        <div class="glass reveal" style="padding:1.4rem;border-radius:18px">
          <div style="font-family:'Clash Display';font-size:clamp(2rem,4vw,3.5rem);font-weight:700;color:var(--red)">75
            min</div>
          <div style="font-size:var(--body-size);color:var(--muted);margin-top:.4rem">TikTok captura el equivalente
            a<br /><strong style="color:var(--text)">una telenovela entera</strong> de atención diaria</div>
        </div>
        <div class="glass reveal" style="padding:1.4rem;border-radius:18px">
          <div style="font-size:var(--body-size);color:var(--muted)">Diferencia con Instagram</div>
          <div style="font-family:'Clash Display';font-size:clamp(1.5rem,3vw,2.5rem);font-weight:700;color:var(--cyan)">
            +127%</div>
          <div style="font-size:var(--small-size);color:var(--muted)">más tiempo que en Instagram (33 min/día)</div>
        </div>
        <div class="glass reveal" style="padding:1.4rem;border-radius:18px">
          <div style="font-size:var(--body-size);color:var(--muted)">Diferencia con Facebook</div>
          <div
            style="font-family:'Clash Display';font-size:clamp(1.5rem,3vw,2.5rem);font-weight:700;color:var(--purple)">
            +150%</div>
          <div style="font-size:var(--small-size);color:var(--muted)">más tiempo que en Facebook (30 min/día)</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ════════════════════════════════════════
     SLIDE 6 — ENGAGEMENT COMPARATIVO
════════════════════════════════════════ -->
  <section class="slide" id="s6" style="
  background:radial-gradient(ellipse 55% 50% at 20% 60%,rgba(254,44,85,.12) 0%,transparent 60%),var(--bg)">

    <h2 class="reveal slide-title">📊 ¿Por qué TikTok y no solo las otras redes?</h2>
    <p class="reveal slide-sub">La interacción promedio por publicación es 10× mayor en TikTok. No es una moda: son los
      números.</p>

    <div class="g2" style="flex:1;min-height:0">
      <div class="glass chart-card reveal">
        <h3>Interacción promedio por publicación (%)</h3>
        <div class="sub">Cuanto más alto, más conectadas están las personas con el contenido</div>
        <div class="prog-list" style="margin-top:.5rem" id="progList">
          <div class="prog-item">
            <label><b>🎵 TikTok (videos)</b><span>4.90%</span></label>
            <div class="prog-track">
              <div class="prog-fill fill-tk" data-w="98%"></div>
            </div>
          </div>
          <div class="prog-item">
            <label><b>📸 Instagram Reels</b><span>4.20%</span></label>
            <div class="prog-track">
              <div class="prog-fill fill-ig" data-w="84%"></div>
            </div>
          </div>
          <div class="prog-item">
            <label><b>📸 Instagram Feed</b><span>0.48%</span></label>
            <div class="prog-track">
              <div class="prog-fill fill-ig" data-w="9.6%"></div>
            </div>
          </div>
          <div class="prog-item">
            <label><b>▶️ YouTube</b><span>0.38%</span></label>
            <div class="prog-track">
              <div class="prog-fill fill-yt" data-w="7.6%"></div>
            </div>
          </div>
          <div class="prog-item">
            <label><b>👍 Facebook</b><span>0.15%</span></label>
            <div class="prog-track">
              <div class="prog-fill fill-fb" data-w="3%"></div>
            </div>
          </div>
        </div>
        <div class="src-tag">📌 SocialInsider Benchmark 2025 · WebFX 2025 · Sprout Social 2024</div>
      </div>
      <div class="glass chart-card reveal">
        <h3>Confianza en contenido de salud por plataforma</h3>
        <div class="sub">Las personas confían más en recomendaciones de salud en TikTok por el formato auténtico en
          video</div>
        <div class="chart-wrap"><canvas id="cTrust"></canvas></div>
        <div class="src-tag">📌 Health-Union.com 2024 · Singlegrain 2024 · TikTok for Business 2024</div>
      </div>
    </div>
  </section>

  <!-- ════════════════════════════════════════
     SLIDE 7 — ALCANCE
════════════════════════════════════════ -->
  <section class="slide" id="s7" style="
  background:radial-gradient(ellipse 60% 55% at 80% 30%,rgba(37,244,238,.1) 0%,transparent 60%),var(--bg)">

    <h2 class="reveal slide-title">🗺 Alcance real: países clave</h2>
    <p class="reveal slide-sub">Tamaño de audiencia disponible en TikTok para campaña de salud solo con presencia
      orgánica.</p>

    <div class="g2" style="flex:1;min-height:0">
      <div class="glass chart-card reveal">
        <h3>Usuarios TikTok — países clave (millones)</h3>
        <div class="sub">Audiencia potencial sin inversión en publicidad</div>
        <div class="chart-wrap"><canvas id="cReach"></canvas></div>
        <div class="src-tag">📌 Resourcera / DataReportal / Statista — ene 2025</div>
      </div>
      <div style="display:flex;flex-direction:column;gap:.7rem;justify-content:center">
        <div class="glass reveal" style="padding:1.2rem;border-radius:16px;border-left:3px solid var(--red)">
          <div style="font-size:var(--small-size);color:var(--muted)">🇧🇷 Brasil</div>
          <div style="font-family:'Clash Display';font-size:clamp(1.4rem,3vw,2.2rem);color:var(--red)">105.2M</div>
        </div>
        <div class="glass reveal" style="padding:1.2rem;border-radius:16px;border-left:3px solid #ff758c">
          <div style="font-size:var(--small-size);color:var(--muted)">🇲🇽 México</div>
          <div style="font-family:'Clash Display';font-size:clamp(1.4rem,3vw,2.2rem);color:#ff758c">85.4M</div>
        </div>
        <div class="glass reveal" style="padding:1.2rem;border-radius:16px;border-left:3px solid var(--cyan)">
          <div style="font-size:var(--small-size);color:var(--muted)">🇨🇴 Colombia</div>
          <div style="font-family:'Clash Display';font-size:clamp(1.4rem,3vw,2.2rem);color:var(--cyan)">32M</div>
        </div>
        <div class="glass reveal" style="padding:1.2rem;border-radius:16px;border-left:3px solid var(--purple)">
          <div style="font-size:var(--small-size);color:var(--muted)">🇵🇪 Perú · 🇦🇷 Argentina · 🇨🇱 Chile</div>
          <div style="font-family:'Clash Display';font-size:clamp(1.4rem,3vw,2.2rem);color:var(--purple)">66.8M</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ════════════════════════════════════════
     SLIDE 8 — POR QUÉ AHORA
════════════════════════════════════════ -->
  <section class="slide" id="s8" style="
  background:radial-gradient(ellipse 60% 50% at 50% 100%,rgba(254,44,85,.14) 0%,transparent 60%),var(--bg)">

    <h2 class="reveal slide-title">✅ Hoy es el momento</h2>
    <p class="reveal slide-sub">Razones con datos para que nuestra campaña de salud incluya TikTok ahora.</p>

    <div class="g2" style="flex:1;min-height:0">
      <div class="glass reveal" style="padding:1.6rem;border-radius:20px">
        <ul class="ins-list">
          <li class="reveal">
            <span class="ins-num">01</span>
            <div><strong>270M de personas</strong> en LATAM están activas hoy en TikTok — el mayor mercado regional del
              mundo.</div>
          </li>
          <li class="reveal">
            <span class="ins-num">02</span>
            <div>Pasan <strong>75 minutos por día</strong> — casi el doble que en Instagram o Facebook.</div>
          </li>
          <li class="reveal">
            <span class="ins-num">03</span>
            <div><strong>1 de cada 3 personas</strong> que ve contenido de salud toma una acción concreta (busca médico,
              compra, se registra).</div>
          </li>
          <li class="reveal">
            <span class="ins-num">04</span>
            <div>El contenido de salud en video corto es <strong>2.4× más confiable</strong> que la publicidad
              tradicional.</div>
          </li>
          <li class="reveal">
            <span class="ins-num">05</span>
            <div>Genera <strong>10× más conversaciones</strong> que una publicación en Instagram — crecimiento orgánico
              real.</div>
          </li>
        </ul>
      </div>
      <div class="glass chart-card reveal">
        <h3>Confianza relativa del contenido de salud</h3>
        <div class="sub">Comparativa entre plataformas en 5 dimensiones clave</div>
        <div class="chart-wrap"><canvas id="cRadar2"></canvas></div>
        <div class="src-tag">📌 Health-Union.com 2024 · TikTok for Business 2024 · Singlegrain 2024</div>
      </div>
    </div>
  </section>

  <!-- ════════════════════════════════════════
     SLIDE 9 — CTA FINAL
════════════════════════════════════════ -->
  </section>

  <!-- ════════════════════════════════════════
     SLIDE 9 — PERFORMANCE CPL
════════════════════════════════════════ -->
  <section class="slide" id="s9" style="
  background:radial-gradient(ellipse 60% 50% at 0% 100%,rgba(37,244,238,.1) 0%,transparent 60%),var(--bg)">

    <h2 class="reveal slide-title">📉 Eficiencia en Adquisición (CPL)</h2>
    <p class="reveal slide-sub">Comparativa de costo por lead: TikTok vs Meta en el sector salud (LATAM).</p>

    <div class="g2" style="flex:1;min-height:0">
      <div class="glass chart-card reveal">
        <h3>CPL Promedio Sector Salud ($ USD)</h3>
        <div class="sub">Benchmarks 2024: Captación de alta intención vs volumen masivo</div>
        <div class="chart-wrap"><canvas id="cCPL"></canvas></div>
        <div class="src-tag">📌 WordStream 2024 (Global) · Benchmarks Regionales (LATAM)</div>
      </div>
      <div style="display:flex;flex-direction:column;gap:1.4rem;justify-content:center">
        <div class="glass reveal"
          style="padding:1.6rem;border-radius:20px;background:rgba(255,255,255,0.02);border-left:4px solid var(--cyan)">
          <div style="color:var(--cyan);font-weight:700;margin-bottom:.5rem;text-transform:uppercase;font-size:0.75rem">
            TikTok Ads (LATAM AVG)</div>
          <div style="font-size:2.4rem;font-family:'Clash Display';font-weight:700">$5.00</div>
          <div style="font-size:.8rem;opacity:.6">Alcance masivo y descubrimiento de marca.</div>
        </div>
        <div class="glass reveal"
          style="padding:1.6rem;border-radius:20px;background:rgba(255,255,255,0.02);border-left:4px solid var(--red)">
          <div style="color:var(--red);font-weight:700;margin-bottom:.5rem;text-transform:uppercase;font-size:0.75rem">
            Meta Ads</div>
          <div style="font-size:2.4rem;font-family:'Clash Display';font-weight:700">$32.46</div>
          <div style="font-size:.8rem;opacity:.6">Segmentación de intención directa (WordStream).</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ════════════════════════════════════════
     SLIDE 10 — ESTRATEGIA HÍBRIDA
════════════════════════════════════════ -->
  <section class="slide" id="s10" style="
  background:radial-gradient(ellipse 60% 50% at 100% 0%,rgba(156,39,176,.1) 0%,transparent 60%),var(--bg)">

    <h2 class="reveal slide-title">🚀 Estrategia de Pauta Ganadora</h2>
    <p class="reveal slide-sub">Cómo combinar lo mejor de ambos mundos para escalar tu negocio.</p>

    <div class="g2" style="flex:1;min-height:0">
      <div class="glass chart-card reveal">
        <h3>Escalabilidad del Mix de Medios</h3>
        <div class="sub">Proyección de leads al integrar TikTok en el presupuesto principal</div>
        <div class="chart-wrap"><canvas id="cVolume"></canvas></div>
      </div>
      <div style="display:flex;flex-direction:column;gap:1rem;justify-content:center">
        <div class="glass reveal" style="padding:1.4rem;border-radius:18px">
          <h4 style="color:var(--cyan);margin-bottom:.4rem">Fase 1: TikTok Spark Ads</h4>
          <p style="font-size:.85rem;opacity:.7">Uso de contenido auténtico para generar leads a bajo costo (~$5.00).
          </p>
        </div>
        <div class="glass reveal" style="padding:1.4rem;border-radius:18px">
          <h4 style="color:var(--red);margin-bottom:.4rem">Fase 2: Meta Retargeting</h4>
          <p style="font-size:.85rem;opacity:.7">Cierre de agendas con audiencias de alta intención provenientes de
            TikTok.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ════════════════════════════════════════
     SLIDE 11 — CTA FINAL
════════════════════════════════════════ -->
  <section class="slide" id="s11"
    style="justify-content:center;align-items:center;text-align:center;
  background:radial-gradient(ellipse 70% 60% at 50% 50%,rgba(254,44,85,.15) 0%,rgba(156,39,176,.08) 50%,transparent 70%),var(--bg)">

    <div class="reveal" style="font-family:'Clash Display';font-size:var(--small-size);
    color:var(--red);letter-spacing:.15em;text-transform:uppercase;margin-bottom:1rem">
      Conclusión Estratégica
    </div>

    <h2 class="reveal" style="font-family:'Clash Display';font-size:var(--title-size);
    font-weight:700;line-height:1.1;max-width:16ch">
      La audiencia ya está ahí.<br />
      <span class="gtext">Escalemos hoy.</span>
    </h2>

    <div class="reveal" style="display:flex;gap:1.5rem;justify-content:center;margin:2rem 0">
      <div style="text-align:center">
        <div style="font-size:2rem;font-weight:700;color:var(--cyan)">-32%</div>
        <div style="font-size:.7rem;opacity:.6">CPL Proyectado</div>
      </div>
      <div style="text-align:center">
        <div style="font-size:2rem;font-weight:700;color:var(--red)">3.5x</div>
        <div style="font-size:.7rem;opacity:.6">ROAS Estimado</div>
      </div>
    </div>

    <div class="reveal" style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap">
      <button class="cta-btn" onclick="goTo(0)">Volver al inicio</button>
    </div>

    <div class="reveal"
      style="margin-top:2.5rem;font-size:0.6rem;color:#333d55;line-height:1.6;max-width:900px;margin-left:auto;margin-right:auto">
      Fuentes Verificadas 2025:
      <a href="https://limaretail.com/marketing-digital/tiktok-ads-vs-meta-ads-2025/" target="_blank"
        style="color:inherit;text-decoration:underline">Lima Retail (Meta vs TikTok 2025)</a> ·
      <a href="https://www.roisense.com/tiktok-ads-vs-meta-ads-2025-cual-es-la-mejor/" target="_blank"
        style="color:inherit;text-decoration:underline">Roisense (Creatividad y ROI)</a> ·
      <a href="https://www.somoschili.com/post/meta-vs-tiktok-ads-qu%C3%A9-dice-el-estudio-2025-de-metricool-y-c%C3%B3mo-lo-aplicamos-en-chili"
        target="_blank" style="color:inherit;text-decoration:underline">Somos Chili (Estudio Metricool 2025)</a> ·
      <a href="https://soyjhoelfernandez.com/publicidad-digital-2025/" target="_blank"
        style="color:inherit;text-decoration:underline">Jhoel Fernandez (Google vs TikTok)</a> ·
      <a href="https://bunkerdb.com/blog/facebook-vs-tiktok-2025" target="_blank"
        style="color:inherit;text-decoration:underline">Bunker DB (Métricas 2025)</a>
    </div>
  </section>

  <!-- ═══ JAVASCRIPT ═══ -->
  <script>
    /* ── SLIDE SYSTEM ── */
    const slides = document.querySelectorAll('.slide');
    const N = slides.length;
    let cur = 0;
    const dotsEl = document.getElementById('dots');
    const counter = document.getElementById('slide-counter');
    let chartsInited = {};

    slides.forEach((_, i) => {
      const d = document.createElement('button');
      d.className = 'dot' + (i === 0 ? ' active' : '');
      d.onclick = () => goTo(i);
      dotsEl.appendChild(d);
    });

    function goTo(i) {
      i = Math.max(0, Math.min(N - 1, i));
      cur = i;
      slides[i].scrollIntoView({ behavior: 'smooth' });
    }

    document.getElementById('btn-prev').onclick = () => goTo(cur - 1);
    document.getElementById('btn-next').onclick = () => goTo(cur + 1);
    document.addEventListener('keydown', e => {
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') goTo(cur + 1);
      if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') goTo(cur - 1);
    });

    /* ── INTERSECTION OBSERVER ── */
    const io = new IntersectionObserver(entries => {
      entries.forEach(en => {
        const idx = [...slides].indexOf(en.target);
        if (en.isIntersecting) {
          en.target.classList.add('active');
          cur = idx;
          document.querySelectorAll('.dot').forEach((d, i) => d.classList.toggle('active', i === cur));
          counter.textContent = String(cur + 1).padStart(2, '0') + ' / ' + String(N).padStart(2, '0');
          initChart(idx);
          // progress bars
          if (idx === 5) {
            setTimeout(() => {
              document.querySelectorAll('.prog-fill[data-w]').forEach(el => { el.style.width = el.dataset.w });
            }, 400);
          }
        } else {
          en.target.classList.remove('active');
        }
      });
    }, { threshold: .5 });
    slides.forEach(s => io.observe(s));

    /* ── CHART CONFIG ── */
    Chart.defaults.color = '#8892b0';
    Chart.defaults.font.family = 'Satoshi';
    Chart.defaults.plugins.legend.labels.boxWidth = 10;
    Chart.defaults.plugins.legend.labels.padding = 12;
    const GRID = 'rgba(255,255,255,.05)';
    const R = '#fe2c55', C = '#25f4ee', P = '#9c27b0', G = '#ffd700', B = '#2196f3';

    function initChart(idx) {
      if (chartsInited[idx]) return;
      chartsInited[idx] = true;
      if (idx === 2) initS3();
      if (idx === 3) initS4();
      if (idx === 4) initS5();
      if (idx === 5) initS6();
      if (idx === 6) initS7();
      if (idx === 7) initS8();
      if (idx === 8) initS9();
      if (idx === 9) initS10();
    }

    function cfg(extra) {
      return Object.assign({
        responsive: true, maintainAspectRatio: false,
        plugins: { legend: { display: false } }
      }, extra);
    }
    function scales(x, y) { return { scales: { x: Object.assign({ grid: { color: GRID }, ticks: { color: '#8892b0' } }, x), y: Object.assign({ grid: { color: GRID }, ticks: { color: '#8892b0' } }, y) } } }

    function initS3() {
      new Chart(document.getElementById('cLatam'), {
        type: 'bar',
        data: {
          labels: ['Brasil', 'México', 'Colombia', 'Perú', 'Argentina', 'Chile'],
          datasets: [{
            label: 'Millones', data: [105.2, 85.4, 32, 24.4, 24.4, 18],
            backgroundColor: [R, '#ff758c', '#ff9eb5', C, '#80fff9', P], borderRadius: 8
          }]
        },
        options: {
          ...cfg(), indexAxis: 'y', ...scales({ ticks: { callback: v => v + 'M' } }, {}),
          plugins: { legend: { display: false }, tooltip: { callbacks: { label: c => ` ${c.parsed.x}M usuarios` } } }
        }
      });
      new Chart(document.getElementById('cAge'), {
        type: 'bar',
        data: {
          labels: ['<18', '18–24', '25–34', '35–44', '45–54', '>55'],
          datasets: [{
            data: [10.5, 30.7, 35.3, 14.1, 6.1, 3.3],
            backgroundColor: ['rgba(254,44,85,.3)', '#ff758c', R, '#ff9eb5', 'rgba(254,44,85,.4)', 'rgba(254,44,85,.2)'], borderRadius: 6
          }]
        },
        options: {
          ...cfg(), ...scales({}, { ticks: { callback: v => v + '%' } }),
          plugins: { legend: { display: false }, tooltip: { callbacks: { label: c => ` ${c.parsed.y}% del total` } } }
        }
      });
    }

    function initS4() {
      new Chart(document.getElementById('cActions'), {
        type: 'doughnut',
        data: {
          labels: ['Tomaron acción (92%)', 'Buscaron info (67%)', 'Acción concreta (35%)', 'Siguieron creador (28%)'],
          datasets: [{ data: [92, 67, 35, 28], backgroundColor: [R, C, P, G], borderWidth: 2, borderColor: '#0a0f1c', hoverOffset: 8 }]
        },
        options: {
          responsive: true, maintainAspectRatio: false,
          plugins: { legend: { position: 'bottom', labels: { color: '#8892b0', font: { size: 10 } } } }
        }
      });
    }

    function initS5() {
      new Chart(document.getElementById('cTime'), {
        type: 'bar',
        data: {
          labels: ['TikTok', 'YouTube', 'Instagram', 'Facebook', 'Twitter/X'],
          datasets: [{
            label: 'min/día', data: [75, 48, 33, 30, 18],
            backgroundColor: [R, '#ff0000', '#e1306c', B, '#1da1f2'], borderRadius: 8
          }]
        },
        options: {
          ...cfg(), ...scales({}, { ticks: { callback: v => v + ' min' } }),
          plugins: { legend: { display: false }, tooltip: { callbacks: { label: c => ` ${c.parsed.y} min/día` } } }
        }
      });
    }

    function initS6() {
      new Chart(document.getElementById('cTrust'), {
        type: 'radar',
        data: {
          labels: ['Confianza\nen mensaje', 'Conexión\nemocional', 'Contenido\ncompartido', 'Acción\nrealizada', 'Permanencia\nen memoria'],
          datasets: [
            { label: 'TikTok', data: [9, 9, 8, 9, 8], backgroundColor: 'rgba(254,44,85,.18)', borderColor: R, pointBackgroundColor: R, pointRadius: 4 },
            { label: 'Instagram', data: [6, 6, 6, 5, 5], backgroundColor: 'rgba(225,48,108,.1)', borderColor: '#e1306c', pointBackgroundColor: '#e1306c', pointRadius: 4 },
            { label: 'Facebook', data: [4, 4, 5, 3, 4], backgroundColor: 'rgba(33,150,243,.08)', borderColor: B, pointBackgroundColor: B, pointRadius: 4 }
          ]
        },
        options: {
          responsive: true, maintainAspectRatio: false,
          scales: { r: { angleLines: { color: GRID }, grid: { color: GRID }, pointLabels: { color: '#8892b0', font: { size: 9 } }, ticks: { display: false }, suggestedMin: 0, suggestedMax: 10 } },
          plugins: { legend: { position: 'bottom', labels: { color: '#8892b0', font: { size: 10 } } } }
        }
      });
    }

    function initS7() {
      new Chart(document.getElementById('cReach'), {
        type: 'pie',
        data: {
          labels: ['Brasil (105M)', 'México (85M)', 'Colombia (32M)', 'Perú (24M)', 'Argentina (24M)', 'Chile (18M)'],
          datasets: [{ data: [105.2, 85.4, 32, 24.4, 24.4, 18], backgroundColor: [R, '#ff758c', C, '#80fff9', P, B], borderWidth: 2, borderColor: '#0a0f1c', hoverOffset: 6 }]
        },
        options: {
          responsive: true, maintainAspectRatio: false,
          plugins: {
            legend: { position: 'bottom', labels: { color: '#8892b0', font: { size: 9 }, padding: 8, boxWidth: 8 } },
            tooltip: { callbacks: { label: c => ` ${c.label}: ${c.parsed}M` } }
          }
        }
      });
    }

    function initS8() {
      new Chart(document.getElementById('cRadar2'), {
        type: 'radar',
        data: {
          labels: ['Confianza\nen mensaje', 'Conexión\nemocional', 'Contenido\ncompartido', 'Acción\nrealizada', 'Permanencia\nen memoria'],
          datasets: [
            { label: 'TikTok', data: [9, 9, 8, 9, 8], backgroundColor: 'rgba(254,44,85,.18)', borderColor: R, pointBackgroundColor: R, pointRadius: 4 },
            { label: 'Instagram', data: [6, 6, 6, 5, 5], backgroundColor: 'rgba(225,48,108,.1)', borderColor: '#e1306c', pointBackgroundColor: '#e1306c', pointRadius: 4 },
            { label: 'Facebook', data: [4, 4, 5, 3, 4], backgroundColor: 'rgba(33,150,243,.08)', borderColor: B, pointBackgroundColor: B, pointRadius: 4 }
          ]
        },
        options: {
          responsive: true, maintainAspectRatio: false,
          scales: { r: { angleLines: { color: GRID }, grid: { color: GRID }, pointLabels: { color: '#8892b0', font: { size: 9 } }, ticks: { display: false }, suggestedMin: 0, suggestedMax: 10 } },
          plugins: { legend: { position: 'bottom', labels: { color: '#8892b0', font: { size: 10 } } } }
        }
      });
    }

    function initS9() {
      new Chart(document.getElementById('cCPL'), {
        type: 'bar',
        data: {
          labels: ['TikTok Ads', 'Meta Ads', 'Google Ads'],
          datasets: [{
            label: 'CPL ($ USD)', data: [5.00, 32.46, 45.00],
            backgroundColor: [R, B, G], borderRadius: 8
          }]
        },
        options: {
          ...cfg(), ...scales({}, { ticks: { callback: v => '$' + v } }),
          plugins: { legend: { display: false }, tooltip: { callbacks: { label: c => ` $${c.parsed.y} por lead` } } }
        }
      });
    }

    function initS10() {
      new Chart(document.getElementById('cVolume'), {
        type: 'line',
        data: {
          labels: ['Mes 1', 'Mes 2', 'Mes 3', 'Mes 4', 'Mes 5', 'Mes 6'],
          datasets: [
            { label: 'TikTok', data: [100, 250, 480, 720, 1050, 1500], borderColor: C, backgroundColor: 'rgba(37,244,238,.1)', fill: true, tension: 0.4 },
            { label: 'Meta', data: [80, 150, 260, 380, 510, 650], borderColor: R, borderDash: [5, 5], fill: false, tension: 0.4 }
          ]
        },
        options: {
          ...cfg(), ...scales({}, { ticks: { callback: v => v + ' leads' } }),
          plugins: { legend: { display: true, labels: { color: '#8892b0' } } }
        }
      });
    }
  </script>
</body>

</html>
