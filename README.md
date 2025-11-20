# 🤖 Previsor de Impacto da IA no Mercado de Trabalho

Aplicativo web interativo desenvolvido com **Streamlit** e **Machine Learning** para prever o impacto da Inteligência Artificial em diferentes profissões, analisando características como indústria, educação, salário, experiência e trabalho remoto.

---

## 👥 Integrantes

| Nome | RM |
|------|-----|
| **Luis Fernando de Oliveira Salgado** | 561401 |
| **Igor Paixão Sarak** | 563726 |
| **Lucca Phelipe Masini** | 564121 |

---

## 🎯 Objetivo do Projeto

Desenvolver e treinar um modelo de **Machine Learning** capaz de analisar as características de uma profissão (Indústria, Salário, Educação, Experiência) para prever seu nível de impacto pela IA.

---

## 📖 Jornada do Projeto: Da Análise aos Resultados Interpretáveis

### 1. 📊 Análise Exploratória de Dados (EDA)

O projeto começou com uma **análise exploratória profunda** do dataset `ai_job_trends_dataset.csv`, contendo 30.000 registros de profissões. Durante a EDA, identificamos padrões cruciais:

#### Descobertas Principais:

- **Distribuição Balanceada**: O dataset possui três classes de impacto (Low, Moderate, High) com distribuição equilibrada (~10.000 amostras cada)
- **Correlações Identificadas**: Análise de correlação revelou relações entre salário, experiência e risco de automação
- **Padrões por Indústria**: Visualizações mostraram que certas indústrias (IT, Manufacturing) apresentam perfis distintos de automação
- **Insight Crítico**: Descobrimos que **Indústria** e **Nível de Educação** são os fatores mais determinantes, enquanto salário e experiência têm menor impacto relativo

> 📓 **Notebook Jupyter**: Todo o processo de EDA, visualizações e descobertas está documentado em `GS_ML_Impacto_da_IA_no_Mercado_de_Trabalho.ipynb`

### 2. 🧠 Aprendizado Não Supervisionado (Clustering)

Antes de construir o modelo preditivo, utilizamos **KMeans Clustering** para validar se os padrões identificados na EDA poderiam ser "descobertos" automaticamente pelo algoritmo:

- **Método do Cotovelo**: Confirmou que **K=3** é o número ideal de clusters
- **Validação Cruzada**: Os clusters formados pelo KMeans corresponderam fortemente às três categorias de impacto da IA
- **Interpretação**: Cada cluster revelou um perfil distinto de profissões (alto/baixo risco de automação)

Esta etapa validou que os padrões observados na EDA não eram aleatórios, mas sim padrões reais e identificáveis pelos algoritmos de ML.

### 3. 🎯 Modelagem: Construção do Modelo Preditivo

Com base nas descobertas da EDA e validação do clustering, construímos um **pipeline de Machine Learning** completo:

#### Features Selecionadas (baseadas na EDA):
- **Industry** (Categórica) - Identificada como fator crítico
- **Required Education** (Categórica) - Identificada como fator crítico  
- **Median Salary (USD)** (Numérica) - Fator secundário
- **Experience Required (Years)** (Numérica) - Fator secundário
- **Remote Work Ratio (%)** (Numérica) - Fator complementar

#### Pipeline de Pré-processamento:
- **Features Categóricas**: `OneHotEncoder` para transformar em variáveis numéricas
- **Features Numéricas**: `StandardScaler` para normalização
- **Modelo**: `RandomForestClassifier` (100 árvores, random_state=42)

#### Divisão dos Dados:
- **Treinamento**: 24.000 amostras (80%)
- **Validação**: 6.000 amostras (20%)
- **Estratificação**: Mantida a proporção das classes

### 4. ✅ Validação e Performance

O modelo foi rigorosamente validado no conjunto de teste:

#### Métricas de Performance:
- **Acurácia**: **96%** 
- **Precisão Média**: Alta performance em todas as classes
- **Recall**: Boa capacidade de identificar corretamente cada nível de impacto
- **Matriz de Confusão**: Visualização mostra poucos erros de classificação

#### Feature Importance (Validação das Descobertas da EDA):
A análise de importância das features confirmou as descobertas da EDA:
1. **Indústria** - Fator mais importante
2. **Nível de Educação** - Segundo fator mais importante
3. **Salário e Experiência** - Fatores secundários
4. **Trabalho Remoto** - Fator complementar

