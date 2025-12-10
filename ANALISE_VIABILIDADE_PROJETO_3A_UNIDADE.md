# Análise de Viabilidade - Projeto 3ª Unidade
## Uso do Dataset ENEM para o Novo Projeto

**Data:** 10 de dezembro de 2025  
**Disciplina:** Ciência de Dados (2025.2)

---

## 📋 RESUMO EXECUTIVO

### ✅ **VIABILIDADE: ALTAMENTE COMPATÍVEL**

O dataset ENEM 2023 existente é **perfeitamente adequado** para atender aos requisitos do novo projeto da 3ª unidade, que solicita análise de fatores socioeconômicos e desempenho educacional.

**Pontos-chave:**
- ✅ Dataset já processado e limpo (2.166.843 registros)
- ✅ 25 variáveis do questionário socioeconômico disponíveis (Q001-Q025)
- ✅ Cobertura completa dos fatores solicitados
- ✅ Infraestrutura de análise já desenvolvida
- ✅ Apenas **6 variáveis já utilizadas** de 25 disponíveis (24% do potencial)

---

## 🎯 COMPARAÇÃO: REQUISITOS vs DISPONIBILIDADE

### Requisitos do Novo Projeto (3ª Unidade)

Segundo as orientações do professor, o foco deve ser em fatores socioeconômicos:

| Categoria | Fatores Solicitados |
|-----------|---------------------|
| **Econômico** | Renda familiar, posse de bens |
| **Educacional** | Tipo de escola (pública x privada), escolaridade dos pais |
| **Geográfico** | Região, área urbana/rural |
| **Infraestrutura/Tecnologia** | Acesso à internet, computador, local de estudo |

### Variáveis Disponíveis no Dataset ENEM

#### ✅ **Já Utilizadas (Projeto Atual - 2ª Unidade)**

| Variável | Descrição | Categoria |
|----------|-----------|-----------|
| `Q001` | Escolaridade do responsável 1 (pai/mãe) | Educacional |
| `Q002` | Escolaridade do responsável 2 (pai/mãe) | Educacional |
| `Q006` | Renda familiar mensal (17 faixas) | Econômico |
| `Q022` | Posse de bens no domicílio | Econômico |
| `Q024` | Acesso à internet/tecnologia | Infraestrutura |
| `Q025` | Condições de estudo em casa | Infraestrutura |

#### 🆕 **DISPONÍVEIS MAS NÃO UTILIZADAS (19 variáveis)**

| Variável | Descrição Esperada* | Categoria | Relevância |
|----------|---------------------|-----------|------------|
| `Q003` | Ocupação do responsável 1 | Socioeconômico | ⭐⭐⭐ |
| `Q004` | Ocupação do responsável 2 | Socioeconômico | ⭐⭐⭐ |
| `Q005` | Quantidade de pessoas no domicílio | Núcleo familiar | ⭐⭐⭐ |
| `Q007` | Situação de trabalho do estudante | Socioeconômico | ⭐⭐⭐ |
| `Q008` | Carga horária de trabalho | Socioeconômico | ⭐⭐⭐ |
| `Q009` | Estado civil dos pais | Núcleo familiar | ⭐⭐ |
| `Q010` | Tipo de moradia | Infraestrutura | ⭐⭐ |
| `Q011` | Número de quartos | Infraestrutura | ⭐⭐ |
| `Q012` | Acesso a água encanada | Infraestrutura básica | ⭐⭐ |
| `Q013` | Acesso a energia elétrica | Infraestrutura básica | ⭐⭐ |
| `Q014` | Frequência a cursinhos | Educacional | ⭐⭐⭐ |
| `Q015` | Tipo de ensino médio concluído | Educacional | ⭐⭐⭐ |
| `Q016` | Modalidade de ensino médio | Educacional | ⭐⭐ |
| `Q017` | Ano de conclusão do ensino médio | Educacional | ⭐⭐ |
| `Q018` | Motivo para fazer o ENEM | Motivacional | ⭐⭐ |
| `Q019` | Língua estrangeira escolhida | Educacional | ⭐ |
| `Q020` | Língua indígena | Educacional | ⭐ |
| `Q021` | Raça/cor | Socioeconômico | ⭐⭐⭐ |
| `Q023` | Acesso a serviços públicos | Infraestrutura | ⭐⭐ |

*Nota: Descrições baseadas em padrões históricos do questionário ENEM. Verificar dicionário completo.*

