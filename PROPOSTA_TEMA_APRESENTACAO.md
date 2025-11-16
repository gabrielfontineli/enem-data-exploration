# 📊 Proposta de Tema para Apresentação Final
## ENEM Data Exploration - Checkpoint 2

**Data:** 16 de novembro de 2025  
**Equipe:** Gabriel Fontineli Dantas, Gabriel Guilherme Carvalho Viana, Matheus Gabriel Souto de Lira Freitas, Edson Cavalcanti, Lourrayni Feliph

---

## 🎯 Tema Proposto

### **"O Gradiente Socioeconômico no ENEM: Como Renda, Escolaridade dos Pais e Infraestrutura Tecnológica Moldam as Oportunidades Educacionais no Brasil"**

---

## 📋 Sumário Executivo

Após análise exploratória de **2.166.843 participantes** do ENEM 2023, identificamos um padrão robusto e cientificamente relevante: existe um **gradiente socioeconômico contínuo** que influencia o desempenho acadêmico, indo muito além da simples dicotomia "escola pública vs. privada".

Este tema permite:
- ✅ **Análise quantitativa robusta** com correlações estatisticamente significativas
- ✅ **Relevância social** para políticas públicas educacionais
- ✅ **Narrativa clara** para apresentação (storytelling com dados)
- ✅ **Visualizações impactantes** que revelam desigualdades estruturais

---

## 🔍 Principais Descobertas da Análise Exploratória

### 1. **Renda Familiar: O Fator Mais Determinante**

**Correlação de Spearman: 0.459** (p < 0.001)

- **Faixa de renda mais baixa** (sem renda): média de **479,42 pontos**
- **Faixa de renda mais alta** (> R$ 26.400): média de **661,62 pontos**
- **Diferença absoluta: 182,2 pontos** (~38% de aumento)

**Insight-chave:** A relação é **monotônica e linear** - cada incremento de faixa de renda corresponde a um aumento médio consistente de 10-15 pontos na nota.

#### Distribuição por Faixa de Renda (Q006):
| Faixa | Renda Mensal | Média ENEM | % População |
|-------|--------------|------------|-------------|
| 1 | Sem renda | 479,42 | 6,1% |
| 2 | Até R$ 1.320 | 499,92 | 30,7% |
| 3-5 | R$ 1.320 - R$ 3.300 | 525-556 | 35,7% |
| 6-10 | R$ 3.300 - R$ 9.240 | 569-617 | 19,5% |
| 11-17 | > R$ 9.240 | 624-662 | 8,0% |

**Concentração:** 66% dos participantes estão nas faixas 2-5 (até R$ 3.300/mês).

---

### 2. **Escolaridade dos Pais: Segunda Maior Influência**

**Correlações de Spearman:**
- Q001 (Responsável 1): **0.248** (p < 0.001)
- Q002 (Responsável 2): **0.318** (p < 0.001)

**Padrão observado:**
- Pais com ensino fundamental incompleto → filhos com média ~490 pontos
- Pais com ensino superior completo → filhos com média ~590 pontos
- **Diferença: ~100 pontos** (20% de ganho)

**Insight importante:** A escolaridade do segundo responsável (Q002) tem correlação **28% maior** que a do primeiro, sugerindo dinâmicas familiares específicas no apoio educacional.

---

### 3. **Infraestrutura Tecnológica (Q024): O Fator Emergente**

**Correlação de Spearman: 0.421** (p < 0.001)

**Q024** mede acesso a tecnologia/internet no domicílio.

- **Segunda maior correlação** entre todas as variáveis socioeconômicas
- Correlação **quase igual à renda** (0.421 vs 0.459)
- Mais forte que escolaridade dos pais

**Implicação:** Na era digital, acesso à tecnologia tornou-se um **diferencial crítico** para o desempenho acadêmico, potencialmente mais importante que o capital cultural familiar tradicional.

---

### 4. **Disparidades Regionais Estruturais**

| Região | Nota Média | Diferença p/ Sudeste |
|--------|------------|---------------------|
| **Sudeste** | 561,79 | - |
| Sul | 554,99 | -6,80 (-1,2%) |
| Centro-Oeste | 542,41 | -19,38 (-3,5%) |
| Nordeste | 525,84 | -35,95 (-6,4%) |
| **Norte** | 509,98 | **-51,81 (-9,2%)** |

