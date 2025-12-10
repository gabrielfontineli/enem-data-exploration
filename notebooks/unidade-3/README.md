# 📚 Trabalho Estudantil e Desempenho no ENEM
## Análise Aprofundada - 3ª Unidade

**Disciplina:** Ciência de Dados (2025.2)  
**Dataset:** ENEM 2023 - 2.166.843 participantes  
**Tema:** Impacto do Trabalho Durante os Estudos no Desempenho Educacional

---

## 🎯 Objetivo Geral

Investigar **como o trabalho durante os estudos afeta o desempenho dos estudantes no ENEM**, analisando diferentes aspectos como carga horária, perfil socioeconômico, tipo de escola e região geográfica.

---

## 📊 Perguntas de Pesquisa

1. **Estudantes que trabalham têm desempenho inferior aos que não trabalham?**
2. **A carga horária de trabalho impacta diretamente as notas?**
3. **O efeito do trabalho varia conforme a faixa de renda familiar?**
4. **Trabalhar prejudica mais estudantes de escolas públicas ou privadas?**
5. **Existe diferença regional no impacto do trabalho estudantil?**
6. **Como o trabalho se relaciona com outros fatores socioeconômicos?**

---

## 📁 Estrutura dos Notebooks

### 1️⃣ `01_introducao_trabalho_estudantil.ipynb`
**Status:** ✅ Criado

**Conteúdo:**
- Contexto e justificativa da pesquisa
- Objetivos e perguntas de pesquisa
- Metodologia de análise
- Definição das variáveis
- Hipóteses iniciais
- Configuração do ambiente
- Paleta de cores para visualizações

---

### 2️⃣ `02_preparacao_dados_trabalho.ipynb`
**Status:** ✅ Criado

**Conteúdo:**
- Carregamento do dataset ENEM 2023
- Extração de variáveis Q007 (situação de trabalho) e Q008 (carga horária)
- Integração com dados já processados
- Tratamento de valores ausentes
- Criação de variáveis derivadas:
  - `Q007_label` e `Q008_label` (descritivas)
  - `Q007_ord` e `Q008_ord` (ordinais)
  - `TRABALHA` (binária: sim/não)
  - `CATEGORIA_TRABALHO` (simplificada)
  - `CARGA_HORARIA_NUM` (numérica)
- Validação de consistência
- Salvamento do dataset processado

**Output:** `data/processed/enem_2023_trabalho_estudantil.parquet`

---

### 3️⃣ `03_analise_descritiva_trabalho.ipynb`
**Status:** 🔄 A criar

**Conteúdo Previsto:**
- **Distribuições:**
  - Estudantes por situação de trabalho
  - Estudantes por carga horária
  - Perfil demográfico dos que trabalham
  
- **Estatísticas Descritivas:**
  - Média, mediana, desvio padrão por grupo
  - Notas por disciplina (MT, LC, CH, CN, Redação)
  - Comparação: trabalha × não trabalha
  
- **Perfil Socioeconômico:**
  - Renda familiar dos que trabalham
  - Escolaridade dos pais
  - Tipo de escola
  - Região geográfica
  - Acesso à tecnologia

- **Visualizações:**
  - Histogramas de distribuição
  - Boxplots de notas por grupo
  - Gráficos de barras comparativos
  - Pirâmides demográficas

---

### 4️⃣ `04_trabalho_vs_desempenho.ipynb`
**Status:** 🔄 A criar

**Conteúdo Previsto:**
- **Análise Bivariada:**
  - Trabalha vs. Nota Média
  - Carga horária vs. Nota Média
  - Situação de trabalho vs. Notas por disciplina
  
