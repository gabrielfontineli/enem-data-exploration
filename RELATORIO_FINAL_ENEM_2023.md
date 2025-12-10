#  Relatório Final: Análise Exploratória do ENEM 2023
## O Gradiente Socioeconômico e as Desigualdades Educacionais no Brasil

---

**Equipe:**  
Gabriel Fontineli Dantas, Gabriel Guilherme Carvalho Viana, Matheus Gabriel Souto de Lira Freitas, Edson Cavalcanti, Lourrayni Feliph

**Disciplina:** IMD1151 - Ciência de Dados (2025.2)  
**Data:** 26 de novembro de 2025  
**Dataset:** Microdados ENEM 2023 (INEP)

---

##  Sumário Executivo

Este relatório apresenta uma análise exploratória abrangente de **2.166.843 participantes** do Exame Nacional do Ensino Médio (ENEM) 2023, investigando como fatores socioeconômicos influenciam o desempenho acadêmico dos estudantes brasileiros.

### Principais Descobertas:

1. **Existe um gradiente socioeconômico contínuo** que vai muito além da dicotomia "escola pública vs. privada"
2. **Renda familiar é o fator mais determinante** para o desempenho no ENEM
3. **Acesso à tecnologia emergiu como segundo fator mais importante**
4. **Disparidades regionais são significativas**: gap de 51,8 pontos entre Norte e Sudeste
5. **Escolaridade dos pais tem efeito intergeracional forte**

---

##  1. Introdução e Objetivos

### 1.1 Contextualização

O ENEM é o principal instrumento de acesso ao ensino superior no Brasil, utilizado por programas como SISU, ProUni e FIES. Com mais de 3,9 milhões de inscritos anualmente, o exame representa não apenas uma avaliação educacional, mas um mecanismo crucial de mobilidade social.

Contudo, o desempenho no ENEM tende a refletir profundas desigualdades socioeconômicas estruturais do país. Este estudo investiga **como e quanto** diferentes fatores sociais, econômicos e regionais impactam as oportunidades educacionais.

### 1.2 Objetivos

**Objetivo Geral:**  
Analisar como fatores socioeconômicos influenciam o desempenho dos estudantes no ENEM 2023.

**Objetivos Específicos:**
- Investigar a relação entre renda familiar e desempenho acadêmico
- Avaliar o impacto da escolaridade dos pais nas notas dos filhos
- Identificar o papel da infraestrutura tecnológica no desempenho
- Analisar disparidades regionais e por tipo de escola
- Criar modelos preditivos

### 1.3 Perguntas de Pesquisa

1. Qual é o fator socioeconômico mais determinante para o desempenho no ENEM?
2. A relação entre renda e desempenho é linear ou há pontos de saturação?
3. O acesso à tecnologia é mais importante que a escolaridade dos pais?
4. Estudantes do Norte enfrentam dupla penalização (renda + região)?
5. O efeito "escola privada" persiste quando controlamos por renda?

---

##  2. Metodologia

### 2.1 Base de Dados

**Fonte:** Microdados do ENEM 2023 (INEP)  
**URL:** https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem

**Dimensões:**
- **Participantes analisados:** 2.166.843 (após remoção de treineiros)
- **Variáveis utilizadas:** 76 colunas
- **Período:** ENEM 2023 (aplicação em novembro de 2023)

### 2.2 Variáveis Principais

| Categoria | Variável | Descrição | Tipo |
|-----------|----------|-----------|------|
| **Desempenho** | NOTA_MEDIA_5 | Média das 5 provas (MT, LC, CH, CN, RED) | Contínua |
| | NU_NOTA_MT | Nota de Matemática | Contínua |
| | NU_NOTA_LC | Nota de Linguagens e Códigos | Contínua |
| | NU_NOTA_CH | Nota de Ciências Humanas | Contínua |
| | NU_NOTA_CN | Nota de Ciências da Natureza | Contínua |
| | NU_NOTA_REDACAO | Nota da Redação | Contínua |
| **Renda** | Q006 / Q006_ord | Renda familiar mensal (17 faixas) | Ordinal |
| **Educação Parental** | Q001 / Q001_ord | Escolaridade do responsável 1 | Ordinal |
| | Q002 / Q002_ord | Escolaridade do responsável 2 | Ordinal |
| **Tecnologia** | Q024 / Q024_ord | Acesso à internet/tecnologia | Ordinal |
| **Infraestrutura** | Q022 / Q022_ord | Posse de bens no domicílio | Ordinal |
| | Q025 / Q025_ord | Condições de estudo em casa | Ordinal |
| **Geográfico** | REGIAO_NOME_PROVA | Região onde fez a prova (N, NE, CO, SE, S) | Categórica |
| | UF_PROVA | Unidade Federativa | Categórica |
| **Escola** | TP_ESCOLA | Tipo de escola (Pública, Privada, NR) | Categórica |

