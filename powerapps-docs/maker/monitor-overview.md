---
title: Overview of Power Apps with Monitor | Microsoft Docs
description: Learn about Power Apps Monitor.
author: hasharaf
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 11/19/2020
ms.author: hasharaf
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---

# Monitor overview

**Monitor** is a tool that offers makers the ability to view a stream of events from a user’s session to diagnose and troubleshoot problems. Makers can either use Monitor to view events while building a new app in Power Apps Studio, or to monitor published apps during runtime.

## Benefits

Monitor can help you diagnose and troubleshoot problems faster and build more
reliable apps. It provides a deep view into how an app runs by providing a log
of all activities in your app as the app runs. Monitor tool also provides a
better understanding of how the events and formulas contained in your app work
so you can improve performance and identify any errors or problems.

## Debugging an app

The key to debugging an problem is to have a better understanding of what your app does, and how. Sometimes, it is difficult to isolate an problem when just looking at the app formulas, or even reviewing runtime errors. Watching the events as they occur in your app can help you understand the order and performance of events and errors to diagnose problems faster.

A few example problems and queries that you can uncover when using Monitor are:

- **High number of network calls**
    - Is the app fetching data too frequently?
    - Can you optimize the app to only fetch data when required?
    - Are timer controls firing too often?
    - Are too many events occurring when the app starts? And can fetching some of the data be delayed?

-   **Retrieve data from the same data source**
    - Can you use different patterns such as caching data in collections or variables instead of fetching same data multiple times?

-   **The response data size**
    - Can you use query filters to reduce the amount of data requested?

-   **The duration of the request**
    - Are integrations optimized?
    - Can you reduce the size of the response using query filters?

-   **Errors**
    - Have you configured the required permissions to run the app correctly?
    - Are your requests throttled by the platform?

## Monitor dashboard

You can review various properties for each event inside Monitor. Depending on
the event category, some of these properties might not contain data.

![Monitor dashboard](media/monitor/monitor.png "Monitor dashboard")

| Column name       | Description                                                                                                                                                                                                                                       |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Id**            | Sequence number for the events.                                                                                                                                                                                                        |
| **Time**          | Time of the event.                                                                                                                                                                                                                     |
| **Category**      | Type of event, such as *Network*.                                                                                                                                                                                                      |
| **Operation**     | The resulting internal operation name of the request inside the app. For example, *createRow* is the operation name from the **Patch** function.                                                                                       |
| **Result**        | Status Code description in words. For example, a 429 Status will show as an *“Error”* in the result column. Row colors also help to identify any errors and warnings quickly.                                                          |
| **Result Info**   | Detailed translation of error codes and Results. For example, a 429 Status code will show as “Too many requests” in results info column.                                                                                               |
| **Status**        | The [http status code](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) of a network request. For example, a 2XX code represents a successful request while a 4XX code represents an error.                                    |
| **Duration**      | Depends on the type of event. For example, for a network request, duration is the time taken for the request to be sent and a response to be received. Duration can be used to understand the performance of network calls in the app. |
| **Data Source**   | Name of the data source accessed by the raised event operation (e.g. name of a CDS entity)                                                                                                                                             |
| **Control**       | The Control Name associated with this event                                                                                                                                                                                            |
| **Property**      | Active Control Property of the raised event.                                                                                                                                                                                           |
| **Response size** | For a network request event, represents response size in bytes received from the sender to your app.                                                                                                                                   |

When you select an event in the grid, a panel displays containing additional
details about the event. The panel has four tabs:

- **Details**: Shows a high-level overview of the event that you select. Some
    of the data might be collapsed in the tree view. You can expand and drill
    down to view content:

    ![Monitor - Details](media/monitor/monitor-details.png "Monitor - Details")

- **Formula**: Shows related formula from your app for the selected event. The
    name of the control property triggering the event is displayed on top of the tab, and inside the event table:

    ![Monitor - Formula](media/monitor/monitor-formula.png "Monitor - Formula")

- **Request**: Shows the HTTP request sent:

    ![Monitor - Request](media/monitor/monitor-request.png "Monitor - Request")

- **Response**: Shows the HTTP response received. You can view the response in
    JSON format.

    ![Monitor - Response](media/monitor/monitor-response.png "Monitor - Response")

## Next steps

- [Monitor canvas apps using Monitor](monitor-canvasapps.md)
- Monitor model-driven apps using Monitor

### See also

[Monitor - advanced monitoring and scenarios](monitor-advanced.md)
