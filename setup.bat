@echo off
echo Installing Kivy Designer dependencies...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo.
echo Installation completed!
echo.
echo To run the Kivy Designer, use:
echo python main.py
echo.
pause