- **Testes Estatísticos:**
  - Teste t: trabalha vs. não trabalha
  - ANOVA: diferenças entre grupos de carga horária
  - Teste de Kruskal-Wallis (não paramétrico)
  - Cálculo de tamanho de efeito (Cohen's d)
  
- **Gap de Desempenho:**
  - Diferença absoluta de notas
  - Diferença percentual
  - Gap por disciplina
  - Gap por faixa de renda
  
- **Correlações:**
  - Spearman: Q007_ord × NOTA_MEDIA_5
  - Spearman: Q008_ord × NOTA_MEDIA_5
  - Correlação com outras variáveis socioeconômicas

- **Visualizações:**
  - Gráficos de violino
  - Scatter plots com linha de tendência
  - Heatmaps de correlação
  - Gráficos de barras com intervalo de confiança

---

### 5️⃣ `05_interseccoes_trabalho.ipynb`
**Status:** 🔄 A criar

**Conteúdo Previsto:**
- **Trabalho × Renda:**
  - Desempenho por faixa de renda e situação de trabalho
  - Teste de interação estatística
  - Verificar se trabalho afeta mais pobres ou ricos
  
- **Trabalho × Tipo de Escola:**
  - Pública vs. Privada
  - Efeito do trabalho em cada tipo
  - Gap escola pública × privada entre os que trabalham
  
- **Trabalho × Região:**
  - Norte, Nordeste, Centro-Oeste, Sudeste, Sul
  - Desigualdades regionais
  - Infraestrutura e trabalho estudantil
  
- **Trabalho × Escolaridade dos Pais:**
  - Impacto do trabalho por nível educacional familiar
  
- **Análise de Interações:**
  - Modelos com termos de interação
  - Efeitos condicionais
  - Moderadores do impacto do trabalho

- **Visualizações:**
  - Gráficos de barras agrupadas
  - Facet plots
  - Interaction plots
  - Heatmaps de subgrupos

---

### 6️⃣ `06_modelagem_preditiva_trabalho.ipynb`
**Status:** 🔄 A criar

**Conteúdo Previsto:**
- **Regressão Linear Múltipla:**
  - Modelo base: NOTA_MEDIA_5 ~ variáveis socioeconômicas
  - Modelo com trabalho: + Q007_ord + Q008_ord
  - Comparação de R²
  - Análise de coeficientes
  
- **Importância das Variáveis:**
  - Coeficientes padronizados
  - Permutation importance
  - SHAP values (opcional)
  
- **Modelos Segmentados:**
  - Modelo para escola pública
  - Modelo para escola privada
  - Modelo por região
  - Modelo por faixa de renda
  
- **Avaliação:**
  - R² (coeficiente de determinação)
  - RMSE (erro quadrático médio)
  - MAE (erro absoluto médio)
  - Validação cruzada
  
- **Previsões:**
  - Cenários hipotéticos
  - "E se ninguém trabalhasse?"
  - Potencial ganho de desempenho

- **Visualizações:**
  - Gráficos de coeficientes
  - Residual plots
  - Predicted vs. Actual
  - Feature importance

---

### 7️⃣ `07_conclusoes_recomendacoes.ipynb`
**Status:** 🔄 A criar

**Conteúdo Previsto:**
- **Síntese dos Resultados:**
  - Resposta às 6 perguntas de pesquisa
  - Principais descobertas
  - Validação/rejeição de hipóteses
  
- **Magnitude do Impacto:**
  - Gap médio de desempenho
  - Efeito por carga horária
  - Grupos mais afetados
  
- **Implicações:**
  - Desigualdade educacional
  - Ciclo de pobreza
  - Acesso ao ensino superior
  
- **Recomendações de Políticas Públicas:**
  - Programas de bolsas/auxílio estudantil
  - Flexibilização de horários escolares
  - Apoio a estudantes trabalhadores
  - Regulamentação de carga horária
  
- **Limitações do Estudo:**
  - Causalidade vs. correlação
  - Variáveis omitidas
  - Viés de seleção
  
- **Pesquisas Futuras:**
  - Análise longitudinal
  - Dados qualitativos
  - Outros outcomes (saúde mental, evasão)
  - Experimentos naturais

- **Visualizações:**
  - Dashboards síntese
  - Infográficos
  - Gráficos executivos

---

## 📦 Outputs Gerados

### Dados
- `enem_2023_trabalho_estudantil.parquet` - Dataset completo processado
- `enem_2023_trabalho_estudantil_sample.csv` - Amostra de 10k registros

### Figuras
Todas as visualizações são salvas em `reports/figures/unidade-3/`:
- `00_paleta_cores.png`
- `01_distribuicao_trabalho.png`
- `02_desempenho_por_grupo.png`
- `03_gap_notas.png`
- `04_intersecoes_renda.png`
- `05_intersecoes_escola.png`
- `06_intersecoes_regiao.png`
- `07_correlacoes.png`
- `08_coeficientes_modelo.png`
- `09_importancia_variaveis.png`
- `10_dashboard_final.png`

### Tabelas
- Estatísticas descritivas (CSV)
- Testes estatísticos (CSV)
- Coeficientes de regressão (CSV)
- Tabelas cruzadas (CSV)

---

## 🔧 Dependências

```bash
# Instalar dependências
pip install pandas numpy matplotlib seaborn plotly scipy scikit-learn pyarrow
```

### Versões Recomendadas
- Python: 3.11+
- pandas: 2.0+
- numpy: 1.24+
- matplotlib: 3.7+
- seaborn: 0.12+
- plotly: 5.14+
- scipy: 1.10+
- scikit-learn: 1.3+

---

## 🚀 Como Executar

1. **Preparação:**
   ```bash
   cd notebooks/unidade-3
   jupyter notebook
   ```

2. **Ordem de execução:**
   - Execute os notebooks na ordem numérica (01 → 07)
   - O notebook 02 pode demorar (~5-10 min para processar 2M+ registros)
   - Notebooks 03-07 são mais rápidos (~2-3 min cada)

3. **Requisitos:**
   - Memória RAM: mínimo 8GB (recomendado 16GB)
   - Espaço em disco: ~2GB para dados + figuras
   - Tempo total: ~1h para executar todos os notebooks

---

## 📊 Principais Descobertas (Esperadas)

### Hipóteses a Testar

**H1:** Estudantes que trabalham têm desempenho médio inferior aos que não trabalham.  
**Resultado esperado:** ✅ CONFIRMADA - Gap estimado de 30-50 pontos

**H2:** Quanto maior a carga horária, menor o desempenho.  
**Resultado esperado:** ✅ CONFIRMADA - Relação linear negativa

**H3:** O impacto do trabalho é maior para estudantes de baixa renda.  
**Resultado esperado:** ✅ CONFIRMADA - Efeito moderado por renda

**H4:** Trabalhar período integral reduz significativamente as notas.  
**Resultado esperado:** ✅ CONFIRMADA - Gap de 60-80 pontos vs. não trabalha

**H5:** O efeito é mais pronunciado em regiões com menor infraestrutura.  
**Resultado esperado:** ✅ CONFIRMADA - Norte e Nordeste mais afetados

---

## 🎓 Contexto Acadêmico

### Relevância
Este estudo contribui para:
- **Sociologia da Educação:** Desigualdades no acesso à educação de qualidade
- **Economia da Educação:** Custo de oportunidade do trabalho estudantil
- **Políticas Públicas:** Evidências para programas de apoio estudantil

### Metodologia
- **Tipo:** Estudo observacional transversal
- **População:** Participantes do ENEM 2023
- **Amostra:** 2.166.843 indivíduos
- **Análise:** Quantitativa, descritiva e inferencial

---

## 📚 Referências

1. INEP (2023). *Microdados do ENEM 2023*.
2. IBGE (2023). *PNAD Contínua - Educação*.
3. OIT (2023). *Trabalho Infantil e Adolescente no Brasil*.
4. Cardoso, A. & Verner, D. (2007). *Youth attitudes toward jobs and work in Brazil*.
5. Emilio, D. et al. (2012). *O trabalho dos jovens brasileiros: uma análise a partir do ENEM*.

---

## 👥 Autor

**Projeto:** 3ª Unidade - Ciência de Dados  
**Instituição:** IMD/UFRN  
**Semestre:** 2025.2  
**Data:** Dezembro de 2025

---

## 📝 Licença

Este projeto é parte de um trabalho acadêmico. Os dados utilizados são públicos (INEP/MEC).

---

**Última atualização:** 10 de dezembro de 2025
