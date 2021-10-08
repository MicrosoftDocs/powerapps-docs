---
title: Insert waypoints as map pins and draw routes between them
description: Add waypoints to your map component as pins and draw routes between them
author: iaanw
manager: shellyha
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas, ce06122020
ms.reviewer: tapanm
ms.date: 10/6/2021
ms.subservice: canvas-maker
ms.author: iawilt
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - iaanw
---

# Insert waypoint pins and draw routes between them (Preview)

[!INCLUDE[Preview disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

You can load a table that contains a dataset of waypoints into the map component. The component will then place pins on the map for each waypoint, and it can draw routes between the waypoints.

The component has options to reorder the waypoints or rearrange the route to improve travel time or travel distance.


## Prerequisites
1. Create a Canvas app and make sure it meets the [Geospatial prerequisites](geospatial-overview.md#prerequisites). 
2. In your app, [insert a map](geospatial-component-map.md#use-the-component). 


## Add waypoint data from an Excel workbook

Your data source needs to contain a named table with the following columns that should then be mapped to the associated property in the component's **Advanced** pane.

While all properties are optional, either the address field or the longitude and latitude fields must be provided so that the waypoint locations can be found.

Column description | Maps to property | Required
-- | -- | --
Label for the waypoint | RouteWaypointsLabels | Optional
Longitude of the waypoint | RouteWaypointsLongitudes | Optional
Latitude of the waypoint | RouteWaypointsLatitudes | Optional
Address of the waypoint | RouteWaypointsAddresses | Optional
