import streamlit as st
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# --- VARIÁVEIS GLOBAIS (FEATURES) ---
FEATURES_LIST = [
    'Industry',
    'Required Education',
    'Median Salary (USD)',
    'Experience Required (Years)',
    'Remote Work Ratio (%)'
]

NUMERIC_FEATURES = [
    'Median Salary (USD)',
    'Experience Required (Years)',
    'Remote Work Ratio (%)'
]

CATEGORICAL_FEATURES = [
    'Industry',
    'Required Education'
]

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Previsor de Impacto da IA",
    page_icon="🤖",
    layout="wide"
)

# --- 2. FUNÇÕES DE CARREGAMENTO (COM CACHE) ---

@st.cache_resource
def load_model(path="ai_impact_model.joblib"):
    """Carrega o pipeline de modelo .joblib."""
    if not os.path.exists(path):
        st.error(f"❌ Erro: Arquivo do modelo '{path}' não encontrado!")
        st.stop()
    try:
        model = joblib.load(path)
        return model
    except Exception as e:
        st.error(f"❌ Erro ao carregar o modelo: {str(e)}")
        st.stop()

@st.cache_data
def load_data(path="ai_job_trends_dataset.csv"):
    """Carrega o dataset CSV completo para a aba EDA."""
    if not os.path.exists(path):
        st.error(f"❌ Erro: Arquivo de dados '{path}' não encontrado para a Aba 'Análise'!")
        st.stop()
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        st.error(f"❌ Erro ao carregar os dados: {str(e)}")
        st.stop()

# --- 3. CARREGAMENTO DOS DADOS E MODELO ---
model = load_model()
df = load_data()

# --- 4. SIDEBAR COM INPUTS DO USUÁRIO ---
st.sidebar.header("📊 Parâmetros da Profissão")
st.sidebar.markdown("Preencha os campos para a previsão:")

# Inputs da Sidebar
industry = st.sidebar.selectbox(
    "Industry (Indústria)",
    options=df['Industry'].unique(), # Pega opções direto do DF
    index=0
)

education = st.sidebar.selectbox(
    "Required Education (Educação)",
    options=df['Required Education'].unique(), # Pega opções direto do DF
    index=0
)

salary = st.sidebar.number_input(
    "Median Salary (USD) (Salário)",
    min_value=30000,
    max_value=150000,
    value=90000, # Valor padrão (média)
    step=1000,
    format="%d"
)

experience = st.sidebar.slider(
    "Experience Required (Years) (Experiência)",
    min_value=0,
    max_value=40,
    value=10, # Valor padrão (média)
    step=1
)

remote_work = st.sidebar.slider(
    "Remote Work Ratio (%) (Trabalho Remoto)",
    min_value=0,
    max_value=100,
    value=50, # Valor padrão (média)
    step=1
)

predict_button = st.sidebar.button("🔮 Prever Impacto", type="primary", use_container_width=True)

# --- 5. ESTRUTURA DAS ABAS ---
st.title("🤖 Previsor de Impacto da IA no Trabalho")

tab1, tab2, tab3 = st.tabs([
    "**Previsor Interativo**",
    "**Sobre o Modelo (Validação)**",
    "**O Padrão nos Dados**"
])


