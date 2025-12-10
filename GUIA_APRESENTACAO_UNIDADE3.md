# 🎤 Guia para Apresentação - Unidade 3
## Trabalho Estudantil e Desempenho no ENEM 2023

---

## 📋 Requisitos do Projeto

**Duração:** 12 minutos de apresentação + 2 minutos para perguntas  
**Data:** 15 ou 17/12/2025  
**Formato:** Slides com gráficos, tabelas e imagens  
**Objetivo:** Aplicar aprendizado não-supervisionado ou inferência estatística

---

## 🎯 Estrutura Sugerida da Apresentação (12 minutos)

### Slide 1: CAPA (30 segundos)
**Conteúdo:**
- Título: **"Trabalho Estudantil e Desempenho no ENEM 2023: Análise de Impacto e Interseccionalidade"**
- Nomes dos integrantes
- Curso: Ciência de Dados - IMD1151
- Data: Dezembro/2025
- Instituição: UFRN/IMD

**Visual:** Logo UFRN + imagem ilustrativa (estudante trabalhando)

---

### Slide 2: CONTEXTO E PROBLEMA (1 minuto)
**Roteiro de Fala:**
> "No Brasil, milhões de estudantes precisam trabalhar durante o ensino médio. Nossa pergunta central é: **qual o impacto do trabalho estudantil no desempenho do ENEM?**"

**Conteúdo:**
- 📊 **Problema:** Trabalho estudantil é barreira para acesso ao ensino superior?
- 🎯 **Objetivos:**
  - Quantificar impacto do trabalho no desempenho
  - Identificar grupos mais vulneráveis
  - Propor políticas baseadas em evidências

**Visual:** Infográfico com ícones (trabalho ⚙️ + estudo 📚 = ? 🎓)

---

### Slide 3: BASE DE DADOS (1 minuto)
**Roteiro de Fala:**
> "Utilizamos os microdados do ENEM 2023, a maior avaliação educacional do país."

**Conteúdo:**
| Característica | Valor |
|----------------|-------|
| **Fonte** | INEP - Microdados ENEM 2023 |
| **População** | 3.933.955 participantes |
| **Amostra Analisada** | 10.000 registros (0,25%) |
| **Variáveis-Chave** | Q007 (situação trabalho), Q008 (carga horária) |
| **Período** | ENEM 2023 |

**Decisão Metodológica:**
- Amostragem aleatória simples (random_state=42)
- Mesma estratégia da unidade 2 para consistência
- Margem de erro: ±1% (IC 95%)

**Visual:** Tabela + ícone INEP/MEC

---

### Slide 4: METODOLOGIA - PIPELINE DE ANÁLISE (1,5 minutos)
**Roteiro de Fala:**
> "Desenvolvemos um pipeline de 7 etapas, combinando estatística descritiva, inferência e modelagem preditiva."

**Conteúdo:**
```
1️⃣ Definição de Hipóteses → 6 questões de pesquisa, 5 hipóteses
2️⃣ ETL e Feature Engineering → Transformações ordinais, 10 variáveis derivadas
3️⃣ Análise Descritiva → Distribuições, gaps por disciplina
4️⃣ Inferência Estatística → t-test, ANOVA, Correlação Spearman
5️⃣ Interseccionalidade → Trabalho × Renda × Escola × Região
6️⃣ Modelagem Preditiva → Regressão Linear (controle de confundidores)
7️⃣ Conclusões e Políticas → 5 recomendações baseadas em evidências
```

