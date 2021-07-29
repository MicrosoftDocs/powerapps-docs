---
title: "Send in-app notifications within model-driven apps" 
description: Learn how to configure notifications in model-driven apps using client API.
ms.custom: ""
ms.date: 07/30/2021
ms.reviewer: "nabuthuk"
ms.service: powerapps
ms.subservice: mda-maker
ms.topic: "article"
author: "aorth"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---

# Send in-app notifications within model-driven apps (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../../includes/cc-beta-prerelease-disclaimer.md)]

In-app notification system uses the `App Notification` table to store notifications per user. Model-driven app polls the system for new notifications to be shown to the user. The notification sender can indicate if a toast is shown and how it is dismissed. Notifications are present in the notification center until they are dismissed or expired. The default expiration time for a notification defaults is 14 days. The default expiration time for notifications can be overridden by the sender.

This article outlines the steps on how to send in-app notifications to a specific user.

  > [!IMPORTANT]
  > - This is a preview feature, and isn't available in all regions.
  > - [!INCLUDE[cc_preview_features_definition](../../../includes/cc-preview-features-definition.md)]

To use the in-app notification feature, enable the `AllowNotificationsEarlyAccess` app setting in model-driven app.

## Send basic in-app notifications

Since the notification system uses a table, any of the table functionalities can be used to create new notifications.  

> [!div class="mx-imgBorder"] 
> [Mention notification](../../../media/send-in-app-notifications/basic-notification.png "This image shows a mention notification")


The following examples use the notification table and a simple notification record to create this notification.

### Send basic in-app notification using client API

In-app notifications can be sent using the [Create record using client API](reference/xrm-webapi/createrecord.md).

```javascript
var data =
{
  "title": "Welcome",
  "body": "Welcome to the world of app notifications!",
  "owner": "GUID of the user.",
  "icontype": 100000000, // info
  "toasttype": 200000000 // timed
}
// Create notification record
Xrm.WebApi.createRecord("appnotification", data).
  then(
      function success(result) {
          console.log("notification created with ID: " + result.id);
      },
      function (error) {
          console.log(error.message);
          // handle error conditions
      }
  );
```

### Send basic in-app notification using Web API

In-app notifications can be sent using the [Create a table record using Web API](../developer/common-data-service/webapi/create-entity-web-api.md).

```Http
POST [Organization URI]/api/data/v9.0/appnotifications 
HTTP/1.1
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json

{
  "title": "Welcome",
  "body": "Welcome to the world of app notifications!",
  "owner": <Guid of the user.>,
  "icontype": 100000000, // info
  "toasttype": 200000000 // timed
}
```

## Notification table

The follow are the primary fields to send a user a notification.

|Column|Description|
|---|---|
|Title|Title of the notification.
|Owner|User who receives the notification.
|Body|Details of the notification.
|Icon Type|List of predefined icons. The default value is `Info`. |
|Toast Type|List of toast behaviors. The default value is `Timed`.|
|Expires on|Date when notification should be deleted if not already dismissed.|

### Changing the toast notification behavior

An in-app notification behavior can be changed by setting **Toast Type** to one of the following values:

|Toast Type|Behavior|Value|
|---|---|---|
|Timed|Notification appears for a brief duration and then disappears. (default 4 seconds)|200000000|
|Hidden|Notification appears only in the notification center and not as a toast.|200000001|

### Changing the notification icon

An in-app notification icon can be changed by setting **Icon Type** to one of the predefined values:

|Icon Type|Value|
|---|---|
|Info|100000000|
|Success|100000001|
|Failure|100000002|
|Warning|100000003|
|Mention|100000004|
|Custom|100000005|

## Changing the navigation target in notification link

An in-app notification link can target different locations. 

|Navigation target|Behavior|Example|
|----------|-----------|-----------|
|Dialog|Opens in center dialog.|`"navigationTarget": "dialog"` |
|Inline|Default. Opens in the current page.|`"navigationTarget": "inline"` |
|newWindow|Opens in the new browser tab.|`"navigationTarget": " newWindow"` |

## Examples

### Notification with action link

Within the body of the notification include an **action** with one of the following patterns.

#### Notification action link opening full URL

By adding **actions** with title and full URL, the user click will open in a new browser tab.

```json
{
  "data": {
    "actions": [
      {
        "title": "Open Bing",
        "data" : {
          "url": "https://bing.com"
        }
      }
    ]
  }
}
```

### Notification with one action 
 
```JavaScript
var notificationRecord = 
{ 
  "title": "Congratulations!", 
  "body": "Your customer rating is now an A. You resolved 80% of your cases within SLA this week and average customer rating was A+.", 
  "owner": "<user-guid>", 
  "icontype": 100000001, // success 
  "data": JSON.stringify({ 
    "actions": [ 
      { 
        "title": "View Cases", 
        "data": { 
        "url": "?pagetype=entitylist&etn=incident&viewid=bad2fbea-2673-df11-986c-00155d2e3002&viewType=1039" 
        } 
      } 
    ] 
  }) 
} 

Xrm.WebApi.createRecord("appnotification", notificationRecord);
``` 

### Notification with multiple primary actions 

This is another notification example with a custom body with an inline link and bold styling. Coho Winery has a service appointment coming up on 4/1/2021.Call Jim Glynn to confirm appointment. 