> ✅ **Validação**: O modelo não apenas aprendeu os padrões, mas confirmou que as hipóteses levantadas na EDA eram corretas.

### 5. 💾 Exportação e Implementação

O pipeline completo (pré-processamento + modelo) foi exportado como `ai_impact_model.joblib` usando `joblib`, permitindo:

- **Reutilização**: Carregar o modelo treinado sem retreinar
- **Consistência**: Garantir que novos dados passem pelo mesmo pré-processamento
- **Portabilidade**: Usar o modelo em diferentes ambientes (Colab → Streamlit)

### 6. 🎨 Aplicação Interativa: Transformando Resultados em Insights

A aplicação Streamlit foi desenvolvida para tornar os resultados do modelo **interpretáveis e acessíveis**:

#### Aba 1: Previsor Interativo
- **Input do Usuário**: Permite inserir características de uma profissão
- **Previsão em Tempo Real**: O modelo retorna o nível de impacto (Low/Moderate/High)
- **Nível de Confiança**: Gráfico de barras mostra a probabilidade para cada classe
- **Interpretação Visual**: Cores (🟢🟡🔴) facilitam a compreensão imediata

#### Aba 2: Validação do Modelo
- **Matriz de Confusão**: Visualização da performance do modelo
- **Métricas Detalhadas**: Acurácia, Precisão, Recall por classe
- **Feature Importance**: Gráfico mostrando quais fatores o modelo mais considera
- **Transparência**: Usuário entende como o modelo toma decisões

#### Aba 3: O Padrão nos Dados
- **Insights da EDA**: Apresenta os padrões descobertos durante a análise
- **Comparação Estatística**: Mostra diferenças entre profissões de alto e baixo risco
- **Validação de Intuição**: Permite ao usuário testar se consegue "desafiar" o modelo

### 7. 🔄 Fluxo Completo: Da Análise ao Resultado

```
Dataset (30k amostras)
    ↓
[EDA] → Descoberta de Padrões
    ↓
[Clustering] → Validação dos Padrões
    ↓
[Modelagem] → Treinamento do RandomForest
    ↓
[Validação] → 96% de Acurácia
    ↓
[Exportação] → Modelo .joblib
    ↓
[Aplicação Streamlit] → Interface Interativa
    ↓
[Usuário] → Resultado Interpretável (Low/Moderate/High + Confiança)
```

---

## 🚀 Como Usar

### Opção 1: Usando os scripts .bat (Recomendado para Windows)

1. **Primeira vez - Configurar ambiente:**
   ```bash
   setup.bat
   ```
   Este script irá:
   - Criar o ambiente virtual (venv)
   - Instalar todas as dependências com as versões corretas

2. **Executar o aplicativo:**
   ```bash
   run_app.bat
   ```
   Este script irá:
   - Ativar o ambiente virtual automaticamente
   - Iniciar o aplicativo Streamlit
   - Abrir automaticamente no navegador (geralmente em `http://localhost:8501`)

### Opção 2: Manualmente

1. **Criar e ativar o ambiente virtual:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Executar o aplicativo:**
   ```bash
   streamlit run app.py
   ```

---

## 📊 Interpretando os Resultados

### Níveis de Impacto:

- 🟢 **Low (Baixo)**: Profissão com menor probabilidade de automação pela IA. Geralmente associada a:
  - Indústrias que requerem interação humana complexa
  - Níveis de educação mais altos (Master's, PhD)
  - Tarefas criativas ou estratégicas

- 🟡 **Moderate (Moderado)**: Profissão com automação parcial esperada. Características:
  - Combinação de tarefas automatizáveis e não-automatizáveis
  - Necessidade de adaptação profissional

- 🔴 **High (Alto)**: Profissão com maior probabilidade de automação. Geralmente:
  - Tarefas repetitivas e padronizadas
  - Indústrias com processos altamente estruturados
  - Requisitos educacionais mais baixos

### Nível de Confiança:

O gráfico de barras mostra a **probabilidade** atribuída pelo modelo para cada classe. Quanto maior a barra, maior a confiança do modelo naquela previsão. Valores acima de 80% indicam alta confiança.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+** - Linguagem de programação
- **Streamlit** - Framework web para interface interativa
- **scikit-learn** - Biblioteca de Machine Learning
- **pandas** - Manipulação e análise de dados
- **numpy** - Operações numéricas
- **matplotlib & seaborn** - Visualização de dados
- **joblib** - Serialização de modelos
- **Jupyter Notebook** - Análise exploratória e desenvolvimento

---

## 📦 Dependências

Todas as dependências estão especificadas no arquivo `requirements.txt`:

- `streamlit>=1.28.0` - Framework web interativo
- `pandas>=2.0.0` - Manipulação de dados
- `scikit-learn==1.6.1` - Machine Learning (versão exata para compatibilidade)
- `joblib>=1.3.0` - Carregamento de modelos
- `numpy>=1.24.0` - Operações numéricas
- `matplotlib==3.9.0` - Visualização de dados
- `seaborn==0.13.2` - Visualizações estatísticas avançadas

---

## 📁 Estrutura do Projeto

```
ML/
├── app.py                    # Aplicativo principal Streamlit
├── requirements.txt          # Dependências do projeto
├── ai_impact_model.joblib    # Modelo treinado (RandomForest) - Git LFS
├── ai_job_trends_dataset.csv # Dataset utilizado para treinamento
├── GS_ML_Impacto_da_IA_no_Mercado_de_Trabalho.ipynb  # Notebook Jupyter com EDA e treinamento
├── setup.bat                 # Script de configuração (Windows)
├── run_app.bat              # Script de execução (Windows)
├── .gitattributes            # Configuração Git LFS para arquivos grandes
├── .gitignore               # Arquivos ignorados pelo Git
├── venv/                     # Ambiente virtual (criado automaticamente)
└── README.md                 # Documentação do projeto
```

> **Nota**: O arquivo `ai_impact_model.joblib` é gerenciado pelo **Git LFS** (Large File Storage) devido ao seu tamanho. Ao clonar o repositório, certifique-se de ter o Git LFS instalado. Se o arquivo não baixar automaticamente, execute: `git lfs pull`

---

## 🔧 Troubleshooting

### Erro: "streamlit não é reconhecido"
- Certifique-se de que o ambiente virtual está ativado
- Execute `setup.bat` novamente para reinstalar dependências

### Avisos de versão do scikit-learn
- O modelo foi treinado com scikit-learn 1.6.1
- O `requirements.txt` especifica a versão exata para evitar incompatibilidades
- Se ainda aparecerem avisos, verifique se está usando o venv correto

### Porta já em uso
- O Streamlit tenta usar a porta 8501 por padrão
- Se estiver ocupada, ele automaticamente tentará 8502, 8503, etc.

### Arquivo do modelo não encontrado
- Certifique-se de que o arquivo `ai_impact_model.joblib` está na raiz do projeto
- Verifique se o arquivo não foi corrompido ou movido
- Se você clonou o repositório, o arquivo pode estar no Git LFS. Execute: `git lfs pull`

### Problemas com Git LFS
- O arquivo do modelo é grande (160 MB) e usa Git LFS
- Para clonar o repositório com os arquivos LFS: `git clone` (Git LFS baixa automaticamente)
- Se o arquivo não baixar: `git lfs install` e depois `git lfs pull`
- Instale o Git LFS: https://git-lfs.github.com/

---

## ⚠️ Aviso Importante

Este modelo é uma **ferramenta de análise baseada em dados de 2024** e não representa uma previsão definitiva do futuro. Os resultados devem ser interpretados como **indicadores probabilísticos** e não como garantias absolutas.

O impacto da IA no mercado de trabalho é um fenômeno complexo e multifatorial que depende de diversos aspectos não capturados pelo modelo, incluindo:
- Mudanças tecnológicas futuras
- Políticas governamentais
- Adaptação das empresas e profissionais
- Fatores socioeconômicos globais

---

## 📚 Referências

- **Streamlit Documentation**: https://docs.streamlit.io/
- **scikit-learn Documentation**: https://scikit-learn.org/stable/
- **pandas Documentation**: https://pandas.pydata.org/docs/

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos e educacionais.

---

## 🔗 Links Úteis

- **Repositório GitHub**: https://github.com/9luis7/AI-Impacto-Mercado-Trabalho
- **Documentação Streamlit**: https://docs.streamlit.io/

---

**Desenvolvido com ❤️ pelos alunos da FIAP**
