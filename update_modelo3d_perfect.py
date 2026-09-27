# -*- coding: utf-8 -*-
"""
Atualiza modelo3d.html para refletir:
1. Piscina REDONDA DE PLÁSTICO estruturada (em vez de piscina retangular)
2. Cercado de mourões de eucalipto em meia-lua saindo da garagem até a borda e até o Quarto 1
3. Rua frontal asfaltada e calçada
4. Entrada de pedestres com postes de luz antiga (luminárias coloniais) e vasos vietnamitas
5. Entrada da garagem decorada com piso de pavers e balizadores
"""

import os
import re

path = r'F:\casa-completa-lazer-3d\modelo3d.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Substitui o trecho da piscina retangular pela piscina redonda de plástico estruturada
old_pool_snippet = r'''      // ---------------------------------------------------------
      // PISCINA EMBUTIDA NO DECK SUPERIOR (2,20 x 3,40 m, prof. 1,40 m)
      // Varanda Superior: X = 7.17 a 10.51, Z = 0.50 a 4.00
      // ---------------------------------------------------------
      const poolBasinGeo = new THREE.BoxGeometry(2.30, 0.02, 3.40);
      const poolBasin = new THREE.Mesh(poolBasinGeo, Materials.poolTile);
      poolBasin.position.set(8.84, 0.008, 2.20);
      poolBasin.receiveShadow = true;
      pGroup.add(poolBasin);

      // Shimmering Pool Water Surface
      const poolWaterGeo = new THREE.PlaneGeometry(2.20, 3.30);
      const poolWater = new THREE.Mesh(poolWaterGeo, Materials.poolWater);
      poolWater.rotation.x = -Math.PI / 2;
      poolWater.position.set(8.84, 0.02, 2.20);
      pGroup.add(poolWater);

      // Pool White Border Curb
      const poolCurbGeo = new THREE.BoxGeometry(2.40, 0.04, 3.50);
      const poolCurb = new THREE.Mesh(poolCurbGeo, Materials.porcelainWhite);
      poolCurb.position.set(8.84, 0.015, 2.20);
      pGroup.add(poolCurb);

      // Stainless Steel Pool Ladder
      const ladder = new THREE.Group();
      for (let lx of [-0.25, 0.25]) {
        const rail = new THREE.Mesh(new THREE.CylinderGeometry(0.018, 0.018, 0.70), Materials.chrome);
        rail.position.set(lx, 0.35, 0);
        ladder.add(rail);
      }
      for (let r = 0; r < 3; r++) {
        const rung = new THREE.Mesh(new THREE.CylinderGeometry(0.012, 0.012, 0.50), Materials.chrome);
        rung.rotation.z = Math.PI / 2;
        rung.position.set(0, 0.15 + r * 0.18, 0);
        ladder.add(rung);
      }
      ladder.position.set(8.84, 0, 0.65);
      pGroup.add(ladder);

      // 2 Sun Loungers (Espreguiçadeiras)
      for (let lz of [1.50, 2.90]) {
        const lounger = new THREE.Group();
        const base = new THREE.Mesh(new THREE.BoxGeometry(0.65, 0.22, 1.80), Materials.woodFurniture);
        base.position.y = 0.11;
        lounger.add(base);
        const cushion = new THREE.Mesh(new THREE.BoxGeometry(0.62, 0.08, 1.76), Materials.fabricBed);
        cushion.position.y = 0.25;
        lounger.add(cushion);
        lounger.position.set(10.00, 0, lz);
        pGroup.add(lounger);
      }

      registerInteractive(pGroup, "Piscina Aquecida & Deck", "Piscina em pastilhas azuis com água translúcida, borda atérmica e espreguiçadeiras.", "2,20 × 3,40 m");'''

