#include "thingProperties.h"
#include <HTTPClient.h>

// Configuracion de Back4App
const char* serverURL = "https://parseapi.back4app.com/classes/YOUR-CLASS-NAME";
const char* applicationId = "YOUR-APPLICATION-ID";
const char* restApiKey = "YOUR-REST-API-KEY";

void setup() {
    Serial.begin(9600);
    delay(1500);
    initProperties();
    ArduinoCloud.begin(ArduinoIoTPreferredConnection);
    setDebugMessageLevel(2);
    ArduinoCloud.printDebugInfo();
}

void loop() {
    ArduinoCloud.update();

    HTTPClient http;

    http.begin(serverURL);
    http.addHeader("X-Parse-Application-Id", applicationId);
    http.addHeader("X-Parse-REST-API-Key", restApiKey);
    http.addHeader("Content-Type", "application/json");

    String json = "YOUR-JSON";
    int httpResponseCode = http.POST(json);

    http.end();
}
