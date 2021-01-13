import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Google Drive API (importante poner el segundo scope ya que si no te da un error.)
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Buscamos el nombre del libro de Drive y la hoja que queremos extraer
#OJO!! Cuidado con los espacios en el nombre de la hoja.
#Utilizaremos tantas hojas como necesitemos importar. 
sheet = client.open("Prueba API").sheet1

# Sacamos todos los resultados y los printeamos
resultados = sheet.get_all_records()
print(resultados)
df = pd.DataFrame.from_dict(resultados, orient='columns')

print(df)

#df = pd.read_json(resultados)
df.to_csv('PruebaAPI.csv')