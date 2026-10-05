**Analisis de sensores industriales**  
**Objetivo**  
Analizar 100,000 mediciones de temperatura y vibracion de sensores instalados  
   
 en cuatro plantas industriales: cantidad de registros y sensores, temperatura  
   
 promedio por planta, temperatura maxima y alertas (temperatura > 85 C).  
**Datos**  
Archivo: data/sensores_industriales.csv  
| | |  
|-|-|  
| **Columna** | **Significado** |   
| id_registro | Identificador de la medicion |   
| fecha_hora | Fecha y hora de la lectura |   
| id_sensor | Identificador del sensor |   
| planta | Planta donde esta instalado |   
| temperatura_c | Temperatura en grados Celsius |   
| vibracion_mm_s | Vibracion en milimetros por segundo |   
   
**Requisitos**  
- Git  
- Python 3.14 (probado con esta version) o superior  
- Dependencia externa: pandas (ver requirements.txt)  
**Instalacion y ejecucion**  
git clone https://github.com/eliasfmaltrana1805-stack/examen_sensores_industriales.git  
 cd examen_sensores_industriales  
 python3 -m venv .venv  
 source .venv/bin/activate  
 pip install -r requirements.txt  
 python analisis.py  
   
**Salidas**  
- Resultados impresos en la terminal.  
- resultados/alertas.csv: lecturas con temperatura > 85 C, con las columnas originales.  
**Estructura del proyecto**  
data/          CSV original (datos simulados)  
 resultados/    alertas.csv generado por analisis.py  
 evidencias/    captura de reproducibilidad  
 analisis.py    programa de analisis  
 informe.md     respuestas de la Parte II  
 requirements.txt  
   
