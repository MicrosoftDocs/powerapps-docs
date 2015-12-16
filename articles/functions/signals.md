<properties
	pageTitle="Acceleration, App, Compass, Connection, and Location signals | Microsoft PowerApps"
	description="Reference information, including syntax and examples, for the Acceleration, App, Compass, Connection, and Location sensors in PowerApps"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="dwrede"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/07/2015"
   ms.author="gregli"/>

# Acceleration, App, Compass, Connection, and Location signals in PowerApps #

Access to the app's environment, such as where the user is located in the world and which screen is currently displayed.  

## Description and syntax ##

All signals return a [record](working-with-tables.md#records) of information. You can use and store this information as a record, or extract individual properties with the **!** [operator](operators.md).

### Acceleration ###

The **Acceleration** signal returns the device's acceleration in three dimensions relative to the device's screen.  

Acceleration is measured in *g* units of 9.81 m/second<sup>2</sup> or 32.2 ft/second<sup>2</sup>, the acceleration that the Earth imparts to objects at its surface due to gravity.

| Signal Property | Description |
|--------------------|-------------|
| **Acceleration!X** | Right and left.  Right is a positive number. |
| **Acceleration!Y** | Forward and back.  Forward is a positive number. |
| **Acceleration!Z** | Up and down.  Up is a positive number. |

### App ###

The **App** signal returns information about the running app.

| Signal Property | Description |
|--------------------|-------------|
| **App!ActiveScreen** | Screen that is currently displayed.  Returns a screen object, which you can use to reference properties of the screen or compare to another screen to determeine which screen is currently displayed.  You change the currently displayed screen with the **[Back](function-navigate.md)** and **[Navigate](function-navigate.md)** functions.  |

### Compass ###

The **Compass** signal returns the compass heading of the top of the screen.  

The heading is based on magnetic north.

| Signal Property | Description |
|--------------------|-------------|
| **Compass!Heading** | Heading in degrees.  Returns a number 0 to 360, 0 is north. |

### Connection ###

The **Connection** signal returns the information about the network connection.

When on a metered connection, you may want to limit how much data you send or receive over the network.

| Signal Property | Description |
|--------------------|-------------|
| **Connection!Connected** | Is the device connected to a network? Returns a Boolean **true** or **false** value.  |
| **Connection!Metered** | Is the connection metered?  Returns a Boolean **true** or **false** value.  |

### Location ###

The **Location** signal returns the location of the device, based on the Global Positioning System (GPS) and other device information such as cell tower communications and and IP address.

When accessing the location information for the first time, the device may prompt the user to allow access to this information.

As the location changes, dependencies on the location will continuously recalculate, which will consume power from the device's battery.  To conserve battery life, you can use the **[Enable](function-enable-disable.md)** and **[Disable](function-enable-disable.md)** functions to turn location updates on and off.  Location is automatically turned off if the currently displayed screen does not depend on location information.

| Signal Property | Description |
|--------------------|-------------|
| **Location!Altitude** | The altitude above sea level.  Returns a number, measured in feet.
| **Location!Latitude** | The latitude, measured in degrees from the equator.  Returns a number from -90 to 90, north is positive.  |
| **Location!Longitude** | The longitude, measured in degrees west from Greenwich, England.  Returns a number from 0 to 180.  |

## Examples ##

From the pitcher's mound at Safeco Field in Seattle, a baseball pitcher throws a phone to a waiting catcher.  The phone is lying flat with respect to the ground, the top of the screen is pointed at the catcher, and the pitcher adds no spin.  At this location, the phone has cellular network service that is metered but no WiFi.  The currently displayed screen is **PlayBall**.   

| Formula | Description | Result |
|---------|-------------|--------|
| **Location!Latitude** | Latitude of the current location.  Safeco Field is located at map coordinates 47.591 N, 122.333 W. | 47.591<br><br>The latitude will change continuously as the ball moves between the pitcher and the catcher. |
| **Location!Longitude** | Longitude of the current location. | 122.333<br><br>The longitude will change continuously as the ball moves between the pitcher and the catcher.  |
| **Location** | Latitude and longitude of the current location, as a record.    | {&nbsp;Latitude:&nbsp;47.591, Longitude:&nbsp;122.333&nbsp;}  |
| **Compass!Heading** | Compass heading of the top of the screen.  Safeco Field's baseball diamond is oriented with home plate roughly southwest from the pitcher's mound.  | 230.25 |
| **Acceleration!X** | Acceleration of the device side to side.  Since the pitcher is throwing the phone straight ahead with respect to the screen's top, there is no side to side acceleration. | 0 |
| **Acceleration!Y** | Acceleration of the device front to back.  The pitcher initially gives the phone a large acceleration when the throw is made, going from 0 to 90 miles per hour (132 feet per second) in half a second.  After the phone is in the air, ignoring air friction, there is no further acceleration.  When the catcher catches the phone, there is a large reverse acceleration as the phone comes to a stop.  | 8.2, while the pitcher is actively throwing.<br><br>0, while the ball is in the air.<br><br>-8.2, as the catcher catches the ball. |
| **Acceleration!Z** | Acceleration of the device top to bottom.  While the ball is in the air, it experiences the effects of gravity.  | 0, before the pitch.<br><br>1, while the phone is in the air.<br><br>0, after the catcher catches it. |
| **Acceleration** | Acceleration as a record.  | { X: 0, Y: 264, Z: 0 } as the pitcher actively throws the phone. |
| **Connection!Connected** | Is the device currently connected to a network?  | **true** |
| **Connection!Metered** | Is the device currently connected network metered? | **true** |
| **App!ActiveScreen** | The screen object that is currently displayed. | **PlayBall** |
| **App!ActiveScreen = PlayBall** | Tests if the currently displayed screen is **PlayBall**.  | **true** |
| **App!ActiveScreen!Fill** | Returns the background color for the currently displayed screen. | **Color!Green** |
