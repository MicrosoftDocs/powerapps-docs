---
title: Testing and monitoring
description: Testing and monitoring
ms.date: 04/26/2024
ms.topic: conceptual
ms.service: powerapps
author: robstand
ms.author: rstand
 
---

# Monitoring and testing

PowerApps Authoring provides various capabilities to validate the app for any warnings or errors, check monitor log for runtime performance and log app session details and traces to Application Insights for deeper analysis.  
These tools are really powerful and should be utilized to help build a strong, robust and a high performance app.

## Monitor

Power Apps Monitor is a debugging tool that can be used to monitor a stream of events from a users sessions to diagnose and troubleshoot problems specially related to performance.

The tool can be used from PowerApps studio or to monitor published apps during runtime. To access monitor for published app, go to App -&gt; Details -&gt; monitor

![A screenshot of a computer Description automatically generated](media/image31.png)

The monitor tool can return some important information like

- Nature of the Operation such as Select, Load Screen, Navigate, GetRows etc.

- Result and Result Info – Whether the call is Success, Failure or Warning, Result info includes information such as Number of rows returned, any runtime errors like 404 or 429 etc.

- Duration- Amount of time taken to complete a given request

- Data source and Control information

![A screenshot of a computer Description automatically generated](media/image32.png)

On Selecting the event grid you can get some more information like Overview of the event, Formula that's related to the selected event, HTTP request sent and response received.

![A screenshot of a computer Description automatically generated](media/image33.png)

## App Checker

The introduction of the App checker represents a more streamlined method for identifying formula issues and addressing accessibility concerns within your app. Easily accessible through the App checker button situated in the upper right corner of PowerApps Studio, this tool presents a comprehensive list of formula-related issues and actionable recommendations. Its purpose extends beyond mere error detection, as it also contributes to improving debugging efficiency, optimizing performance, and ensuring alignment with best practices. The ongoing commitment of the PowerApps team involves continuous investment and expansion of the App checker, aiming to simplify the debugging process and empower developers with informed decision-making in app development.

![A screenshot of a computer Description automatically generated](media/image34.png)

![A screenshot of a checklist Description automatically generated](media/image35.png)

### Accessibility Checker

The Accessibility Checker functions in a manner similar to the formula errors checker, scrutinizing your app for potential accessibility issues and presenting them in a comprehensive list. Presently, the Accessibility Checker offers guidance on enabling keyboard and screen reader support within apps, although it does not currently identify color contrast issues.

Upon select an item from the Accessibility Checker list, it opens the relevant property for addressing the identified issue. Clicking the right chevron reveals detailed information along with a link to additional resources providing insights into creating accessible apps. For more in-depth information on the Accessibility Checker and general principles of accessibility, refer [here](/power-apps/maker/canvas-apps/accessibility-checker).

![A screenshot of a computer Description automatically generated](media/image36.png)

## Application Insights

Azure Application Insights can be used to log telemetry data from Canvas apps in PowerApps. This integration allows you to monitor and gain insights into the performance and usage of your Canvas apps.

To setup Azure App Insights resource follow the given [steps](/power-apps/maker/canvas-apps/application-insights#create-an-application-insights-resource). App Insights can help you track following details from canvas apps

- Where the app is accessed from

- Which devices are used

- The browsers types used, OS and browser versions details of the users

- Number of users who viewed the app

- Region and location of the users

- Number of sessions by the users for the app

- Number of events logged from the app

To see **usage metrics within App Insights,**

![A screenshot of a computer Description automatically generated](media/image37.png)

![A screenshot of a computer Description automatically generated](media/image38.png)

You can further review the custom traces and unhandled errors within the App Insights as well. To this, use **Trace** function. Trace function can be used to log custom telemetry from Canvas Apps to Azure Application Insights. Consider using this when you want to have feedback around User experience.

Formula details - [Trace function - Power Platform | Microsoft Learn](/power-platform/power-fx/reference/function-trace)

```typescript
Trace(

"App Feedback",

TraceSeverity.Information,

{

UserName: User().FullName,

UserEmail: User().Email,

Screen: FeedbackComponent.FeedbackScreen.Name,

FeedbackValue: "-1"

}

);

Notify("Thanks for you feedback!");
```

Once the traces are logged, you can view them by going to logs and review the traces table. Search with Message keyword to begin with.

**Example**


traces \| extend customdims = parse\_json(customDimensions) \| where message == "App Feedback" \| project timestamp , message , AppName = customdims.\['ms-appName'\] , AppId = customdims.\['ms-appId'\] , FeedbackFrom = customdims.UserEmail , Screen = customdims.Screen , FeedbackValue = customdims.FeedbackValue \| order by timestamp desc

----------------------------------------------------------------

traces

\| where timestamp &gt;ago(30m)

\| where session\_Id == "bc03290d-b9c5-4db4-b482-b11915c5efd4"

![A screenshot of a computer Description automatically generated](media/image39.png)

