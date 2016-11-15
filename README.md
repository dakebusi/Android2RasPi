# Android2RasPi

Small project to connect an Android phone to a Raspberry Pi.

The aim of the project is to be able to send information from the Android phone (e.g. GPS readings, battery levels, accelerometer data...) to a Raspberry Pi.

This is achieved via websockets:

* A process in the Raspberry Pi opens and listens to a websocket
* The Android phone sends the data to the websocket opened by the Raspberry Pi
