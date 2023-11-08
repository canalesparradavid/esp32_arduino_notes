### ¿Que es una petición GET?
Una petición GET es una llamada a un servicio que está alojado en un servidor HTTP; una vez el servidor recibe una petición, este la procesa y posteriormente devuelve un resultado al proceso que ha realizado la petición.

En este tipo de solicitudes, los datos que se envian al servidor van "incrustados" en la URL de la petición a diferencia de otros tipos como podria ser el POST.

### ¿Como se hace en Arduino?
Para poder hacer este tipo de peticiones en una placa de Arduino debemos seguir los siguientes pasos:

1. Incluir las cabeceras de las librerias.
```cpp
#include <HTTPClient.h>
```
2. Definir la url del servidor como variable global.
```cpp
String serverName = "http://192.168.1.106:1880/";
```
3. Realizar las peticiones GET dentro de `loop`.
```cpp
String serverPath = serverName + "?temperature=24.37";
http.begin(serverPath.c_str());
int httpResponseCode = http.GET();
```
4. Si se desea recuperar los datos devueltos se hace de la siguiente forma:
```cpp
String response = http.getString();
```
5. Liberar los recursos del cliente http
```cpp
http.end();
```