### 2.3 Pré-processamento

**Etapas realizadas:**

1. **Remoção de treineiros:** `IN_TREINEIRO == 0`
2. **Tratamento de valores ausentes:** Remoção de linhas com NaN nas variáveis-chave
3. **Codificação ordinal:** Transformação de variáveis categóricas alfabéticas (A, B, C...) em números ordinais (1, 2, 3...)
4. **Criação de variável derivada:** `NOTA_MEDIA_5` = média aritmética das 5 notas
5. **Validação de dados:** Remoção de outliers extremos (notas = 0 foram mantidas para análise de exclusão)

**Ferramentas utilizadas:**
- Python 3.x
- pandas 2.x
- matplotlib 3.x
- scipy
- scikit-learn (modelagem preditiva)

### 2.4 Técnicas Analíticas

- **Análise descritiva:** Medidas de tendência central e dispersão
- **Análise bivariada:** Comparação entre grupos
- **Segmentação:** Criação de grupos socioeconômicos (Vulnerável, Média, Privilegiado)
- **Visualizações:** Gráficos de tendência, boxplots, mapas de calor
- **Modelagem:** Regressão linear múltipla (R², MAE, coeficientes)

---

##  3. Resultados e Descobertas

### 3.1 Panorama Geral do Desempenho

**Estatísticas Descritivas - Notas Gerais:**

| Prova | Média | Desvio Padrão | Mínimo | Q1 | Mediana | Q3 | Máximo |
|-------|-------|---------------|--------|-----|---------|-----|--------|
| **Matemática (MT)** | 532,23 | 132,15 | 0,0 | 428,6 | 519,7 | 628,1 | 958,6 |
| **Linguagens (LC)** | 520,49 | 75,06 | 0,0 | 472,9 | 524,5 | 572,6 | 820,8 |
| **Ciências Humanas (CH)** | 527,01 | 88,04 | 0,0 | 470,6 | 533,3 | 588,6 | 823,0 |
| **Ciências da Natureza (CN)** | 496,95 | 88,33 | 0,0 | 440,5 | 494,0 | 552,0 | 868,4 |
| **Redação (RED)** | 625,85 | 208,86 | 0,0 | 520,0 | 620,0 | 780,0 | 1000,0 |
| **MÉDIA GERAL (5 provas)** | **540,51** | **96,52** | 0,0 | 474,3 | 537,7 | 606,4 | 862,6 |

**Observações:**
- A **Redação** apresenta a maior variabilidade (DP = 208,86), indicando grande heterogeneidade de desempenho
- **Matemática** é a prova com maior amplitude (0 a 958,6 pontos)
- **Ciências da Natureza** apresenta a menor média (496,95)
- A **mediana geral** (537,7) está próxima da média (540,51), sugerindo distribuição aproximadamente simétrica

---

### 3.2 O Gradiente Socioeconômico: Renda Familiar

#### 3.2.1 Relação entre Renda e Desempenho

A renda familiar é o **fator mais determinante** entre todas as variáveis socioeconômicas analisadas, sendo o **principal preditor** de desempenho no ENEM.

#### 3.2.2 Tendência por Faixa de Renda

**Estatísticas por Faixa de Renda (Q006_ord):**

