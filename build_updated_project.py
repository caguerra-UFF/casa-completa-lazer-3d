# -*- coding: utf-8 -*-
"""
Gerador Completo da Planta Baixa 2D Técnica e Atualização do Modelo 3D
Atende com rigor a todas as diretrizes do cliente:
1. Rua na frente da casa (lado oeste) com asfalto, faixa amarela, calçada e meio-fio rebaixado
2. Cercado de eucalipto (mourão) em meia-lua partindo da extremidade da garagem até a borda, seguindo aos fundos e contornando até o Quarto 1
3. Cozinha conectada à Sala, Corredor e também à Varanda de Lazer em Conceito Aberto total
4. No centro da cozinha há SOMENTE a bancada retangular 'centro' (2,14 x 0,54 m)
5. Ilha de granito (1,68 x 1,26 m) com 3 banquetas na divisa da cozinha com sala/corredor
6. Piscina redonda de plástico estruturada no deck de lazer
7. Entrada de pedestres pela varanda frontal com luz antiga (postes coloniais) e decoração (vasos vietnamitas)
8. Entrada da garagem decorada para carros com pavers, balizadores em LED e vaga demarcada com carro
9. Jardins 100% conectados em manto contínuo
10. Varandas conectadas em complexo contínuo
"""

import os
import math

def generate_fence_svg():
    # 1. Meia lua da extremidade da garagem (127.8, 538.1) até a borda (28.5, 620.0)
    p0 = (127.8, 538.1)
    p1 = (45.0, 550.0)
    p2 = (28.5, 620.0)
    
    posts = []
    # Curva em meia lua
    for i in range(7):
        t = i / 6.0
        x = (1-t)**2 * p0[0] + 2*(1-t)*t * p1[0] + t**2 * p2[0]
        y = (1-t)**2 * p0[1] + 2*(1-t)*t * p1[1] + t**2 * p2[1]
        posts.append((round(x, 1), round(y, 1)))
        
    # Segue para os fundos na extremidade: (28.5, 620.0) até (28.5, 749.0)
    for y in [645.0, 670.0, 695.0, 720.0, 749.0]:
        posts.append((28.5, y))
        
    # Segue pelos fundos: (28.5, 749.0) até (519.4, 749.0)
    for x in range(65, 520, 35):
        posts.append((float(x), 749.0))
    posts.append((519.4, 749.0))
    
    # Segue pela lateral leste: (519.4, 749.0) até (519.4, 109.5)
    for y in range(715, 105, -35):
        posts.append((519.4, float(y)))
    posts.append((519.4, 109.5))
    
    # Segue pelo fundo superior: (519.4, 109.5) até (165.2, 109.5)
    for x in range(485, 160, -35):
        posts.append((float(x), 109.5))
    posts.append((165.2, 109.5))
    
    # Segue até o Quarto 1: (165.2, 109.5) até (165.2, 207.0)
    for y in [135.0, 160.0, 185.0, 207.0]:
        posts.append((165.2, y))
        
    # Gera SVG da linha e dos mourões
    path_d = f"M 127.8,538.1 Q 45.0,550.0 28.5,620.0 L 28.5,749.0 L 519.4,749.0 L 519.4,109.5 L 165.2,109.5 L 165.2,207.0"
    
    svg_posts = []
    for px, py in posts:
        svg_posts.append(f'<circle cx="{px}" cy="{py}" r="2.4" fill="#6c4a27" stroke="#3e2723" stroke-width="0.8"/>')
        svg_posts.append(f'<circle cx="{px}" cy="{py}" r="1.0" fill="#a47148"/>')
        
    return path_d, "\n          ".join(svg_posts)

fence_path, fence_posts_svg = generate_fence_svg()