```javascript
// Notification with multiple primary actions as center dialog 
var notificationRecord = 
{ 
  "title": "Upcoming Service Reminder", 
  "body": "", 
  "owner": "<user-guid>", 
  "icontype": 100000005, // custom 
  "data": JSON.stringify({ 
    "body": "Coho Winery has a service appointment coming up on 4/1/2021. Call **[Jim Glynn](?pagetype=entityrecord&etn=contact&id=03f770b2-6567-eb11-bb2b-000d3ac2be4d)** to confirm appointment.", 
    "iconUrl": "/WebResources/contoso_Phone", 
    "actions": [ 
      { 
        "title": "Coho Winery", 
        "data": { 
          "url": "?pagetype=entityrecord&etn=account&id=9df670b2-6567-eb11-bb2b-000d3ac2be4d", 
          "navigationTarget": "dialog" 
        } 
      }, 
      { 
        "title": "Service Appointment", 
        "data": { 
          "url": "?pagetype=entityrecord&etn=appointment&id=03f770b2-6567-eb11-bb2b-000d3ac2be4d", 
          "navigationTarget": "dialog" 
        } 
      } 
    ] 
  }) 
} 

Xrm.WebApi.createRecord("appnotification", notificationRecord);
``` 

### Notification with custom body 

This example has a custom body with an inline link and bold styling. 

```javascript
var notificationRecord = 
{ 
  "title": "SLA critical", 
  "body": "Case record assigned to you is critically past SLA", 
  "owner": "<user-guid>", 
  "icontype": 100000002, // failure 
  "data": JSON.stringify({ 
    "body": "Case record [Complete overhaul required (sample)](?pagetype=entityrecord&etn=incident&id=b1f670b2-6567-eb11-bb2b-000d3ac2be4d) assigned to you is **critically** past SLA and has been escalated to your manager." 
  }) 
} 
Xrm.WebApi.createRecord("appnotification", notificationRecord);
```

This is another example with a custom body with an inline link and bold styling. 

```javascript
var notificationRecord = 
{ 
  "title": "SLA missed", 
  "body": "Case record assigned to you is critically past SLA", 
  "owner": "<user-guid>", 
  "icontype": 100000003, // warning 
  "data": JSON.stringify({ 
    "body": "Case record [Average order shipment time (sample)](?pagetype=entityrecord&etn=incident&id=aff670b2-6567-eb11-bb2b-000d3ac2be4d) assigned to you just went out of SLA." 
  }) 
} 

Xrm.WebApi.createRecord("appnotification", notificationRecord);
```

### Notification with custom icon

Within the notification, set Icon to **Custom** and in body include **iconUrl** with a value pointing to a web resource.  The notification work with either SVG or PNG file types.

> [!div class="mx-imgBorder"] 
> [Mention notification](media/send-in-app-notifications/welcome-notification.png "This image shows a mention notification")

```json
var data =
{
  "title": "Welcome",
  "body": "Welcome to the world of app notifications!",
  "owner": "<user-guid>",
  "icontype": 100000005, // custom
  "data": "{ 'data': { 'iconUrl': '/WebResources/cr245_AlertOn' } }"
}
```

### Notification with custom title and body

This notification example adds custom title and body definition, which allow multiple links, bold, and italics. 

> [!div class="mx-imgBorder"] 
> ![Mention notification](media/send-in-app-notifications/mention-notification.png "This image shows a mention notification")

```json
var data =
{
  "title": "Complete overhaul required (sample)",
  "body": "Maria Campbell mentioned you in a post",
  "owner": "<user-guid>",
  "icontype": 100000004, // mention
  "data": "{
    "title": "[Complete overhaul required (sample)](?pagetype=entityrecord&etn=incident&id=b1f670b2-6567-eb11-bb2b-000d3ac2be4d)",
    "body": "[Maria Campbell](?pagetype=entityrecord&etn=contact&id=f7f670b2-6567-eb11-bb2b-000d3ac2be4d) mentioned you in a post: _\"**[@Paul](?pagetype=entityrecord&etn=contact&id=fff670b2-6567-eb11-bb2b-000d3ac2be4d)** we need to prioritize this overdue case, [@Robert](?pagetype=entityrecord&etn=contact&id=fdf670b2-6567-eb11-bb2b-000d3ac2be4d) will work with you to engage engineering team ASAP.\"_",
    "actions": [
      {
        "title": "View record",
        "data": {
          "url": "?pagetype=entityrecord&etn=incident&id=b1f670b2-6567-eb11-bb2b-000d3ac2be4d"
        }
      }
    ]
  }
}"
}

```

## In-app notifications vs. push notifications

Power Apps Notification Connector is for push notifications and is separate from the In-app Notification. The push notification only appears in the mobile device notifications list to prompt to open the app.  The in-app notification appears when the app is open.  We recommend limiting use of push notification to higher priority items to avoid overwhelming the user.

- [Power Apps Notification Connector](https://docs.microsoft.com/connectors/powerappsnotification)
- [Power Apps Notification Connector V2](https://docs.microsoft.com/connectors/powerappsnotificationv2/)
- [Create push notifications for the Power Apps mobile app](../../../mobile/power-apps-mobile-notification.md)

## Related articles

- [Create an entity record using the Web API](../../developer/data-platform/webapi/create-entity-web-api.md)
- [Create an entity record with Client API](reference/xrm-webapi/createrecord.md)
- [Use in-app notifications](../../user/use-in-app-notifications.md)