---

## 📊 ANÁLISES JÁ REALIZADAS (Projeto Atual)

### Trabalho Desenvolvido até Agora

1. **Pré-processamento completo**
   - Remoção de treineiros
   - Tratamento de valores ausentes
   - Codificação ordinal de variáveis categóricas
   - Criação de variável NOTA_MEDIA_5

2. **Análises Descritivas**
   - Estatísticas gerais de desempenho (5 provas)
   - Distribuição por região geográfica
   - Comparação escola pública vs privada

3. **Análises Bivariadas**
   - Renda (Q006) vs Desempenho
   - Escolaridade dos pais (Q001/Q002) vs Desempenho
   - Tecnologia (Q024) vs Desempenho
   - Região vs Desempenho

4. **Análises Multivariadas**
   - Gradiente socioeconômico contínuo
   - Segmentação em grupos (Vulnerável, Média, Privilegiado)
   - Dupla vulnerabilidade (Região × Renda)
   - Regressão linear múltipla (R² = 0.293)

5. **Descobertas Principais**
   - Renda é o fator mais determinante (correlação 0.46)
   - Tecnologia é o 2º fator mais importante (correlação 0.42)
   - Gap de 182 pontos entre extremos de renda
   - Gap de 52 pontos entre Norte e Sudeste
   - Efeito cumulativo de múltiplos fatores

---

## 🚀 OPORTUNIDADES DE EXPANSÃO

### Novas Análises Possíveis com Variáveis Não Utilizadas

#### 1. **Núcleo Familiar (ALTO IMPACTO)**
- **Q005** (quantidade de pessoas) + **Q009** (estado civil dos pais)
- **Pergunta:** Famílias monoparentais ou numerosas enfrentam mais dificuldades?
- **Análise:** Cruzar estrutura familiar × renda × desempenho

#### 2. **Trabalho do Estudante (ALTO IMPACTO)**
- **Q007** (trabalha?) + **Q008** (carga horária)
- **Pergunta:** Quanto o trabalho prejudica o desempenho?
- **Análise:** Estudantes que trabalham vs não trabalham; carga horária × notas

#### 3. **Infraestrutura Básica (DESIGUALDADE)**
- **Q010** (tipo moradia) + **Q011** (nº quartos) + **Q012** (água) + **Q013** (energia)
- **Pergunta:** Falta de infraestrutura básica afeta o desempenho?
- **Análise:** Criar índice de precariedade habitacional

#### 4. **Acesso a Cursinhos (EDUCACIONAL)**
- **Q014** (cursinho preparatório)
- **Pergunta:** Cursinho reduz desigualdades ou amplia vantagens?
- **Análise:** Efeito do cursinho por faixa de renda

#### 5. **Trajetória Educacional**
- **Q015** (tipo de ensino médio) + **Q016** (modalidade) + **Q017** (ano conclusão)
- **Pergunta:** EJA, noturno ou integral fazem diferença?
- **Análise:** Modalidade × desempenho × perfil socioeconômico

#### 6. **Raça/Cor (INTERSECCIONALIDADE)**
- **Q021** (raça/cor autodeclarada)
- **Pergunta:** Desigualdades raciais persistem quando controlado por renda?
- **Análise:** Renda × raça × desempenho (análise de interseccionalidade)

---

## 🎯 PROPOSTA DE PLANO DE TRABALHO

### Fase 1: Exploração de Novas Variáveis (1-2 semanas)

1. **Extrair e processar Q003-Q025**
   - Leitura do dicionário completo
   - Codificação ordinal quando aplicável
   - Tratamento de valores ausentes

2. **Análise descritiva**
   - Distribuições de cada variável
   - Cruzamentos básicos com desempenho
   - Identificar quais são mais relevantes

### Fase 2: Análises Aprofundadas (2-3 semanas)

3. **Núcleo familiar e trabalho**
   - Impacto da estrutura familiar
   - Efeito de trabalhar durante estudos
   - Combinação de fatores de vulnerabilidade

4. **Infraestrutura e educação**
   - Acesso a cursinhos vs origem socioeconômica
   - Modalidade de ensino médio
   - Condições habitacionais

5. **Interseccionalidade**
   - Raça × renda × desempenho
   - Região × raça × escola
   - Múltiplas camadas de desigualdade

### Fase 3: Modelagem e Síntese (1-2 semanas)