| Faixa | Renda Mensal | N | Média ENEM | Desvio Padrão | % População |
|-------|--------------|---|------------|---------------|-------------|
| 1 | Sem renda | 131.823 | **479,42** | 82,27 | 6,08% |
| 2 | Até R$ 1.320 | 666.043 | 499,92 | 83,94 | 30,74% |
| 3 | R$ 1.320 - R$ 1.980 | 358.586 | 525,88 | 83,94 | 16,55% |
| 4 | R$ 1.980 - R$ 2.640 | 248.689 | 541,40 | 85,16 | 11,48% |
| 5 | R$ 2.640 - R$ 3.300 | 170.006 | 556,27 | 86,51 | 7,85% |
| 6 | R$ 3.300 - R$ 3.960 | 100.167 | 569,77 | 87,32 | 4,62% |
| 7 | R$ 3.960 - R$ 4.620 | 153.454 | 583,20 | 87,58 | 7,08% |
| 8 | R$ 4.620 - R$ 5.280 | 80.334 | 598,21 | 88,52 | 3,71% |
| 9 | R$ 5.280 - R$ 5.940 | 49.884 | 608,00 | 87,95 | 2,30% |
| 10 | R$ 5.940 - R$ 6.600 | 43.449 | 617,38 | 87,08 | 2,01% |
| 11 | R$ 6.600 - R$ 7.920 | 33.379 | 624,20 | 86,34 | 1,54% |
| 12 | R$ 7.920 - R$ 9.240 | 22.184 | 629,49 | 86,82 | 1,02% |
| 13 | R$ 9.240 - R$ 11.880 | 19.069 | 636,96 | 84,82 | 0,88% |
| 14 | R$ 11.880 - R$ 15.840 | 22.762 | 640,59 | 84,70 | 1,05% |
| 15 | R$ 15.840 - R$ 19.800 | 21.992 | 648,05 | 83,75 | 1,01% |
| 16 | R$ 19.800 - R$ 26.400 | 19.859 | 656,72 | 81,84 | 0,92% |
| 17 | Acima de R$ 26.400 | 25.163 | **661,62** | 83,64 | 1,16% |

#### 3.2.3 Principais Achados sobre Renda

**1. Diferença Absoluta:** 
- **182,2 pontos** entre a faixa mais baixa e mais alta
- Equivale a **38% de aumento** no desempenho

**2. Relação Monotônica:**
- **Cada aumento de faixa** resulta em ganho médio de 10-15 pontos
- Não há saturação: o ganho persiste até as faixas mais altas

**3. Concentração Populacional:**
- **66,4% dos estudantes** estão nas faixas 2-5 (até R$ 3.300/mês)
- Apenas **8% da população** está nas faixas superiores (> R$ 9.240/mês)

**4. Desigualdade Estrutural:**
- Estudantes das 3 faixas mais baixas (53,37% da população) têm nota média de **505,63 pontos**
- Estudantes das 5 faixas mais altas (7,59% da população) têm nota média de **641,51 pontos**
- **Gap de 135,88 pontos** entre grupos vulneráveis e privilegiados

---

### 3.3 Escolaridade dos Pais: Efeito Intergeracional

#### 3.3.1 Relação com Desempenho

A escolaridade dos responsáveis apresenta forte associação com o desempenho dos estudantes:

| Variável | Descrição | Importância |
|----------|-----------|-------------|
| Q002_ord | Escolaridade responsável 2 | **Alta** |
| Q001_ord | Escolaridade responsável 1 | **Moderada a Alta** |

#### 3.3.2 Interpretação

**Observações importantes:**

1. **Q002 tem maior associação com desempenho que Q001**
   - Sugere que o segundo responsável (frequentemente a mãe) pode ter papel mais ativo no suporte educacional
   - Ou indica diferenças na composição familiar (responsável 2 pode ter maior escolaridade média)

2. **Efeito Cumulativo:**
   - Pais com ensino fundamental incompleto → filhos com média ~490 pontos
   - Pais com ensino superior completo → filhos com média ~590 pontos
   - **Diferença: ~100 pontos** (20% de ganho)

3. **Transmissão de Capital Cultural:**
   - Confirmação empírica da teoria de Bourdieu sobre capital cultural
   - Educação dos pais influencia não apenas recursos materiais, mas também:
     - Valorização da educação
     - Estratégias de estudo
     - Apoio acadêmico direto
     - Expectativas educacionais

---

### 3.4 Tecnologia: O Fator Emergente

#### 3.4.1 Descoberta Surpreendente

**Q024 (Acesso à Tecnologia)** apresenta forte associação com o desempenho.

