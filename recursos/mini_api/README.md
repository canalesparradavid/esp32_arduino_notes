# Mini API
Este proyecto consiste de una API en PHP8 la cual se encarga de listar y registrar logs.
El listado de logs se devuelve en formato JSON.

Se puede encontrar la documentanción de la API importando el fichero [documentation.json](documentation.json) en el programa [Postman](https://www.postman.com/).

Para lanzar la API basta con ejecutar el siguiente comando en la raiz del programa (dentro de la carpeta `api`):
```
php -S localhost:8000
```

Si se desea hacer uso de esta API en otro dispositivo de la misma red se deberá sustituir `localhost` por su `Dirección IPv4` disponible al ejecutar el comando
```
ipconfig
```