html_template = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Planta Baixa 2D Técnica Oficial • Residência & Lazer Integrados</title>
  <style>
    :root {{
      --bg-dark: #0f172a;
      --panel-bg: rgba(15, 23, 42, 0.92);
      --panel-border: rgba(255, 255, 255, 0.12);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --accent: #38bdf8;
      --accent-hover: #0ea5e9;
      --color-sala-unida: #ffd8cc;
      --color-cozinha: #ffffff;
      --color-lazer-conectado: #ffb703;
      --color-varanda-lilas: #e2c4f0;
      --color-jardim: #c7f9cc;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
      user-select: none;
    }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background: #111827;
      color: var(--text-main);
      overflow: hidden;
      width: 100vw;
      height: 100vh;
      display: flex;
      flex-direction: column;
    }}

    /* Header Bar */
    header {{
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
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .brand-icon {{
      width: 36px;
      height: 36px;
      background: linear-gradient(135deg, #f97316, #ea580c);
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 2px 8px rgba(249, 115, 22, 0.4);
    }}

    .brand-icon svg {{
      width: 22px;
      height: 22px;
      stroke: #fff;
      fill: none;
      stroke-width: 2;
    }}

    .brand-text h1 {{
      font-size: 1.02rem;
      font-weight: 700;
      color: #fff;
      letter-spacing: -0.01em;
    }}

    .brand-text span {{
      font-size: 0.72rem;
      color: var(--text-muted);
      display: block;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .btn-action {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--panel-border);
      color: var(--text-main);
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
      text-decoration: none;
    }}

    .btn-action:hover {{
      background: rgba(255, 255, 255, 0.15);
      border-color: rgba(255, 255, 255, 0.25);
    }}

    .btn-action.primary {{
      background: #0284c7;
      border-color: #38bdf8;
      color: #fff;
    }}

    .btn-action.primary:hover {{
      background: #0369a1;
    }}

    /* Workspace Canvas */
    #workspace {{
      flex: 1;
      position: relative;
      overflow: hidden;
      cursor: grab;
      background: radial-gradient(circle at 50% 50%, #1e293b 0%, #0f172a 100%);
    }}

    #workspace:active {{
      cursor: grabbing;
    }}

    #blueprint-svg {{
      width: 100%;
      height: 100%;
      display: block;
      transform-origin: 0 0;
    }}

    /* Floating UI Controls */
    .floating-bar {{
      position: absolute;
      background: var(--panel-bg);
      backdrop-filter: blur(12px);
      border: 1px solid var(--panel-border);
      border-radius: 12px;
      padding: 8px 14px;
      z-index: 40;
      display: flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }}

    /* Layer Bar (Top Center) */
    #layer-bar {{
      top: 16px;
      left: 50%;
      transform: translateX(-50%);
      flex-wrap: wrap;
      max-width: 95vw;
      justify-content: center;
    }}

    .chip-toggle {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: var(--text-muted);
      padding: 5px 12px;
      border-radius: 20px;
      font-size: 0.76rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }}

    .chip-toggle.active {{
      background: rgba(56, 189, 248, 0.2);
      border-color: rgba(56, 189, 248, 0.6);
      color: #fff;
    }}

    .chip-toggle .dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      display: inline-block;
    }}

    /* Original Overlay Opacity Slider */
    #overlay-control {{
      bottom: 20px;
      left: 20px;
      font-size: 0.8rem;
    }}

    #overlay-control input[type="range"] {{
      width: 110px;
      accent-color: var(--accent);
      cursor: pointer;
    }}

    /* Zoom / Reset Controls (Bottom Right) */
    #nav-controls {{
      bottom: 20px;
      right: 20px;
      gap: 6px;
      padding: 6px;
    }}

    .btn-icon {{
      width: 38px;
      height: 38px;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--panel-border);
      border-radius: 8px;
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s ease;
    }}

    .btn-icon:hover {{
      background: rgba(255, 255, 255, 0.15);
      border-color: var(--accent);
    }}

    .btn-icon svg {{
      width: 18px;
      height: 18px;
      stroke: currentColor;
      fill: none;
      stroke-width: 2;
    }}

    /* Inspector Drawer */
    #inspector {{
      position: absolute;
      top: 16px;
      right: 16px;
      width: 340px;
      max-height: calc(100vh - 120px);
      background: var(--panel-bg);
      backdrop-filter: blur(16px);
      border: 1px solid var(--panel-border);
      border-radius: 14px;
      padding: 18px;
      z-index: 45;
      overflow-y: auto;
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.5);
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease;
      transform: translateX(380px);
      opacity: 0;
      pointer-events: none;
    }}

    #inspector.open {{
      transform: translateX(0);
      opacity: 1;
      pointer-events: auto;
    }}

    .inspector-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
      padding-bottom: 10px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }}

    .inspector-header h3 {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #fff;
    }}

    .inspector-close {{
      background: none;
      border: none;
      color: var(--text-muted);
      font-size: 1.2rem;
      cursor: pointer;
      line-height: 1;
    }}

    .inspector-badge {{
      display: inline-block;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      margin-bottom: 12px;
      background: rgba(56, 189, 248, 0.15);
      color: var(--accent);
      border: 1px solid rgba(56, 189, 248, 0.3);
    }}

    .stat-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 14px;
    }}

    .stat-card {{
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 8px;
      padding: 10px;
    }}

    .stat-card span {{
      display: block;
      font-size: 0.7rem;
      color: var(--text-muted);
      margin-bottom: 4px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .stat-card strong {{
      font-size: 0.95rem;
      color: #fff;
    }}

    .inspector-details {{
      font-size: 0.84rem;
      line-height: 1.5;
      color: #cbd5e1;
      background: rgba(0, 0, 0, 0.2);
      border-radius: 8px;
      padding: 12px;
      border-left: 3px solid var(--accent);
    }}

    /* SVG Interactive Highlights */
    .room-poly {{
      cursor: pointer;
      transition: filter 0.2s ease, opacity 0.2s ease;
    }}

    .room-poly:hover {{
      filter: brightness(1.15) drop-shadow(0 0 6px rgba(56, 189, 248, 0.6));
    }}

    .room-selected {{
      filter: brightness(1.25) drop-shadow(0 0 10px #38bdf8) !important;
      stroke: #38bdf8 !important;
      stroke-width: 3 !important;
    }}

    /* Pulse animation for open-concept dashed lines */
    @keyframes dashPulse {{
      0% {{ stroke-dashoffset: 0; opacity: 0.8; }}
      50% {{ stroke-dashoffset: 12; opacity: 1; }}
      100% {{ stroke-dashoffset: 24; opacity: 0.8; }}
    }}

    .pulse-line {{
      animation: dashPulse 1.8s linear infinite;
    }}

    /* Vintage Lantern Glow Animation */
    @keyframes lanternFlicker {{
      0% {{ opacity: 0.55; transform: scale(1); }}
      50% {{ opacity: 0.75; transform: scale(1.05); }}
      100% {{ opacity: 0.55; transform: scale(1); }}
    }}

    .glow-flicker {{
      animation: lanternFlicker 3s ease-in-out infinite;
      transform-origin: center;
    }}
  </style>
</head>
<body>

  <!-- Top Header Navigation -->
  <header>
    <div class="brand">
      <div class="brand-icon">
        <svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
      </div>
      <div class="brand-text">
        <h1>Planta Baixa 2D Técnica Oficial • Residência & Lazer Integrados</h1>
        <span>Cozinha Aberta (Sala & Varanda) • Piscina Redonda • Cercado Eucalipto • Rua Frontal</span>
      </div>
    </div>
    <div class="header-actions">
      <button class="btn-action" id="btn-open-3d" onclick="window.location.href='modelo3d.html'">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>
        Ver Modelo 3D
      </button>
      <button class="btn-action primary" id="btn-center-view">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
        Centralizar Planta
      </button>
    </div>
  </header>

  <!-- Workspace Canvas -->
  <div id="workspace">
    <svg id="blueprint-svg" viewBox="-75 0 615 780" preserveAspectRatio="xMidYMid meet">
      <defs>
        <!-- Blue Pool Gradient -->
        <radialGradient id="poolPlasticGrad" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#38bdf8" />
          <stop offset="65%" stop-color="#0284c7" />
          <stop offset="100%" stop-color="#0369a1" />
        </radialGradient>

        <!-- Vintage Lantern Glow Radial Gradient -->
        <radialGradient id="vintageGlow" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="#fef08a" stop-opacity="0.9" />
          <stop offset="40%" stop-color="#f59e0b" stop-opacity="0.5" />
          <stop offset="100%" stop-color="#d97706" stop-opacity="0" />
        </radialGradient>

        <!-- Driveway Paver Paving Pattern -->
        <pattern id="paverPattern" width="12" height="12" patternUnits="userSpaceOnUse">
          <rect width="12" height="12" fill="#334155" />
          <rect x="1" y="1" width="10" height="4.5" fill="#475569" rx="0.5"/>
          <rect x="1" y="6.5" width="10" height="4.5" fill="#3f4e65" rx="0.5"/>
          <line x1="6" y1="1" x2="6" y2="5.5" stroke="#1e293b" stroke-width="0.6"/>
          <line x1="6" y1="6.5" x2="6" y2="11" stroke="#1e293b" stroke-width="0.6"/>
        </pattern>

        <!-- Pedestrian Stone Steps Pattern -->
        <pattern id="stonePathPattern" width="16" height="16" patternUnits="userSpaceOnUse">
          <rect width="16" height="16" fill="transparent"/>
          <rect x="2" y="2" width="12" height="12" rx="3" fill="#cbd5e1" stroke="#94a3b8" stroke-width="0.8"/>
        </pattern>

        <!-- Pool Mosaic Water Pattern -->
        <pattern id="poolMosaic" width="6" height="6" patternUnits="userSpaceOnUse">
          <rect width="3" height="3" fill="rgba(255,255,255,0.18)"/>
          <rect x="3" y="3" width="3" height="3" fill="rgba(255,255,255,0.18)"/>
        </pattern>

        <!-- Asphalt Pattern -->
        <pattern id="asphaltPattern" width="20" height="20" patternUnits="userSpaceOnUse">
          <rect width="20" height="20" fill="#1e293b"/>
          <circle cx="5" cy="5" r="0.8" fill="#334155"/>
          <circle cx="15" cy="12" r="0.7" fill="#334155"/>
          <circle cx="8" cy="17" r="0.9" fill="#0f172a"/>
        </pattern>
      </defs>

      <g id="viewport-group">

        <!-- 0. OVERLAY DA PLANTA ORIGINAL (OPACIDADE CONTROLÁVEL) -->
        <g id="layer-original-overlay" opacity="0.0">
          <image href="planta_baixa.png" x="0" y="0" width="540" height="780" preserveAspectRatio="none"/>
        </g>

        <!-- ================================================================= -->
        <!-- 🌟 RUA NA FRENTE DA CASA & PASSEIO PÚBLICO (LADO OESTE)           -->
        <!-- ================================================================= -->
        <g id="layer-rua">
          <!-- Pista de Rolamento Asfáltica da Rua Principal (X: -75 a 10) -->
          <rect id="poly-rua-principal" class="room-poly" x="-75.0" y="100.0" width="70.0" height="655.0" fill="url(#asphaltPattern)" stroke="#0f172a" stroke-width="2"/>
          
          <!-- Faixa Central Tracejada Amarela de Divisão de Pistas -->
          <line x1="-40.0" y1="100.0" x2="-40.0" y2="755.0" stroke="#facc15" stroke-width="2.5" stroke-dasharray="14,10"/>
          
          <!-- Linhas Brancas Laterais de Bordo da Pista -->
          <line x1="-72.0" y1="100.0" x2="-72.0" y2="755.0" stroke="#f8fafc" stroke-width="1.5"/>
          <line x1="-8.0" y1="100.0" x2="-8.0" y2="755.0" stroke="#f8fafc" stroke-width="1.5"/>

          <!-- Calçada / Passeio Público com Meio-Fio de Concreto (X: -6 a 28.5) -->
          <rect id="poly-calcada" class="room-poly" x="-6.0" y="100.0" width="34.5" height="655.0" fill="#94a3b8" stroke="#475569" stroke-width="1.5"/>
          
          <!-- Guias de Meio-Fio Rebaixado para Veículos em frente à Garagem -->
          <rect x="-8.0" y="525.0" width="4.0" height="85.0" fill="#cbd5e1" stroke="#334155" stroke-width="1"/>
          
          <!-- Rebaixo de Calçada com Faixa Tátil de Pedestres em frente à Varanda Frontal -->
          <rect x="-8.0" y="415.0" width="4.0" height="30.0" fill="#facc15" stroke="#ca8a04" stroke-width="0.8"/>

          <!-- Textos Orientadores da Via Pública -->
          <text x="-40.0" y="240.0" font-size="10" font-weight="900" fill="#f8fafc" text-anchor="middle" transform="rotate(-90 -40 240)" letter-spacing="2">RUA PRINCIPAL • ACESSO FRONTAL</text>
          <text x="12.0" y="240.0" font-size="7.5" font-weight="800" fill="#1e293b" text-anchor="middle" transform="rotate(-90 12 240)">PASSEIO PÚBLICO (CALÇADA)</text>
          <text x="-40.0" y="660.0" font-size="9" font-weight="800" fill="#94a3b8" text-anchor="middle" transform="rotate(-90 -40 660)">SENTIDO DA VIA ↑</text>
        </g>

        <!-- ================================================================= -->
        <!-- 1. JARDINS 100% CONECTADOS (GRAMADO PERIMETRAL CONTÍNUO)          -->
        <!-- ================================================================= -->
        <g id="layer-jardins">
          <!-- Manto Unificado de Jardim Conectado em todo o Perímetro do Lote -->
          <polygon id="poly-jardim-conectado" class="room-poly"
            points="28.5,109.5 519.4,109.5 519.4,749.0 28.5,749.0"
            fill="#c7f9cc" stroke="#2d6a4f" stroke-width="2"/>

          <!-- Linhas Suaves de Continuidade do Jardim Conectado -->
          <path d="M 28.5,207.0 C 90,207.0 120,207.0 165.2,207.0" stroke="#74c69d" stroke-width="1.2" stroke-dasharray="4,4"/>
          <path d="M 28.5,469.0 C 60,469.0 90,469.0 127.8,469.0" stroke="#74c69d" stroke-width="1.2" stroke-dasharray="4,4"/>
          <path d="M 127.8,538.1 C 280,538.1 360,538.1 519.4,538.1" stroke="#74c69d" stroke-width="1.2" stroke-dasharray="4,4"/>

          <!-- Casa do Cachorro (Canto superior direito: X:434.7, Y:114.0, 82.4x86.5) -->
          <g id="poly-casa-cachorro" class="room-poly" transform="translate(434.7, 114.0)">
            <rect width="82.4" height="86.5" rx="4" fill="#d4a373" stroke="#7f4f24" stroke-width="2"/>
            <polygon points="0,0 41.2,-10 82.4,0" fill="#a0522d" stroke="#5c2e14" stroke-width="1.5"/>
            <path d="M 26,86.5 L 26,45 Q 41.2,30 56.4,45 L 56.4,86.5 Z" fill="#43281c"/>
            <text x="41.2" y="32.0" font-size="11" font-weight="800" fill="#3e2723" text-anchor="middle">Casa do</text>
            <text x="41.2" y="44.0" font-size="11" font-weight="800" fill="#3e2723" text-anchor="middle">cachorro</text>
          </g>

          <!-- Casa da Árvore (Canto inferior esquerdo: X:37.7, Y:634.3, 82.5x86.5) -->
          <g id="poly-casa-arvore" class="room-poly" transform="translate(37.7, 634.3)">
            <rect x="25" y="60" width="32" height="26" fill="#8d5b4c" stroke="#5c2e14" stroke-width="1.5"/>
            <rect width="82.5" height="60" rx="3" fill="#cca43b" stroke="#7f4f24" stroke-width="2"/>
            <rect x="12" y="15" width="18" height="18" rx="2" fill="#e0f2fe" stroke="#0284c7" stroke-width="1"/>
            <rect x="52" y="15" width="18" height="28" rx="1" fill="#43281c"/>
            <line x1="58" y1="43" x2="58" y2="86.5" stroke="#7f4f24" stroke-width="2"/>
            <line x1="66" y1="43" x2="66" y2="86.5" stroke="#7f4f24" stroke-width="2"/>
            <line x1="56" y1="52" x2="68" y2="52" stroke="#7f4f24" stroke-width="1.5"/>
            <line x1="56" y1="62" x2="68" y2="62" stroke="#7f4f24" stroke-width="1.5"/>
            <line x1="56" y1="72" x2="68" y2="72" stroke="#7f4f24" stroke-width="1.5"/>
            <text x="41.2" y="-4.0" font-size="12" font-weight="800" fill="#2d6a4f" text-anchor="middle">Casa da árvore</text>
          </g>

          <!-- Pergolado (Canto inferior direito: X:382.3, Y:583.1, 114.6x111.1) -->
          <g id="poly-pergolado" class="room-poly" transform="translate(382.3, 583.1)">
            <rect width="114.6" height="111.1" fill="#cca43b" stroke="#7f4f24" stroke-width="2" rx="4"/>
            <line x1="0" y1="20" x2="114.6" y2="20" stroke="#7f4f24" stroke-width="2.5"/>
            <line x1="0" y1="40" x2="114.6" y2="40" stroke="#7f4f24" stroke-width="2.5"/>
            <line x1="0" y1="60" x2="114.6" y2="60" stroke="#7f4f24" stroke-width="2.5"/>
            <line x1="0" y1="80" x2="114.6" y2="80" stroke="#7f4f24" stroke-width="2.5"/>
            <line x1="0" y1="100" x2="114.6" y2="100" stroke="#7f4f24" stroke-width="2.5"/>
            <rect x="3" y="3" width="10" height="10" fill="#43281c"/>
            <rect x="101.6" y="3" width="10" height="10" fill="#43281c"/>
            <rect x="3" y="98.1" width="10" height="10" fill="#43281c"/>
            <rect x="101.6" y="98.1" width="10" height="10" fill="#43281c"/>
            <text x="57.3" y="58.0" font-size="13" font-weight="800" fill="#3e2723" text-anchor="middle">Pergolado</text>
          </g>
        </g>

        <!-- ================================================================= -->
        <!-- 🌟 2. CERCADO DE MADEIRA EUCALIPTO (MOURÃO) EM MEIA-LUA           -->
        <!-- Começa na garagem, meia-lua até a borda, segue fundos até Quarto 1-->
        <!-- ================================================================= -->
        <g id="layer-cercado-eucalipto">
          <!-- Trilho / Travessas Horizontais do Cercado de Eucalipto -->
          <path id="poly-cercado-eucalipto" class="room-poly"
            d="{fence_path}"
            fill="none" stroke="#78350f" stroke-width="3.2" stroke-linecap="round"/>
          <path d="{fence_path}" fill="none" stroke="#b45309" stroke-width="1.5" stroke-linecap="round"/>

          <!-- Mourões Cilíndricos Verticais de Eucalipto Tratado Cravados no Solo -->
          {fence_posts_svg}

          <!-- Identificação do Cercado -->
          <g transform="translate(68.0, 565.0)">
            <rect x="-45" y="-9" width="90" height="18" rx="4" fill="rgba(62, 39, 35, 0.9)" stroke="#d4a373" stroke-width="1"/>
            <text x="0" y="3" font-size="6.5" font-weight="800" fill="#fff" text-anchor="middle">Mourões de Eucalipto</text>
          </g>
        </g>

        <!-- ================================================================= -->
        <!-- 3. ENTRADA DA GARAGEM DECORADA PARA CARROS (DRIVEWAY & VAGAS)     -->
        <!-- ================================================================= -->
        <g id="layer-acesso-carros">
          <!-- Rampa / Pista de Acesso de Carros (Driveway pavimentada com Intertravado) -->
          <rect id="poly-driveway-garagem" class="room-poly" x="127.8" y="538.1" width="131.5" height="95.0" fill="url(#paverPattern)" stroke="#1e293b" stroke-width="1.5"/>
          
          <!-- Faixas Guia de Rolamento dos Pneus em Concreto Aparente -->
          <rect x="142.0" y="538.1" width="24.0" height="95.0" fill="#94a3b8" opacity="0.6"/>
          <rect x="180.0" y="538.1" width="24.0" height="95.0" fill="#94a3b8" opacity="0.6"/>
          <rect x="220.0" y="538.1" width="24.0" height="95.0" fill="#94a3b8" opacity="0.6"/>

          <!-- Balizadores de Piso em LED (Iluminação Noturna de Acesso de Veículos) -->
          <circle cx="134.0" cy="555.0" r="2.5" fill="#fef08a" stroke="#d97706" stroke-width="0.8"/>
          <circle cx="134.0" cy="585.0" r="2.5" fill="#fef08a" stroke="#d97706" stroke-width="0.8"/>
          <circle cx="134.0" cy="615.0" r="2.5" fill="#fef08a" stroke="#d97706" stroke-width="0.8"/>
          <circle cx="253.0" cy="555.0" r="2.5" fill="#fef08a" stroke="#d97706" stroke-width="0.8"/>
          <circle cx="253.0" cy="585.0" r="2.5" fill="#fef08a" stroke="#d97706" stroke-width="0.8"/>
          <circle cx="253.0" cy="615.0" r="2.5" fill="#fef08a" stroke="#d97706" stroke-width="0.8"/>

          <!-- Texto do Acesso Automotivo -->
          <text x="193.5" y="605.0" font-size="8" font-weight="800" fill="#f8fafc" text-anchor="middle" filter="drop-shadow(0 1px 2px #000)">ENTRADA DE VEÍCULOS (PAVERS)</text>

          <!-- Demarcação da Garagem Interna (5,71 x 3,00 m: X:127.8, Y:469.0, W:131.5, H:69.1) -->
          <rect id="poly-garagem" class="room-poly" x="127.8" y="469.0" width="131.5" height="69.1" fill="#334155" stroke="#000" stroke-width="1.8"/>

          <!-- Linhas de Demarcação Técnica das Vagas de Carros -->
          <line x1="193.5" y1="472.0" x2="193.5" y2="535.0" stroke="#facc15" stroke-width="1.8" stroke-dasharray="5,3"/>
          <rect x="133.0" y="473.0" width="55.0" height="60.0" fill="none" stroke="rgba(255,255,255,0.4)" stroke-width="1" rx="2"/>
          <rect x="199.0" y="473.0" width="55.0" height="60.0" fill="none" stroke="rgba(255,255,255,0.4)" stroke-width="1" rx="2"/>

          <!-- Desenho de Carro Elegante na Vaga 1 -->
          <g id="furn-carro-estilizado" class="room-poly" transform="translate(138.0, 477.0)">
            <rect x="4" y="2" width="38" height="52" rx="7" fill="#0284c7" stroke="#0f172a" stroke-width="1.2"/>
            <path d="M 7,12 L 39,12" stroke="#38bdf8" stroke-width="1"/>
            <polygon points="6,2 14,2 11,-6 3,-6" fill="rgba(254, 240, 138, 0.4)"/>
            <polygon points="32,2 40,2 43,-6 35,-6" fill="rgba(254, 240, 138, 0.4)"/>
            <rect x="6" y="2" width="8" height="3" rx="1" fill="#fef08a"/>
            <rect x="32" y="2" width="8" height="3" rx="1" fill="#fef08a"/>
            <path d="M 8,14 Q 23,10 38,14 L 36,22 Q 23,20 10,22 Z" fill="#1e293b" stroke="#0f172a" stroke-width="0.8"/>
            <rect x="11" y="23" width="24" height="15" rx="2" fill="#0f172a" stroke="#38bdf8" stroke-width="0.6"/>
            <path d="M 10,39 Q 23,41 36,39 L 38,45 Q 23,47 8,45 Z" fill="#1e293b" stroke="#0f172a" stroke-width="0.8"/>
            <rect x="6" y="51" width="8" height="2.5" rx="1" fill="#ef4444"/>
            <rect x="32" y="51" width="8" height="2.5" rx="1" fill="#ef4444"/>
            <rect x="1" y="16" width="3" height="5" rx="1" fill="#0369a1"/>
            <rect x="42" y="16" width="3" height="5" rx="1" fill="#0369a1"/>
            <rect x="1" y="8" width="3" height="9" rx="1" fill="#0f172a"/>
            <rect x="42" y="8" width="3" height="9" rx="1" fill="#0f172a"/>
            <rect x="1" y="38" width="3" height="9" rx="1" fill="#0f172a"/>
            <rect x="42" y="38" width="3" height="9" rx="1" fill="#0f172a"/>
            <text x="23" y="33" font-size="6" font-weight="700" fill="#fff" text-anchor="middle">VAGA 1</text>
          </g>

          <text x="226.0" y="510.0" font-size="7.5" font-weight="700" fill="#94a3b8" text-anchor="middle">VAGA 2</text>
          <text x="226.0" y="520.0" font-size="6" font-weight="600" fill="#64748b" text-anchor="middle">(Livre)</text>
          <text x="193.5" y="464.0" font-size="11" font-weight="800" fill="#1e293b" text-anchor="middle">garagem (5,71 x 3,00 m)</text>
        </g>

        <!-- ================================================================= -->
        <!-- 4. ENTRADA DE PEDESTRES PELA VARANDA FRONTAL COM LUZ ANTIGA       -->
        <!-- ================================================================= -->
        <g id="layer-acesso-pedestres">
          <!-- Passarela de Pedestres em Pedras Naturais (São Tomé / Lajotas) -->
          <g id="poly-caminho-pedestres" class="room-poly">
            <rect x="10.0" y="415.0" width="86.0" height="28.0" fill="url(#stonePathPattern)"/>
            <line x1="10.0" y1="415.0" x2="96.0" y2="415.0" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3,3"/>
            <line x1="10.0" y1="443.0" x2="96.0" y2="443.0" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3,3"/>
          </g>

          <!-- Poste Colonial Norte (Luz Antiga 1) -->
          <g id="furn-luz-antiga-norte" class="room-poly" transform="translate(60.0, 403.0)">
            <circle cx="0" cy="0" r="28" fill="url(#vintageGlow)" class="glow-flicker"/>
            <circle cx="0" cy="0" r="4.5" fill="#1e293b" stroke="#000" stroke-width="1"/>
            <path d="M -3,-3 L 3,-3 L 4,3 L -4,3 Z" fill="#0f172a"/>
            <polygon points="-5,-4 5,-4 4,-12 -4,-12" fill="#334155" stroke="#000" stroke-width="0.8"/>
            <polygon points="0,-16 5,-12 -5,-12" fill="#1e293b" stroke="#000" stroke-width="0.8"/>
            <circle cx="0" cy="-8" r="2.2" fill="#fef08a" stroke="#f59e0b" stroke-width="0.6"/>
            <text x="0" y="-18" font-size="6.5" font-weight="800" fill="#b45309" text-anchor="middle">Luz Antiga</text>
          </g>

          <!-- Poste Colonial Sul (Luz Antiga 2) -->
          <g id="furn-luz-antiga-sul" class="room-poly" transform="translate(60.0, 455.0)">
            <circle cx="0" cy="0" r="28" fill="url(#vintageGlow)" class="glow-flicker"/>
            <circle cx="0" cy="0" r="4.5" fill="#1e293b" stroke="#000" stroke-width="1"/>
            <path d="M -3,-3 L 3,-3 L 4,3 L -4,3 Z" fill="#0f172a"/>
            <polygon points="-5,-4 5,-4 4,-12 -4,-12" fill="#334155" stroke="#000" stroke-width="0.8"/>
            <polygon points="0,-16 5,-12 -5,-12" fill="#1e293b" stroke="#000" stroke-width="0.8"/>
            <circle cx="0" cy="-8" r="2.2" fill="#fef08a" stroke="#f59e0b" stroke-width="0.6"/>
            <text x="0" y="14" font-size="6.5" font-weight="800" fill="#b45309" text-anchor="middle">Luz Antiga</text>
          </g>

          <!-- Decoração Lateral: Vasos Vietnamitas Azuis -->
          <g id="furn-vaso-norte" class="room-poly" transform="translate(85.0, 404.0)">
            <ellipse cx="0" cy="0" rx="5" ry="4" fill="#0284c7" stroke="#0369a1" stroke-width="1"/>
            <circle cx="0" cy="-1" r="6" fill="#15803d" opacity="0.85"/>
            <circle cx="-2" cy="-4" r="3.5" fill="#22c55e" opacity="0.9"/>
            <circle cx="3" cy="-4" r="3.5" fill="#16a34a" opacity="0.9"/>
            <text x="-8" y="-7" font-size="5.5" font-weight="700" fill="#047857">Decoração</text>
          </g>

          <g id="furn-vaso-sul" class="room-poly" transform="translate(85.0, 454.0)">
            <ellipse cx="0" cy="0" rx="5" ry="4" fill="#0284c7" stroke="#0369a1" stroke-width="1"/>
            <circle cx="0" cy="-1" r="6" fill="#15803d" opacity="0.85"/>
            <circle cx="-2" cy="-4" r="3.5" fill="#22c55e" opacity="0.9"/>
            <circle cx="3" cy="-4" r="3.5" fill="#16a34a" opacity="0.9"/>
            <text x="-8" y="14" font-size="5.5" font-weight="700" fill="#047857">Decoração</text>
          </g>

          <rect x="94.0" y="414.0" width="4.0" height="30.0" fill="#f8fafc" stroke="#475569" stroke-width="1"/>
          
          <g transform="translate(48.0, 429.0)">
            <rect x="-30" y="-8" width="60" height="16" rx="4" fill="rgba(15, 23, 42, 0.85)" stroke="#38bdf8" stroke-width="1"/>
            <text x="0" y="3" font-size="6.5" font-weight="800" fill="#fff" text-anchor="middle">🚶 ENTRADA PEDESTRES</text>
          </g>
        </g>

        <!-- ================================================================= -->
        <!-- 5. PISOS DOS CÔMODOS & ESPAÇO SOCIAL TOTALMENTE INTEGRADO         -->
        <!-- ================================================================= -->
        <g id="layer-pisos">
          <!-- Quarto 1 (Superior Esquerdo: 3,01 x 4,00 m) -->
          <rect id="poly-quarto1" class="room-poly" x="165.2" y="207.0" width="69.3" height="92.1" fill="#fed7aa" stroke="#000" stroke-width="1.8"/>

          <!-- Quarto 2 (Superior Centro: 3,51 x 3,01 m) -->
          <rect id="poly-quarto2" class="room-poly" x="236.7" y="208.1" width="80.9" height="69.4" fill="#fed7aa" stroke="#000" stroke-width="1.8"/>

          <!-- Banheiro Superior (Abaixo do Quarto 2: 2,43 x 1,87 m) -->
          <rect id="poly-banheiro-sup" class="room-poly" x="260.8" y="279.6" width="55.9" height="43.0" fill="#bde0fe" stroke="#000" stroke-width="1.8"/>

          <!-- ================================================================= -->
          <!-- 🌟 A COZINHA, A SALA E O CORREDOR SÃO CONECTADOS!                  -->
          <!-- E A COZINHA TAMBÉM É CONECTADA À VARANDA DE LAZER!                 -->
          <!-- ================================================================= -->
          <polygon id="poly-espaco-social-integrado" class="room-poly"
            points="165.8,301.6 234.5,301.6 234.5,279.6 260.8,279.6 260.8,325.3 357.1,325.3 357.1,419.2 272.4,419.2 272.4,466.1 165.8,466.1"
            fill="#fff7ed" stroke="#ea580c" stroke-width="2.5"/>

          <!-- Varanda Lilás Frontal (Lateral Esquerda: 96.0 a 165.8, Y:390.7 a 467.2) -->
          <polygon id="poly-varanda-lilas-conectada" class="room-poly"
            points="96.0,390.7 165.8,390.7 165.8,467.2 96.0,467.2"
            fill="#e2c4f0" stroke="#000" stroke-width="1.8"/>

          <!-- Quarto 3 (Abaixo da Cozinha: 2,17 x 1,90 m) -->
          <rect id="poly-quarto3" class="room-poly" x="272.4" y="421.9" width="50.0" height="43.8" fill="#fed7aa" stroke="#000" stroke-width="1.8"/>

          <!-- Banheiro Inferior (Ao lado do Quarto 3: 1,79 x 1,52 m) -->
          <rect id="poly-banheiro-inf" class="room-poly" x="324.3" y="423.7" width="35.0" height="41.2" fill="#bde0fe" stroke="#000" stroke-width="1.8"/>

          <!-- Quarto 5 (Inferior Centro: 5,41 x 3,00 m) -->
          <rect id="poly-quarto5" class="room-poly" x="261.7" y="468.4" width="124.6" height="69.1" fill="#fed7aa" stroke="#000" stroke-width="1.8"/>

          <!-- Lavanderia (Inferior Direito: 2,24 x 2,95 m) -->
          <rect id="poly-lavanderia" class="room-poly" x="388.7" y="468.2" width="51.6" height="68.0" fill="#ffb703" stroke="#000" stroke-width="1.8"/>

          <!-- ================================================================= -->
          <!-- 🌟 VARANDAS CONECTADAS: COMPLEXO DE LAZER & GOURMET INTEGRADO     -->
          <!-- ================================================================= -->
          <polygon id="poly-varanda-lazer-conectada" class="room-poly"
            points="319.3,207.3 478.5,207.3 478.5,536.2 440.3,536.2 440.3,468.2 359.3,468.2 359.3,423.7 357.1,419.2 357.1,325.3 319.3,322.6"
            fill="#ffb703" stroke="#000" stroke-width="1.8"/>

          <!-- ================================================================= -->
          <!-- 🌟 PISCINA REDONDA DE PLÁSTICO (ESTRUTURADA NO DECK)              -->
          <!-- ================================================================= -->
          <g id="poly-piscina-redonda" class="room-poly" transform="translate(401.2, 265.0)">
            <circle cx="0" cy="0" r="32.5" fill="none" stroke="#64748b" stroke-width="2.5" stroke-dasharray="3,13.5"/>
            <circle cx="32" cy="0" r="1.8" fill="#334155"/>
            <circle cx="-32" cy="0" r="1.8" fill="#334155"/>
            <circle cx="0" cy="32" r="1.8" fill="#334155"/>
            <circle cx="0" cy="-32" r="1.8" fill="#334155"/>
            <circle cx="22.6" cy="22.6" r="1.8" fill="#334155"/>
            <circle cx="-22.6" cy="22.6" r="1.8" fill="#334155"/>
            <circle cx="22.6" cy="-22.6" r="1.8" fill="#334155"/>
            <circle cx="-22.6" cy="-22.6" r="1.8" fill="#334155"/>

            <circle cx="0" cy="0" r="30" fill="#0284c7" stroke="#0369a1" stroke-width="1.5"/>
            <circle cx="0" cy="0" r="28" fill="url(#poolPlasticGrad)"/>
            <circle cx="0" cy="0" r="26" fill="url(#poolMosaic)" opacity="0.4"/>
            <circle cx="0" cy="0" r="28.5" fill="none" stroke="#f8fafc" stroke-width="3" opacity="0.95"/>
            <circle cx="0" cy="0" r="29.8" fill="none" stroke="#cbd5e1" stroke-width="0.8"/>

            <g transform="translate(0, 26)">
              <rect x="-5" y="0" width="10" height="6" fill="#e2e8f0" stroke="#475569" stroke-width="0.8" rx="1"/>
              <line x1="-3" y1="2" x2="3" y2="2" stroke="#475569" stroke-width="0.8"/>
              <line x1="-3" y1="4" x2="3" y2="4" stroke="#475569" stroke-width="0.8"/>
            </g>

            <g transform="translate(10, -10)">
              <circle cx="0" cy="0" r="6" fill="#f43f5e" stroke="#fff" stroke-width="1"/>
              <circle cx="0" cy="0" r="2.8" fill="#0284c7"/>
            </g>

            <text x="0" y="2" font-size="7.5" font-weight="900" fill="#fff" text-anchor="middle" filter="drop-shadow(0 1px 2px #000)">PISCINA REDONDA</text>
            <text x="0" y="10" font-size="6" font-weight="700" fill="#e0f2fe" text-anchor="middle" filter="drop-shadow(0 1px 2px #000)">DE PLÁSTICO</text>
          </g>

          <!-- Horta com Cerca (Faixa Lateral Direita: 484.6 a 518.7, Y:206.2 a 536.2) -->
          <rect id="poly-horta" class="room-poly" x="484.6" y="206.2" width="34.1" height="330.0" fill="#cca43b" stroke="#7f4f24" stroke-width="2"/>
        </g>

        <!-- ================================================================= -->
        <!-- 6. PAREDES ESTRUTURAIS REAIS                                      -->
        <!-- ================================================================= -->
        <g id="layer-paredes">
          <!-- Parede Norte Quarto 1 e Quarto 2 -->
          <line x1="165.2" y1="207.0" x2="317.6" y2="207.0" stroke="#000" stroke-width="2.5"/>
          <line x1="234.5" y1="207.0" x2="234.5" y2="299.1" stroke="#000" stroke-width="2.5"/>
          <line x1="165.2" y1="299.1" x2="234.5" y2="299.1" stroke="#000" stroke-width="2.5"/>
          <line x1="236.7" y1="277.5" x2="317.6" y2="277.5" stroke="#000" stroke-width="2.5"/>
          <line x1="260.8" y1="277.5" x2="260.8" y2="322.6" stroke="#000" stroke-width="2.5"/>
          <line x1="316.7" y1="277.5" x2="316.7" y2="322.6" stroke="#000" stroke-width="2.5"/>

          <!-- Parede Norte Cozinha (Apoio de Pia P, Armário AE e Fogão F) -->
          <line x1="260.9" y1="325.3" x2="357.1" y2="325.3" stroke="#000" stroke-width="2.5"/>

          <!-- Parede Sul Cozinha (Divisão com Q3 e Banheiro Inf) -->
          <line x1="272.4" y1="419.2" x2="357.1" y2="419.2" stroke="#000" stroke-width="2.5"/>

          <!-- Paredes Q3 e Banheiro Inf -->
          <line x1="272.4" y1="419.2" x2="272.4" y2="465.7" stroke="#000" stroke-width="2.5"/>
          <line x1="322.4" y1="419.2" x2="322.4" y2="465.7" stroke="#000" stroke-width="2.5"/>
          <line x1="359.3" y1="419.2" x2="359.3" y2="464.9" stroke="#000" stroke-width="2.5"/>
          <line x1="272.4" y1="465.7" x2="359.3" y2="465.7" stroke="#000" stroke-width="2.5"/>

          <!-- Parede Sul Sala (Divisão com Garagem) -->
          <line x1="165.8" y1="466.1" x2="272.4" y2="466.1" stroke="#000" stroke-width="2.5"/>

          <!-- Parede Sul Garagem e Q5 -->
          <line x1="127.8" y1="538.1" x2="440.3" y2="538.1" stroke="#000" stroke-width="2.5"/>
          <line x1="261.7" y1="468.4" x2="261.7" y2="538.1" stroke="#000" stroke-width="2.5"/>
          <line x1="386.3" y1="468.4" x2="386.3" y2="538.1" stroke="#000" stroke-width="2.5"/>
        </g>

        <!-- ================================================================= -->
        <!-- 7. LINHAS VERMELHAS TRACEJADAS DE CONCEITO ABERTO                 -->
        <!-- Cozinha aberta para a Sala/Corredor (Oeste) e para a Varanda (Leste)-->
        <!-- ================================================================= -->
        <g id="layer-linhas-vermelhas">
          <!-- Abertura Oeste: Cozinha Americana aberta para Sala e Corredor -->
          <line x1="260.9" y1="325.3" x2="260.9" y2="419.2" stroke="#dc2626" stroke-width="3" stroke-dasharray="6,4" class="pulse-line"/>
          
          <!-- Abertura Leste: Cozinha Americana aberta para Varanda de Lazer -->
          <line x1="357.1" y1="325.3" x2="357.1" y2="419.2" stroke="#dc2626" stroke-width="3" stroke-dasharray="6,4" class="pulse-line"/>

          <!-- Livre Passagem do Corredor para a Sala -->
          <line x1="234.5" y1="301.6" x2="234.5" y2="393.6" stroke="#ea580c" stroke-width="1.8" stroke-dasharray="4,4" opacity="0.6"/>

          <!-- Abertura da Varanda Frontal para a Sala -->
          <line x1="165.8" y1="390.7" x2="165.8" y2="466.1" stroke="#9333ea" stroke-width="2" stroke-dasharray="4,3"/>

          <!-- Textos explicativos -->
          <text x="252.0" y="340.0" font-size="6.5" font-weight="900" fill="#dc2626" transform="rotate(-90 252 340)">INTEGRAÇÃO COZINHA + CORREDOR + SALA</text>
          <text x="365.0" y="375.0" font-size="6.5" font-weight="900" fill="#dc2626" transform="rotate(90 365 375)">INTEGRAÇÃO ABERTA COM A VARANDA</text>
        </g>

        <!-- ================================================================= -->
        <!-- 8. MOBILIÁRIO OFICIAL DA COZINHA, SALA & ÁREA EXTERNA            -->
        <!-- NO CENTRO DA COZINHA SÓ HÁ A BANCADA RETANGULAR 'CENTRO'          -->
        <!-- ================================================================= -->
        <g id="layer-mobiliario">
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

          <!-- ============================================================= -->
          <!-- 🌟 ILHA / BALCÃO NA DIVISA COM A SALA/CORREDOR (1,68 x 1,26 m)-->
          <!-- ============================================================= -->
          <g id="furn-Ilha" class="room-poly">
            <rect x="236.7" y="364.7" width="37.3" height="27.5" fill="#0f172a" stroke="#38bdf8" stroke-width="1.8" rx="2"/>
            <text x="255.3" y="377.0" font-size="7.5" font-weight="900" fill="#fff" text-anchor="middle">Ilha / Balcão</text>
            <text x="255.3" y="385.0" font-size="6" font-weight="800" fill="#38bdf8" text-anchor="middle">Americano</text>
            
            <!-- 3 Banquetas Altas Voltadas para a Sala/Corredor -->
            <g transform="translate(231.0, 369.0)">
              <circle cx="0" cy="0" r="3.4" fill="#d97706" stroke="#000" stroke-width="0.8"/>
              <line x1="-2" y1="0" x2="2" y2="0" stroke="#fff" stroke-width="0.6"/>
            </g>
            <g transform="translate(231.0, 378.0)">
              <circle cx="0" cy="0" r="3.4" fill="#d97706" stroke="#000" stroke-width="0.8"/>
              <line x1="-2" y1="0" x2="2" y2="0" stroke="#fff" stroke-width="0.6"/>
            </g>
            <g transform="translate(231.0, 387.0)">
              <circle cx="0" cy="0" r="3.4" fill="#d97706" stroke="#000" stroke-width="0.8"/>
              <line x1="-2" y1="0" x2="2" y2="0" stroke="#fff" stroke-width="0.6"/>
            </g>
          </g>

          <!-- ============================================================= -->
          <!-- 🌟 BANCADA RETANGULAR NO CENTRO DA COZINHA ('CENTRO': 2,14x0,54)-->
          <!-- ÚNICA BANCADA NO CENTRO DA COZINHA                            -->
          <!-- ============================================================= -->
          <g id="furn-Centro" class="room-poly">
            <rect x="287.9" y="367.1" width="49.2" height="12.5" fill="#f8fafc" stroke="#000" stroke-width="1.5" rx="1"/>
            <text x="312.5" y="376.0" font-size="8.5" font-weight="900" fill="#000" text-anchor="middle">centro</text>
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

          <!-- G: Geladeira Duplex Inox (0,72 x 0,76 m) -->
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

          <!-- Sala Integrada: Jantar e Living -->
          <g id="furn-jantar" transform="translate(180.0, 315.0)">
            <rect width="32.0" height="46.0" rx="3" fill="#8c6747" stroke="#4a3525" stroke-width="1.2"/>
            <rect x="-6" y="5" width="5" height="10" rx="1" fill="#cbd5e1" stroke="#475569"/>
            <rect x="-6" y="18" width="5" height="10" rx="1" fill="#cbd5e1" stroke="#475569"/>
            <rect x="-6" y="31" width="5" height="10" rx="1" fill="#cbd5e1" stroke="#475569"/>
            <rect x="33" y="5" width="5" height="10" rx="1" fill="#cbd5e1" stroke="#475569"/>
            <rect x="33" y="18" width="5" height="10" rx="1" fill="#cbd5e1" stroke="#475569"/>
            <rect x="33" y="31" width="5" height="10" rx="1" fill="#cbd5e1" stroke="#475569"/>
            <text x="16.0" y="26.0" font-size="6.5" font-weight="700" fill="#fff" text-anchor="middle">Jantar</text>
          </g>

          <g id="furn-living" transform="translate(182.0, 415.0)">
            <rect x="0" y="0" width="52.0" height="18.0" rx="3" fill="#475569" stroke="#1e293b" stroke-width="1"/>
            <rect x="0" y="18" width="18.0" height="24.0" rx="3" fill="#475569" stroke="#1e293b" stroke-width="1"/>
            <rect x="26.0" y="22.0" width="20.0" height="14.0" rx="2" fill="#a16207"/>
            <text x="26.0" y="12.0" font-size="6.5" font-weight="700" fill="#fff" text-anchor="middle">Estar / TV</text>
          </g>

          <!-- Varandas Conectadas: Lazer Gourmet -->
          <g transform="translate(366.0, 428.0)">
            <rect width="26.0" height="32.0" rx="2" fill="#a34731" stroke="#000" stroke-width="1.2"/>
            <rect x="4" y="5" width="18" height="22" fill="#1e293b"/>
            <text x="13.0" y="18.0" font-size="6.5" font-weight="800" fill="#fff" text-anchor="middle">Churrasq.</text>
          </g>

          <g transform="translate(400.0, 395.0)">
            <rect width="34.0" height="22.0" rx="2" fill="#8c6747" stroke="#000" stroke-width="1"/>
            <text x="17.0" y="14.0" font-size="6.5" font-weight="700" fill="#fff" text-anchor="middle">Mesa Gourmet</text>
          </g>
        </g>

        <!-- ================================================================= -->
        <!-- 9. NOMES E IDENTIFICAÇÃO DOS AMBIENTES INTEGRADOS                 -->
        <!-- ================================================================= -->
        <g id="layer-textos">
          <text x="200.0" y="255.0" font-size="12" font-weight="700" fill="#000" text-anchor="middle">quarto1</text>
          <text x="277.0" y="222.0" font-size="12" font-weight="700" fill="#000" text-anchor="middle">quarto2</text>
          <text x="288.0" y="302.0" font-size="10" font-weight="700" fill="#000" text-anchor="middle">banheiro</text>

          <!-- RÓTULO PRINCIPAL DO GRANDE ESPAÇO SOCIAL INTEGRADO -->
          <g transform="translate(255.0, 310.0)">
            <rect x="-85" y="-12" width="170" height="24" rx="6" fill="rgba(234, 88, 12, 0.95)" stroke="#fff" stroke-width="1.5"/>
            <text x="0" y="1" font-size="8" font-weight="900" fill="#fff" text-anchor="middle">COZINHA, SALA & CORREDOR INTEGRADOS</text>
            <text x="0" y="9" font-size="6" font-weight="700" fill="#ffedd5" text-anchor="middle">Conceito Aberto Americano • ~47,4 m²</text>
          </g>

          <text x="312.0" y="355.0" font-size="12" font-weight="900" fill="#000" text-anchor="middle">cozinha</text>

          <text x="297.4" y="432.0" font-size="9" font-weight="700" fill="#000" text-anchor="middle">quarto3</text>
          <text x="341.8" y="432.0" font-size="8" font-weight="700" fill="#000" text-anchor="middle">banheiro</text>

          <text x="324.0" y="505.0" font-size="12" font-weight="700" fill="#000" text-anchor="middle">quarto5</text>
          <text x="414.5" y="505.0" font-size="9" font-weight="700" fill="#000" text-anchor="middle">lavanderia</text>

          <g transform="translate(415.0, 335.0)">
            <text font-size="10" font-weight="800" fill="#78350f" text-anchor="middle">Varandas Conectadas</text>
            <text y="12" font-size="8.5" font-weight="700" fill="#92400e" text-anchor="middle">Área Gourmet & Piscina</text>
          </g>

          <g transform="translate(130.0, 425.0)">
            <text font-size="10" font-weight="800" fill="#6b21a8" text-anchor="middle">Varanda Frontal</text>
            <text y="10" font-size="7.5" font-weight="700" fill="#7e22ce" text-anchor="middle">(Pedestres)</text>
          </g>

          <text x="501.5" y="310.0" font-size="11" font-weight="700" fill="#1b4332" text-anchor="middle">Hor-</text>
          <text x="501.5" y="325.0" font-size="11" font-weight="700" fill="#1b4332" text-anchor="middle">ta</text>
          <text x="501.5" y="340.0" font-size="11" font-weight="700" fill="#1b4332" text-anchor="middle">co-</text>
          <text x="501.5" y="355.0" font-size="11" font-weight="700" fill="#1b4332" text-anchor="middle">m -</text>
          <text x="501.5" y="370.0" font-size="11" font-weight="700" fill="#1b4332" text-anchor="middle">cer-</text>
          <text x="501.5" y="385.0" font-size="11" font-weight="700" fill="#1b4332" text-anchor="middle">ca</text>

          <text x="342.2" y="159.0" font-size="13" font-weight="700" fill="#1b4332" text-anchor="middle">jardim</text>
          <text x="96.4" y="250.0" font-size="13" font-weight="700" fill="#1b4332" text-anchor="middle">jardim</text>
          <text x="77.2" y="610.0" font-size="13" font-weight="700" fill="#1b4332" text-anchor="middle">jardim</text>
          <text x="323.7" y="645.0" font-size="14" font-weight="800" fill="#1b4332" text-anchor="middle">Jardim</text>
        </g>

        <!-- ================================================================= -->
        <!-- 10. CAIXAS DE MEDIDAS TÉCNICAS ORIGINAIS DA PRANCHA               -->
        <!-- ================================================================= -->
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

          <!-- Varandas Lilás Frontais: 3,26x2,78 cm e 3,32x2,94 cm -->
          <g class="callout-box" transform="translate(34.2, 365.9)">
            <rect width="53.8" height="43.8" rx="4" fill="#e5e7eb" stroke="#9ca3af" stroke-width="1"/>
            <text x="6" y="16" font-size="7.5" font-weight="700">3,26 cm</text>
            <text x="6" y="34" font-size="7.5" font-weight="700">2,78 cm</text>
          </g>
          <g class="callout-box" transform="translate(103.9, 365.2)">
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

        <!-- 11. LEGENDA OFICIAL DOS MÓVEIS (CANTO SUPERIOR ESQUERDO) -->
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

        <!-- 12. RODAPÉ DA PRANCHA -->
        <g transform="translate(180, 765)">
          <text font-size="7" font-weight="600" fill="#64748b" text-anchor="middle">( X ) Público   ( ) Interno   ( ) Setorial   ( ) Confidencial</text>
          <text font-size="6.5" font-weight="500" fill="#94a3b8" text-anchor="middle" y="10">Dados Pessoais</text>
        </g>

      </g>
    </svg>

    <!-- Layer Toggles Floating Bar -->
    <div id="layer-bar" class="floating-bar">
      <button class="chip-toggle active" data-layer="layer-rua">
        <span class="dot" style="background:#0284c7"></span> Rua & Calçada
      </button>
      <button class="chip-toggle active" data-layer="layer-cercado-eucalipto">
        <span class="dot" style="background:#78350f"></span> Cercado Eucalipto
      </button>
      <button class="chip-toggle active" data-layer="layer-mobiliario">
        <span class="dot" style="background:#38bdf8"></span> Móveis & Centro
      </button>
      <button class="chip-toggle active" data-layer="layer-linhas-vermelhas">
        <span class="dot" style="background:#dc2626"></span> Aberturas Americana
      </button>
      <button class="chip-toggle active" data-layer="layer-acesso-pedestres">
        <span class="dot" style="background:#b45309"></span> Pedestres & Luz Antiga
      </button>
      <button class="chip-toggle active" data-layer="layer-acesso-carros">
        <span class="dot" style="background:#059669"></span> Garagem & Carros
      </button>
      <button class="chip-toggle active" data-layer="layer-caixas-medidas">
        <span class="dot" style="background:#ef4444"></span> Medidas da Prancha
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
    const floorPlanDatabase = {{
      'poly-rua-principal': {{
        name: 'Rua Principal (Frente da Casa)',
        badge: 'Via Pública Asfaltada',
        dims: 'Largura 7,00 m (Pista)',
        area: 'Via Pública',
        scale: 'Rua na Frente da Casa',
        desc: 'Rua asfaltada em frente à residência com faixa central amarela e calçada de pedestres com meio-fio rebaixado para a garagem.'
      }},
      'poly-cercado-eucalipto': {{
        name: 'Cercado de Eucalipto (Mourão)',
        badge: 'Fechamento Rústico Ecológico',
        dims: 'Extensão ~115 m lineares',
        area: 'Perímetro Protegido',
        scale: 'Mourões de Eucalipto c/ Travessas',
        desc: 'Cercado de madeira de eucalipto tratado com mourões cilíndricos cravados no solo. Inicia na extremidade da garagem, faz uma elegante meia-lua em direção à borda do terreno, segue para os fundos contornando a Casa da Árvore e o Pergolado, e sobe até o Quarto 1.'
      }},
      'poly-espaco-social-integrado': {{
        name: 'Cozinha, Sala e Corredor Integrados',
        badge: 'Espaço Social • Conceito Aberto',
        dims: 'Ambiente Fluido Integrado',
        area: '47,40 m²',
        scale: 'Cozinha (4,18x4,08 cm) + Salas + Corredor',
        desc: 'Espaço social totalmente integrado no estilo cozinha americana. Não existem paredes divisórias entre a Cozinha, a Sala e o Corredor. Além disso, a cozinha também se conecta à Varanda Gourmet num conceito aberto com linhas vermelhas tracejadas de livre circulação.'
      }},
      'furn-Centro': {{
        name: 'Centro: Bancada Central Retangular',
        badge: 'Bancada Central Única da Cozinha',
        dims: '2,14 × 0,54 m',
        area: '1,16 m²',
        scale: 'Centro = 2,14 x 0,54 m',
        desc: 'Única bancada retangular localizada no centro da cozinha (identificada como "centro" na planta original). Serve de bancada de preparo, apoio de corte e montagem de pratos gourmet.'
      }},
      'furn-Ilha': {{
        name: 'Ilha / Balcão da Cozinha Americana',
        badge: 'Divisa Aberta & Refeições',
        dims: '1,68 × 1,26 m',
        area: '2,12 m²',
        scale: 'Ilha = 1,68 x 1,26 m',
        desc: 'Ilha de granito preto São Gabriel polido situada na divisa oeste entre a Cozinha e a Sala/Corredor. Possui 3 banquetas giratórias estofadas voltadas para a sala.'
      }},
      'poly-piscina-redonda': {{
        name: 'Piscina Redonda de Plástico (Estruturada)',
        badge: 'Lazer Aquático',
        dims: 'Ø ~5,00 m (Diâmetro)',
        area: '19,63 m²',
        scale: 'Piscina Redonda Estruturada no Deck',
        desc: 'Piscina redonda de plástico/lona de PVC azul laminada reforçada com suportes metálicos tubulares externos em T ao redor de todo o perímetro, anel tubular superior reforçado branco e escada externa de 3 degraus apoiada no deck.'
      }},
      'furn-luz-antiga-norte': {{
        name: 'Poste Colonial de Luz Antiga (Norte)',
        badge: 'Iluminação Vintage / Retrô',
        dims: '0,40 × 0,40 × 2,20 m',
        area: 'Halo de 2,5 m',
        scale: 'Luz Antiga Lateral da Entrada',
        desc: 'Poste colonial clássico em ferro forjado negro com lanterna hexagonal de vidros bisotados e lâmpada vintage de filamento quente âmbar (2700K).'
      }},
      'furn-luz-antiga-sul': {{
        name: 'Poste Colonial de Luz Antiga (Sul)',
        badge: 'Iluminação Vintage / Retrô',
        dims: '0,40 × 0,40 × 2,20 m',
        area: 'Halo de 2,5 m',
        scale: 'Luz Antiga Lateral da Entrada',
        desc: 'Poste colonial clássico em ferro forjado negro com lanterna hexagonal e lâmpada quente de filamento retrô, harmonizando a iluminação noturna aos lados do acesso de pedestres.'
      }},
      'furn-vaso-norte': {{
        name: 'Vaso Vietnamita Ornamental (Norte)',
        badge: 'Decoração Paisagística',
        dims: 'Ø 0,55 m × Altura 0,90 m',
        area: '0,24 m²',
        scale: 'Decoração Lateral da Entrada',
        desc: 'Vaso cerâmico esmaltado vitificado em azul petróleo com composição paisagística de palmeira-ráfia e zamioculcas junto à entrada de pedestres.'
      }},
      'furn-vaso-sul': {{
        name: 'Vaso Vietnamita Ornamental (Sul)',
        badge: 'Decoração Paisagística',
        dims: 'Ø 0,55 m × Altura 0,90 m',
        area: '0,24 m²',
        scale: 'Decoração Lateral da Entrada',
        desc: 'Vaso cerâmico esmaltado azul petróleo com folhagens tropicais densas compondo o portal verde de entrada para a varanda frontal.'
      }},
      'poly-caminho-pedestres': {{
        name: 'Acesso de Pedestres à Varanda Frontal',
        badge: 'Circulação Principal',
        dims: '5,83 × 2,00 m',
        area: '11,66 m²',
        scale: 'Passarela de Pedras São Tomé',
        desc: 'Caminho de pedestres em lajotas de pedra natural conectando a calçada da rua diretamente à Varanda Frontal, ladeado por postes coloniais de luz antiga e vasos ornamentais.'
      }},
      'poly-driveway-garagem': {{
        name: 'Entrada da Garagem Decorada para Carros',
        badge: 'Acesso Automotivo',
        dims: '5,71 × 6,00 m',
        area: '34,26 m²',
        scale: 'Driveway Intertravada com Balizadores',
        desc: 'Rampa de acesso e manobra de veículos com piso intertravado (paver) antiderrapante e faixas de concreto reforçado para pneus com balizadores de LED.'
      }},
      'furn-carro-estilizado': {{
        name: 'Vaga 1 Garagem (Veículo Moderno)',
        badge: 'Vaga Automotiva Coberta',
        dims: '4,60 × 1,90 m (Carro)',
        area: '8,74 m²',
        scale: 'Vaga Técnica Demarcada',
        desc: 'Vaga coberta demarcada com pintura termoplástica técnica, acomodando veículo moderno com segurança e conforto térmico.'
      }},
      'poly-garagem': {{
        name: 'Garagem Coberta (Vaga Dupla)',
        badge: 'Garagem Residencial',
        dims: '5,71 × 3,00 m',
        area: '17,13 m²',
        scale: 'Altura: 3 cm • Largura: 5,71 cm',
        desc: 'Garagem coberta ampla para até dois veículos, com piso reforçado resinado, demarcação técnica de vagas e acesso direto pela entrada pavimentada com pavers.'
      }},
      'poly-varanda-lilas-conectada': {{
        name: 'Varanda Frontal Lilás (Pedestres)',
        badge: 'Varanda de Recepção',
        dims: '2,94 × 3,32 m / 2,78 × 3,26 m',
        area: '18,82 m²',
        scale: '3,26 x 2,78 cm e 3,32 x 2,94 cm',
        desc: 'Varanda de recepção frontal no tom lilás da prancha. É a entrada oficial de pedestres da residência, conectando o jardim iluminado à grande sala unificada.'
      }},
      'poly-varanda-lazer-conectada': {{
        name: 'Complexo de Lazer & Varandas Conectadas',
        badge: 'Lazer & Gourmet Integrados',
        dims: 'Complexo Contínuo Leste',
        area: '56,31 m²',
        scale: 'Deck Piscina + Varanda Gourmet (7,02x3,34 cm)',
        desc: 'Área externa contínua integrando o Deck da piscina redonda de plástico, a Varanda Gourmet com churrasqueira e a circulação lateral sem barreiras ou paredes intermediárias, conectada abertamente com a cozinha.'
      }},
      'poly-jardim-conectado': {{
        name: 'Jardins Perimetrais 100% Conectados',
        badge: 'Paisagismo & Manto Verde',
        dims: 'Perímetro Total Contínuo',
        area: '184,50 m²',
        scale: 'Jardins Norte, Oeste e Sul Conectados',
        desc: 'Manto verde contínuo e integrado ao redor de toda a residência. Conecta o Jardim Norte (superior), o Jardim Oeste, o Jardim da Casa da Árvore e o Jardim dos Fundos com Pergolado.'
      }},
      'furn-P': {{
        name: 'P: Pia Cuba Dupla',
        badge: 'Bancada Molhada',
        dims: '2,00 × 0,60 m',
        area: '1,20 m²',
        scale: 'P = 2 x 0,6 m',
        desc: 'Bancada na parede norte da cozinha (compartilhada com o banheiro), equipada com duas cubas de aço inox e torneira gourmet.'
      }},
      'furn-AE': {{
        name: 'AE: Bancada c/ Armário Aéreo',
        badge: 'Marcenaria Superior',
        dims: '1,15 × 0,54 m',
        area: '0,62 m²',
        scale: 'AE = 1,15 x 0,54 m',
        desc: 'Bancada contígua à pia com armário aéreo superior para louças e mantimentos.'
      }},
      'furn-F': {{
        name: 'F: Fogão Cooktop & Coifa',
        badge: 'Área Quente',
        dims: '0,83 × 0,70 m',
        area: '0,58 m²',
        scale: 'F = 0,83 x 0,70 m',
        desc: 'Cooktop de 4 bocas com grelhas de ferro fundido, forno embutido e coifa em inox.'
      }},
      'furn-BL': {{
        name: 'BL: Bancada Lado',
        badge: 'Bancada de Serviço',
        dims: '1,97 × 0,51 m',
        area: '1,00 m²',
        scale: 'BL = 1,97 x 0,51 m',
        desc: 'Bancada lateral com gaveteiros para talheres e utensílios gourmet na parede sul da cozinha.'
      }},
      'furn-AM': {{
        name: 'AM: Armário Torre Quente',
        badge: 'Torre de Fornos',
        dims: '0,66 × 0,54 m',
        area: '0,36 m²',
        scale: 'AM = 0,66 x 0,54 m',
        desc: 'Coluna vertical com nichos embutidos para forno elétrico e micro-ondas.'
      }},
      'furn-G': {{
        name: 'G: Geladeira Duplex Inox',
        badge: 'Refrigeração',
        dims: '0,72 × 0,76 m',
        area: '0,55 m²',
        scale: 'G = 0,72 x 0,76 m',
        desc: 'Geladeira duplex frost-free com acabamento em aço inoxidável.'
      }},
      'poly-quarto1': {{
        name: 'Quarto 1',
        badge: 'Dormitório Superior Esquerdo',
        dims: '3,01 × 4,00 m',
        area: '12,04 m²',
        scale: 'Altura: 4 cm • Largura: 3,01 cm',
        desc: 'Dormitório localizado no canto superior esquerdo da residência, onde o cercado de mourões de eucalipto encerra sua trajetória perimetral.'
      }},
      'poly-quarto2': {{
        name: 'Quarto 2',
        badge: 'Dormitório Superior Centro',
        dims: '3,51 × 3,01 m',
        area: '10,57 m²',
        scale: 'Altura: 3,01 cm • Largura: 3,51 cm',
        desc: 'Dormitório localizado no topo da residência, ao lado do Quarto 1 e acima do Banheiro Superior.'
      }},
      'poly-banheiro-sup': {{
        name: 'Banheiro Superior',
        badge: 'Área Molhada Superior',
        dims: '2,43 × 1,87 m',
        area: '4,54 m²',
        scale: 'Abaixo do Quarto 2',
        desc: 'Banheiro completo da área íntima superior.'
      }},
      'poly-quarto3': {{
        name: 'Quarto 3',
        badge: 'Dormitório Compacto',
        dims: '2,17 × 1,90 m',
        area: '4,12 m²',
        scale: '1,9 cm • 2,17 cm',
        desc: 'Quarto posicionado abaixo da Cozinha e ao lado do Banheiro Inferior.'
      }},
      'poly-banheiro-inf': {{
        name: 'Banheiro Inferior',
        badge: 'Área Molhada Social',
        dims: '1,79 × 1,52 m',
        area: '2,72 m²',
        scale: '1,79 cm • 1,52 cm',
        desc: 'Banheiro social posicionado junto ao Quarto 3 e à lavanderia.'
      }},
      'poly-quarto5': {{
        name: 'Quarto 5 (Suíte Térrea)',
        badge: 'Dormitório Amplo',
        dims: '5,41 × 3,00 m',
        area: '16,23 m²',
        scale: 'Altura: 3 cm • Largura: 5,41 cm',
        desc: 'Quarto amplo no setor inferior da casa, com vista para o jardim dos fundos e pergolado.'
      }},
      'poly-lavanderia': {{
        name: 'Lavanderia & Serviços',
        badge: 'Área de Serviço',
        dims: '2,24 × 2,95 m',
        area: '6,61 m²',
        scale: '2,24 cm • 2,95 cm',
        desc: 'Área de serviço com tanque, máquina de lavar e bancada com armário de canto (AC).'
      }},
      'poly-horta': {{
        name: 'Horta com Cerca',
        badge: 'Cultivo Orgânico',
        dims: '1,48 × 14,33 m',
        area: '21,21 m²',
        scale: 'Horta com Cerca Lateral',
        desc: 'Canteiro longitudinal protegido para cultivo de temperos e hortaliças frescas.'
      }},
      'poly-casa-cachorro': {{
        name: 'Casa do Cachorro',
        badge: 'Área Pet',
        dims: '2,50 × 2,60 m',
        area: '6,50 m²',
        scale: 'Canto Superior Direito',
        desc: 'Abrigo rústico de madeira com cobertura inclinada no jardim superior.'
      }},
      'poly-casa-arvore': {{
        name: 'Casa da Árvore',
        badge: 'Espaço Lúdico',
        dims: '2,50 × 2,60 m',
        area: '6,50 m²',
        scale: 'Canto Inferior Esquerdo',
        desc: 'Casinha de madeira suspensa em tronco robusto com escada de marinheiro.'
      }},
      'poly-pergolado': {{
        name: 'Pergolado de Madeira',
        badge: 'Espaço Zen & Convivência',
        dims: '3,05 × 2,91 m',
        area: '8,88 m²',
        scale: 'Altura: 3,05 cm • Largura: 2,91 cm',
        desc: 'Pergolado em vigamento de eucalipto tratado com trepadeiras e bancos de descanso.'
      }}
    }};

    /* ==========================================================================
       2. INTERATIVIDADE: PAN & ZOOM
       ========================================================================== */
    const svg = document.getElementById('blueprint-svg');
    const viewportGroup = document.getElementById('viewport-group');
    const workspace = document.getElementById('workspace');

    let scale = 1.0;
    let pointX = 0;
    let pointY = 0;
    let isPanning = false;
    let startX = 0;
    let startY = 0;

    function updateTransform() {{
      viewportGroup.setAttribute('transform', `translate(${{pointX}}, ${{pointY}}) scale(${{scale}})`);
    }}

    workspace.addEventListener('mousedown', (e) => {{
      if (e.target.closest('#inspector') || e.target.closest('.floating-bar')) return;
      isPanning = true;
      startX = e.clientX - pointX;
      startY = e.clientY - pointY;
    }});

    window.addEventListener('mousemove', (e) => {{
      if (!isPanning) return;
      pointX = e.clientX - startX;
      pointY = e.clientY - startY;
      updateTransform();
    }});

    window.addEventListener('mouseup', () => {{ isPanning = false; }});

    workspace.addEventListener('wheel', (e) => {{
      e.preventDefault();
      const zoomFactor = 1.12;
      const rect = workspace.getBoundingClientRect();
      const mouseX = e.clientX - rect.left;
      const mouseY = e.clientY - rect.top;

      let newScale = e.deltaY < 0 ? scale * zoomFactor : scale / zoomFactor;
      newScale = Math.min(Math.max(0.4, newScale), 5.0);

      pointX = mouseX - (mouseX - pointX) * (newScale / scale);
      pointY = mouseY - (mouseY - pointY) * (newScale / scale);
      scale = newScale;
      updateTransform();
    }}, {{ passive: false }});

    document.getElementById('btn-zoom-in').addEventListener('click', () => {{
      scale = Math.min(scale * 1.25, 5.0);
      updateTransform();
    }});

    document.getElementById('btn-zoom-out').addEventListener('click', () => {{
      scale = Math.max(scale / 1.25, 0.4);
      updateTransform();
    }});

    function resetView() {{
      scale = 0.95;
      pointX = 35;
      pointY = 10;
      updateTransform();
    }}

    document.getElementById('btn-zoom-reset').addEventListener('click', resetView);
    document.getElementById('btn-center-view').addEventListener('click', resetView);

    /* ==========================================================================
       3. CONTROLE DE CAMADAS (LAYERS)
       ========================================================================== */
    document.querySelectorAll('.chip-toggle[data-layer]').forEach(btn => {{
      btn.addEventListener('click', () => {{
        const layerId = btn.dataset.layer;
        const layerEl = document.getElementById(layerId);
        if (!layerEl) return;
        btn.classList.toggle('active');
        layerEl.style.display = btn.classList.contains('active') ? '' : 'none';
      }});
    }});

    const overlaySlider = document.getElementById('overlay-slider');
    const overlayVal = document.getElementById('overlay-val');
    const overlayLayer = document.getElementById('layer-original-overlay');

    overlaySlider.addEventListener('input', (e) => {{
      const val = e.target.value;
      overlayVal.textContent = val + '%';
      overlayLayer.setAttribute('opacity', val / 100);
    }});

    /* ==========================================================================
       4. GAVETA DE INSPEÇÃO TÉCNICA (INSPECTOR DRAWER)
       ========================================================================== */
    const inspector = document.getElementById('inspector');
    const inspTitle = document.getElementById('insp-title');
    const inspBadge = document.getElementById('insp-badge');
    const inspDims = document.getElementById('insp-dims');
    const inspArea = document.getElementById('insp-area');
    const inspScale = document.getElementById('insp-scale');
    const inspDesc = document.getElementById('insp-desc');
    let selectedElement = null;

    function openInspector(data) {{
      inspTitle.textContent = data.name;
      inspBadge.textContent = data.badge;
      inspDims.textContent = data.dims;
      inspArea.textContent = data.area;
      inspScale.textContent = data.scale;
      inspDesc.textContent = data.desc;
      inspector.classList.add('open');
    }}

    document.getElementById('insp-close').addEventListener('click', () => {{
      inspector.classList.remove('open');
      if (selectedElement) {{
        selectedElement.classList.remove('room-selected');
        selectedElement = null;
      }}
    }});

    document.querySelectorAll('.room-poly').forEach(poly => {{
      poly.addEventListener('click', (e) => {{
        e.stopPropagation();
        if (selectedElement) selectedElement.classList.remove('room-selected');
        
        selectedElement = poly;
        selectedElement.classList.add('room-selected');

        const key = poly.id;
        if (floorPlanDatabase[key]) {{
          openInspector(floorPlanDatabase[key]);
        }} else {{
          const parentGroup = poly.closest('[id]');
          if (parentGroup && floorPlanDatabase[parentGroup.id]) {{
            openInspector(floorPlanDatabase[parentGroup.id]);
          }}
        }}
      }});
    }});

    resetView();
  </script>
</body>
</html>
'''

with open(r'F:\casa-completa-lazer-3d\index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)
print("F:\\casa-completa-lazer-3d\\index.html atualizado com sucesso!")
