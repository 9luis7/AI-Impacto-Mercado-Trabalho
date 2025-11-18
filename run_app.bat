@echo off
echo ========================================
echo   Previsor de Impacto da IA - Streamlit
echo ========================================
echo.

REM Ativar o ambiente virtual
call venv\Scripts\activate.bat

REM Verificar se o venv foi ativado corretamente
if errorlevel 1 (
    echo ERRO: Nao foi possivel ativar o ambiente virtual.
    echo Criando ambiente virtual...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo Instalando dependencias...
    pip install -r requirements.txt
)

REM Executar o aplicativo Streamlit
echo.
echo Iniciando aplicativo Streamlit...
echo.
python -m streamlit run app.py

pause