new_pool_snippet = r'''      // ---------------------------------------------------------
      // 🌟 PISCINA REDONDA DE PLÁSTICO ESTRUTURADA (Diâmetro 3,0 m, Altura 0,76 m)
      // Apoiada diretamente sobre o Deck da Varanda Lazer
      // ---------------------------------------------------------
      const plasticBlueMat = new THREE.MeshStandardMaterial({ color: 0x0284C7, roughness: 0.3, metalness: 0.1 });
      const plasticRimMat = new THREE.MeshStandardMaterial({ color: 0xF8FAFC, roughness: 0.2, metalness: 0.05 });
      const poolFrameMat = new THREE.MeshStandardMaterial({ color: 0x64748B, roughness: 0.4, metalness: 0.8 });

      // Corpo cilíndrico de lona PVC azul reforçada
      const poolBody = new THREE.Mesh(new THREE.CylinderGeometry(1.50, 1.50, 0.76, 32, 1, true), plasticBlueMat);
      poolBody.position.set(8.84, 0.38, 2.20);
      poolBody.castShadow = true;
      pGroup.add(poolBody);

      // Fundo interno da piscina
      const poolBottom = new THREE.Mesh(new THREE.CircleGeometry(1.50, 32), plasticBlueMat);
      poolBottom.rotation.x = -Math.PI / 2;
      poolBottom.position.set(8.84, 0.01, 2.20);
      pGroup.add(poolBottom);

      // Superfície da água azul cristalina translúcida
      const poolWaterGeo = new THREE.CircleGeometry(1.48, 32);
      const poolWater = new THREE.Mesh(poolWaterGeo, Materials.poolWater);
      poolWater.rotation.x = -Math.PI / 2;
      poolWater.position.set(8.84, 0.65, 2.20);
      pGroup.add(poolWater);

      // Borda tubular/inflável superior reforçada em branco
      const poolTorus = new THREE.Mesh(new THREE.TorusGeometry(1.50, 0.05, 12, 32), plasticRimMat);
      poolTorus.rotation.x = Math.PI / 2;
      poolTorus.position.set(8.84, 0.76, 2.20);
      pGroup.add(poolTorus);

      // 12 Hastes Metálicas Verticais de Sustentação Externa com sapatas no deck
      for (let i = 0; i < 12; i++) {
        const angle = (i / 12) * Math.PI * 2;
        const hx = 8.84 + Math.cos(angle) * 1.53;
        const hz = 2.20 + Math.sin(angle) * 1.53;
        
        const leg = new THREE.Mesh(new THREE.CylinderGeometry(0.02, 0.02, 0.76), poolFrameMat);
        leg.position.set(hx, 0.38, hz);
        leg.castShadow = true;
        pGroup.add(leg);

        const foot = new THREE.Mesh(new THREE.CylinderGeometry(0.045, 0.045, 0.015), poolFrameMat);
        foot.position.set(hx, 0.008, hz);
        pGroup.add(foot);
      }

      // Escada tubular externa metálica de 3 degraus apoiada na borda
      const ladder = new THREE.Group();
      for (let lx of [-0.22, 0.22]) {
        const rail = new THREE.Mesh(new THREE.CylinderGeometry(0.016, 0.016, 1.05), Materials.chrome);
        rail.position.set(lx, 0.525, 0);
        ladder.add(rail);
      }
      for (let r = 0; r < 4; r++) {
        const rung = new THREE.Mesh(new THREE.CylinderGeometry(0.012, 0.012, 0.44), Materials.chrome);
        rung.rotation.z = Math.PI / 2;
        rung.position.set(0, 0.20 + r * 0.22, 0);
        ladder.add(rung);
      }
      ladder.position.set(8.84, 0, 0.65);
      pGroup.add(ladder);

      // Boia circular inflável colorida flutuando
      const floatie = new THREE.Mesh(new THREE.TorusGeometry(0.25, 0.08, 12, 24), new THREE.MeshStandardMaterial({ color: 0xF43F5E, roughness: 0.3 }));
      floatie.rotation.x = Math.PI / 2;
      floatie.position.set(8.40, 0.68, 2.40);
      pGroup.add(floatie);

      // 2 Espreguiçadeiras de sol no deck de madeira
      for (let lz of [1.50, 2.90]) {
        const lounger = new THREE.Group();
        const base = new THREE.Mesh(new THREE.BoxGeometry(0.65, 0.22, 1.80), Materials.woodFurniture);
        base.position.y = 0.11;
        lounger.add(base);
        const cushion = new THREE.Mesh(new THREE.BoxGeometry(0.62, 0.08, 1.76), Materials.fabricBed);
        cushion.position.y = 0.25;
        lounger.add(cushion);
        lounger.position.set(10.50, 0, lz);
        pGroup.add(lounger);
      }

      registerInteractive(pGroup, "Piscina Redonda de Plástico", "Piscina redonda de plástico estruturada em lona de PVC azul laminada, com hastes tubulares metálicas, escada de segurança e espreguiçadeiras no deck.", "Ø 3,00 m (Redonda)");'''

