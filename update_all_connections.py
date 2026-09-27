# -*- coding: utf-8 -*-
"""
Script para atualizar a Planta Baixa 2D com:
1. Cozinha Americana (totalmente aberta, balcão de granito e banquetas)
2. Salas UNIDAS (uma única sala de estar e jantar integrada sem divisórias)
3. Varandas CONECTADAS (deck da piscina, varanda gourmet e circulação totalmente integradas)
"""

html_code = r'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Planta Baixa 2D Técnica Oficial • Salas Unidas, Cozinha Americana & Varandas Conectadas</title>
  <style>
    :root {
      --bg-dark: #0f172a;
      --panel-bg: rgba(15, 23, 42, 0.92);
      --panel-border: rgba(255, 255, 255, 0.12);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --accent: #38bdf8;
      --accent-hover: #0ea5e9;
      --color-sala-unida: #ffa07a;
      --color-cozinha: #ffffff;
      --color-lazer-conectado: #ffb703;
      --color-varanda-lilas: #e2c4f0;
      --color-jardim: #c7f9cc;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
      user-select: none;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background: #111827;
      color: var(--text-main);
      overflow: hidden;
      width: 100vw;
      height: 100vh;
      display: flex;
      flex-direction: column;
    }

    /* Header Bar */
    header {
      height: 60px;
      background: var(--panel-bg);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--panel-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 16px;
      z-index: 50;
      flex-shrink: 0;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .brand-icon {
      width: 36px;
      height: 36px;
      background: linear-gradient(135deg, #f97316, #ea580c);
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 2px 8px rgba(249, 115, 22, 0.4);
    }

    .brand-icon svg {
      width: 22px;
      height: 22px;
      stroke: #fff;
      fill: none;
      stroke-width: 2;
    }

    .brand-text h1 {
      font-size: 1.02rem;
      font-weight: 700;
      color: #fff;
      letter-spacing: -0.01em;
    }

    .brand-text span {
      font-size: 0.72rem;
      color: var(--text-muted);
      display: block;
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 7px 12px;
      font-size: 0.8rem;
      font-weight: 600;
      border-radius: 8px;
      border: 1px solid var(--panel-border);
      background: rgba(255, 255, 255, 0.06);
      color: #fff;
      cursor: pointer;
      transition: all 0.2s ease;
      text-decoration: none;
    }

    .btn:hover {
      background: rgba(255, 255, 255, 0.14);
      border-color: rgba(255, 255, 255, 0.25);
    }

    .btn.active {
      background: var(--accent);
      color: #0f172a;
      border-color: var(--accent);
    }

    .btn-3d {
      background: linear-gradient(135deg, #10b981, #059669);
      border-color: #10b981;
      color: #fff;
      box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3);
    }

    /* Main Workspace */
    #workspace {
      flex: 1;
      position: relative;
      overflow: hidden;
      cursor: grab;
      background: #1e293b;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    #workspace:active {
      cursor: grabbing;
    }

    .theme-blueprint #workspace {
      background: #0a192f;
      background-image: 
        linear-gradient(rgba(255, 255, 255, 0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.05) 1px, transparent 1px);
      background-size: 50px 50px;
    }

    svg#blueprint-svg {
      width: 100%;
      height: 100%;
      display: block;
      transform-origin: 0 0;
    }

    /* Floating Toolbars */
    .floating-bar {
      position: absolute;
      background: var(--panel-bg);
      backdrop-filter: blur(12px);
      border: 1px solid var(--panel-border);
      border-radius: 12px;
      padding: 6px;
      display: flex;
      gap: 6px;
      z-index: 40;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }

    #nav-controls {
      bottom: 20px;
      right: 20px;
      flex-direction: column;
    }

    #nav-controls .btn-icon {
      width: 38px;
      height: 38px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--panel-border);
      color: #fff;
      cursor: pointer;
      transition: all 0.15s;
    }

    #nav-controls .btn-icon:hover {
      background: rgba(255, 255, 255, 0.15);
    }

    #nav-controls .btn-icon svg {
      width: 20px;
      height: 20px;
      stroke: currentColor;
      fill: none;
      stroke-width: 2;
    }

    #layer-bar {
      top: 16px;
      left: 16px;
      flex-wrap: wrap;
      max-width: calc(100vw - 32px);
    }

    .chip-toggle {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 6px 10px;
      font-size: 0.75rem;
      font-weight: 600;
      border-radius: 8px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--panel-border);
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.2s;
    }

    .chip-toggle:hover {
      color: #fff;
      background: rgba(255, 255, 255, 0.1);
    }

    .chip-toggle.active {
      background: rgba(56, 189, 248, 0.15);
      border-color: rgba(56, 189, 248, 0.4);
      color: #38bdf8;
    }

    .chip-toggle .dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: currentColor;
    }

    #btn-focus-integrado {
      background: linear-gradient(135deg, rgba(249, 115, 22, 0.25), rgba(234, 88, 12, 0.35));
      border: 1px solid #f97316;
      color: #ffedd5;
    }
    #btn-focus-integrado:hover {
      background: linear-gradient(135deg, rgba(249, 115, 22, 0.4), rgba(234, 88, 12, 0.5));
    }

    /* Opacity Slider Bar */
    #overlay-control {
      bottom: 20px;
      left: 20px;
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 14px;
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--text-muted);
    }

    #overlay-control input[type=range] {
      width: 100px;
      accent-color: #38bdf8;
      cursor: pointer;
    }

    /* Inspector Drawer */
    #inspector {
      position: absolute;
      top: 16px;
      right: 16px;
      width: 320px;
      max-width: calc(100vw - 32px);
      background: var(--panel-bg);
      backdrop-filter: blur(16px);
      border: 1px solid var(--panel-border);
      border-radius: 14px;
      padding: 16px;
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.5);
      z-index: 45;
      transform: translateX(360px);
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    #inspector.open {
      transform: translateX(0);
    }

    .inspector-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding-bottom: 10px;
      margin-bottom: 12px;
    }

    .inspector-header h3 {
      font-size: 1.05rem;
      font-weight: 700;
      color: #fff;
    }

    .inspector-close {
      background: none;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      font-size: 1.3rem;
      line-height: 1;
    }

    .inspector-badge {
      display: inline-block;
      font-size: 0.68rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 3px 8px;
      border-radius: 4px;
      background: rgba(56, 189, 248, 0.18);
      color: #38bdf8;
      margin-bottom: 8px;
    }

    .stat-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      margin: 12px 0;
    }

    .stat-card {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 8px;
      padding: 8px;
    }

    .stat-card span {
      display: block;
      font-size: 0.68rem;
      color: var(--text-muted);
      text-transform: uppercase;
    }

    .stat-card strong {
      display: block;
      font-size: 0.95rem;
      color: #fff;
      font-weight: 700;
      margin-top: 2px;
    }

    .inspector-details {
      font-size: 0.8rem;
      color: #cbd5e1;
      line-height: 1.45;
      background: rgba(0, 0, 0, 0.2);
      border-radius: 8px;
      padding: 10px;
      border: 1px solid rgba(255, 255, 255, 0.05);
    }

    .room-poly {
      cursor: pointer;
      transition: filter 0.2s, opacity 0.2s;
    }

    .room-poly:hover {
      filter: brightness(1.15);
    }

    .room-selected {
      stroke: #38bdf8 !important;
      stroke-width: 4px !important;
      filter: drop-shadow(0 0 10px rgba(56, 189, 248, 0.7));
    }

    .callout-box {
      cursor: pointer;
      filter: drop-shadow(0 2px 4px rgba(0,0,0,0.18));
      transition: transform 0.15s;
    }
    .callout-box:hover {
      transform: scale(1.05);
    }

    /* Pulse integration highlight */
    .pulse-zone {
      animation: pulseOpen 2.5s infinite alternate;
    }
    @keyframes pulseOpen {
      0% { opacity: 0.7; }
      100% { opacity: 1.0; filter: drop-shadow(0 0 8px rgba(220, 38, 38, 0.6)); }
    }

    @media print {
      header, .floating-bar, #inspector, #overlay-control {
        display: none !important;
      }
      body, #workspace {
        background: #fff !important;
        overflow: visible !important;
      }
    }
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="brand">
      <div class="brand-icon">
        <svg viewBox="0 0 24 24"><path d="M3 3h18v18H3V3zm16 16V5H5v14h14zM7 7h10v2H7V7zm0 4h10v2H7v-2zm0 4h7v2H7v-2z"/></svg>
      </div>
      <div class="brand-text">
        <h1>Planta Baixa 2D Técnica Oficial</h1>
        <span>Salas Unidas • Cozinha Americana • Varandas Conectadas • Escala 1 cm = 1,00 m</span>
      </div>
    </div>

    <div class="header-actions">
      <button class="btn active" id="btn-theme-human" title="Cores Originais da Planta">🎨 Humanizada</button>
      <button class="btn" id="btn-theme-blue" title="Prancha CAD Blueprint">📐 Blueprint</button>
      <button class="btn" id="btn-print" title="Imprimir Prancha Técnica">🖨️ Imprimir</button>
      <a href="modelo3d.html" class="btn btn-3d" title="Alternar para Maquete 3D">🏠 Ver Modelo 3D</a>
    </div>
  </header>

  <!-- Workspace Canvas -->
  <div id="workspace">
    <svg id="blueprint-svg" viewBox="0 0 540 780" preserveAspectRatio="xMidYMid meet">
      <defs>
        <!-- Blue Pool Gradient -->
        <linearGradient id="poolGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#00b4d8" />
          <stop offset="100%" stop-color="#0077b6" />
        </linearGradient>
      </defs>

      <g id="viewport-group">

        <!-- 0. OVERLAY DA PLANTA ORIGINAL (OPACIDADE CONTROLÁVEL) -->
        <g id="layer-original-overlay" opacity="0.0">
          <image href="planta_baixa.png" x="0" y="0" width="540" height="780" preserveAspectRatio="none"/>
        </g>

        <!-- 1. JARDINS & ÁREAS EXTERNAS (VERDE) -->
        <g id="layer-jardins">
          <!-- Jardim Superior (15,38 x 4,00 cm) -->
          <rect id="poly-jardim-sup" class="room-poly" x="165.2" y="111.3" width="354.2" height="92.1" fill="#c7f9cc" stroke="#38a3a5" stroke-width="1.5"/>
          
          <!-- Jardim Lateral Esquerdo (5,83 x 12,13 cm) -->
          <rect id="poly-jardim-esq" class="room-poly" x="29.3" y="109.5" width="134.3" height="279.3" fill="#c7f9cc" stroke="#38a3a5" stroke-width="1.5"/>

          <!-- Jardim dos Fundos (17,00 x 9,00 cm) -->
          <rect id="poly-jardim-fundos" class="room-poly" x="127.8" y="540.9" width="391.6" height="207.2" fill="#c7f9cc" stroke="#38a3a5" stroke-width="1.5"/>

          <!-- Jardim Casa da Árvore (4,24 x 12,15 cm) -->
          <rect id="poly-jardim-arvore" class="room-poly" x="28.5" y="469.0" width="97.5" height="279.9" fill="#c7f9cc" stroke="#38a3a5" stroke-width="1.5"/>

          <!-- Casa do Cachorro (Canto superior direito) -->
          <rect id="poly-casa-cachorro" class="room-poly" x="434.7" y="114.0" width="82.4" height="86.5" fill="#cca43b" stroke="#7f4f24" stroke-width="2"/>
          <text x="475.9" y="152.0" font-size="12" font-weight="700" fill="#3e2723" text-anchor="middle">Casa do</text>
          <text x="475.9" y="167.0" font-size="12" font-weight="700" fill="#3e2723" text-anchor="middle">cachorro</text>

          <!-- Casa da Árvore (Canto inferior esquerdo) -->
          <rect id="poly-casa-arvore" class="room-poly" x="37.7" y="634.3" width="82.5" height="86.5" fill="#cca43b" stroke="#7f4f24" stroke-width="2"/>
          <text x="78.9" y="672.0" font-size="12" font-weight="700" fill="#3e2723" text-anchor="middle">Casa da</text>
          <text x="78.9" y="687.0" font-size="12" font-weight="700" fill="#3e2723" text-anchor="middle">árvore</text>

          <!-- Pergolado (Canto inferior direito: 3,05 x 2,91 cm) -->
          <rect id="poly-pergolado" class="room-poly" x="382.3" y="583.1" width="114.6" height="111.1" fill="#cca43b" stroke="#7f4f24" stroke-width="2"/>
          <text x="439.6" y="642.0" font-size="13" font-weight="700" fill="#3e2723" text-anchor="middle">Pergolado</text>
        </g>

        <!-- 2. CÔMODOS INTERNOS (SALAS UNIDAS, COZINHA AMERICANA & VARANDAS CONECTADAS) -->
        <g id="layer-pisos">
          <!-- Quarto 1 (Superior Esquerdo: 3,01 x 4,00 cm) -->
          <rect id="poly-quarto1" class="room-poly" x="165.2" y="207.0" width="69.3" height="92.1" fill="#ffa07a" stroke="#000" stroke-width="1.8"/>

          <!-- Quarto 2 (Superior Centro: 3,51 x 3,01 cm) -->
          <rect id="poly-quarto2" class="room-poly" x="236.7" y="208.1" width="80.9" height="69.4" fill="#ffa07a" stroke="#000" stroke-width="1.8"/>

          <!-- Banheiro Superior (Abaixo do Quarto 2) -->
          <rect id="poly-banheiro-sup" class="room-poly" x="260.8" y="279.6" width="55.9" height="43.0" fill="#bde0fe" stroke="#000" stroke-width="1.8"/>

          <!-- ================================================================= -->
          <!-- 🌟 AS SALAS SÃO UNIDAS! (SALA UNIFICADA ESTAR + JANTAR INTEGRADA)  -->
          <!-- ================================================================= -->
          <!-- Polígono Único Contínuo da Sala Unificada (sem divisórias internas) -->
          <polygon id="poly-sala-unificada" class="room-poly" 
            points="165.8,301.6 257.9,301.6 257.9,325.3 260.9,325.3 260.9,419.2 272.4,419.2 272.4,466.1 165.8,466.1" 
            fill="#ffa07a" stroke="#000" stroke-width="1.8"/>

          <!-- ================================================================= -->
          <!-- 🌟 AS VARANDAS SÃO CONECTADAS! (OESTE: VARANDA LILÁS INTEGRADA)   -->
          <!-- ================================================================= -->
          <!-- Varanda Lilás Contínua e Conectada à Sala (3,26x2,78 e 3,32x2,94 cm unidas) -->
          <polygon id="poly-varanda-lilas-conectada" class="room-poly"
            points="96.0,390.7 165.8,390.7 165.8,467.2 96.0,467.2"
            fill="#e2c4f0" stroke="#000" stroke-width="1.8"/>

          <!-- ================================================================= -->
          <!-- 🌟 A COZINHA É AMERICANA! (TOTALMENTE ABERTA PARA SALA E LAZER)   -->
          <!-- ================================================================= -->
          <!-- Piso da Cozinha Americana Central (Sem parede oeste e sem parede leste) -->
          <rect id="poly-cozinha" class="room-poly" x="260.9" y="325.3" width="96.2" height="93.9" fill="#ffffff"/>

          <!-- Quarto 3 (Abaixo da Cozinha: 2,17 x 1,90 cm) -->
          <rect id="poly-quarto3" class="room-poly" x="272.4" y="421.9" width="50.0" height="43.8" fill="#ffa07a" stroke="#000" stroke-width="1.8"/>

          <!-- Banheiro Inferior (Ao lado do Quarto 3: 1,79 x 1,52 cm) -->
          <rect id="poly-banheiro-inf" class="room-poly" x="324.3" y="423.7" width="35.0" height="41.2" fill="#bde0fe" stroke="#000" stroke-width="1.8"/>

          <!-- Garagem (Inferior Esquerdo: 5,71 x 3,00 cm) -->
          <rect id="poly-garagem" class="room-poly" x="127.8" y="469.0" width="131.5" height="69.1" fill="#ffa07a" stroke="#000" stroke-width="1.8"/>

          <!-- Quarto 5 (Inferior Centro: 5,41 x 3,00 cm) -->
          <rect id="poly-quarto5" class="room-poly" x="261.7" y="468.4" width="124.6" height="69.1" fill="#ffa07a" stroke="#000" stroke-width="1.8"/>

          <!-- Lavanderia (Inferior Direito: 2,24 x 2,95 cm) -->
          <rect id="poly-lavanderia" class="room-poly" x="388.7" y="468.2" width="51.6" height="68.0" fill="#ffb703" stroke="#000" stroke-width="1.8"/>

          <!-- ================================================================= -->
          <!-- 🌟 AS VARANDAS SÃO CONECTADAS! (LESTE: COMPLEXO TOTAL DE LAZER)   -->
          <!-- ================================================================= -->
          <!-- Polígono Único Total das Varandas Conectadas: Deck Piscina + Varanda Lazer + Circulação -->
          <polygon id="poly-varanda-lazer-conectada" class="room-poly"
            points="319.3,207.3 478.5,207.3 478.5,536.2 440.3,536.2 440.3,468.2 359.3,468.2 359.3,423.7 357.1,419.2 357.1,325.3 319.3,322.6"
            fill="#ffb703" stroke="#000" stroke-width="1.8"/>

          <!-- Piscina Oval Azul Integrada no Deck Conectado -->
          <ellipse id="poly-piscina" class="room-poly" cx="401.2" cy="268.5" rx="28.7" ry="28.1" fill="url(#poolGrad)" stroke="#023e8a" stroke-width="2"/>
          <text x="401.2" y="271.0" font-size="9" font-weight="700" fill="#fff" text-anchor="middle">Piscina</text>

          <!-- Horta com Cerca (Faixa Lateral Direita) -->
          <rect id="poly-horta" class="room-poly" x="484.6" y="206.2" width="34.1" height="330.0" fill="#cca43b" stroke="#7f4f24" stroke-width="2"/>
        </g>

        <!-- 3. PAREDES ESTRUTURAIS REAIS (SEM PAREDES ONDE HÁ ABERTURA/LIGAÇÃO) -->
        <g id="layer-paredes">
          <!-- Parede Norte Quarto 1 e Quarto 2 -->
          <line x1="165.2" y1="207.0" x2="317.6" y2="207.0" stroke="#000" stroke-width="2.5"/>
          <!-- Parede Divisória Q1 e Q2 -->
          <line x1="234.5" y1="207.0" x2="234.5" y2="299.1" stroke="#000" stroke-width="2.5"/>
          <!-- Parede Sul Quarto 1 (Divisão com Sala Unificada) -->
          <line x1="165.2" y1="299.1" x2="234.5" y2="299.1" stroke="#000" stroke-width="2.5"/>
          <!-- Parede Sul Quarto 2 (Divisão com Banheiro Sup) -->
          <line x1="236.7" y1="277.5" x2="317.6" y2="277.5" stroke="#000" stroke-width="2.5"/>
          <!-- Paredes Banheiro Sup -->
          <line x1="260.8" y1="277.5" x2="260.8" y2="322.6" stroke="#000" stroke-width="2.5"/>
          <line x1="316.7" y1="277.5" x2="316.7" y2="322.6" stroke="#000" stroke-width="2.5"/>

          <!-- PAREDE NORTE DA COZINHA (Apoio de P, AE, F - Parede com Banheiro) -->
          <line x1="260.9" y1="325.3" x2="357.1" y2="325.3" stroke="#000" stroke-width="2.5"/>

          <!-- PAREDE SUL DA COZINHA (Divisão com Q3 e Banheiro Inf) -->
          <line x1="260.9" y1="419.2" x2="357.1" y2="419.2" stroke="#000" stroke-width="2.5"/>

          <!-- Paredes Q3 e Banheiro Inf -->
          <line x1="272.4" y1="419.2" x2="272.4" y2="465.7" stroke="#000" stroke-width="2.5"/>
          <line x1="322.4" y1="419.2" x2="322.4" y2="465.7" stroke="#000" stroke-width="2.5"/>
          <line x1="359.3" y1="419.2" x2="359.3" y2="464.9" stroke="#000" stroke-width="2.5"/>
          <line x1="272.4" y1="465.7" x2="359.3" y2="465.7" stroke="#000" stroke-width="2.5"/>

          <!-- Parede Sul Sala Unificada (Divisão com Garagem) -->
          <line x1="165.8" y1="466.1" x2="272.4" y2="466.1" stroke="#000" stroke-width="2.5"/>

          <!-- Parede Sul Garagem e Q5 -->
          <line x1="127.8" y1="538.1" x2="440.3" y2="538.1" stroke="#000" stroke-width="2.5"/>
          <line x1="261.7" y1="468.4" x2="261.7" y2="538.1" stroke="#000" stroke-width="2.5"/>
          <line x1="386.3" y1="468.4" x2="386.3" y2="538.1" stroke="#000" stroke-width="2.5"/>
        </g>

        <!-- 4. LINHAS VERMELHAS TRACEJADAS DE CONCEITO ABERTO (COZINHA AMERICANA) -->
        <g id="layer-linhas-vermelhas" class="pulse-zone">
          <!-- Abertura Oeste da Cozinha para a Sala Unificada -->
          <line x1="260.9" y1="325.3" x2="260.9" y2="419.2" stroke="#dc2626" stroke-width="3" stroke-dasharray="6,4"/>
          <!-- Abertura Leste da Cozinha para as Varandas Conectadas de Lazer -->
          <line x1="357.1" y1="325.3" x2="357.1" y2="419.2" stroke="#dc2626" stroke-width="3" stroke-dasharray="6,4"/>

          <!-- Texto explicativo de abertura -->
          <text x="250.0" y="345.0" font-size="6.5" font-weight="800" fill="#dc2626" transform="rotate(-90 250 345)">LIGAÇÃO COZINHA AMERICANA</text>
          <text x="365.0" y="375.0" font-size="6.5" font-weight="800" fill="#dc2626" transform="rotate(90 365 375)">INTEGRAÇÃO VARANDA GOURMET</text>
        </g>

        <!-- 5. MOBILIÁRIO COMPLETO (COZINHA AMERICANA, SALA UNIDA & LAZER) -->
        <g id="layer-mobiliario">
          <!-- ============================================================= -->
          <!-- COZINHA AMERICANA: MÓVEIS REAIS                               -->
          <!-- ============================================================= -->
          <!-- P: Pia Cuba Dupla (2,00 x 0,60 m) -->
          <g id="furn-P" class="room-poly">
            <rect x="262.4" y="327.8" width="46.1" height="12.9" fill="#e2e8f0" stroke="#000" stroke-width="1.2"/>
            <rect x="278.7" y="331.5" width="8.3" height="6.2" fill="#94a3b8" stroke="#475569" stroke-width="0.8"/>
            <rect x="289.8" y="331.5" width="8.2" height="6.2" fill="#94a3b8" stroke="#475569" stroke-width="0.8"/>
            <circle cx="288.5" cy="329.5" r="1.5" fill="#000"/>
            <text x="271.0" y="337.0" font-size="8" font-weight="800" fill="#000">P</text>
          </g>

          <!-- AE: Bancada com Armário Aéreo (1,15 x 0,54 m) -->
          <g id="furn-AE" class="room-poly">
            <rect x="309.0" y="327.5" width="25.6" height="12.5" fill="#e2e8f0" stroke="#000" stroke-width="1.2"/>
            <text x="321.8" y="336.5" font-size="8" font-weight="800" fill="#000" text-anchor="middle">AE</text>
          </g>

          <!-- F: Fogão 4 bocas com forno e coifa (0,83 x 0,70 m) -->
          <g id="furn-F" class="room-poly">
            <rect x="335.8" y="327.7" width="19.2" height="15.5" fill="#1e293b" stroke="#000" stroke-width="1.2"/>
            <circle cx="339.8" cy="332.0" r="2.2" fill="#f97316"/>
            <circle cx="350.3" cy="331.7" r="2.2" fill="#f97316"/>
            <circle cx="339.7" cy="338.7" r="2.2" fill="#f97316"/>
            <circle cx="351.2" cy="339.1" r="2.2" fill="#f97316"/>
            <text x="345.4" y="336.5" font-size="7" font-weight="800" fill="#fff" text-anchor="middle">F</text>
          </g>

          <!-- ILHA / BALCÃO AMERICANO INTEGRADO (1,68 x 1,26 m) + 3 BANQUETAS -->
          <g id="furn-Ilha" class="room-poly">
            <!-- Bancada de Granito Preto São Gabriel -->
            <rect x="236.7" y="364.7" width="37.3" height="27.5" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" rx="1.5"/>
            <text x="255.3" y="377.0" font-size="7.5" font-weight="800" fill="#fff" text-anchor="middle">Ilha / Balcão</text>
            <text x="255.3" y="385.0" font-size="6" font-weight="700" fill="#38bdf8" text-anchor="middle">Americano</text>
            
            <!-- 3 Banquetas Altas Modernas no lado da Sala Unificada -->
            <g transform="translate(231.0, 369.0)">
              <circle cx="0" cy="0" r="3.2" fill="#9b633d" stroke="#000" stroke-width="0.8"/>
              <line x1="-2" y1="0" x2="2" y2="0" stroke="#fff" stroke-width="0.6"/>
            </g>
            <g transform="translate(231.0, 378.0)">
              <circle cx="0" cy="0" r="3.2" fill="#9b633d" stroke="#000" stroke-width="0.8"/>
              <line x1="-2" y1="0" x2="2" y2="0" stroke="#fff" stroke-width="0.6"/>
            </g>
            <g transform="translate(231.0, 387.0)">
              <circle cx="0" cy="0" r="3.2" fill="#9b633d" stroke="#000" stroke-width="0.8"/>
              <line x1="-2" y1="0" x2="2" y2="0" stroke="#fff" stroke-width="0.6"/>
            </g>
          </g>

          <!-- CENTRO: Bancada Central Gourmet (2,14 x 0,54 m) -->
          <g id="furn-Centro" class="room-poly">
            <rect x="287.9" y="367.1" width="49.2" height="12.5" fill="#e2e8f0" stroke="#000" stroke-width="1.2"/>
            <text x="312.5" y="376.0" font-size="8" font-weight="800" fill="#000" text-anchor="middle">centro</text>
          </g>

          <!-- BL: Bancada Lado (1,97 x 0,51 m) -->
          <g id="furn-BL" class="room-poly">
            <rect x="274.4" y="406.1" width="45.4" height="11.7" fill="#e2e8f0" stroke="#000" stroke-width="1.2"/>
            <text x="285.0" y="415.0" font-size="8" font-weight="800" fill="#000">BL</text>
          </g>

          <!-- AM: Armário Torre Quente Forno (0,66 x 0,54 m) -->
          <g id="furn-AM" class="room-poly">
            <rect x="321.7" y="405.0" width="15.2" height="12.6" fill="#1e293b" stroke="#000" stroke-width="1.2"/>
            <text x="329.3" y="414.0" font-size="7" font-weight="800" fill="#fff" text-anchor="middle">AM</text>
          </g>

          <!-- G: Geladeira Duplex (0,72 x 0,76 m) -->
          <g id="furn-G" class="room-poly">
            <rect x="338.8" y="401.8" width="16.5" height="16.0" fill="#cbd5e1" stroke="#000" stroke-width="1.2"/>
            <line x1="338.8" y1="407.0" x2="355.3" y2="407.0" stroke="#64748b" stroke-width="0.8"/>
            <text x="347.0" y="414.0" font-size="8" font-weight="800" fill="#000" text-anchor="middle">G</text>
          </g>

          <!-- AC: Armário de Canto (1,33 x 0,94 m) na Lavanderia -->
          <g id="furn-AC" class="room-poly">
            <rect x="418.3" y="522.4" width="20.9" height="12.5" fill="#e2e8f0" stroke="#000" stroke-width="1.2"/>
            <text x="428.7" y="531.5" font-size="7" font-weight="800" fill="#000" text-anchor="middle">AC</text>
          </g>

          <!-- ============================================================= -->
          <!-- SALA UNIFICADA: JANTAR INTEGRADO & HOME THEATER               -->
          <!-- ============================================================= -->
          <!-- Mesa de Jantar (Na parte superior da Sala, ao lado do balcão) -->
          <g id="furn-jantar" transform="translate(180.0, 315.0)">
            <rect width="28.0" height="42.0" rx="2" fill="#8c6747" stroke="#4a3525" stroke-width="1"/>
            <!-- 4 Cadeiras -->
            <rect x="-6" y="6" width="5" height="12" rx="1" fill="#cbd5e1" stroke="#475569"/>
            <rect x="-6" y="24" width="5" height="12" rx="1" fill="#cbd5e1" stroke="#475569"/>
            <rect x="29" y="6" width="5" height="12" rx="1" fill="#cbd5e1" stroke="#475569"/>
            <rect x="29" y="24" width="5" height="12" rx="1" fill="#cbd5e1" stroke="#475569"/>
            <text x="14.0" y="24.0" font-size="6" font-weight="700" fill="#fff" text-anchor="middle">Jantar</text>
          </g>

          <!-- Living / Sofá em L na parte inferior da Sala Unificada -->
          <g id="furn-living" transform="translate(185.0, 420.0)">
            <!-- Sofá Confortável Integrado -->
            <rect x="0" y="0" width="46.0" height="18.0" rx="3" fill="#52606d" stroke="#334155" stroke-width="1"/>
            <rect x="0" y="18" width="18.0" height="20.0" rx="3" fill="#52606d" stroke="#334155" stroke-width="1"/>
            <!-- Mesa de Centro -->
            <rect x="24.0" y="22.0" width="18.0" height="14.0" rx="2" fill="#8c6747"/>
            <text x="23.0" y="12.0" font-size="6" font-weight="700" fill="#fff" text-anchor="middle">Estar / TV</text>
          </g>

          <!-- ============================================================= -->
          <!-- VARANDAS CONECTADAS: ÁREA DE LAZER GOURMET                    -->
          <!-- ============================================================= -->
          <!-- Churrasqueira em Tijolos Refratários -->
          <g transform="translate(366.0, 428.0)">
            <rect width="26.0" height="32.0" rx="2" fill="#a34731" stroke="#000" stroke-width="1.2"/>
            <rect x="4" y="5" width="18" height="22" fill="#1e293b"/>
            <text x="13.0" y="18.0" font-size="6.5" font-weight="800" fill="#fff" text-anchor="middle">Churrasq.</text>
          </g>
          <!-- Mesa Gourmet da Varanda -->
          <g transform="translate(398.0, 395.0)">
            <rect width="32.0" height="20.0" rx="2" fill="#8c6747" stroke="#000" stroke-width="1"/>
            <text x="16.0" y="13.0" font-size="6" font-weight="700" fill="#fff" text-anchor="middle">Mesa Lazer</text>
          </g>
        </g>

        <!-- 6. NOMES E IDENTIFICAÇÃO DOS ESPAÇOS INTEGRADOS -->
        <g id="layer-textos">
          <text x="200.0" y="255.0" font-size="12" font-weight="700" fill="#000" text-anchor="middle">quarto1</text>
          <text x="277.0" y="222.0" font-size="12" font-weight="700" fill="#000" text-anchor="middle">quarto2</text>
          <text x="288.0" y="302.0" font-size="10" font-weight="700" fill="#000" text-anchor="middle">banheiro</text>

          <!-- RÓTULO PRINCIPAL: SALA UNIFICADA -->
          <g transform="translate(210.0, 388.0)">
            <rect x="-55" y="-12" width="110" height="24" rx="4" fill="rgba(255,255,255,0.85)" stroke="#f97316" stroke-width="1.2"/>
            <text x="0" y="0" font-size="9" font-weight="900" fill="#ea580c" text-anchor="middle">SALA UNIFICADA</text>
            <text x="0" y="9" font-size="6.5" font-weight="700" fill="#431407" text-anchor="middle">Estar & Jantar • ~26,0 m²</text>
          </g>

          <!-- RÓTULO PRINCIPAL: COZINHA AMERICANA -->
          <g transform="translate(310.0, 355.0)">
            <text font-size="12" font-weight="900" fill="#ea580c" text-anchor="middle">COZINHA</text>
            <text y="10" font-size="8.5" font-weight="800" fill="#c2410c" text-anchor="middle">AMERICANA</text>
          </g>

          <text x="297.4" y="432.0" font-size="9" font-weight="700" fill="#000" text-anchor="middle">quarto3</text>
          <text x="341.8" y="432.0" font-size="8" font-weight="700" fill="#000" text-anchor="middle">banheiro</text>

          <text x="193.5" y="505.0" font-size="12" font-weight="700" fill="#000" text-anchor="middle">garagem</text>
          <text x="324.0" y="505.0" font-size="12" font-weight="700" fill="#000" text-anchor="middle">quarto5</text>
          
          <text x="414.5" y="505.0" font-size="9" font-weight="700" fill="#000" text-anchor="middle">lavanderia</text>

          <!-- RÓTULO: VARANDAS CONECTADAS DE LAZER -->
          <g transform="translate(405.0, 335.0)">
            <text font-size="10" font-weight="800" fill="#78350f" text-anchor="middle">Varandas Conectadas</text>
            <text y="12" font-size="8.5" font-weight="700" fill="#92400e" text-anchor="middle">Área de Lazer & Piscina</text>
          </g>

          <!-- Varanda Lilás Conectada -->
          <g transform="translate(130.0, 425.0)">
            <text font-size="10" font-weight="800" fill="#6b21a8" text-anchor="middle">Varanda Lilás</text>
            <text y="10" font-size="7.5" font-weight="700" fill="#7e22ce" text-anchor="middle">Conectada</text>
          </g>

          <!-- Horta com cerca -->
          <text x="501.5" y="310.0" font-size="11" font-weight="700" fill="#1b4332" text-anchor="middle">Hor-</text>
          <text x="501.5" y="325.0" font-size="11" font-weight="700" fill="#1b4332" text-anchor="middle">ta</text>
          <text x="501.5" y="340.0" font-size="11" font-weight="700" fill="#1b4332" text-anchor="middle">co-</text>
          <text x="501.5" y="355.0" font-size="11" font-weight="700" fill="#1b4332" text-anchor="middle">m -</text>
          <text x="501.5" y="370.0" font-size="11" font-weight="700" fill="#1b4332" text-anchor="middle">cer-</text>
          <text x="501.5" y="385.0" font-size="11" font-weight="700" fill="#1b4332" text-anchor="middle">ca</text>

          <!-- Jardins -->
          <text x="342.2" y="159.0" font-size="13" font-weight="700" fill="#1b4332" text-anchor="middle">jardim</text>
          <text x="96.4" y="250.0" font-size="13" font-weight="700" fill="#1b4332" text-anchor="middle">jardim</text>
          <text x="77.2" y="610.0" font-size="13" font-weight="700" fill="#1b4332" text-anchor="middle">jardim</text>
          <text x="323.7" y="645.0" font-size="14" font-weight="800" fill="#1b4332" text-anchor="middle">Jardim</text>
        </g>

        <!-- 7. CAIXAS DE MEDIDAS TÉCNICAS ORIGINAIS DA PRANCHA -->
        <g id="layer-caixas-medidas">
          <!-- Jardim Superior: Altura: 4 cm, Largura: 15,38 cm -->
          <g class="callout-box" transform="translate(191.5, 130.6)">
            <rect width="117.0" height="56.7" rx="6" fill="#e5e7eb" stroke="#9ca3af" stroke-width="1.2"/>
            <text x="12" y="24" font-size="9" fill="#1f2937">↕ Altura: 4 cm</text>
            <text x="12" y="47" font-size="9" fill="#1f2937">↔ Largura: 15,38 cm</text>
          </g>

          <!-- Jardim Esquerdo: Altura: 12,13 cm, Largura: 5,83 cm -->
          <g class="callout-box" transform="translate(39.2, 274.7)">
            <rect width="115.8" height="50.6" rx="6" fill="#e5e7eb" stroke="#9ca3af" stroke-width="1.2"/>
            <text x="10" y="21" font-size="8.5" fill="#1f2937">↕ Altura: 12,13 cm</text>
            <text x="10" y="42" font-size="8.5" fill="#1f2937">↔ Largura: 5,83 cm</text>
          </g>

          <!-- Quarto 1: Altura: 4 cm, Largura: 3,01 cm -->
          <g class="callout-box" transform="translate(167.6, 265.3)">
            <rect width="65.8" height="28.7" rx="4" fill="#e5e7eb" stroke="#9ca3af" stroke-width="1"/>
            <text x="4" y="12" font-size="6.5" fill="#1f2937">↕ Altura: 4 cm</text>
            <text x="4" y="23" font-size="6.5" fill="#1f2937">↔ Largura: 3,01 cm</text>
          </g>

          <!-- Quarto 2: Altura: 3,01 cm, Largura: 3,51 cm -->
          <g class="callout-box" transform="translate(236.4, 239.1)">
            <rect width="77.5" height="35.8" rx="4" fill="#e5e7eb" stroke="#9ca3af" stroke-width="1"/>
            <text x="6" y="15" font-size="7.5" fill="#1f2937">↕ Altura: 3,01 cm</text>
            <text x="6" y="29" font-size="7.5" fill="#1f2937">↔ Largura: 3,51 cm</text>
          </g>

          <!-- Sala Setor Superior: Altura: 4,01 cm, Largura: 3,01 cm -->
          <g class="callout-box" transform="translate(172.0, 359.8)">
            <rect width="61.6" height="27.8" rx="4" fill="#e5e7eb" stroke="#9ca3af" stroke-width="1"/>
            <text x="4" y="11" font-size="6.5" fill="#1f2937">↕ Altura: 4,01 cm</text>
            <text x="4" y="22" font-size="6.5" fill="#1f2937">↔ Largura: 3,01 cm</text>
          </g>

          <!-- Sala Setor Inferior: Altura: 3,02 cm, Largura: 4,63 cm -->
          <g class="callout-box" transform="translate(166.9, 438.6)">
            <rect width="59.6" height="25.7" rx="3" fill="#e5e7eb" stroke="#9ca3af" stroke-width="1"/>
            <text x="3" y="10" font-size="6.5" fill="#1f2937">↕ Altura: 3,02 cm</text>
            <text x="3" y="20" font-size="6.5" fill="#1f2937">↔ Largura: 4,63 cm</text>
          </g>

          <!-- Varandas Lilás: 3,26x2,78 cm e 3,32x2,94 cm -->
          <g class="callout-box" transform="translate(34.2, 399.9)">
            <rect width="53.8" height="43.8" rx="4" fill="#e5e7eb" stroke="#9ca3af" stroke-width="1"/>
            <text x="6" y="16" font-size="7.5" font-weight="700">3,26 cm</text>
            <text x="6" y="34" font-size="7.5" font-weight="700">2,78 cm</text>
          </g>
          <g class="callout-box" transform="translate(103.9, 400.2)">
            <rect width="54.2" height="42.1" rx="4" fill="#e5e7eb" stroke="#9ca3af" stroke-width="1"/>
            <text x="6" y="15" font-size="7.5" font-weight="700">3,32 cm</text>
            <text x="6" y="33" font-size="7.5" font-weight="700">2,94 cm</text>
          </g>

          <!-- Cozinha: Altura: 4,08 cm, Largura: 4,18 cm -->
          <g class="callout-box" transform="translate(282.0, 381.6)">
            <rect width="51.8" height="22.9" rx="3" fill="#e5e7eb" stroke="#9ca3af" stroke-width="1"/>
            <text x="3" y="9" font-size="6.5" fill="#1f2937">↕ Altura: 4,08 cm</text>
            <text x="3" y="18" font-size="6.5" fill="#1f2937">↔ Largura: 4,18 cm</text>
          </g>

          <!-- Varandas Conectadas Lazer: Altura: 7,02 cm, Largura: 3,34 cm -->
          <g class="callout-box" transform="translate(365.5, 304.6)">
            <rect width="72.5" height="29.0" rx="3" fill="#e5e7eb" stroke="#9ca3af" stroke-width="1"/>
            <text x="4" y="11" font-size="6.8" fill="#1f2937">↕ Altura: 7,02 cm</text>
            <text x="4" y="23" font-size="6.8" fill="#1f2937">↔ Largura: 3,34 cm</text>
          </g>

          <!-- Quarto 3: 1,9 x 2,17 cm -->
          <g class="callout-box" transform="translate(282.0, 436.4)">
            <rect width="33.2" height="28.1" rx="2" fill="#e5e7eb" stroke="#9ca3af" stroke-width="1"/>
            <text x="3" y="11" font-size="6.5" font-weight="700">1,9 cm</text>
            <text x="3" y="22" font-size="6.5" font-weight="700">2,17 cm</text>
          </g>

          <!-- Banheiro Inferior: 1,79 x 1,52 cm -->
          <g class="callout-box" transform="translate(325.6, 440.9)">
            <rect width="29.3" height="23.9" rx="2" fill="#e5e7eb" stroke="#9ca3af" stroke-width="1"/>
            <text x="2" y="9" font-size="6" font-weight="700">1,79 cm</text>
            <text x="2" y="19" font-size="6" font-weight="700">1,52 cm</text>
          </g>

          <!-- Garagem: Altura: 3 cm, Largura: 5,71 cm -->
          <g class="callout-box" transform="translate(127.2, 513.0)">
            <rect width="58.7" height="25.5" rx="3" fill="#e5e7eb" stroke="#9ca3af" stroke-width="1"/>
            <text x="3" y="10" font-size="6.5" fill="#1f2937">↕ Altura: 3 cm</text>
            <text x="3" y="20" font-size="6.5" fill="#1f2937">↔ Largura: 5,71 cm</text>
          </g>

          <!-- Quarto 5: Altura: 3 cm, Largura: 5,41 cm -->
          <g class="callout-box" transform="translate(265.4, 512.2)">
            <rect width="49.9" height="24.5" rx="3" fill="#e5e7eb" stroke="#9ca3af" stroke-width="1"/>
            <text x="3" y="10" font-size="6.5" fill="#1f2937">↕ Altura: 3 cm</text>
            <text x="3" y="20" font-size="6.5" fill="#1f2937">↔ Largura: 5,41 cm</text>
          </g>

          <!-- Lavanderia: 2,24 x 2,95 cm -->
          <g class="callout-box" transform="translate(389.3, 469.0)">
            <rect width="23.8" height="21.0" rx="2" fill="#e5e7eb" stroke="#9ca3af" stroke-width="1"/>
            <text x="2" y="8" font-size="5.5" font-weight="700">2,24 cm</text>
            <text x="2" y="17" font-size="5.5" font-weight="700">2,95 cm</text>
          </g>

          <!-- Pergolado: Altura: 3,05 cm, Largura: 2,91 cm -->
          <g class="callout-box" transform="translate(386.5, 650.9)">
            <rect width="82.2" height="40.2" rx="4" fill="#e5e7eb" stroke="#9ca3af" stroke-width="1"/>
            <text x="4" y="16" font-size="7.5" fill="#1f2937">↕ Altura: 3,05 cm</text>
            <text x="4" y="32" font-size="7.5" fill="#1f2937">↔ Largura: 2,91 cm</text>
          </g>
        </g>

        <!-- 8. LEGENDA OFICIAL DOS MÓVEIS (CANTO SUPERIOR ESQUERDO) -->
        <g id="layer-legenda" transform="translate(30.6, 9.9)">
          <text font-size="6.8" font-weight="800" fill="#1e293b" y="10">Largura x Profundidade (metros)</text>
          <text font-size="6.2" font-weight="600" fill="#334155" y="20">G = geladeira = 0,72 x 0,76</text>
          <text font-size="6.2" font-weight="600" fill="#334155" y="30">Ilha = ilha de granito = 1,68 x 1,26</text>
          <text font-size="6.2" font-weight="600" fill="#334155" y="40">F = fogão = 0,83 x 0,70</text>
          <text font-size="6.2" font-weight="600" fill="#334155" y="50">P = pia cuba dupla = 2 x 0,6</text>
          <text font-size="6.2" font-weight="600" fill="#334155" y="60">AC = banca de canto com armário aéreo = 1,33 x 0,94</text>
          <text font-size="6.2" font-weight="600" fill="#334155" y="70">AE = bancada com armário aéreo = 1,15 x 0,54</text>
          <text font-size="6.2" font-weight="600" fill="#334155" y="80">AM = armário vertical forno = 0,66 x 0,54</text>
          <text font-size="6.2" font-weight="600" fill="#334155" y="90">BL = Bancada Lado = 1,97 x 0,51</text>
          <text font-size="6.2" font-weight="600" fill="#334155" y="100">Centro = 2,14 x 0,54</text>
        </g>

        <!-- 9. RODAPÉ DA PRANCHA -->
        <g transform="translate(180, 765)">
          <text font-size="7" font-weight="600" fill="#64748b" text-anchor="middle">( X ) Público   ( ) Interno   ( ) Setorial   ( ) Confidencial</text>
          <text font-size="6.5" font-weight="500" fill="#94a3b8" text-anchor="middle" y="10">Dados Pessoais</text>
        </g>

      </g>
    </svg>

    <!-- Layer Toggles Floating Bar -->
    <div id="layer-bar" class="floating-bar">
      <button class="chip-toggle active" data-layer="layer-caixas-medidas">
        <span class="dot" style="background:#ef4444"></span> Caixas da Prancha
      </button>
      <button class="chip-toggle active" data-layer="layer-mobiliario">
        <span class="dot" style="background:#38bdf8"></span> Móveis & Bancadas
      </button>
      <button class="chip-toggle active" data-layer="layer-linhas-vermelhas">
        <span class="dot" style="background:#dc2626"></span> Aberturas Vermelhas
      </button>
      <button class="chip-toggle active" data-layer="layer-textos">
        <span class="dot" style="background:#facc15"></span> Identificação
      </button>
      <button class="chip-toggle active" data-layer="layer-jardins">
        <span class="dot" style="background:#52b788"></span> Jardins & Lazer
      </button>
      <button class="chip-toggle active" id="btn-focus-integrado">
        <span class="dot" style="background:#f97316"></span> Foco Sala + Cozinha + Varandas
      </button>
    </div>

    <!-- Opacity Slider for Original Overlay Comparison -->
    <div id="overlay-control" class="floating-bar">
      <span>Comparar com Desenho Original:</span>
      <input type="range" id="overlay-slider" min="0" max="100" value="0">
      <span id="overlay-val">0%</span>
    </div>

    <!-- Navigation Pan/Zoom Controls -->
    <div id="nav-controls" class="floating-bar">
      <button class="btn-icon" id="btn-zoom-in" title="Aproximar Zoom ( + )">
        <svg viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
      </button>
      <button class="btn-icon" id="btn-zoom-out" title="Afastar Zoom ( - )">
        <svg viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/></svg>
      </button>
      <button class="btn-icon" id="btn-zoom-reset" title="Ver Prancha Completa">
        <svg viewBox="0 0 24 24"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
      </button>
    </div>

    <!-- Inspector Drawer on Click -->
    <aside id="inspector">
      <div class="inspector-header">
        <h3 id="insp-title">Detalhes do Ambiente</h3>
        <button class="inspector-close" id="insp-close">&times;</button>
      </div>
      <div class="inspector-badge" id="insp-badge">CÔMODO</div>

      <div class="stat-grid">
        <div class="stat-card">
          <span>Dimensões Reais (m)</span>
          <strong id="insp-dims">0,00 × 0,00 m</strong>
        </div>
        <div class="stat-card">
          <span>Área Útil</span>
          <strong id="insp-area">0,0 m²</strong>
        </div>
      </div>

      <div class="stat-card" style="margin-bottom: 10px;">
        <span>Medida na Prancha Original</span>
        <strong id="insp-scale">0,00 × 0,00 cm</strong>
      </div>

      <div class="inspector-details" id="insp-desc">
        Clique em qualquer cômodo ou móvel para inspecionar medidas e especificações técnicas.
      </div>
    </aside>
  </div>

  <script>
    /* ==========================================================================
       1. DATABASE EXATO DE TODOS OS CÔMODOS E MÓVEIS
       ========================================================================== */
    const floorPlanDatabase = {
      'poly-sala-unificada': {
        name: 'Sala Unificada (Estar & Jantar)',
        badge: 'Ambiente Social Integrado',
        dims: '4,63 × 7,03 m (Área Total Integrada)',
        area: '26,05 m²',
        scale: 'Setor Jantar: 4,01x3,01 cm • Setor Estar: 3,02x4,63 cm',
        desc: 'As salas superior e inferior estão UNIDAS em um amplo espaço social integrado em L. Acomoda a mesa de jantar de frente para o balcão americano e a sala de estar/TV na porção inferior, com circulação fluida e abertura direta para a varanda lilás lateral.'
      },
      'poly-cozinha': {
        name: 'Cozinha Americana',
        badge: 'Conceito Aberto Total',
        dims: '4,18 × 4,08 m',
        area: '17,05 m²',
        scale: 'Altura: 4,08 cm • Largura: 4,18 cm',
        desc: 'Cozinha americana 100% aberta, sem paredes divisórias com a Sala Unificada (oeste) nem com as Varandas Conectadas de Lazer (leste). A integração oeste ocorre através do Balcão Americano / Ilha de Granito com 3 banquetas e passagens livres de circulação.'
      },
      'furn-Ilha': {
        name: 'Balcão Americano / Ilha de Granito',
        badge: 'Divisa Aberta & Refeições',
        dims: '1,68 × 1,26 m',
        area: '2,12 m²',
        scale: 'Ilha = 1,68 x 1,26 m',
        desc: 'Ilha de granito Preto São Gabriel posicionada na abertura entre a Cozinha e a Sala Unificada. Funciona como balcão passa-pratos e bancada de refeições rápidas com 3 banquetas voltadas para a sala.'
      },
      'poly-varanda-lazer-conectada': {
        name: 'Varandas Conectadas de Lazer',
        badge: 'Complexo Total de Lazer',
        dims: '6,90 × 14,33 m (Deck, Piscina, Gourmet & Circulação)',
        area: '75,47 m²',
        scale: 'Varanda Piscina + Área de Lazer + Varanda Lateral',
        desc: 'Todas as varandas de lazer estão CONECTADAS em um único e amplo ambiente ao ar livre. O deck da piscina, a varanda gourmet com churrasqueira e a galeria lateral de circulação formam um espaço contínuo, conectado diretamente à Cozinha Americana.'
      },
      'poly-varanda-lilas-conectada': {
        name: 'Varanda Lilás Conectada',
        badge: 'Varanda Lateral Unificada',
        dims: '2,94 × 6,58 m',
        area: '18,82 m²',
        scale: '3,26 x 2,78 cm e 3,32 x 2,94 cm (Unidas)',
        desc: 'Varanda em tom lilás totalmente conectada na lateral esquerda da residência, com acesso direto a partir da Sala Unificada.'
      },
      'furn-P': {
        name: 'P: Pia Cuba Dupla',
        badge: 'Bancada Molhada',
        dims: '2,00 × 0,60 m',
        area: '1,20 m²',
        scale: 'P = 2 x 0,6 m',
        desc: 'Bancada com 2 cubas de aço inox e torneira gourmet na parede norte da cozinha americana.'
      },
      'furn-AE': {
        name: 'AE: Bancada c/ Armário Aéreo',
        badge: 'Marcenaria Superior',
        dims: '1,15 × 0,54 m',
        area: '0,62 m²',
        scale: 'AE = 1,15 x 0,54 m',
        desc: 'Módulo de bancada com armário aéreo suspenso para organização de louças e mantimentos.'
      },
      'furn-F': {
        name: 'F: Fogão & Coifa',
        badge: 'Área Quente',
        dims: '0,83 × 0,70 m',
        area: '0,58 m²',
        scale: 'F = 0,83 x 0,70 m',
        desc: 'Fogão de 4 bocas com forno e coifa de aço inox na parede norte da cozinha.'
      },
      'furn-Centro': {
        name: 'Centro: Bancada Central',
        badge: 'Ilha de Preparo',
        dims: '2,14 × 0,54 m',
        area: '1,16 m²',
        scale: 'Centro = 2,14 x 0,54 m',
        desc: 'Bancada ilha no miolo da cozinha americana para corte e preparação de alimentos.'
      },
      'furn-BL': {
        name: 'BL: Bancada Lado',
        badge: 'Bancada de Serviço',
        dims: '1,97 × 0,51 m',
        area: '1,00 m²',
        scale: 'BL = 1,97 x 0,51 m',
        desc: 'Bancada lateral de serviço equipada com gaveteiros para talheres e utensílios.'
      },
      'furn-AM': {
        name: 'AM: Armário Vertical Forno',
        badge: 'Torre Quente',
        dims: '0,66 × 0,54 m',
        area: '0,36 m²',
        scale: 'AM = 0,66 x 0,54 m',
        desc: 'Torre quente vertical com forno elétrico e micro-ondas embutidos.'
      },
      'furn-G': {
        name: 'G: Geladeira Duplex',
        badge: 'Refrigeração',
        dims: '0,72 × 0,76 m',
        area: '0,55 m²',
        scale: 'G = 0,72 x 0,76 m',
        desc: 'Geladeira duplex frost-free com dispenser de água.'
      },
      'poly-quarto1': {
        name: 'Quarto 1',
        badge: 'Canto Superior Esquerdo',
        dims: '3,01 × 4,00 m',
        area: '12,04 m²',
        scale: 'Altura: 4 cm • Largura: 3,01 cm',
        desc: 'Dormitório no canto superior esquerdo com acesso ao hall de circulação.'
      },
      'poly-quarto2': {
        name: 'Quarto 2',
        badge: 'Topo Central',
        dims: '3,51 × 3,01 m',
        area: '10,57 m²',
        scale: 'Altura: 3,01 cm • Largura: 3,51 cm',
        desc: 'Dormitório no topo da residência, ao lado do Quarto 1 e acima do Banheiro Superior.'
      },
      'poly-banheiro-sup': {
        name: 'Banheiro Superior',
        badge: 'Área Molhada',
        dims: '2,43 × 1,87 m',
        area: '4,54 m²',
        scale: 'Abaixo do Quarto 2',
        desc: 'Banheiro posicionado logo abaixo do Quarto 2. Sua parede inferior é a parede superior da Cozinha.'
      },
      'poly-quarto3': {
        name: 'Quarto 3',
        badge: 'Dormitório Compacto',
        dims: '2,17 × 1,90 m',
        area: '4,12 m²',
        scale: '1,9 cm • 2,17 cm',
        desc: 'Quarto localizado logo abaixo da Cozinha e ao lado do Banheiro Inferior.'
      },
      'poly-banheiro-inf': {
        name: 'Banheiro Inferior',
        badge: 'Área Molhada',
        dims: '1,79 × 1,52 m',
        area: '2,72 m²',
        scale: '1,79 cm • 1,52 cm',
        desc: 'Banheiro ao lado do Quarto 3, servindo à área íntima inferior.'
      },
      'poly-garagem': {
        name: 'Garagem (Quarto 4)',
        badge: 'Vaga Coberta',
        dims: '5,71 × 3,00 m',
        area: '17,13 m²',
        scale: 'Altura: 3 cm • Largura: 5,71 cm',
        desc: 'Garagem coberta para veículos no canto inferior esquerdo da residência.'
      },
      'poly-quarto5': {
        name: 'Quarto 5 (Suíte)',
        badge: 'Área Íntima Inferior',
        dims: '5,41 × 3,00 m',
        area: '16,23 m²',
        scale: 'Altura: 3 cm • Largura: 5,41 cm',
        desc: 'Quarto amplo ao lado da garagem e da lavanderia, com vista para o jardim dos fundos.'
      },
      'poly-lavanderia': {
        name: 'Lavanderia & Serviço',
        badge: 'Área de Serviço',
        dims: '2,24 × 2,95 m',
        area: '6,61 m²',
        scale: '2,24 cm • 2,95 cm',
        desc: 'Área de serviço com tanque, máquina e armário de canto (AC).'
      },
      'poly-piscina': {
        name: 'Piscina de Alvenaria',
        badge: 'Lazer Aquático',
        dims: '2,50 × 2,45 m',
        area: '4,81 m²',
        scale: 'Piscina Oval Integrada',
        desc: 'Piscina com revestimento cerâmico e sistema de filtragem no deck de madeira.'
      },
      'poly-horta': {
        name: 'Horta com Cerca',
        badge: 'Cultivo Orgânico',
        dims: '1,48 × 14,33 m',
        area: '21,21 m²',
        scale: 'Faixa Lateral Leste',
        desc: 'Horta fechada com cerquinha rústica de madeira para hortaliças e temperos frescos.'
      },
      'poly-casa-cachorro': {
        name: 'Casa do Cachorro',
        badge: 'Espaço Pet',
        dims: '3,58 × 3,76 m',
        area: '13,46 m²',
        scale: 'Canto Superior Direito',
        desc: 'Casinha protegida e confortável para os animais de estimação no jardim superior.'
      },
      'poly-casa-arvore': {
        name: 'Casa da Árvore',
        badge: 'Lazer Família',
        dims: '3,58 × 3,76 m',
        area: '13,46 m²',
        scale: 'Jardim 4,24 x 12,15 cm',
        desc: 'Casinha suspensa em madeira com plataforma elevada e escada no jardim lateral esquerdo.'
      },
      'poly-pergolado': {
        name: 'Pergolado em Madeira',
        badge: 'Lounge Externo',
        dims: '2,91 × 3,05 m',
        area: '8,88 m²',
        scale: 'Altura: 3,05 cm • Largura: 2,91 cm',
        desc: 'Estrutura contemporânea de pergolado ripado para descanso ao ar livre no jardim dos fundos.'
      },
      'poly-jardim-sup': {
        name: 'Jardim Superior',
        badge: 'Paisagismo',
        dims: '15,38 × 4,00 m',
        area: '61,52 m²',
        scale: 'Altura: 4 cm • Largura: 15,38 cm',
        desc: 'Área ajardinada frontal/superior da propriedade.'
      },
      'poly-jardim-esq': {
        name: 'Jardim Lateral Esquerdo',
        badge: 'Paisagismo',
        dims: '5,83 × 12,13 m',
        area: '70,72 m²',
        scale: 'Altura: 12,13 cm • Largura: 5,83 cm',
        desc: 'Gramado lateral com arborização.'
      },
      'poly-jardim-fundos': {
        name: 'Jardim dos Fundos',
        badge: 'Paisagismo & Lazer',
        dims: '17,00 × 9,00 m',
        area: '153,00 m²',
        scale: 'Altura: 9 cm • Largura: 17 cm',
        desc: 'Grande quintal gramado dos fundos contendo o Pergolado de descanso.'
      }
    };

    /* ==========================================================================
       2. CONTROLE DE PAN E ZOOM
       ========================================================================== */
    const svg = document.getElementById('blueprint-svg');
    const viewportGroup = document.getElementById('viewport-group');
    const workspace = document.getElementById('workspace');

    let currentScale = 1;
    let pointX = 0;
    let pointY = 0;
    let isPanning = false;
    let startX = 0;
    let startY = 0;

    function updateTransform() {
      viewportGroup.setAttribute('transform', `translate(${pointX}, ${pointY}) scale(${currentScale})`);
    }

    workspace.addEventListener('mousedown', (e) => {
      if (e.target.closest('#inspector') || e.target.closest('.floating-bar')) return;
      isPanning = true;
      startX = e.clientX - pointX;
      startY = e.clientY - pointY;
    });

    window.addEventListener('mousemove', (e) => {
      if (!isPanning) return;
      pointX = e.clientX - startX;
      pointY = e.clientY - startY;
      updateTransform();
    });

    window.addEventListener('mouseup', () => { isPanning = false; });

    let touchDist = null;
    workspace.addEventListener('touchstart', (e) => {
      if (e.touches.length === 1) {
        isPanning = true;
        startX = e.touches[0].clientX - pointX;
        startY = e.touches[0].clientY - pointY;
      } else if (e.touches.length === 2) {
        isPanning = false;
        touchDist = Math.hypot(
          e.touches[0].clientX - e.touches[1].clientX,
          e.touches[0].clientY - e.touches[1].clientY
        );
      }
    }, { passive: true });

    workspace.addEventListener('touchmove', (e) => {
      if (isPanning && e.touches.length === 1) {
        pointX = e.touches[0].clientX - startX;
        pointY = e.touches[0].clientY - startY;
        updateTransform();
      } else if (e.touches.length === 2 && touchDist) {
        const curDist = Math.hypot(
          e.touches[0].clientX - e.touches[1].clientX,
          e.touches[0].clientY - e.touches[1].clientY
        );
        zoomAt(e.touches[0].clientX, e.touches[0].clientY, curDist / touchDist > 1 ? 1.04 : 0.96);
        touchDist = curDist;
      }
    }, { passive: true });

    workspace.addEventListener('touchend', () => { isPanning = false; touchDist = null; });

    workspace.addEventListener('wheel', (e) => {
      e.preventDefault();
      zoomAt(e.clientX, e.clientY, e.deltaY < 0 ? 1.12 : 0.89);
    }, { passive: false });

    function zoomAt(clientX, clientY, factor) {
      const rect = workspace.getBoundingClientRect();
      const mouseX = clientX - rect.left;
      const mouseY = clientY - rect.top;

      const newScale = Math.min(Math.max(currentScale * factor, 0.4), 6.0);
      const ratio = newScale / currentScale;

      pointX = mouseX - (mouseX - pointX) * ratio;
      pointY = mouseY - (mouseY - pointY) * ratio;
      currentScale = newScale;

      updateTransform();
    }

    document.getElementById('btn-zoom-in').addEventListener('click', () => {
      const r = workspace.getBoundingClientRect();
      zoomAt(r.width/2, r.height/2, 1.25);
    });

    document.getElementById('btn-zoom-out').addEventListener('click', () => {
      const r = workspace.getBoundingClientRect();
      zoomAt(r.width/2, r.height/2, 0.8);
    });

    document.getElementById('btn-zoom-reset').addEventListener('click', () => {
      currentScale = 1;
      pointX = 0;
      pointY = 0;
      updateTransform();
    });

    // Foco Integrado: Salas Unidas + Cozinha Americana + Varandas Conectadas
    document.getElementById('btn-focus-integrado').addEventListener('click', () => {
      currentScale = 2.4;
      pointX = -450;
      pointY = -680;
      updateTransform();
      selectElement('poly-cozinha');
    });

    /* ==========================================================================
       3. CONTROLE DE CAMADAS (LAYERS)
       ========================================================================== */
    document.querySelectorAll('.chip-toggle[data-layer]').forEach(btn => {
      btn.addEventListener('click', () => {
        btn.classList.toggle('active');
        const layerId = btn.getAttribute('data-layer');
        const layer = document.getElementById(layerId);
        if (layer) {
          layer.style.display = btn.classList.contains('active') ? '' : 'none';
        }
      });
    });

    /* ==========================================================================
       4. SUPERPOSIÇÃO DA IMAGEM ORIGINAL (SLIDER OPACIDADE)
       ========================================================================== */
    const overlaySlider = document.getElementById('overlay-slider');
    const overlayVal = document.getElementById('overlay-val');
    const layerOverlay = document.getElementById('layer-original-overlay');

    overlaySlider.addEventListener('input', (e) => {
      const val = e.target.value;
      overlayVal.textContent = `${val}%`;
      layerOverlay.setAttribute('opacity', val / 100);
    });

    /* ==========================================================================
       5. TEMAS VISUAIS
       ========================================================================== */
    const btnHuman = document.getElementById('btn-theme-human');
    const btnBlue = document.getElementById('btn-theme-blue');

    btnHuman.addEventListener('click', () => {
      document.body.className = '';
      btnHuman.classList.add('active');
      btnBlue.classList.remove('active');
    });

    btnBlue.addEventListener('click', () => {
      document.body.className = 'theme-blueprint';
      btnBlue.classList.add('active');
      btnHuman.classList.remove('active');
    });

    document.getElementById('btn-print').addEventListener('click', () => {
      window.print();
    });

    /* ==========================================================================
       6. INSPETOR DE ELEMENTOS CLICADOS
       ========================================================================== */
    const inspector = document.getElementById('inspector');
    const inspTitle = document.getElementById('insp-title');
    const inspBadge = document.getElementById('insp-badge');
    const inspDims = document.getElementById('insp-dims');
    const inspArea = document.getElementById('insp-area');
    const inspScale = document.getElementById('insp-scale');
    const inspDesc = document.getElementById('insp-desc');
    let selectedEl = null;

    function selectElement(id) {
      const data = floorPlanDatabase[id];
      if (!data) return;

      if (selectedEl) selectedEl.classList.remove('room-selected');

      const el = document.getElementById(id);
      if (el) {
        el.classList.add('room-selected');
        selectedEl = el;
      }

      inspTitle.textContent = data.name;
      inspBadge.textContent = data.badge;
      inspDims.textContent = data.dims;
      inspArea.textContent = data.area;
      inspScale.textContent = data.scale;
      inspDesc.textContent = data.desc;

      inspector.classList.add('open');
    }

    document.querySelectorAll('.room-poly').forEach(el => {
      el.addEventListener('click', (e) => {
        e.stopPropagation();
        selectElement(el.id);
      });
    });

    document.getElementById('insp-close').addEventListener('click', () => {
      inspector.classList.remove('open');
      if (selectedEl) {
        selectedEl.classList.remove('room-selected');
        selectedEl = null;
      }
    });

    workspace.addEventListener('click', (e) => {
      if (!e.target.closest('.room-poly') && !e.target.closest('#inspector') && !e.target.closest('.floating-bar')) {
        inspector.classList.remove('open');
        if (selectedEl) {
          selectedEl.classList.remove('room-selected');
          selectedEl = null;
        }
      }
    });
  </script>
</body>
</html>
'''

with open('F:/casa-completa-lazer-3d/index.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print("index.html updated successfully with Salas Unidas, Cozinha Americana e Varandas Conectadas!")