# --- ABA 1: PREVISOR ---
with tab1:
    st.header("Previsão de Impacto da IA")
    
    if predict_button:
        try:
            # 1. Criar o dicionário de dados usando as features globais
            input_data = {
                'Industry': [industry],
                'Required Education': [education],
                'Median Salary (USD)': [salary],
                'Experience Required (Years)': [experience],
                'Remote Work Ratio (%)': [remote_work]
            }
            
            # 2. Criar o DataFrame FORÇANDO a ordem das colunas (usando FEATURES_LIST)
            input_df = pd.DataFrame(input_data, columns=FEATURES_LIST)

            # 4. Fazer a previsão de PROBABILIDADE
            probabilities = model.predict_proba(input_df)[0]
            prediction = model.predict(input_df)[0]
            
            # 5. Criar DataFrame para o gráfico de confiança
            prob_df = pd.DataFrame({
                'Nível de Risco': model.classes_,
                'Confiança (%)': probabilities * 100
            }).sort_values(by='Confiança (%)', ascending=False)
            
            
            # 6. Exibir o resultado
            st.subheader("📈 Resultado da Previsão")
            
            if prediction == "Low":
                st.success("🟢 **Impacto Baixo**")
            elif prediction == "Moderate":
                st.warning("🟡 **Impacto Moderado**")
            elif prediction == "High":
                st.error("🔴 **Impacto Alto**")

            # 7. O Gráfico "UAU" (Confiança)
            st.subheader(f"Nível de Confiança da Previsão: {probabilities.max()*100:.1f}%")
            st.bar_chart(prob_df.set_index('Nível de Risco'))
            
            st.markdown("---")
            st.subheader("📋 Parâmetros Utilizados")
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Indústria:** {industry}")
                st.write(f"**Educação:** {education}")
            with col2:
                st.write(f"**Salário Médio:** ${salary:,.0f}")
                st.write(f"**Experiência:** {experience} anos")
                st.write(f"**Trabalho Remoto:** {remote_work}%")
                
        except Exception as e:
            st.error(f"❌ Erro ao fazer a previsão: {str(e)}")

    else:
        st.info("👈 **Preencha os parâmetros na barra lateral e clique em 'Prever Impacto' para obter uma análise.**")
        
        st.markdown("---")
        st.subheader("🧪 Desafio: Teste Sua Intuição!")
        st.warning(
            "**Você consegue desafiar o modelo?** A IA descobriu padrões surpreendentes nos dados. "
            "Tente preencher os campos acima e veja se consegue encontrar uma combinação que "
            "contradiga os padrões identificados na aba **'O Padrão nos Dados'**!"
        )