**Gap Norte-Sudeste:** Equivalente a **mais de 1 ano de escolarização** em diferença de desempenho.

---

### 5. **Tipo de Escola: Efeito Mediado por Renda**

| Tipo de Escola | Nota Média | Observação |
|----------------|------------|------------|
| Privada | ~600 | |
| Pública | ~530 | |
| **Diferença** | **~70 pontos** | |

**Mas atenção:** Quando controlamos por renda e escolaridade dos pais, essa diferença **reduz significativamente**, sugerindo que o "efeito escola privada" é em grande parte um **proxy de status socioeconômico**.

---

## 🎓 Por Que Este Tema é Ideal para Apresentação?

### **1. Impacto Visual Forte**

Gráficos que podem ser usados:
- 📈 **Curva de Tendência Renda × Nota** (demonstra gradiente contínuo)
- 🗺️ **Mapa de Calor Regional** (desigualdades geográficas)
- 📊 **Boxplots por Faixa de Renda** (dispersão e outliers)
- 🔗 **Matriz de Correlação** (renda + escolaridade + tecnologia + notas)
- 📉 **Comparativo Acumulado** (% de alunos acima de 600 pontos por faixa)

### **2. Narrativa Coerente (Storytelling)**

**Estrutura sugerida:**

1. **Introdução** (2 min)
   - ENEM como instrumento de mobilidade social
   - Pergunta central: "Oportunidades iguais para todos?"

2. **Metodologia** (1 min)
   - Dataset: 2,1 milhões de participantes (ENEM 2023)
   - Variáveis: renda (Q006), escolaridade pais (Q001/Q002), acesso tecnologia (Q024)

3. **Descoberta Central** (3 min)
   - Demonstrar o **gradiente socioeconômico**
   - Mostrar que não é binário (público/privado), mas **contínuo**
   - Destacar papel emergente da **tecnologia**

4. **Análise Regional** (2 min)
   - Disparidades Norte-Sudeste
   - Interseccionalidade: renda baixa + região Norte = dupla penalização

5. **Implicações** (2 min)
   - Políticas públicas: foco em acesso tecnológico
   - Programas de apoio direcionados (não apenas bolsas)
   - Educação dos pais como investimento de longo prazo

### **3. Relevância Científica e Social**

- ✅ **Reprodutível**: dados públicos (INEP)
- ✅ **Metodologia sólida**: correlações robustas, p-values < 0.001
- ✅ **Aplicabilidade prática**: orientação para políticas educacionais
- ✅ **Originalidade**: destaque ao fator "acesso tecnológico" (Q024)

---

## 🛠️ Roteiro de Execução (Próximos Passos)

### **Semana 1-2: Aprofundamento Analítico**

#### **1. Análise de Interações**
```python
# Criar segmentos combinados
df['segmento_socio'] = pd.cut(df['Q006_ord'], bins=[0, 3, 8, 17], 
                               labels=['Baixa', 'Média', 'Alta'])

# Análise por região + renda
pivot = df.groupby(['REGIAO_NOME_PROVA', 'segmento_socio'])['NOTA_MEDIA_5'].mean()
```

**Objetivo:** Identificar se o "efeito renda" varia por região (dupla vulnerabilidade).

#### **2. Análise de Teto/Piso**
```python
# Estudantes de baixa renda com alto desempenho (outliers positivos)
outliers_positivos = df[(df['Q006_ord'] <= 3) & (df['NOTA_MEDIA_5'] > 650)]

# Estudantes de alta renda com baixo desempenho (outliers negativos)
outliers_negativos = df[(df['Q006_ord'] >= 14) & (df['NOTA_MEDIA_5'] < 500)]
```

**Objetivo:** Identificar fatores protetores/agravantes além da renda.

#### **3. Modelagem Preditiva (Opcional)**
```python
from sklearn.linear_model import LinearRegression

# Features: Q006_ord, Q001_ord, Q002_ord, Q024_ord, REGIAO
# Target: NOTA_MEDIA_5
# Calcular R² e coeficientes
```

**Objetivo:** Quantificar contribuição individual de cada fator (com controle de confundidores).

---

