pyinstaller --onefile --noconsole --hiddenimport tkinter --hiddenimport numpy --hiddenimport sqlite3 aplikacja.py
copy lokalizacje.csv .\dist\lokalizacje.csv
copy czasy_przejazdow.csv .\dist\czasy_przejazdow.csv
copy api_key.txt .\dist\api_key.txt
pause