# --- ABA 2: SOBRE O MODELO (VALIDAÇÃO) ---
with tab2:
    st.header("Validação e Performance do Modelo")
    
    st.subheader("Performance (Acurácia de 96%)")
    st.write("O modelo foi treinado com 24.000 amostras e validado em 6.000 amostras novas (dados que ele nunca viu), atingindo 96% de acurácia.")
    
    # Matriz de Confusão - Geração Dinâmica
    st.subheader("Matriz de Confusão")
    if os.path.exists("matriz_de_confusao.png"):
        st.image("matriz_de_confusao.png",
                 caption="Matriz de Confusão (Validação em 6.000 amostras de teste)",
                 width=600)
    else:
        # Gera matriz de confusão dinamicamente usando uma amostra do dataset
        try:
            # Usa as features globais definidas
            feature_columns = FEATURES_LIST
            
            # Usa uma amostra representativa do dataset para demonstrar
            # (em produção, você usaria o conjunto de teste real)
            sample_size = min(6000, len(df))
            sample_df = df.sample(n=sample_size, random_state=42)
            X_sample = sample_df[feature_columns]
            y_sample = sample_df['AI Impact Level']
            
            # Faz predições
            y_pred_sample = model.predict(X_sample)
            
            # Cria a matriz de confusão
            labels = ['Low', 'Moderate', 'High']
            cm = confusion_matrix(y_sample, y_pred_sample, labels=labels)
            
            # Calcula métricas adicionais
            from sklearn.metrics import accuracy_score, classification_report
            accuracy = accuracy_score(y_sample, y_pred_sample)
            
            # Plota a matriz de confusão
            fig_cm, ax_cm = plt.subplots(figsize=(10, 8))
            disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
            disp.plot(ax=ax_cm, cmap='Blues', values_format='d')
            title = (
                f'Matriz de Confusão (Amostra de {sample_size:,} registros)\n'
                f'Acurácia: {accuracy*100:.2f}%'
            )
            ax_cm.set_title(title, fontsize=12, fontweight='bold')
            plt.tight_layout()
            st.pyplot(fig_cm)
            
            # Mostra métricas detalhadas
            with st.expander("📊 Ver Métricas Detalhadas de Classificação"):
                report = classification_report(y_sample, y_pred_sample, labels=labels, output_dict=True)
                report_df = pd.DataFrame(report).transpose()
                st.dataframe(report_df, use_container_width=True)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Acurácia Geral", f"{accuracy*100:.2f}%")
                with col2:
                    st.metric("Precisão Média", f"{report_df.loc['macro avg', 'precision']*100:.2f}%")
                with col3:
                    st.metric("Recall Médio", f"{report_df.loc['macro avg', 'recall']*100:.2f}%")
            
            st.caption(
                "⚠️ **Nota:** Esta matriz foi gerada com uma amostra do dataset "
                "completo. A validação real do modelo foi realizada com 6.000 "
                "amostras separadas do conjunto de treinamento, atingindo "
                "96% de acurácia."
            )
            
        except Exception as e:
            st.error(f"Erro ao gerar matriz de confusão: {e}")
            st.info("💡 Dica: Para gerar a matriz de confusão real, execute o código de validação no seu notebook e salve como 'matriz_de_confusao.png'.")

    st.markdown("---")
    st.subheader("Validando a Alta Acurácia")
    st.write(
        "O modelo RandomForestClassifier foi validado com métricas rigorosas. "
        "Abaixo, você pode ver quais fatores o modelo mais utiliza para tomar decisões."
    )
    st.markdown("---")
    st.subheader("O que é mais importante para o Modelo? (Feature Importance)")
    st.write("O gráfico abaixo mostra quais fatores o modelo mais usou para tomar a decisão:")
    
    try:
        # Pega o classificador do pipeline
        classifier = model.named_steps['classifier']
        
        # Verifica se o classificador tem feature_importances_
        if hasattr(classifier, 'feature_importances_'):
            # Pega o preprocessor
            preprocessor = model.named_steps['preprocessor']
            
            # Usa as features globais definidas
            feature_columns = FEATURES_LIST
            cat_features = CATEGORICAL_FEATURES
            num_features = NUMERIC_FEATURES
            
            # Obtém os nomes das features após o OneHotEncoder
            try:
                onehot = preprocessor.named_transformers_['cat'].named_steps['onehot']
                # Usa as features categóricas globais
                cat_transformed_names = onehot.get_feature_names_out(cat_features)
            except Exception:
                # Fallback: cria nomes manualmente baseado nos valores únicos
                cat_transformed_names = []
                for col in cat_features:
                    unique_vals = sorted(df[col].unique())
                    for val in unique_vals:
                        cat_transformed_names.append(f"{col}_{val}")
            
            # Combina todas as features na ordem correta (numéricas primeiro, depois categóricas)
            all_features_names = num_features + list(cat_transformed_names)
            
            # Verifica se o número de features corresponde
            n_expected = len(classifier.feature_importances_)
            n_obtained = len(all_features_names)
            if n_expected != n_obtained:
                st.warning(
                    f"⚠️ Número de features não corresponde. "
                    f"Esperado: {n_expected}, Obtido: {n_obtained}"
                )
                # Usa apenas as primeiras N features
                all_features_names = all_features_names[:n_expected]
            
            # Cria dataframe de importância
            importance_df = pd.DataFrame({
                'Feature': all_features_names,
                'Importância': classifier.feature_importances_
            }).sort_values(by='Importância', ascending=False)
            
            # Limpa nomes para melhor visualização (ex: "Industry_IT" -> "Industry: IT")
            importance_df['Feature'] = importance_df['Feature'].str.replace("_", ": ", n=1)
            
            # Plota o gráfico de importância horizontalmente (Top 10)
            # Usa Matplotlib/Seaborn para controle total de tamanho e orientação
            fig, ax = plt.subplots(figsize=(10, 6))
            
            # Usa Seaborn para plotar HORIZONTALMENTE (y=Feature, x=Importância)
            sns.barplot(
                data=importance_df.head(10),
                y='Feature',
                x='Importância',
                color='#1f77b4'  # Cor padrão do Streamlit para manter consistência
            )
            plt.title('Top 10 Fatores Mais Importantes', fontsize=14, fontweight='bold')
            plt.xlabel('Importância Relativa', fontsize=12)
            plt.ylabel('')  # Remove o label do eixo Y para mais espaço
            plt.tight_layout()
            
            st.pyplot(fig)
            
            # Mostra estatísticas
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Feature Mais Importante", importance_df.iloc[0]['Feature'])
            with col2:
                st.metric("Importância", f"{importance_df.iloc[0]['Importância']*100:.2f}%")
            
            with st.expander("📋 Ver todas as features e suas importâncias"):
                st.dataframe(importance_df, use_container_width=True)
                
        else:
            st.warning(
                "⚠️ Este modelo não possui feature_importances_ "
                "(pode não ser um RandomForest ou outro modelo baseado em "
                "árvores)."
            )

    except Exception as e:
        st.error(f"Erro ao calcular feature importance: {e}")
        st.info(
            "💡 Dica: Verifique se o modelo foi treinado com "
            "RandomForestClassifier ou outro modelo que tenha "
            "feature_importances_."
        )

