### ¿Que es Back4App?
Back4App es una herramienta que nos permite construir REST APIs de una forma muy rápida e intuitiva y que además cuenta con plan gratuito que te permite construir lo que ellos llaman una App con un total de 25K peticiones al mes con una limitación de 10 peticiones por segundo.

### Como hacer una peticion POST a Back4App
Para poder enviar una petición POST al servidor de Back4App debemos seguir los siguientes pasos:

1. Crearse una cuenta gratuita en Back4App.
2. Crear una App de Back4App.
3. Crear una clase con sus columnas
4. Crearse unas variables de configuración con la siguiente forma

```cpp
const char* serverURL = "https://parseapi.back4app.com/classes/YOUR-CLASS-NAME";
const char* applicationId = "YOUR-APPLICATION-ID";
const char* restApiKey = "YOUR-REST-API-KEY";
```
5. Construir la petición HTTP
```cpp
HTTPClient http;

http.begin(serverURL);
http.addHeader("X-Parse-Application-Id", applicationId);
http.addHeader("X-Parse-REST-API-Key", restApiKey);
http.addHeader("Content-Type", "application/json");

String json = "YOUR-JSON";
int httpResponseCode = http.POST(json);

http.end();
```
6. Enviar el programa a una placa ESP32 con conexión WiFi.

### Documentación
Si en algún momento tienes dudas de como funcionan las peticiones a esta API puedes encontrar ayuda dentro del Dashboard en el apartado `API > API Reference` de su aplicación; en este apartado podrá encontrar la documentación de sus clases y ejemplos de codigo de peticiones HTTP.

### Ejemplo
Puedes encontrar un ejemplo de como realizar la petición explicada aquí arriba en este código: [Ejemplo POST](../ejemplos/Back4App)
