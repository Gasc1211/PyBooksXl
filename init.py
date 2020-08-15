
import datetime
import os
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Border, Side, PatternFill, Font, GradientFill, Alignment

date = datetime.datetime.now()
dirName = input('Ingresa el nombre del directorio: ')
dirName += f'\{date.year}'

os.makedirs(dirName)
os.chdir(dirName)