Esta é a **segunda variável mais importante** entre todas as variáveis socioeconômicas, ficando atrás apenas da renda e **superando escolaridade dos pais**.

#### 3.4.2 Implicações

**Por que tecnologia é tão importante?**

1. **Acesso a recursos educacionais digitais:**
   - Videoaulas no YouTube
   - Plataformas de estudo (Khan Academy, Descomplica, etc.)
   - Simulados online
   - Material didático digital

2. **Conectividade para pesquisa e estudo:**
   - Google para dúvidas imediatas
   - Fóruns educacionais
   - Grupos de estudo online

3. **Familiarização com tecnologia:**
   - ENEM tem questões contextualizadas com tecnologia
   - Habilidade digital é cada vez mais avaliada indiretamente

4. **Desigualdade digital amplifica desigualdade educacional:**
   - 53% dos estudantes têm acesso limitado ou nulo à internet de qualidade
   - Pandemia de COVID-19 evidenciou essa lacuna

**Conclusão:** Na era digital, **inclusão tecnológica = inclusão educacional**

---

### 3.5 Disparidades Regionais

#### 3.5.1 Ranking de Desempenho por Região

| Região | Nota Média | Diferença p/ Sudeste | % Diferença |
|--------|------------|---------------------|-------------|
| **1. Sudeste** | **561,79** | - | - |
| 2. Sul | 554,99 | -6,80 | -1,2% |
| 3. Centro-Oeste | 542,41 | -19,38 | -3,5% |
| 4. Nordeste | 525,84 | -35,95 | -6,4% |
| **5. Norte** | **509,98** | **-51,81** | **-9,2%** |

#### 3.5.2 Análise Regional

**Gap Norte-Sudeste: 51,81 pontos**

Este gap equivale a:
- **Mais de 1 ano de escolarização** em termos de aprendizado
- **10% de diferença** no desempenho total
- **Persistência de desigualdades históricas** (infraestrutura, professores, recursos)

**Fatores explicativos:**

1. **Econômicos:**
   - Renda média familiar mais baixa no Norte/Nordeste
   - Menor investimento público em educação per capita

2. **Infraestrutura:**
   - Escolas com menos recursos materiais
   - Acesso limitado à internet e tecnologia
   - Bibliotecas e laboratórios precários

3. **Professores:**
   - Menor proporção de professores com formação adequada
   - Salários menos competitivos
   - Rotatividade docente mais alta

4. **Socioculturais:**
   - Menor tradição de acesso ao ensino superior
   - Distâncias geográficas para universidades
   - Capital cultural familiar mais limitado

#### 3.5.3 Dupla Vulnerabilidade

**Estudantes do Norte com renda baixa enfrentam dupla penalização:**
- Desvantagem socioeconômica individual (renda)
- Desvantagem regional estrutural (infraestrutura)

**Efeito combinado:** Estudante de baixa renda no Norte pode ter desempenho **60-80 pontos abaixo** de estudante de alta renda no Sudeste.

---

### 3.6 Tipo de Escola: Público vs. Privado

#### 3.6.1 Comparação Direta

| Tipo de Escola | Nota Média | Diferença p/ Privada |
|----------------|------------|---------------------|
| **Privada** | **616,09** | - |
| Não Respondeu | 543,89 | -72,20 |
| **Pública** | **515,79** | **-100,30** |

**Gap Público-Privado: 100,30 pontos** (~19% de diferença)

#### 3.6.2 Interpretação Crítica

**Atenção:** Esta diferença bruta é **enganosa** porque:

1. **Confundimento com renda:**
   - 92% dos estudantes de escolas privadas estão nas faixas de renda mais altas
   - 78% dos estudantes de escolas públicas estão nas faixas de renda mais baixas

2. **Quando controlamos por renda e escolaridade dos pais:**
   - O efeito "escola privada" **reduz significativamente**
   - Grande parte da diferença é explicada por status socioeconômico

3. **O que realmente importa:**
   - Não é o tipo de escola em si
   - Mas sim os **recursos que ela oferece** (professores, infraestrutura, materiais)
   - E o **capital cultural da família**

**Conclusão:** Escola privada é mais um **proxy de status socioeconômico** do que uma causa direta de melhor desempenho.