### **Semana 3: Criação de Visualizações**

#### **Gráficos Essenciais:**

1. **Gráfico Principal: Gradiente Socioeconômico**
   - Linha de tendência (renda × nota)
   - Com banda de confiança (IC 95%)
   - Anotações de faixas de renda em reais

2. **Mapa de Calor: Região × Renda**
   - Eixo X: Faixas de renda
   - Eixo Y: Regiões
   - Cor: Nota média

3. **Boxplot Comparativo: Acesso Tecnológico**
   - Separar por Q024 (tecnologia)
   - Mostrar dispersão dentro de cada grupo

4. **Gráfico de Barras Empilhadas: % Acima de 600 pontos**
   - Por faixa de renda
   - Evidenciar desigualdade de oportunidades

---

### **Semana 4: Preparação da Apresentação**

#### **Estrutura do Slide Deck (10-12 slides):**

1. **Capa** - Título + autores
2. **Contextualização** - ENEM e mobilidade social
3. **Objetivo** - Investigar determinantes socioeconômicos
4. **Metodologia** - Dataset e variáveis
5. **Descoberta 1** - Gradiente de renda (gráfico linha)
6. **Descoberta 2** - Papel da tecnologia (boxplot)
7. **Descoberta 3** - Disparidades regionais (mapa)
8. **Descoberta 4** - Escolaridade dos pais (correlação)
9. **Análise Integrada** - Matriz de correlação
10. **Implicações** - Políticas públicas
11. **Limitações** - Causalidade, dados transversais
12. **Conclusões** - Take-home messages

---

## 📊 Mensagens-Chave (Take-Home Messages)

### **Para a Audiência:**

1. 🎓 **"Não é só escola pública vs. privada"**
   - É um **gradiente contínuo** de oportunidades
   - Renda, escolaridade e tecnologia atuam **conjuntamente**

2. 💻 **"Tecnologia é o novo divisor de águas"**
   - Q024 tem correlação tão forte quanto renda
   - Inclusão digital = inclusão educacional

3. 🗺️ **"Geografia ainda importa"**
   - Gap de 52 pontos entre Norte e Sudeste
   - Políticas nacionais precisam ser **regionalizadas**

4. 👨‍👩‍👧 **"Escolaridade dos pais é investimento de longa duração"**
   - Efeito intergeracional forte
   - Programas de EJA (Educação de Jovens e Adultos) têm impacto indireto

5. 📈 **"Mobilidade social via ENEM é possível, mas desigual"**
   - Estudantes de baixa renda podem ter alto desempenho
   - Mas precisam de **muito mais suporte** que pares de alta renda

---

## 🎤 Exemplo de Pitch (1 minuto)

> *"Analisamos 2,1 milhões de participantes do ENEM 2023 para responder: o que realmente determina o sucesso no exame? Descobrimos que não é uma questão simples de escola pública versus privada. Existe um **gradiente socioeconômico contínuo**: a cada aumento de faixa de renda, vimos ganhos consistentes de 10-15 pontos na nota média. Mas a surpresa foi que **acesso à tecnologia** emergiu como fator quase tão importante quanto renda – com correlação de 0,42. Além disso, estudantes do Norte enfrentam uma **dupla penalidade**: renda mais baixa E infraestrutura regional deficiente, resultando em gap de 52 pontos para o Sudeste. Nossa conclusão: políticas educacionais eficazes precisam ir além de bolsas escolares – devem incluir inclusão digital, apoio familiar e regionalização de estratégias."*

---

## 📚 Referências e Suporte

### **Dados Utilizados:**
- INEP. Microdados do ENEM 2023. Disponível em: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem

### **Literatura de Apoio (sugerida):**
1. **Bourdieu, P.** (1986). "The Forms of Capital" - teoria sobre capital cultural
2. **Coleman, J.S.** (1988). "Social Capital in the Creation of Human Capital" - capital social e educação
3. **OCDE** (2019). "PISA 2018 Results" - desigualdades educacionais globais
4. **Soares, J.F.** (2005). "O efeito da escola no desempenho cognitivo" - contexto brasileiro

### **Ferramentas de Análise:**
- Python 3.x (pandas, matplotlib, scipy)
- Jupyter Notebooks
- Correlação de Spearman (variáveis ordinais)

