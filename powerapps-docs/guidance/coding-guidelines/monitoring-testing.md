---
title: Testing and monitoring in Power Apps
description: Learn about testing and monitoring your Power Apps.
ms.date: 06/12/2024
ms.topic: concept-article
ms.subservice: guidance
ms.service: powerapps
author: robstand
ms.author: rachaudh
---

# Monitoring and testing

Power Apps Authoring provides various capabilities to validate the app for any warnings or errors, check monitor log for runtime performance and log app session details and traces to Application Insights for deeper analysis.  
These tools are really powerful and should be utilized to help build a strong, robust and a high performance app.

## Monitor

Power Apps Monitor is a debugging tool that can be used to monitor a stream of events from a users sessions to diagnose and troubleshoot problems specially related to performance.

The tool can be used from Power Apps studio or to monitor published apps during runtime. To access monitor for published app, go to App, select Details, and then select Monitor.

![A screenshot of Power Apps with the context menu open, showing Monitor](media/image33.png)

The monitor tool can return some important information, such as:

- Nature of the Operation such as `Select`, `Load Screen`, `Navigate`, `GetRows`, etc.

- Result and Result Info, indicating whether the call is Success, Failure or Warning, Result info includes information such as Number of rows returned, any runtime errors like 404 or 429 etc.

- Duration, which is the amount of time taken to complete a given request

- Data source and control information

![A screenshot of the monitor results showing the columns described](media/image34.png)

On selecting the event grid you can get some more information like overview of the event, formula that's related to the selected event, HTTP request sent and response received. By default, the formula is only available during authoring, not for published apps. To show the formula for published apps, you need to enable an option in the app settings. Go to *File*, then *Settings*, and turn on *Debug published app*.

![A screenshot of Power Apps showing that the *Debug published app* option is turned on](media/image35.png)

![A screenshot of Power Apps showing the JSON details of an item selected in the event grid](media/image36.png)

## App Checker

The introduction of the App checker represents a more streamlined method for identifying formula issues and addressing accessibility concerns within your app. Easily accessible through the App checker button situated in the upper right corner of Power Apps Studio, this tool presents a comprehensive list of formula-related issues and actionable recommendations. Its purpose extends beyond mere error detection, as it also contributes to improving debugging efficiency, optimizing performance, and ensuring alignment with best practices. The ongoing commitment of the Power Apps team involves continuous investment and expansion of the App checker, aiming to simplify the debugging process and empower developers with informed decision-making in app development.

![A screenshot of Power Apps showing the App Checker icon highlighted](media/image37.png)

![A screenshot of Power Apps showing the App Checker user interface](media/image38.png)

### Accessibility Checker

The Accessibility Checker functions in a manner similar to the formula errors checker, scrutinizing your app for potential accessibility issues and presenting them in a comprehensive list. Presently, the Accessibility Checker offers guidance on enabling keyboard and screen reader support within apps, although it does not currently identify color contrast issues.

Upon select an item from the Accessibility Checker list, it opens the relevant property for addressing the identified issue. Clicking the right chevron reveals detailed information along with a link to additional resources providing insights into creating accessible apps. For more in-depth information on the Accessibility Checker and general principles of accessibility, refer [here](/power-apps/maker/canvas-apps/accessibility-checker).

![A screenshot of Power Apps showing the results of Accessibility Checker](media/image39.png)
