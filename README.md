# API GoogleSheets y Google Drive
![](https://como-funciona.com/wp-content/uploads/2020/02/c%C3%B3mo-funciona-google-sheets.png)

Script para descargar tablas de GoogleSheet automaticamente. 

# Token 

Para acceder a la hoja de cálculo mediante programación, tendremos que crear unas credenciales OAuth2 desde la consola API de Google.

## Cómo sacar credenciales
### Sigue estos sencillos pasos 

- Abre la Consola de API de Google.
- Crea un nuevo proyecto.
- Clickea en Habilitar API. Busqua y activa la API de Google Drive y seguidamente la API de GoogleSheet.
- Crea credenciales para un Servidor Web para acceder a Datos de la Aplicación.
- Ponle nombre a tu cuenta y otorgua el papel de Editor del Proyecto.
- Descarga el archivo JSON.
- Copia el archivo JSON en el  directorio de código y cambiale el nombre a: "client_secret.json"

- El ultimo paso y posiblemente el mas importante tienes que darle permiso en tu hoja de GoogleSheet al mail que encontraras dentro del recien creado archivo "client_secret.json" como "client_email". Para ello, ve a tu hoja de GoogleSheet, arriba a la izquierda pulsa compartir y pega el mail en personas. Acepta y ya has creado todo lo necesario. 

# Bibliotecas utizadas
### gspread
### Pandas
### oauth2client


# ¿Como utilizar este archivo?

- ## Crea tu Token
- ## Dale permisos
- ## Cambia el nombre de la hoja dentro del .py
- ## Cambia el nombre del csv a tu gusto! 
- ## Listo! Integrálo dentro de tu empresa!! 

Espero que os haya sido útil! Un saludo. 

