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

O modelo utiliza um **RandomForestClassifier** treinado com 24.000 amostras e validado em 6.000 amostras de teste, atingindo **96% de acurácia** na classificação do impacto da IA em diferentes profissões.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.11+** - Linguagem de programação
- **Streamlit** - Framework web para interface interativa
- **scikit-learn** - Biblioteca de Machine Learning
- **pandas** - Manipulação e análise de dados
- **numpy** - Operações numéricas
- **matplotlib & seaborn** - Visualização de dados
- **joblib** - Serialização de modelos

---

## 📋 Requisitos

- Python 3.11 ou superior
- Ambiente virtual (venv) - será criado automaticamente
- Sistema Operacional: Windows (scripts .bat incluídos)

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

## 🎯 Funcionalidades

### 1. Previsor Interativo
O aplicativo permite prever o impacto da IA em profissões com base em:

- **Industry (Indústria)**: IT, Manufacturing, Finance, Healthcare, Education
- **Required Education (Educação)**: Bachelor's Degree, Master's Degree, Associate Degree, High School, PhD
- **Median Salary (USD)**: Salário médio em dólares (30.000 - 150.000)
- **Experience Required (Years)**: Anos de experiência necessários (0-40)
- **Remote Work Ratio (%)**: Percentual de trabalho remoto (0-100%)

### 2. Análise de Validação do Modelo
- **Matriz de Confusão**: Visualização da performance do modelo
- **Métricas Detalhadas**: Acurácia, Precisão, Recall por classe
- **Feature Importance**: Análise dos fatores mais importantes para o modelo

### 3. Análise Exploratória de Dados (EDA)
- Comparação entre profissões de **Alto Risco** vs **Baixo Risco**
- Estatísticas descritivas por nível de impacto
- Insights sobre padrões identificados pelo modelo

---

## 📊 Resultados

O modelo retorna três níveis de impacto:

- 🟢 **Low (Baixo)**: Impacto baixo da IA - profissão com menor probabilidade de automação
- 🟡 **Moderate (Moderado)**: Impacto moderado da IA - profissão com automação parcial
- 🔴 **High (Alto)**: Impacto alto da IA - profissão com maior probabilidade de automação

### Métricas de Performance

- **Acurácia**: 96%
- **Conjunto de Treinamento**: 24.000 amostras
- **Conjunto de Validação**: 6.000 amostras
- **Algoritmo**: RandomForestClassifier

### Insights do Modelo

O modelo identificou que os fatores mais importantes para determinar o impacto da IA são:

1. **Indústria** (Industry) - O setor em que a profissão está inserida
2. **Nível de Educação** (Required Education) - O grau de escolaridade exigido
3. **Salário Médio** e **Experiência** - Fatores secundários, mas relevantes
4. **Trabalho Remoto** - Fator complementar na análise

---

## 📁 Estrutura do Projeto

```
ML/
├── app.py                    # Aplicativo principal Streamlit
├── requirements.txt          # Dependências do projeto
├── ai_impact_model.joblib    # Modelo treinado (RandomForest)
├── ai_job_trends_dataset.csv # Dataset utilizado para treinamento
├── setup.bat                 # Script de configuração (Windows)
├── run_app.bat              # Script de execução (Windows)
├── venv/                     # Ambiente virtual (criado automaticamente)
└── README.md                 # Documentação do projeto
```

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