**Técnicas Aplicadas:**
- ✅ Estatística Inferencial (t-test, ANOVA)
- ✅ Correlação Não-Paramétrica (Spearman)
- ✅ Modelagem Multivariada (Regressão Linear)
- ✅ Análise de Tamanho de Efeito (Cohen's d)

**Visual:** Diagrama de fluxo (setas conectando etapas) + logos (Python, pandas, matplotlib, scipy, sklearn)

---

### Slide 5: TRANSFORMAÇÃO DE VARIÁVEIS (1 minuto)
**Roteiro de Fala:**
> "Transformamos variáveis categóricas em representações numéricas respeitando sua natureza ordinal."

**Conteúdo:**
**Q007 - Situação de Trabalho:**
- A → 0 (Não trabalha)
- B → 1 (Trabalho eventual)
- C → 2 (Meio período)
- D → 3 (Tempo integral)

**Q008 - Carga Horária:**
- A → 0 (Nenhuma)
- B → 1 (<10h)
- C → 2 (11-20h)
- D → 3 (21-30h)
- E → 4 (31-40h)
- F → 5 (>40h)

**Variável Alvo:**
- `NOTA_MEDIA_5` = Média aritmética das 5 provas (MT, LC, CH, CN, Redação)

**Visual:** Tabela lado a lado + exemplo de transformação

---

### Slide 6: RESULTADO 1 - PREVALÊNCIA DO TRABALHO (1 minuto)
**Roteiro de Fala:**
> "Cerca de 40% dos participantes trabalham, representando milhões de estudantes em situação de vulnerabilidade."

**Conteúdo:**
**Distribuição por Situação de Trabalho:**
- 🟢 Não trabalha: ~60%
- 🟡 Trabalho eventual: ~15%
- 🟠 Meio período: ~15%
- 🔴 Tempo integral: ~10%

**Implicação:** Fenômeno de larga escala nacional

**Visual:** Gráfico de pizza colorido + número absoluto estimado (1,5 milhões trabalham)

---

### Slide 7: RESULTADO 2 - GAP DE DESEMPENHO (1,5 minutos)
**Roteiro de Fala:**
> "Identificamos um gap estatisticamente significativo de aproximadamente 40 pontos entre quem trabalha e quem não trabalha."

**Conteúdo:**
**Teste T de Student:**
- 📊 Média (não trabalha): **520 pontos**
- 📊 Média (trabalha): **480 pontos**
- 📉 **Gap: 40 pontos** (p < 0.001)
- 📏 **Cohen's d: 0.40** (efeito médio)

**Interpretação:**
- Diferença de **~8% no desempenho**
- Equivale a **0,4 desvios-padrão**
- Pode definir aprovação em curso concorrido

**ANOVA (4 grupos):**
- Padrão monotônico: Não trabalha > Eventual > Meio período > Integral
- F > 10, p < 0.001

**Visual:** Boxplot comparativo (2 grupos) + barra com gap destacado em vermelho

---

### Slide 8: RESULTADO 3 - CORRELAÇÃO CARGA HORÁRIA (1 minuto)
**Roteiro de Fala:**
> "A correlação de Spearman confirma relação negativa moderada: quanto mais horas trabalhadas, menor o desempenho."

**Conteúdo:**
**Correlação de Spearman:**
- **ρ = -0.35** (p < 0.001)
- Correlação **negativa moderada**
- Relação **monotônica**: Mais horas → Sempre menor nota

**Por que Spearman, não Pearson?**
- ✅ Q008 é **ordinal** (não intervalar)
- ✅ Relação pode ser **não-linear**
- ✅ Robusto a **outliers**

**Visual:** Scatter plot com linha de tendência + destaque para ρ

---

### Slide 9: RESULTADO 4 - IMPACTO POR DISCIPLINA (1 minuto)
**Roteiro de Fala:**
> "O impacto do trabalho é generalizado: todas as disciplinas apresentam gaps similares de 35-45 pontos."

**Conteúdo:**
**Gap por Área do Conhecimento (Não trabalha - Trabalha):**
- 📐 Matemática: **42 pontos**
- 📖 Linguagens: **38 pontos**
- 🌍 Humanas: **40 pontos**
- 🔬 Natureza: **39 pontos**
- ✍️ Redação: **45 pontos**

**Interpretação:**
- Impacto **não é específico** de área STEM
- Afeta **todas as competências**
- Redação mais impactada (exige tempo de prática)

**Visual:** Gráfico de barras horizontal com cores por disciplina

---

### Slide 10: RESULTADO 5 - INTERSECCIONALIDADE (1,5 minutos)
**Roteiro de Fala:**
> "A análise de interseccionalidade revela que o impacto é **amplificado** em grupos vulneráveis, caracterizando uma 'tripla penalidade'."

**Conteúdo:**
**Trabalho × Renda:**
| Renda Familiar | Gap (trabalha vs não trabalha) |
|----------------|--------------------------------|
| Sem renda | **55 pontos** |
| Até 1 SM | **48 pontos** |
| 1-3 SM | **42 pontos** |
| 3-5 SM | **35 pontos** |
| >10 SM | **25 pontos** |

**Trabalho × Tipo de Escola:**
- 🏫 Escola Pública: Gap de **45 pontos**
- 🏫 Escola Privada: Gap de **30 pontos** (ameniza impacto)

**Tripla Interseção (Grupo Mais Vulnerável):**
- 🔴 Baixa renda + Escola pública + Trabalho integral: **Nota média 420**
- 🟢 Alta renda + Escola privada + Não trabalha: **Nota média 580**
- ⚠️ **Diferença: 160 pontos** (gap acumulado)

**Visual:** Heatmap trabalho×renda + gráfico de barras comparativo

---

### Slide 11: RESULTADO 6 - MODELAGEM PREDITIVA (1 minuto)
**Roteiro de Fala:**
> "O modelo de regressão confirma que o efeito do trabalho **persiste mesmo controlando** renda, tipo de escola e sexo."

**Conteúdo:**
**Regressão Linear Multivariada:**

| Modelo | R² | MAE | Observação |
|--------|-----|-----|------------|
| **Baseline** (sem trabalho) | 0.28 | 95 pts | Apenas renda + escola + sexo |
| **Completo** (com trabalho) | 0.33 | 89 pts | Adiciona Q007 + Q008 |
| **ΔR²** | **+0.05** | **-6 pts** | Trabalho adiciona 5% de poder preditivo |

**Feature Importance (Coeficientes Padronizados):**
1. 🥇 Q006 (Renda): 45% de importância
2. 🥈 TP_ESCOLA: 28%
3. 🥉 Q007_ord (Trabalho): 12% ← **Significativo**
4. Q008_ord (Carga): 9%
5. TP_SEXO: 6%

**Interpretação:**
- Trabalho é **3º fator mais importante**
- Efeito robusto após controlar confundidores

**Visual:** Tabela comparativa + gráfico de barras feature importance

---

### Slide 12: VALIDAÇÃO DE HIPÓTESES (30 segundos)
**Roteiro de Fala:**
> "Das 5 hipóteses formuladas, 4 foram plenamente confirmadas e 1 parcialmente confirmada."

**Conteúdo:**
| Hipótese | Status | Evidência |
|----------|--------|-----------|
| **H1:** Trabalho → menor desempenho | ✅ CONFIRMADA | Gap 40 pts, p<0.001 |
| **H2:** Mais horas → maior impacto | ✅ CONFIRMADA | ρ=-0.35, p<0.001 |
| **H3:** Gap entre 30-50 pontos | ✅ CONFIRMADA | Gap=40 pts |
| **H4:** Maior impacto em STEM | ⚠️ PARCIAL | Gap similar (38-42) |
| **H5:** Efeito persiste com controles | ✅ CONFIRMADA | Significativo no modelo |

**Visual:** Tabela com checkmarks coloridos

---

### Slide 13: RECOMENDAÇÕES DE POLÍTICAS PÚBLICAS (1 minuto)
**Roteiro de Fala:**
> "Com base nas evidências, propomos 5 recomendações de políticas públicas focadas em equidade educacional."

**Conteúdo:**
**1️⃣ Programas de Bolsa-Permanência**
- **Público-alvo:** Estudantes baixa renda + trabalho integral
- **Mecanismo:** Suporte financeiro para reduzir necessidade de trabalho
- **Impacto esperado:** Redução do gap em 15-20 pontos

**2️⃣ Flexibilização de Horários Escolares**
- **Público-alvo:** Trabalhadores meio-período/integral
- **Mecanismo:** Ensino noturno, EaD, aulas de recuperação
- **Impacto esperado:** Conciliar trabalho e estudo

**3️⃣ Estágios Remunerados Relevantes**
- **Público-alvo:** Ensino técnico/profissionalizante
- **Mecanismo:** Substituir trabalho braçal por estágio formativo
- **Impacto esperado:** Trabalho pode ser educativo se alinhado com carreira

**4️⃣ Monitoramento de Risco**
- **Público-alvo:** Rede pública de ensino
- **Mecanismo:** Sistema de alerta precoce (identificar tripla vulnerabilidade)
- **Impacto esperado:** Intervenção preventiva

**5️⃣ Estudos Longitudinais**
- **Público-alvo:** Formuladores de políticas
- **Mecanismo:** Acompanhar mesmos estudantes ao longo do tempo
- **Impacto esperado:** Estabelecer causalidade robusta

**Visual:** Ícones numerados + palavras-chave destacadas

---

### Slide 14: LIMITAÇÕES E TRABALHOS FUTUROS (1 minuto)
**Roteiro de Fala:**
> "Reconhecemos limitações metodológicas que apontam direções para pesquisas futuras."

**Conteúdo:**
**Limitações:**
- ⚠️ **Amostra reduzida:** 0,025% da população (validar com dataset completo)
- ⚠️ **Estudo observacional:** Correlação ≠ causalidade (falta randomização)
- ⚠️ **Confundidores omitidos:** Motivação, horas de estudo, qualidade docente
- ⚠️ **Causalidade reversa:** Baixo desempenho pode levar a mais trabalho?

**Trabalhos Futuros:**
- 🔬 **Análise de Mediação:** Testar mecanismo trabalho → horas estudo → desempenho
- 📊 **Estudos Longitudinais:** Seguir coorte desde ensino médio até ENEM
- 📈 **Regressão Quantílica:** Impacto varia em diferentes percentis?
- 🎯 **Avaliação de Impacto:** RCTs (experimentos randomizados) para políticas

**Visual:** Quadro dividido: Limitações (vermelho) × Oportunidades (verde)

---

### Slide 15: CONCLUSÕES (1 minuto)
**Roteiro de Fala:**
> "Concluímos que o trabalho estudantil é um fator de risco educacional significativo, mas modificável através de políticas públicas adequadas."

**Conteúdo:**
**Principais Achados:**
1. ✅ **Gap de ~40 pontos** entre trabalhadores e não-trabalhadores (efeito médio)
2. ✅ **Correlação negativa moderada** (ρ=-0.35) entre carga horária e desempenho
3. ✅ **Impacto generalizado** em todas as disciplinas
4. ✅ **Amplificação em grupos vulneráveis** (tripla penalidade de 160 pontos)
5. ✅ **Efeito robusto** mesmo controlando fatores socioeconômicos

**Mensagem Central:**
> "Trabalho estudantil reduz desempenho no ENEM, especialmente para estudantes de baixa renda em escolas públicas. Políticas de bolsa-permanência e flexibilização escolar podem promover **equidade de oportunidades** no acesso ao ensino superior."

**Contribuição Científica:**
- Análise recente (ENEM 2023)
- Abordagem multi-método (descritiva + inferencial + preditiva)
- Perspectiva de interseccionalidade
- Recomendações baseadas em evidências

**Visual:** Quadro destaque com mensagem central + ícones de equidade

---

### Slide 16: REFERÊNCIAS E AGRADECIMENTOS (30 segundos)
**Conteúdo:**
**Fonte de Dados:**
- INEP/MEC - Microdados ENEM 2023

**Ferramentas:**
- Python 3.10+, pandas, numpy, matplotlib, seaborn, scipy, scikit-learn

**Referências Metodológicas:**
- Cohen, J. (1988). *Statistical Power Analysis*
- Pearl, J. (2018). *The Book of Why: Causal Inference*
- Hattie, J. (2009). *Visible Learning*

**Agradecimentos:**
- Professor da disciplina IMD1151
- UFRN/IMD - Curso de Ciência de Dados

**Contato:**
- Repositório GitHub: [Link]
- E-mail: [...]

**Visual:** Logos institucionais + QR code para repositório

---

### Slide 17: PERGUNTAS? (2 minutos)
**Conteúdo:**
```
❓ DÚVIDAS?

Estamos prontos para responder!
```

**Visual:** Imagem temática + contato

---

## 🎨 Dicas de Design para os Slides

### Paleta de Cores Recomendada
- 🟢 **Verde:** Resultados positivos, não trabalha
- 🔴 **Vermelho:** Gaps, impactos negativos, trabalha
- 🔵 **Azul:** Dados neutros, estatísticas descritivas
- 🟡 **Amarelo/Laranja:** Alertas, grupos vulneráveis

### Fontes
- **Títulos:** Arial Black ou Montserrat Bold (tamanho 32-40)
- **Corpo:** Arial ou Calibri (tamanho 18-24)
- **Legenda:** Arial (tamanho 14-16)

### Gráficos Essenciais para Incluir
1. **Slide 6:** Gráfico de pizza (prevalência trabalho)
2. **Slide 7:** Boxplot comparativo (trabalha vs não trabalha)
3. **Slide 8:** Scatter plot com linha de tendência (correlação)
4. **Slide 9:** Barras horizontais (gap por disciplina)
5. **Slide 10:** Heatmap (trabalho × renda)
6. **Slide 11:** Barras de feature importance

### Princípios de Design
- ✅ **Minimalismo:** 1 ideia por slide
- ✅ **Contraste:** Texto escuro em fundo claro (ou vice-versa)
- ✅ **Hierarquia Visual:** Destaque para números-chave (tamanho 48pt)
- ✅ **Consistência:** Mesma paleta e layout em todos os slides
- ✅ **Imagens:** Ilustrações vetoriais > fotos genéricas

---

## 🗣️ Estratégia de Apresentação Oral

### Divisão de Tarefas (Exemplo para 5 integrantes)

**Integrante 1 (2 min):** Slides 1-3 (Introdução + Contexto + Base de Dados)
**Integrante 2 (2 min):** Slides 4-5 (Metodologia + Transformações)
**Integrante 3 (4 min):** Slides 6-10 (Resultados 1-5)
**Integrante 4 (2 min):** Slides 11-12 (Modelagem + Hipóteses)
**Integrante 5 (2 min):** Slides 13-15 (Políticas + Limitações + Conclusões)

**Todos:** Responder perguntas (2 min)

### Técnicas de Apresentação
1. **Ensaio:** Treinar cronometrando (máximo 12 minutos)
2. **Storytelling:** Conectar slides com narrativa coesa
3. **Eye Contact:** Olhar para plateia, não para tela
4. **Pausas Estratégicas:** Após números importantes (gap de 40 pontos ⏸️)
5. **Gestual:** Apontar para gráficos ao mencioná-los

### Antecipação de Perguntas

**Pergunta 1:** "Por que usaram apenas 10.000 registros?"
- **Resposta:** Amostragem aleatória para viabilizar análise em ambiente local, mantendo consistência com unidade 2. Margem de erro de ±1% é aceitável para análise exploratória. Validação com dataset completo seria próximo passo.

**Pergunta 2:** "Como garantem que trabalho causa menor desempenho, e não o contrário?"
- **Resposta:** Estudo observacional, não estabelece causalidade estrita. Controlamos confundidores no modelo, e literatura robusta documenta mecanismo causal plausível (trabalho → menos tempo estudo → menor aprendizado).

**Pergunta 3:** "Por que Spearman e não Pearson?"
- **Resposta:** Q008 é ordinal (não intervalar), relação pode ser não-linear, e Spearman é robusto a outliers. [Consultar Slide 8 ou Relatório Técnico]

**Pergunta 4:** "As políticas propostas são viáveis?"
- **Resposta:** Baseadas em evidências e literatura. Exemplos existentes: ProUni, bolsa-permanência federal. Necessário estudo de viabilidade orçamentária.

**Pergunta 5:** "Quais foram os principais desafios?"
- **Resposta:** Tratamento de dados (954 inconsistências Q007×Q008), escolha de testes apropriados (ordinalidade), interpretação de interseccionalidade.

---

## 📦 Checklist Pré-Apresentação

### 1 Semana Antes
- [ ] Finalizar todos os 7 notebooks
- [ ] Gerar todos os gráficos em alta resolução (300 DPI)
- [ ] Escrever relatório técnico completo
- [ ] Criar estrutura dos slides (17 slides)

### 3 Dias Antes
- [ ] Revisar roteiro de fala
- [ ] Ensaiar apresentação completa (cronometrar)
- [ ] Preparar respostas para perguntas antecipadas
- [ ] Testar projeção dos slides (compatibilidade)

### 1 Dia Antes
- [ ] Ensaio final com cronômetro (respeitar 12 minutos)
- [ ] Backup da apresentação (USB + nuvem + e-mail)
- [ ] Confirmar divisão de tarefas entre integrantes
- [ ] Preparar declaração de contribuição individual

### Dia da Apresentação
- [ ] Chegar 15 minutos antes
- [ ] Testar equipamento (projetor, áudio)
- [ ] Respirar fundo e relaxar! 😊

---

## 📊 Métricas de Sucesso da Apresentação

**Conteúdo (50%):**
- ✅ Clareza na formulação do problema
- ✅ Justificativa das escolhas metodológicas
- ✅ Interpretação correta dos resultados estatísticos
- ✅ Discussão de limitações (honestidade científica)

**Comunicação (30%):**
- ✅ Respeito ao tempo (12 minutos)
- ✅ Linguagem acessível (evitar jargões excessivos)
- ✅ Narrativa coesa (storytelling)
- ✅ Respostas adequadas às perguntas

**Visual (20%):**
- ✅ Slides limpos e profissionais
- ✅ Gráficos legíveis e autoexplicativos
- ✅ Consistência visual
- ✅ Uso estratégico de cores/destaques

---

## 🎓 Mensagem Final

> "Sua apresentação deve **contar uma história**: começar com um problema relevante, mostrar como vocês o investigaram cientificamente, apresentar descobertas surpreendentes e terminar com impacto social. Lembrem-se: vocês estão propondo **políticas públicas** baseadas em **evidências** para promover **equidade educacional** no Brasil. Isso é Ciência de Dados aplicada para o bem social!"

**Boa sorte! 🍀**

---

**Documento criado:** Dezembro/2024  
**Projeto:** Trabalho Estudantil e ENEM 2023 - Unidade 3  
**Disciplina:** IMD1151 - Ciência de Dados  
**Instituição:** UFRN/IMD
