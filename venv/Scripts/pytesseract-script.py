#!"C:\Users\김형호\OneDrive - 아주대학교\학과목\캡스톤디자인\Python\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'pytesseract==0.2.6','console_scripts','pytesseract'
__requires__ = 'pytesseract==0.2.6'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pytesseract==0.2.6', 'console_scripts', 'pytesseract')()
    )
