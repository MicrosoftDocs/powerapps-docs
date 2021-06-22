---
title: Connect to Power BI from Power Apps
description: Learn about connecting to Power BI from Power Apps.
author: lancedMicrosoft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 10/12/2016
ms.author: lanced
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Connect to Power BI from Power Apps

![Power BI](./media/connection-powerbi/powerbiicon.png)

Power BI is a suite of business analytics tools to analyze data and share insights. Monitor your business and get answers quickly with rich dashboards available on every device. In your app, you can check the status of the data alerts that you have set up in the Power BI service. For more information on data alerts in Power BI, head to the [documentation page](/power-bi/service-set-data-alerts).

This topic shows you how to use the Power BI connection in an app, and lists the available functions.

> [!NOTE]
> The Power BI connection is not [delegable](../delegation-overview.md).

## Prerequisites
* [Sign up](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc)
* Add the Power BI [connection](https://powerapps.microsoft.com/tutorials/add-manage-connections/)
* Create an app from a [template](https://powerapps.microsoft.com/tutorials/get-started-test-drive/), from [data](https://powerapps.microsoft.com/tutorials/get-started-create-from-data/), or from [scratch](https://powerapps.microsoft.com/tutorials/get-started-create-from-blank/)

## Use the Power BI connection in your app
### List the alerts that you've set up in the Power BI service
1. On the **Insert** menu, select **Gallery**, and add any of the **Text galleries**.
2. To show the current user's alerts, set the [Items](../controls/properties-core.md) property of the gallery to the following formula:

   `PowerBI.GetAlerts()`

The gallery will update with the list of alerts. For each alert, you will receive the alert name, the ID number of the alert, and the ID of the group workspace in which the alert was configured. You will need the alert ID to get further information about the alert.

### View the status of an alert
To view the status of the alert, call the CheckAlertStatus function with the alert ID obtained from the step above.

The alert ID can be passed in either as a literal string (e.g. "1234") or as a reference to a gallery section populated using the GetAlerts() call (e.g. Gallery1.Selected.alertId)

To proceed, add a label, and then set its [Text](../controls/properties-core.md) property to one of these formulas:

* `PowerBI.CheckAlertStatus( /* alert ID that you received from GetAlert */ ).alertTitle`
* `PowerBI.CheckAlertStatus( /* alert ID that you received from GetAlert */ ).currentTileValue`
* `PowerBI.CheckAlertStatus( /* alert ID that you received from GetAlert */ ).alertThreshold`
* `PowerBI.CheckAlertStatus( /* alert ID that you received from GetAlert */ ).isAlertTriggered`

The label will update with the current status of the alert.

## View the available functions
This connection includes the following functions:

| Function Name | Description |
| --- | --- |
| GetAlerts |List the alerts that you have set up in the Power BI service |
| CheckAlertStatus |Check the status of a particular alert |

## GetAlerts
List the alerts that you have set up in the Power BI service.

#### Input properties
None.

#### Output properties

| Property Name | Data Type | Required | Description |
| --- | --- | --- | --- |
| value |array |No |An array of the data alerts that you have set up in the Power BI service. Each element in the array will include: <ul><li>alertTitle: the title of the alert</li><li>alertId: the ID of the alert</li><li>groupId: the ID of the group that the alert was created in</li></ul> |

## CheckAlertStatus
Check the status of an alert.

> [!NOTE]
> Requests to this endpoint will be throttled on a per-alert basis if called too frequently.

#### Input properties

| Property Name | Data Type | Required | Description |
| --- | --- | --- | --- |
| alertId |integer |Yes |The ID of the alert, as returned by GetAlerts |

#### Output properties

| Property Name | Data Type | Required | Description |
| --- | --- | --- | --- |
| tileValue |number |No |The value of the tile when the alert was triggered |
| tileUrl |string |No |URL for the tile that has the alert |
| alertTitle |string |No |Name of the alert |
| isAlertTriggered |boolean |No |Whether the alert is currently triggered |
| alertThreshold |number |No |The threshold at which the alarm is triggered |

## Helpful links
See all the [available connections](../connections-list.md).  
Learn how to [add connections](../add-manage-connections.md) to your apps.



[!INCLUDE[footer-include](../../../includes/footer-banner.md)]