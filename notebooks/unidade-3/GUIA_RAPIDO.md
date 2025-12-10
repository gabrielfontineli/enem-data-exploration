# ⚡ Guia Rápido - Trabalho Estudantil no ENEM

## 🎯 O que vamos descobrir?

**Pergunta Principal:** Como trabalhar durante os estudos afeta o desempenho no ENEM?

---

## 📊 Dados

- **Dataset:** ENEM 2023
- **Tamanho:** 2.166.843 participantes
- **Variáveis principais:**
  - **Q007:** Situação de trabalho (não trabalha, eventualmente, meio período, integral)
  - **Q008:** Carga horária semanal (0h até mais de 40h)
  - **NOTA_MEDIA_5:** Média das 5 provas do ENEM

---

## 📁 Notebooks (7 no total)

### ✅ Prontos para executar:

1. **01_introducao_trabalho_estudantil.ipynb**
   - ⏱️ Tempo: 5 min
   - 📝 Contexto, objetivos, metodologia
   - 🎨 Configuração de visualizações

2. **02_preparacao_dados_trabalho.ipynb**
   - ⏱️ Tempo: 10 min (processamento pesado)
   - 📥 Extrai Q007 e Q008 do dataset original
   - 🔧 Cria 10+ variáveis derivadas
   - 💾 Salva: `enem_2023_trabalho_estudantil.parquet`

### 🔄 A criar/executar:

3. **03_analise_descritiva_trabalho.ipynb**
   - Distribuições e estatísticas
   - Perfil socioeconômico
   - Visualizações básicas

4. **04_trabalho_vs_desempenho.ipynb**
   - Comparação de notas
   - Testes estatísticos
   - Gap de desempenho

5. **05_interseccoes_trabalho.ipynb**
   - Trabalho × Renda
   - Trabalho × Escola
   - Trabalho × Região

6. **06_modelagem_preditiva_trabalho.ipynb**
   - Regressão linear múltipla
   - Importância das variáveis
   - Previsões

7. **07_conclusoes_recomendacoes.ipynb**
   - Síntese dos resultados
   - Políticas públicas
   - Limitações

---

## 🚀 Como Executar

### Opção 1: Todos os notebooks
```bash
cd notebooks/unidade-3
jupyter notebook
# Execute 01 → 02 → 03 → ... → 07
```

### Opção 2: Apenas análise (já tem os dados)
```bash
# Se já existe enem_2023_trabalho_estudantil.parquet
# Pode pular o notebook 02 e ir direto para 03
```

---

## 📈 Resultados Esperados

### Hipóteses

| # | Hipótese | Resultado Esperado |
|---|----------|-------------------|
| H1 | Quem trabalha tem desempenho inferior | ✅ CONFIRMAR (gap ~40 pontos) |
| H2 | Mais horas = menos pontos | ✅ CONFIRMAR (linear) |
| H3 | Impacto maior em baixa renda | ✅ CONFIRMAR |
| H4 | Período integral muito prejudicial | ✅ CONFIRMAR (gap ~70 pontos) |
| H5 | Regiões pobres mais afetadas | ✅ CONFIRMAR |

### Números Importantes (Estimativas)

- **% que trabalha:** ~35-40%
- **Gap médio:** 30-50 pontos (trabalha vs. não trabalha)
- **Gap período integral:** 60-80 pontos
- **Correlação trabalho×nota:** -0.25 a -0.35 (moderada negativa)

---

## 🎨 Visualizações Geradas

### Principais Gráficos

1. **Distribuição por situação de trabalho** (barras)
2. **Boxplot notas por grupo** (trabalha vs. não)
3. **Scatter plot carga horária × nota** (tendência)
4. **Heatmap intersecções** (trabalho × renda × escola)
5. **Coeficientes do modelo** (importância)
6. **Dashboard final** (síntese visual)

**Total:** ~20 visualizações de alta qualidade

---

## 💡 Insights-Chave

### O que vamos mostrar:

1. **Magnitude do problema:**
   - "Trabalhar período integral equivale a perder X meses de estudo"
   
2. **Desigualdade amplificada:**
   - "Estudantes pobres que trabalham têm dupla desvantagem"
   
3. **Diferença regional:**
   - "Norte/Nordeste: impacto do trabalho é Y% maior"
   
4. **Tipo de escola:**
   - "Escola pública + trabalho = Z pontos a menos que privada"

---

## 🎯 Para o Relatório Final

### Estrutura Sugerida

1. **Introdução** (2 páginas)
   - Contexto do trabalho estudantil no Brasil
   - Perguntas de pesquisa

2. **Metodologia** (1 página)
   - Dataset ENEM 2023
   - Variáveis e tratamento de dados

3. **Resultados** (5-7 páginas)
   - Análise descritiva
   - Testes estatísticos
   - Interações e subgrupos
   - Modelagem preditiva

4. **Discussão** (2 páginas)
   - Interpretação dos achados
   - Comparação com literatura

5. **Conclusões e Recomendações** (2 páginas)
   - Síntese
   - Políticas públicas
   - Limitações

**Total:** 12-15 páginas + anexos

---

## 📊 Tabelas para o Relatório

### Essenciais:

1. **Tabela 1:** Estatísticas descritivas por grupo
2. **Tabela 2:** Testes de diferença de médias
3. **Tabela 3:** Correlações (Spearman)
4. **Tabela 4:** Coeficientes do modelo de regressão
5. **Tabela 5:** Gap de desempenho por subgrupo

---

## ✅ Checklist de Entrega

- [ ] Executar notebooks 01-07
- [ ] Gerar todas as visualizações
- [ ] Salvar tabelas em CSV
- [ ] Criar apresentação (slides)
- [ ] Escrever relatório final
- [ ] Revisar código
- [ ] Documentar descobertas
- [ ] Preparar discussão oral

---

## 🔗 Arquivos Importantes

### Dados
```
data/processed/
├── enem_2023_trabalho_estudantil.parquet      # Dataset completo
└── enem_2023_trabalho_estudantil_sample.csv   # Amostra 10k
```

### Figuras
```
reports/figures/unidade-3/
├── 00_paleta_cores.png
├── 01_distribuicao_trabalho.png
├── ...
└── 10_dashboard_final.png
```

### Notebooks
```
notebooks/unidade-3/
├── 01_introducao_trabalho_estudantil.ipynb    ✅
├── 02_preparacao_dados_trabalho.ipynb         ✅
├── 03_analise_descritiva_trabalho.ipynb       🔄
├── 04_trabalho_vs_desempenho.ipynb            🔄
├── 05_interseccoes_trabalho.ipynb             🔄
├── 06_modelagem_preditiva_trabalho.ipynb      🔄
├── 07_conclusoes_recomendacoes.ipynb          🔄
└── README.md                                  ✅
```

---

## 🆘 Problemas Comuns

### 1. Erro de memória
**Solução:** Use amostragem (`df.sample(100000)`) nos notebooks 03-07

### 2. Dados não encontrados
**Solução:** Execute notebook 02 primeiro para gerar o parquet

### 3. Visualizações não aparecem
**Solução:** Adicione `%matplotlib inline` no início

### 4. Demora muito
**Solução:** Amostra menor ou use dados já processados

---

## 💪 Dicas de Produtividade

1. **Execute notebook 02 apenas uma vez** (gera dados processados)
2. **Use a amostra CSV** para testes rápidos
3. **Salve figuras em alta resolução** (dpi=300)
4. **Documente insights** em células markdown
5. **Versionamento:** commit após cada notebook completo

---

## 📞 Ajuda

Caso tenha dúvidas:
1. Veja o README.md completo
2. Consulte os comentários nos notebooks
3. Verifique a documentação do pandas/matplotlib
4. Revise o projeto da 2ª unidade (estrutura similar)

---

**Boa análise! 🚀📊**

*Última atualização: 10/12/2025*