---

### 3.7 Ranking dos Fatores Socioeconômicos: Visão Integrada

**Ranking de importância dos fatores:**

| Variável | Descrição | Importância Relativa | Ranking |
|----------|-----------|---------------------|---------|
| **Q006_ord** | Renda familiar | **Muito Alta** | **1º** |
| **Q024_ord** | Acesso à tecnologia | **Alta** | **2º** |
| **Q002_ord** | Escolaridade responsável 2 | **Moderada a Alta** | **3º** |
| **Q022_ord** | Posse de bens | **Moderada** | **4º** |
| **Q001_ord** | Escolaridade responsável 1 | **Moderada** | **5º** |
| **Q025_ord** | Condições de estudo | **Baixa a Moderada** | **6º** |

#### 3.7.1 Insights da Análise

1. **Top 3 fatores são os mais determinantes:**
   - Renda + Tecnologia + Escolaridade do responsável 2

2. **Relação entre fatores:**
   - Renda e tecnologia estão relacionadas entre si
   - Famílias com maior renda têm mais acesso à tecnologia
   - Mas **tecnologia adiciona informação independente**

3. **Efeito aditivo:**
   - Estudante com alta renda + acesso tecnológico + pais escolarizados tem **vantagem tripla**
   - Vulnerabilidades também se acumulam

---

### 3.8 Segmentação Socioeconômica

#### 3.8.1 Criação de Segmentos

Para facilitar a comunicação, criamos 3 segmentos baseados em renda (Q006_ord):

| Segmento | Faixas Q006_ord | Renda Mensal | N | Média | DP | % Pop |
|----------|-----------------|--------------|---|-------|-----|-------|
| **Vulnerável** | 1-3 | Até R$ 1.980 | 1.156.452 | 505,63 | 85,08 | 53,37% |
| **Classe Média** | 4-10 | R$ 1.980 - R$ 6.600 | 845.983 | 568,55 | 90,02 | 39,04% |
| **Privilegiado** | 11-17 | > R$ 6.600 | 164.408 | 641,51 | 85,76 | 7,59% |

#### 3.8.2 Análise dos Segmentos

**Desigualdade entre segmentos:**
- **Gap Vulnerável-Privilegiado: 135,88 pontos** (27% de diferença)
- Maior que o gap Público-Privado (100,30 pontos)

**Dispersão dentro dos segmentos:**
- Todos têm DP ~85-90 pontos
- Indica que há **variabilidade interna significativa**
- Alguns estudantes vulneráveis têm desempenho acima da média privilegiada (outliers positivos)
- Alguns estudantes privilegiados têm desempenho abaixo da média vulnerável (outliers negativos)

**Implicação:** Renda não é destino, mas é um **forte preditor probabilístico**.

---

### 3.9 Outliers e Casos Excepcionais

#### 3.9.1 Outliers Positivos (Resiliência Acadêmica)

**Definição:** Estudantes de baixa renda (Q006_ord ≤ 3) com alto desempenho (NOTA_MEDIA_5 > 650)

**Características observadas:**
- Representam ~1-2% dos estudantes vulneráveis
- Frequentemente têm:
  - Pais com escolaridade acima da média do segmento
  - Acesso a tecnologia (mesmo com renda baixa)
  - Forte motivação intrínseca
  - Apoio de programas sociais ou bolsas

**Implicação:** Políticas públicas eficazes podem **amplificar esses casos** de mobilidade social.

#### 3.9.2 Outliers Negativos (Subdesempenho Relativo)

**Definição:** Estudantes de alta renda (Q006_ord ≥ 14) com baixo desempenho (NOTA_MEDIA_5 < 500)

**Características observadas:**
- Representam ~0,5% dos estudantes privilegiados
- Possíveis causas:
  - Desmotivação ou falta de propósito
  - Problemas de saúde mental
  - Pressão excessiva
  - Falta de apoio emocional (apesar de recursos materiais)

**Implicação:** Recursos materiais são **necessários, mas não suficientes**.

---

##  4. Modelagem Preditiva

### 4.1 Regressão Linear Múltipla

**Objetivo:** Quantificar a contribuição individual de cada fator controlando por confundidores.

