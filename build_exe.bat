@echo off
setlocal

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

pyinstaller --noconfirm --clean --onefile --windowed ^
  --name "ATEN-PDU-Web-Panel" ^
  --add-data "aten_pdu_web_helper_v2.html;." ^
  app.py

echo.
echo Bitti. EXE dosyasi: dist\ATEN-PDU-Web-Panel.exe
endlocal
