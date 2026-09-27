# Residência Completa, Lazer & Jardins 3D
### Modelo Interativo com Three.js • Cozinha Americana Integrada à Sala

Modelo 3D arquitetônico interativo e imersivo desenvolvido em **Three.js** a partir da planta baixa técnica (escala $1\text{ cm} = 1{,}00\text{ m}$, lote total de ~400 m² / $17 \times 24\text{ m}$).

---

## 🌟 Principais Destaques Arquitetônicos

### 1. Cozinha Americana Integrada com a Sala
- **Conceito Aberto Total**: Transição fluida entre a cozinha e as salas de jantar e estar, sem paredes divisórias que bloqueiem a visão ou a luz natural.
- **Balcão Americano / Ilha de Granito ($1{,}68 \times 1{,}26\text{ m}$)**:
  - Tampo em granito nobre Preto São Gabriel com beiral saliente voltado para a sala.
  - **3 Banquetas Altas Modernas** com apoio para os pés e assento estofado caramelo, proporcionando refeições rápidas e socialização.
  - **3 Luminárias Pendentes** com cúpula preta e iluminação pontual suave.
  - Acessórios de serviço: fruteira decorativa e bandeja com xícaras de café.
- **Ligação e Circulação Ampla**:
  - Passagem norte de $1{,}19\text{ m}$ conectando a sala de jantar diretamente à pia e fogão.
  - Passagem sul de $0{,}67\text{ m}$ interligando o living à torre de fornos e corredor íntimo.
- **Sala de Jantar & Estar Integrada**:
  - Mesa de jantar de 4 lugares em madeira carvalho com cadeiras estofadas.
  - Sofá aconchegante, mesa de centro e painel amadeirado com TV Smart widescreen de 60".

---

### 2. Medidas Exatas da Cozinha Planejada (Móveis & Bancadas)
| Sigla | Elemento | Dimensões Reais ($L \times P$) | Altura / Descrição |
|:---:|:---|:---:|:---|
| **P** | Pia de Cozinha | $2{,}00 \times 0{,}60\text{ m}$ | Bancada com 2 cubas inox e torneira gourmet |
| **AE** | Bancada c/ Armário Aéreo | $1{,}15 \times 0{,}54\text{ m}$ | Gabinete inferior + aéreo suspenso |
| **F** | Fogão e Coifa | $0{,}83 \times 0{,}70\text{ m}$ | Cooktop 4 bocas, forno e coifa inox |
| **Ilha** | Balcão Americano | $1{,}68 \times 1{,}26\text{ m}$ | Passa-pratos, 3 banquetas e 3 pendentes |
| **Centro** | Bancada Central | $2{,}14 \times 0{,}54\text{ m}$ | Ilha de preparo no centro da cozinha |
| **BL** | Bancada Lateral | $1{,}97 \times 0{,}51\text{ m}$ | Balcão de apoio e gaveteiros |
| **AM** | Armário Torre Quente | $0{,}66 \times 0{,}54\text{ m}$ | Coluna vertical até $2{,}20\text{ m}$ com forno |
| **AC** | Bancada de Canto | $1{,}33 \times 0{,}94\text{ m}$ | Formato em L com chanfro a 45° idêntico à planta |
| **G** | Geladeira Duplex | $0{,}72 \times 0{,}76\text{ m}$ | Geladeira inox frost-free |

---

### 3. Área Externa, Lazer & Jardins
- **Piscina com Deck ($3{,}34 \times 4{,}50\text{ m}$)**: Deck em madeira teca e água translúcida iluminada.
- **Varanda Gourmet de Lazer ($3{,}34 \times 7{,}02\text{ m}$)**: Bancada com churrasqueira de tijolos refratários e TV 65".
- **Pergolado em Madeira ($3{,}05 \times 2{,}91\text{ m}$)**: Lounge de descanso com vigas ripadas no jardim dos fundos.
- **Casa na Árvore ($2{,}40 \times 2{,}40\text{ m}$)**: Plataforma rústica elevada a $1{,}85\text{ m}$ com escada e telhado 4 águas.
- **Casa do Cachorro ($1{,}40 \times 1{,}20\text{ m}$)**: Casinha pet estruturada com telhado inclinado.
- **Horta com Cerca ($1{,}20 \times 11{,}50\text{ m}$)**: 4 canteiros elevados com terra fértil, hortaliças e cerquinha de piquete.
- **Área Íntima**: 5 quartos (incluindo Suíte Master), 2 banheiros e lavanderia independente.

---

## ⚡ Otimizações para 60 FPS em Tablets e Celulares
1. **Luzes Sem Cubemaps Excessivos**: Apenas a luz do Sol (DirectionalLight) projeta sombras dinâmicas suaves, evitando sobrecarga na GPU móvel.
2. **Transformações GPU no DOM**: Rótulos e cotas 3D utilizam `transform: translate3d(...)`, eliminando layout reflows na CPU do tablet.
3. **Resolução de Sombras Calibrada**: Mapa de sombra a $1024 \times 1024$, reduzindo em 75% o uso de banda de memória em relação a resoluções pesadas.
4. **Materiais PBR Otimizados**: Dispensado o uso de `transmission` que gerava passagens de renderização extras na tela.
5. **PixelRatio Adaptativo**: Limitado dinamicamente a `1.25` em telas touch para prevenir quedas de framerate em displays de altíssima densidade de pixels.

---

## 🎮 Controles e Interatividade
- **Girar / Orbitar**: 1 dedo no tablet/smartphone ou clique esquerdo do mouse.
- **Mover (Pan)**: 2 dedos no tablet ou clique direito do mouse.
- **Zoom**: Pinça na tela ou roda de rolagem do mouse.
- **Botão Cozinha Americana**: Transfere a câmera imediatamente para a perspectiva humana da sala, observando a integração do balcão e da cozinha.
- **Personalização de Cores**: Paleta interativa com Verde-Sálvia, Azul Petróleo, Grafite, Terracota, Areia e seletor HEX livre.
- **Alternância de Paredes**: Alterne em tempo real entre paredes completas ($2{,}60\text{ m}$) e paredes rebaixadas ($1{,}10\text{ m}$) para visualização panorâmica.
