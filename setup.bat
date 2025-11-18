@echo off
echo ========================================
echo   Configuracao do Ambiente Virtual
echo ========================================
echo.

REM Criar ambiente virtual se não existir
if not exist "venv" (
    echo Criando ambiente virtual...
    python -m venv venv
    echo Ambiente virtual criado!
) else (
    echo Ambiente virtual ja existe.
)

REM Ativar o ambiente virtual
echo.
echo Ativando ambiente virtual...
call venv\Scripts\activate.bat

REM Instalar dependências
echo.
echo Instalando dependencias do requirements.txt...
pip install -r requirements.txt

echo.
echo ========================================
echo   Configuracao concluida!
echo ========================================
echo.
echo Para executar o app, use: run_app.bat
echo Ou execute manualmente:
echo   venv\Scripts\activate.bat
echo   python -m streamlit run app.py
echo.
pause

