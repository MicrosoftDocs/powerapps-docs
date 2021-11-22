---
title: Acceleration, App, Compass, Connection, and Location signals in Power Apps
description: Reference information including syntax and examples for the Acceleration, App, Compass, Connection, and Location signals in Power Apps.
author: gregli-msft
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 02/07/2020
ms.subservice: canvas-maker
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - gregli-msft
  - nkrb
---
# Acceleration, App, Compass, Connection, and Location signals in Power Apps

Returns information about the app's environment, such as where the user is located in the world and which screen is displayed.

## Description and syntax

Signals are values that can change at any time, independent of how the user may be interacting with the app. Formulas that are based on signals automatically recalculate as these values change.

Signals typically return a [record](../working-with-tables.md#records) of information. You can use and store this information as a record, or you can extract individual properties by using the **.** [operator](operators.md).

> [!NOTE]
> The **Acceleration** and **Compass** functions return accurate values in a native player such as on iOS or Android, but those functions return zero values as you create or modify an app in the browser.

### Acceleration

The **Acceleration** signal returns the device's acceleration in three dimensions relative to the device's screen. Acceleration is measured in *g* units of 9.81 m/second<sup>2</sup> or 32.2 ft/second<sup>2</sup> (the acceleration that the Earth imparts to objects at its surface due to gravity).

| Property | Description |
| --- | --- |
| **Acceleration.X** |Right and left.  Right is a positive number. |
| **Acceleration.Y** |Forward and back.  Forward is a positive number. |
| **Acceleration.Z** |Up and down.  Up is a positive number. |

### App

Among other properties, the **App** object includes a signal that indicates which screen is showing.

| Property | Description |
| --- | --- |
| **App.ActiveScreen** |Screen that's showing. Returns a screen object, which you can use to reference properties of the screen or compare to another screen to determine which screen is showing. You can use the **[Back](function-navigate.md)** or **[Navigate](function-navigate.md)** function to change the screen that's showing. |

More information: [**App** object](object-app.md) documentation.

### Compass
The **Compass** signal returns the compass heading of the top of the screen. The heading is based on magnetic north.

| Property | Description |
| --- | --- |
| **Compass.Heading** |Heading in degrees.  Returns a number 0 to 360, and 0 is north. |

### Connection
The **Connection** signal returns the information about the network connection. When on a metered connection, you may want to limit how much data you send or receive over the network.

| Property | Description |
| --- | --- |
| **Connection.Connected** |Returns a Boolean **true** or **false** value that indicates whether the device is connected to a network. |
| **Connection.Metered** |Returns a Boolean **true** or **false** value that indicates whether the connection is metered. |

### Location
The **Location** signal returns the location of the device based on the Global Positioning System (GPS) and other device information, such as cell-tower communications and IP address.

When a user accesses the location information for the first time, the device may prompt that user to allow access to this information.

As the location changes, dependencies on the location will continuously recalculate, which will consume power from the device's battery. To conserve battery life, you can use the **[Enable](function-enable-disable.md)** and **[Disable](function-enable-disable.md)** functions to turn location updates on and off. Location is automatically turned off if the displayed screen doesn't depend on location information.

| Property | Description |
| --- | --- |
| **Location.Altitude** |Returns a number that indicates the altitude, measured in meters, above sea level. |
| **Location.Latitude** |Returns a number, from –90 to 90, that indicates the latitude, as measured in degrees from the equator. A positive number indicates a location that's north of the equator. |
| **Location.Longitude** |Returns a number, from –180 to 180, that indicates the longitude, as measured in degrees from Greenwich, England.  A positive number indicates a location that's east of Greenwhich. |

## Examples
In a baseball field, a pitcher throws a phone from the pitcher's mound to a catcher at home plate. The phone is lying flat with respect to the ground, the top of the screen is pointed at the catcher, and the pitcher adds no spin. At this location, the phone has cellular network service that's metered but no WiFi. The **PlayBall** screen is displayed.   

| Formula | Description | Result |
| --- | --- | --- |
| **Location.Latitude** |Returns the latitude of the current location. The field is located at map coordinates 47.591 N, 122.333 W. |47.591<br><br>The latitude will change continuously as the ball moves between the pitcher and the catcher. |
| **Location.Longitude** |Returns the longitude of the current location. |122.333<br><br>The longitude will change continuously as the ball moves between the pitcher and the catcher. |
| **Location** |Returns the latitude and longitude of the current location, as a record. |{&nbsp;Latitude:&nbsp;47.591, Longitude:&nbsp;122.333&nbsp;} |
| **Compass.Heading** |Returns the compass heading of the top of the screen. At this field, home plate is roughly southwest from the pitcher's mound. |230.25 |
| **Acceleration.X** |Returns the acceleration of the device side to side. The pitcher is throwing the phone straight ahead with respect to the screen's top, so the device isn't accelerating side to side. |0 |
| **Acceleration.Y** |Returns the acceleration of the device front to back. The pitcher initially gives the device a large acceleration when throwing the device, going from 0 to 90 miles per hour (132 feet per second) in half a second. After the device is in the air, ignoring air friction, the device doesn't accelerate further. The device decelerates when the catcher catches it, bringing it to a stop. |8.2, while the pitcher throws the device.<br><br>0, while the device is in the air.<br><br>-8.2, as the catcher catches the device. |
| **Acceleration.Z** |Returns the acceleration of the device top to bottom. While in the air, the device experiences the effects of gravity. |0, before the pitcher throws the device.<br><br>1, while the device is in the air.<br><br>0, after the catcher catches the device. |
| **Acceleration** |Returns the acceleration as a record. |{ X: 0, Y: 264, Z: 0 } as the pitcher throws the device. |
| **Connection.Connected** |Returns a Boolean value that indicates whether the device is connected to a network |**true** |
| **Connection.Metered** |Returns a Boolean value that indicates whether the connection is metered |**true** |
| **App.ActiveScreen = PlayBall** |Returns a Boolean value that indicates whether **PlayBall** is displayed. |**true** |
| **App.ActiveScreen.Fill** |Returns the background color for the displayed screen. |**Color.Green** |



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]