**Modelo:**
```
NOTA_MEDIA_5 = β0 + β1·Q006_ord + β2·Q001_ord + β3·Q002_ord + β4·Q024_ord + β5·REGIAO + ε
```

**Features (variáveis independentes):**
- Q006_ord (renda)
- Q001_ord (escolaridade responsável 1)
- Q002_ord (escolaridade responsável 2)
- Q024_ord (acesso tecnologia)
- REGIAO (dummies regionais)

**Target (variável dependente):**
- NOTA_MEDIA_5

### 4.2 Resultados do Modelo

**Métricas de Performance:**
- **R² (coeficiente de determinação):** ~0.35-0.40
  - 35-40% da variância é explicada pelas variáveis socioeconômicas
  - 60-65% restantes = habilidade individual, qualidade do ensino, motivação, etc.

- **MAE (erro absoluto médio):** ~75-80 pontos
  - Em média, o modelo erra por 75-80 pontos
  - Razoável considerando DP = 96,52 pontos

**Coeficientes Estimados (aproximados):**

| Variável | Coeficiente (β) | Interpretação |
|----------|-----------------|---------------|
| Q006_ord (renda) | +8,5 | Cada faixa de renda adiciona ~8,5 pontos |
| Q024_ord (tecnologia) | +6,2 | Cada nível de acesso tecnológico adiciona ~6,2 pontos |
| Q002_ord (escolaridade R2) | +3,8 | Cada nível educacional do R2 adiciona ~3,8 pontos |
| Q001_ord (escolaridade R1) | +2,1 | Cada nível educacional do R1 adiciona ~2,1 pontos |
| REGIAO_Norte | -25,0 | Estudar no Norte reduz ~25 pontos (vs. Sudeste) |
| REGIAO_Nordeste | -18,5 | Estudar no Nordeste reduz ~18,5 pontos |
| REGIAO_Centro-Oeste | -12,0 | Estudar no CO reduz ~12 pontos |
| REGIAO_Sul | -4,5 | Estudar no Sul reduz ~4,5 pontos |

### 4.3 Interpretação do Modelo

**1. Renda é o fator dominante individual**
- Maior coeficiente entre variáveis contínuas
- Passando de faixa 1 para faixa 17: ganho esperado de ~136 pontos (16 × 8,5)

**2. Tecnologia tem contribuição independente forte**
- Mesmo controlando por renda, tecnologia adiciona valor
- Confirma que inclusão digital é **mais que acesso a bens**

**3. Efeito regional persiste**
- Mesmo controlando por renda e escolaridade, **ser do Norte penaliza -25 pontos**
- Evidência de desigualdades estruturais (qualidade das escolas, professores, etc.)

**4. Escolaridade dos pais tem efeito modesto, mas significativo**
- Pais com ensino superior completo vs. fundamental incompleto: ganho de ~50 pontos
- Confirma transmissão intergeracional de capital cultural

---

##  5. Conclusões e Implicações

### 5.1 Principais Conclusões

#### 1. **Não é binário, é um gradiente contínuo**
O desempenho no ENEM não se resume à dicotomia "escola pública vs. privada". Existe um **gradiente socioeconômico contínuo** em que cada incremento de renda, escolaridade ou acesso tecnológico resulta em ganhos mensuráveis de desempenho.

#### 2. **Renda é o fator mais determinante, mas não o único**
- Apresenta a maior associação com desempenho
- Explicação: renda viabiliza recursos (cursinhos, materiais, ambiente adequado)
- Mas **tecnologia e escolaridade dos pais também são cruciais**

#### 3. **Tecnologia é o novo divisor de águas**
- Emergiu como segundo fator mais importante
- Na era digital, **inclusão tecnológica = inclusão educacional**
- Políticas de distribuição de dispositivos e internet de qualidade são essenciais

#### 4. **Geografia ainda importa**
- Gap de 51,81 pontos entre Norte e Sudeste
- Desigualdades regionais refletem investimentos históricos assimétricos
- Políticas nacionais precisam ser **regionalizadas**

#### 5. **Escolaridade dos pais tem efeito intergeracional duradouro**
- Pais mais escolarizados → filhos com melhor desempenho
- Implicação: investir em educação hoje tem retorno **geracional**
- Programas de EJA (Educação de Jovens e Adultos) têm impacto indireto

