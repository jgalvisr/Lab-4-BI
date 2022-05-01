# Lab 4 - BI

Laboratorio 4 de inteligencia de negocios.

*Laura Quiroga - 201922965    
Diego Rodriguez - 201923986   
Juan Pablo Galvis - 201922278*  

---

## Sobre el API

El API brinda los servicios del pipeline de predicción de esperanza de vida de un país y de verificación del puntaje del modelo. Los servicios que incluye son:
- Make prediction  
**Método HTTP**: POST  
**URL**: /predict  
**Body**: JSON con las estadísticas del país  
**Response**: Expectativa de vida calculada

- Test R^2  
**Método HTTP**: POST  
**URL**: /test  
**Body**: JSON con las estadísticas del país junto con la esperanza de vida esperada  
**Response**: Expectativa de vida calculada

Para más información y ejemplos de uso, consultar la ruta */docs*.  


## Instalación
El API está desplegado en la siguiente aplicación de Heroku:
https://country-life-expectancy-api.herokuapp.com/

Para desplegar el API localmente:
1. Instalar la librería con el transformador personalizado con el comando ``pip install lib/outlremover-0.1.0-py3-none-any.whl``.
2. Desplegar el API en un servidor local con el comando ``uvicorn main:app --reload``.