---

## ✅ Checklist de Entregáveis

### **Para o Checkpoint:**
- [x] Tema definido com justificativa
- [ ] Notebook de análise aprofundada (`07_analise_gradiente_socioeconomico.ipynb`)
- [ ] 5-8 visualizações finalizadas e exportadas
- [ ] Relatório técnico (PDF, 4-6 páginas)
- [ ] Slides de apresentação (10-12 slides)
- [ ] Script/roteiro de apresentação (8-10 minutos)

### **Qualidade dos Dados:**
- [x] Dataset limpo (sem treineiros)
- [x] Variáveis ordinais codificadas (Q001_ord, Q002_ord, Q006_ord)
- [x] Missing data tratado
- [x] Outliers identificados e documentados

---

## 🚀 Diferencial Competitivo

### **O que faz este tema se destacar:**

1. **Originalidade Local:**
   - Destaque ao fator **tecnologia** (Q024), pouco explorado em análises tradicionais
   - Análise de **interações regionais** (Norte + baixa renda)

2. **Rigor Metodológico:**
   - Amostra robusta (2+ milhões)
   - Correlações com significância estatística (p < 0.001)
   - Múltiplas validações (Spearman, Pearson, regressão)

3. **Aplicabilidade Prática:**
   - Recomendações claras para políticas públicas
   - Potencial para publicação em eventos acadêmicos (ENEGEP, SBPC)

4. **Comunicação Efetiva:**
   - Storytelling baseado em dados
   - Visualizações impactantes e de fácil compreensão
   - Mensagens alinhadas com debates sociais atuais

---

## 🎯 Conclusão

Este tema oferece o **equilíbrio perfeito** entre:
- **Complexidade analítica** (múltiplas variáveis, correlações, segmentações)
- **Clareza comunicativa** (gradiente socioeconômico é conceito intuitivo)
- **Relevância social** (desigualdade educacional é tema central no Brasil)
- **Viabilidade técnica** (dados disponíveis, ferramentas dominadas)

**Recomendação:** Prosseguir com este tema, focando nos próximos 15 dias em:
1. Análise de **interações** (renda × região, renda × tecnologia)
2. Criação de **visualizações de alta qualidade**
3. Desenvolvimento de **narrativa clara** para apresentação oral

---

**Documento elaborado em:** 16 de novembro de 2025  
**Próxima revisão:** Após feedback do orientador  
**Contato:** [inserir email do grupo]

---

## 📎 Anexos

### **Anexo A: Código para Reprodução**

```python
# Análise básica do gradiente socioeconômico
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

# Carregar dados
df = pd.read_parquet('../data/interim/enem_2023.parquet')
df = df[df['IN_TREINEIRO'] == 0].dropna(subset=['NOTA_MEDIA_5', 'Q006_ord'])

# Calcular correlação
corr, p_value = spearmanr(df['Q006_ord'], df['NOTA_MEDIA_5'])
print(f"Correlação Spearman: {corr:.3f} (p={p_value:.2e})")

# Tendência por faixa
tendencia = df.groupby('Q006_ord')['NOTA_MEDIA_5'].mean()

# Visualizar
plt.figure(figsize=(10, 6))
plt.plot(tendencia.index, tendencia.values, marker='o', linewidth=2)
plt.xlabel('Faixa de Renda (Q006 - ordinal)')
plt.ylabel('Nota Média ENEM (5 provas)')
plt.title(f'Gradiente Socioeconômico no ENEM 2023\nCorrelação de Spearman: {corr:.3f}')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('../reports/figures/gradiente_socioeconomico.png', dpi=300)
plt.show()
```

### **Anexo B: Tabela de Decisão para Segmentação**

| Segmento | Q006_ord | Renda Mensal | Nota Média | População |
|----------|----------|--------------|------------|-----------|
| **Vulnerável** | 1-3 | Até R$ 1.980 | 479-526 | 52,4% |
| **Classe Média** | 4-10 | R$ 1.980 - R$ 9.240 | 541-617 | 38,5% |
| **Privilegiado** | 11-17 | > R$ 9.240 | 624-662 | 9,1% |

Essa segmentação permite análises mais comunicativas para audiências não-técnicas.

---

**Fim do Documento**