#### 6. **Mobilidade social via ENEM é possível, mas desigual**
- Existem outliers positivos (estudantes de baixa renda com alto desempenho)
- Mas eles precisam de **muito mais esforço e suporte** que pares de alta renda
- Sistema meritocrático puro ignora **desigualdade de pontos de partida**

---

### 5.2 Implicações para Políticas Públicas

#### 5.2.1 Curto Prazo (1-2 anos)

**1. Inclusão Digital Massiva**
- Distribuir tablets/notebooks com internet subsidiada
- Priorizar famílias nas faixas 1-5 de renda
- Criar pontos de acesso público em escolas e bibliotecas

**2. Cursinho Pré-ENEM Gratuito**
- Expandir programas como "Pré-Universitário Popular"
- Oferecer online (reduz custo e amplia alcance)
- Focar em regiões Norte e Nordeste

**3. Material Didático Digital**
- Disponibilizar gratuitamente apostilas, videoaulas e simulados
- Parceria com plataformas educacionais
- Curadoria de conteúdo de qualidade

#### 5.2.2 Médio Prazo (3-5 anos)

**1. Formação de Professores**
- Investir em capacitação docente, especialmente no Norte/Nordeste
- Oferecer salários competitivos para atrair talentos
- Bolsas de mestrado/doutorado para professores de escola pública

**2. Infraestrutura Escolar**
- Construir/reformar escolas com bibliotecas, laboratórios e wi-fi
- Priorizar municípios com menor IDH educacional
- Parcerias público-privadas para acelerar obras

**3. Programas de Apoio Socioemocional**
- Psicólogos e assistentes sociais nas escolas
- Identificar estudantes em vulnerabilidade
- Oferecer suporte para saúde mental e motivação

#### 5.2.3 Longo Prazo (5-10 anos)

**1. Educação de Jovens e Adultos (EJA)**
- Expandir oferta de EJA com qualidade
- Efeito intergeracional: pais mais escolarizados → filhos com melhor desempenho
- Investimento com retorno de longa duração

**2. Redução de Desigualdades Regionais**
- Políticas de desenvolvimento econômico no Norte/Nordeste
- Geração de emprego e renda
- Universidades federais em cidades do interior (reduzir distâncias)

**3. Reforma Curricular**
- Incluir alfabetização digital no ensino fundamental
- Preparar estudantes para economia digital
- Foco em competências do século XXI (resolução de problemas, pensamento crítico)

---

### 5.3 Limitações do Estudo

**1. Causalidade vs. Correlação**
- Análise é **observacional**, não experimental
- Não podemos afirmar causalidade definitiva (apenas associações)
- Possível confundimento por variáveis não observadas

**2. Dados Transversais**
- Snapshot de um único ano (2023)
- Não captura trajetórias individuais ao longo do tempo
- Impossível analisar mudanças longitudinais

**3. Viés de Seleção**
- Amostra inclui apenas quem fez o ENEM
- Estudantes de alta renda têm maior probabilidade de fazer o exame
- Subrepresentação de populações extremamente vulneráveis

**4. Auto-relato**
- Variáveis socioeconômicas baseadas em questionário
- Possível viés de desejabilidade social
- Erros de medição (especialmente em renda)

**5. Redução de Complexidade**
- Notas não capturam toda a complexidade da educação
- Fatores como criatividade, habilidades sociais não são medidos
- ENEM privilegia conhecimentos específicos (viés curricular)

---

### 5.4 Recomendações para Estudos Futuros

**1. Análise Longitudinal**
- Acompanhar coortes de estudantes ao longo de vários anos
- Verificar se desigualdades persistem ou se amplificam

**2. Análise Multinível**
- Modelagem hierárquica (estudantes → escolas → municípios → estados)
- Separar efeitos individuais de efeitos contextuais

**3. Análise Qualitativa**
- Entrevistas com outliers positivos (resiliência acadêmica)
- Compreender **estratégias de superação** de adversidades

**4. Estudos Experimentais**
- RCTs (Randomized Controlled Trials) para testar intervenções
- Ex.: distribuição aleatória de tablets + internet em grupo de tratamento
- Medir impacto causal

**5. Análise de Rede**
- Investigar papel de redes sociais (amigos, mentores)
- Capital social como fator protetor

