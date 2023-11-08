# Pasos para configurar una placa ESP32 con Arduino Cloud
1. Descargar los drivers del [conversor CP2102](../recursos/drivers.zip) y seguir las instrucciones de instalación.
2. Descargar el [Arduino Agent](../recursos/arduino_agent.exe) e instalarlo en tu ordenador.
3. Conectar la placa ESP32 a tu ordenador mediante un cable USB.
4. Acceder a [Arduino Cloud](https://create.arduino.cc/iot/things) y crear un nuevo proyecto.
5. En el proyecto, hacer clic en `Associated Device` para asociar un nuevo dispositivo.
6. Seleccionar `Third party device` como tipo de dispositivo.
7. Elegir `ESP32` como el modelo de la placa.
8. Seleccionar `WEMOS LOLIN32` de la lista desplegable como la placa que estás utilizando.
9. Asignar un nombre a la placa y asegurarte de guardar la `Secret Key` generada.
10. En la sección `Network`, configurar la red a la que deseas que la placa se conecte, ingresando la `Secret Key` previamente guardada.
11. En la pestaña de `Sketch`, cargar el programa que deseas ejecutar en la placa.
12. Seleccionar el dispositivo que configuraste anteriormente (verás el puerto al que está conectado en tu ordenador).
13. Hacer clic en el botón `Upload` para cargar el programa en la placa `ESP32`.