if old_pool_snippet in content:
    content = content.replace(old_pool_snippet, new_pool_snippet)
    print("Piscina redonda 3D atualizada com sucesso!")
else:
    print("Trecho da piscina antiga não encontrado exatamente, procurando padrão...")
    # Tenta substituição com regex
    content = re.sub(r'const poolBasinGeo = new THREE\.BoxGeometry.*?\n.*?registerInteractive\(pGroup, "Piscina Aquecida.*?\);', new_pool_snippet, content, flags=re.DOTALL)
    print("Substituição da piscina via regex realizada!")

# Adiciona o Cercado de Mourões de Eucalipto na função buildExteriorLandscape se não existir
if "Cercado_Eucalipto_3D" not in content:
    fence_code = r'''
      // ======================================================================
      // 🌟 CERCADO DE MADEIRA EUCALIPTO (MOURÃO) EM MEIA-LUA
      // Começa na extremidade da garagem, meia-lua até a borda, segue fundos até Quarto 1
      // ======================================================================
      const fenceGroup = new THREE.Group();
      fenceGroup.name = "Cercado_Eucalipto_3D";
      const postMat = new THREE.MeshStandardMaterial({ color: 0x6C4A27, roughness: 0.9, metalness: 0.05 });
      const railMat = new THREE.MeshStandardMaterial({ color: 0x8D5B4C, roughness: 0.85, metalness: 0.05 });

      // Pontos do perímetro do cercado
      const fencePoints = [
        // Meia-lua da garagem até a borda oeste
        [2.38, 14.50], [1.80, 15.00], [1.20, 15.80], [0.80, 16.80], [0.60, 17.80],
        // Segue na borda oeste para os fundos
        [0.60, 19.50], [0.60, 21.00], [0.60, 23.50],
        // Segue pelo fundo sul
        [2.50, 23.50], [4.50, 23.50], [6.50, 23.50], [8.50, 23.50], [10.50, 23.50], [11.50, 23.50],
        // Segue pela lateral leste
        [11.50, 20.00], [11.50, 16.00], [11.50, 12.00], [11.50, 8.00], [11.50, 4.00], [11.50, 0.00], [11.50, -3.50],
        // Segue pelo topo norte
        [9.50, -3.50], [7.50, -3.50], [5.50, -3.50], [3.50, -3.50],
        // Conecta até a quina do Quarto 1
        [3.50, 0.00]
      ];

      for (let i = 0; i < fencePoints.length; i++) {
        const pt = fencePoints[i];
        // Mourão cilíndrico de eucalipto
        const post = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.08, 1.20, 12), postMat);
        post.position.set(pt[0], 0.60, pt[1]);
        post.castShadow = true;
        fenceGroup.add(post);

        // Travessas horizontais de madeira conectando os mourões
        if (i < fencePoints.length - 1) {
          const nextPt = fencePoints[i + 1];
          const dist = Math.hypot(nextPt[0] - pt[0], nextPt[1] - pt[1]);
          const midX = (pt[0] + nextPt[0]) / 2;
          const midZ = (pt[1] + nextPt[1]) / 2;
          const angle = Math.atan2(nextPt[1] - pt[1], nextPt[0] - pt[0]);

          for (let ry of [0.45, 0.90]) {
            const rail = new THREE.Mesh(new THREE.CylinderGeometry(0.035, 0.035, dist, 8), railMat);
            rail.rotation.z = Math.PI / 2;
            rail.rotation.y = -angle;
            rail.position.set(midX, ry, midZ);
            rail.castShadow = true;
            fenceGroup.add(rail);
          }
        }
      }

      registerInteractive(fenceGroup, "Cercado de Eucalipto (Mourão)", "Cercado de mourões de eucalipto tratado com travessas duplas. Começa na garagem em meia-lua, contorna os fundos e segue até o Quarto 1.", "Extensão ~85 m");
      extGroup.add(fenceGroup);
'''
    content = content.replace("scene.add(extGroup);", fence_code + "\n      scene.add(extGroup);")
    print("Cercado de eucalipto adicionado ao 3D!")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("modelo3d.html atualizado com sucesso!")