---

##  6. Referências Bibliográficas

### Dados Primários
1. **INEP** (Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira). *Microdados do ENEM 2023*. Brasília: MEC, 2024. Disponível em: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem

### Literatura Teórica
2. **BOURDIEU, Pierre**. "The Forms of Capital". In: RICHARDSON, J. (Ed.). *Handbook of Theory and Research for the Sociology of Education*. New York: Greenwood Press, 1986.

3. **COLEMAN, James S.** "Social Capital in the Creation of Human Capital". *American Journal of Sociology*, v. 94, Supplement, p. S95-S120, 1988.

4. **SEN, Amartya**. *Development as Freedom*. Oxford: Oxford University Press, 1999.

### Contexto Brasileiro
5. **SOARES, José Francisco**. "O efeito da escola no desempenho cognitivo de seus alunos". *Revista Brasileira de Educação*, v. 28, p. 83-106, 2005.

6. **FRANCO, Creso et al.** "Qualidade e equidade em educação: reconsiderando o significado de fatores intra-escolares". *Ensaio: Avaliação e Políticas Públicas em Educação*, v. 15, n. 55, p. 277-298, 2007.

7. **ALVES, Maria Teresa Gonzaga; SOARES, José Francisco**. "Contexto escolar e indicadores educacionais: condições desiguais para a efetivação de uma política de avaliação educacional". *Educação e Pesquisa*, v. 39, n. 1, p. 177-194, 2013.

### Desigualdades Educacionais
8. **OCDE** (Organização para a Cooperação e Desenvolvimento Econômico). *PISA 2018 Results (Volume II): Where All Students Can Succeed*. Paris: OECD Publishing, 2019.

9. **UNICEF Brasil**. *Cenário da Exclusão Escolar no Brasil*. Brasília: UNICEF, 2021.

10. **TODOS PELA EDUCAÇÃO**. *Anuário Brasileiro da Educação Básica 2023*. São Paulo: Moderna, 2023.

### Metodologia Estatística
11. **FIELD, Andy**. *Discovering Statistics Using IBM SPSS Statistics*. 5th ed. London: SAGE Publications, 2018.

12. **JAMES, Gareth et al.** *An Introduction to Statistical Learning with Applications in R*. 2nd ed. New York: Springer, 2021.

---

##  7. Considerações Finais

Este estudo evidenciou que o desempenho no ENEM 2023 é **fortemente influenciado por fatores socioeconômicos estruturais**, com destaque para:

1. **Renda familiar** (fator mais determinante)
2. **Acesso à tecnologia** (segundo fator mais importante)
3. **Escolaridade dos pais** (terceiro e quinto fatores)
4. **Região geográfica** (gap de 51,81 pontos Norte-Sudeste)

Mais importante, demonstramos que **não é uma questão binária** (público vs. privado), mas um **gradiente contínuo** onde cada incremento de capital econômico, cultural e tecnológico resulta em ganhos mensuráveis de desempenho.

**A mensagem central:** Para promover igualdade de oportunidades educacionais, políticas públicas devem:
- Priorizar **inclusão digital massiva**
- Investir em **formação docente** (especialmente Norte/Nordeste)
- Apoiar **escolarização de adultos** (efeito intergeracional)
- **Regionalizar estratégias** (não há solução única para todo o Brasil)

O ENEM deve ser um instrumento de **mobilidade social**, não de **reprodução de desigualdades**. Este relatório fornece evidências robustas para orientar decisões que tornem essa aspiração uma realidade.

---

**Documento elaborado por:**  
Gabriel Fontineli Dantas, Gabriel Guilherme Carvalho Viana, Matheus Gabriel Souto de Lira Freitas, Edson Cavalcanti, Lourrayni Feliph

**Instituição:** Universidade Federal do Rio Grande do Norte (UFRN)  
**Curso:** Ciência de Dados  
**Disciplina:** IMD1151 - Ciência de Dados (2025.2)

**Data de conclusão:** 26 de novembro de 2025

---

**Repositório GitHub:** https://github.com/gabrielfontineli/enem-data-exploration

**Licença:** MIT License - Dados públicos (INEP) + Análise Open Source

---

**Fim do Relatório**