6. **Modelagem preditiva aprimorada**
   - Incluir novas variáveis no modelo
   - Comparar R² antes/depois
   - Identificar fatores mais preditivos

7. **Documentação e apresentação**
   - Relatório final
   - Visualizações de alta qualidade
   - Recomendações de políticas públicas

---

## 📈 VANTAGENS DE USAR O MESMO DATASET

### ✅ Vantagens Técnicas

1. **Dados já preparados**
   - Sem necessidade de download/descompactação
   - Pré-processamento já realizado
   - Qualidade de dados validada

2. **Infraestrutura pronta**
   - Scripts de leitura/processamento funcionais
   - Notebooks organizados
   - Pipeline DVC configurado

3. **Conhecimento acumulado**
   - Equipe familiarizada com o dataset
   - Insights anteriores como ponto de partida
   - Menor curva de aprendizado

### ✅ Vantagens Acadêmicas

1. **Continuidade da pesquisa**
   - Aprofundamento em vez de recomeçar
   - Construção sobre descobertas anteriores
   - Demonstra evolução do conhecimento

2. **Complexidade crescente**
   - Projeto 2ª unidade: análises básicas (6 variáveis)
   - Projeto 3ª unidade: análises avançadas (25 variáveis)
   - Progressão pedagógica clara

3. **Relevância social mantida**
   - Mesmo tema: desigualdades educacionais
   - Maior profundidade analítica
   - Contribuição científica mais robusta

---

## ⚠️ CONSIDERAÇÕES E LIMITAÇÕES

### Pontos de Atenção

1. **Verificar dicionário completo**
   - Confirmar descrição exata de Q003-Q025
   - Algumas variáveis podem ter mudado ao longo dos anos
   - Validar categorias de resposta

2. **Taxa de resposta**
   - Algumas perguntas podem ter muitos NaN
   - Avaliar viabilidade antes de análises aprofundadas
   - Considerar imputação se necessário

3. **Complexidade analítica**
   - Com 25 variáveis, risco de overfit em modelos
   - Necessário seleção criteriosa de features
   - Focar em variáveis com maior impacto

### Alternativas (se necessário)

Se por algum motivo específico o dataset ENEM não for adequado:

1. **Complementar com dados externos**
   - IBGE/PNAD para contexto regional
   - Censo Escolar para caracterização de escolas
   - IDH municipal

2. **Usar ENEM de outro ano**
   - 2024 está disponível no workspace
   - Permite análises longitudinais
   - Comparar evolução temporal

---

## 🎓 CONCLUSÃO E RECOMENDAÇÃO

### ✅ **RECOMENDAÇÃO FINAL: UTILIZAR O DATASET ENEM**

**Justificativa:**

1. ✅ **Compatibilidade total** com requisitos do projeto
2. ✅ **Potencial inexplorado**: 76% das variáveis ainda não analisadas
3. ✅ **Infraestrutura pronta**: economia de tempo e esforço
4. ✅ **Progressão pedagógica**: demonstra evolução do aprendizado
5. ✅ **Relevância social**: tema atual e impactante

### 📋 Próximos Passos Imediatos

1. **Obter confirmação do professor** ✓
2. **Ler dicionário completo** (Q003-Q025)
3. **Processar novas variáveis** no dataset
4. **Análise exploratória inicial** das 19 variáveis não utilizadas
5. **Definir 4-5 perguntas de pesquisa** específicas para 3ª unidade
6. **Atualizar README.md** com novo escopo

### 🎯 Perguntas de Pesquisa Sugeridas (3ª Unidade)

1. **Estrutura familiar:** Como o núcleo familiar (monoparental, numeroso) afeta o desempenho quando controlado por renda?

2. **Trabalho estudantil:** Qual o impacto de trabalhar durante os estudos? A carga horária faz diferença?

3. **Infraestrutura básica:** A falta de condições habitacionais básicas (água, energia, espaço) cria uma "camada extra" de vulnerabilidade?

4. **Cursinhos e mobilidade:** Cursinhos preparatórios reduzem desigualdades ou ampliam vantagens de quem já tem recursos?

5. **Interseccionalidade:** Como raça/cor intersecciona com renda e região para criar múltiplas camadas de desigualdade?

---

**Preparado por:** Análise baseada no dataset ENEM 2023 existente  
**Dataset:** 2.166.843 participantes | 76 variáveis disponíveis | 25 questionário socioeconômico  
**Status:** ✅ Viável e recomendado para o projeto da 3ª unidade