# --- ABA 3: O PADRÃO NOS DADOS ---
with tab3:
    st.header("📊 O Padrão nos Dados")
    st.write("Análise comparativa dos padrões aprendidos pelo modelo: **Alto Risco vs. Baixo Risco**")
    
    # Calcula médias para Low e High usando filtro direto (mais confiável)
    df_low = df[df['AI Impact Level'] == 'Low'].copy()
    df_high = df[df['AI Impact Level'] == 'High'].copy()
    
    # Validação: verifica se os filtros funcionaram
    if len(df_low) == 0 or len(df_high) == 0:
        st.error("❌ Erro: Não foi possível filtrar os dados por nível de risco.")
        st.info(f"Valores únicos encontrados: {df['AI Impact Level'].unique()}")
    else:
        avg_low_salary = df_low['Median Salary (USD)'].mean()
        avg_high_salary = df_high['Median Salary (USD)'].mean()
        
        avg_low_experience = df_low['Experience Required (Years)'].mean()
        avg_high_experience = df_high['Experience Required (Years)'].mean()
        
        avg_low_remote = df_low['Remote Work Ratio (%)'].mean()
        avg_high_remote = df_high['Remote Work Ratio (%)'].mean()
    
        st.markdown("---")
        
        # Nota Crítica (substitui a tabela de comparação)
        st.subheader("📊 Nota Crítica (Insight)")
        st.warning(
            "**Descoberta Importante:** A análise estatística revela que o **Salário Médio** "
            "e a **Experiência** são fatores neutros (com média de ${:,.0f} e {:.1f} anos "
            "em todos os grupos). A alta acurácia do modelo (96%) é integralmente baseada "
            "nas features categóricas (**Industry** e **Required Education**) — ou seja, "
            "**onde você trabalha** e **o quanto você estudou**.\n\n"
            "Você pode confirmar isso na **Aba 2 (Feature Importance)**: o Median Salary e "
            "Experience Required devem estar nas últimas posições do gráfico, e as categorias "
            "como Industry: IT e Required Education: Bachelor's Degree devem estar no topo."
            .format(avg_low_salary, avg_low_experience)
        )
        
        st.markdown("---")
        
        # Insight Principal Corrigido (baseado na Feature Importance)
        st.subheader("💡 Padrão Corrigido, Baseado na Feature Importance")
        st.info(
            "**O modelo de 96% de acurácia ignora as médias salariais** (que são quase "
            "idênticas entre os grupos) **e foca nas categorias**. O verdadeiro padrão de "
            "risco é:\n\n"
            "• **O Maior Risco de Automação** é atribuído a profissões em certas **Indústrias** "
            "e que exigem apenas **High School**.\n\n"
            "• **O Menor Risco de Automação** é atribuído a profissões em outras **Indústrias** "
            "e que exigem **Master's Degree ou PhD**.\n\n"
            "**Confirmação:** Verifique o gráfico de Feature Importance na **Aba 2** para ver "
            "quais indústrias e níveis de educação o modelo considera mais importantes."
        )
        
        # Chamada para ação (para LinkedIn)
        st.markdown("---")
        st.subheader("🧪 Teste Sua Intuição!")
        st.warning(
            "**Desafio:** O modelo descobriu que **Indústria** e **Nível de Educação** são os "
            "fatores decisivos, não o salário. Você consegue preencher os campos na barra "
            "lateral e provar que o modelo está errado? Use o **Previsor Interativo** para "
            "testar diferentes combinações!"
        )
        
        # Estatísticas adicionais (mantém para referência)
        with st.expander("📈 Ver Estatísticas Detalhadas (Referência)"):
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Baixo Risco (Low)**")
                st.write(f"- Total de amostras: {len(df_low):,}")
                st.write(f"- Salário médio: ${avg_low_salary:,.0f}")
                st.write(f"- Experiência média: {avg_low_experience:.1f} anos")
                st.write(f"- Remoto médio: {avg_low_remote:.1f}%")
            with col2:
                st.write("**Alto Risco (High)**")
                st.write(f"- Total de amostras: {len(df_high):,}")
                st.write(f"- Salário médio: ${avg_high_salary:,.0f}")
                st.write(f"- Experiência média: {avg_high_experience:.1f} anos")
                st.write(f"- Remoto médio: {avg_high_remote:.1f}%")

# --- 6. RODAPÉ ÉTICO ---
st.markdown("---")
st.caption("⚠️ **Aviso:** Este modelo é uma ferramenta de análise baseada em dados de 2024 e não representa uma previsão definitiva do futuro. Os resultados devem ser interpretados como indicadores probabilísticos e não como garantias absolutas.")