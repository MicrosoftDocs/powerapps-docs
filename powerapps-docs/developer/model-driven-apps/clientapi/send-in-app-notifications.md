---
title: "Send in-app notifications within model-driven apps" 
description: Learn how to configure notifications in model-driven apps using client API.
ms.date: 08/23/2021
ms.reviewer: "nabuthuk"
ms.service: powerapps
ms.subservice: mda-developer
ms.topic: "article"
author: "aorth"
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - maker
  - developer
search.app: 
  - "PowerApps"
  - D365CE
---

# Preview: Send in-app notifications within model-driven apps 

[!INCLUDE [cc-beta-prerelease-disclaimer](../../../includes/cc-beta-prerelease-disclaimer.md)]

App notifications use the notification table to store notifications for each user. Your model-driven app will automatically check the system for new notifications and displays them in the notification center. The notification sender or your system administrator can configure how a toast is shown and how it can be dismissed. Notifications appear in notification center until you dismiss them or until they expire. By default, a notification expires after 14 days but your administrator can override this time.

Each notification record is for a single user identified by the owner column value. If a notification needs to be sent to multiple users, then a record needs to be inserted per recipient. The sender controls the recipient through the owner column.

This article outlines the steps on how to send in-app notifications to a specific user using [Client API](reference.md).

  > [!IMPORTANT]
  > - This is a preview feature, and isn't available in all regions.
  > - [!INCLUDE[cc_preview_features_definition](../../../includes/cc-preview-features-definition.md)]

## Enable in-app notification feature

To use the in-app notification feature, you need enable the `AllowNotificationsEarlyAccess` app setting in model-driven app.

1. Sign in to your model-driven app.
1. Select the app where you want to use this feature.
1. Select **F12** button on your keyboard to open the browser console.
1. In the browser console, copy the code below. Enter your app unique name in the `AppUniqueName` parameter. Press **Enter**.   

   ```javascript
   fetch(window.origin + "/api/data/v9.1/SaveSettingValue()",{
    method: "POST", 
	  headers: {'Content-Type': 'application/json'},
	  body: JSON.stringify({AppUniqueName: "Your app unique name", SettingName:"AllowNotificationsEarlyAccess", Value: "true"})
	  });
   ```
1. Now sign in to [Power Apps](https://make.powerapps.com).
1. Select **Solutions** in the left navigation pane. Select **New solution**. Enter the details and then select **Create**. 
1. Open the solution that you have created. Select **Add** > **App** > **Model-driven app**. From the list of apps, select the model-driven app where you want to see the notifications feature.
1. Select **Publish all customizations**. Refresh the model-driven app, you should see a **Bell** icon on the top-right corner.

> [!TIP]
> The logical name of your model-driven app can be found in the solution explorer under the **Name** column. 

## Send basic in-app notifications

Since the notification system uses a table, any of the table functionalities can be used to create new notifications.  

> [!div class="mx-imgBorder"] 
> ![Welcome notification](../media/welcome-notification.png "Welcome notification")


The following examples use the notification table and a notification record to create notifications.

### Send basic in-app notification using client API

In-app notifications can be sent by [Creating record using client API](reference/xrm-webapi/createrecord.md).

```javascript
var systemuserid = "Guid of the user";
var notificationRecord =
{
  "title": "Welcome",
  "body": "Welcome to the world of app notifications!",
  "ownerid@odata.bind": "/systemusers(" + systemuserid + ")",
  "icontype": 100000000, // info
  "toasttype": 200000000 // timed
}
// Create notification record
Xrm.WebApi.createRecord("appnotification", notificationRecord).
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

In-app notifications can be sent by [Creating a table row using the Web API](../../data-platform/webapi/create-entity-web-api.md).

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
  "ownerid@odata.bind": "/systemusers(<Guid of the user>)",
  "icontype": 100000000, // info
  "toasttype": 200000000 // timed
}
```

## Notification table

The following are the columns for the notification table:

|Column|Description|
|---|---|
|Title|Title of the notification.|
|Owner|User who receives the notification.|
|Body|Details of the notification.|
|Icon Type|List of predefined icons. The default value is `Info`. More information: [Notification icons](#changing-the-notification-icon)|
|Toast Type|List of toast behaviors. The default value is `Timed`. More information: [Toast types](#changing-the-toast-notification-behavior)|
|Expiry (seconds)|Number of seconds from when the notification should be deleted if not already dismissed.|
|Data|Json that is used for extensibility and parsing richer data into the notification. Maximum length is 5000.|

### Changing the toast notification behavior

An in-app notification behavior can be changed by setting **Toast Type** to one of the following values:

|Toast Type|Behavior|Value|
|---|---|---|
|Timed|Notification appears for a brief duration and then disappears. (default 4 seconds)|200000000|
|Hidden|Notification appears only in the notification center and not as a toast.|200000001|

### Changing the notification icon

An in-app notification icon can be changed by setting **Icon Type** to one of the following values. When using a custom icon, a `iconUrl` parameter should be specified within the `data` parameter.

|Icon Type|Value|
|---|---|
|Info|100000000|
|Success|100000001|
|Failure|100000002|
|Warning|100000003|
|Mention|100000004|
|Custom|100000005|

### Changing the navigation target in notification link

You can control where a navigation link should open by setting the `navigationTarget` parameter. 

|Navigation target|Behavior|Example|
|----------|-----------|-----------|
|Dialog|Opens in center dialog.|`"navigationTarget": "dialog"` |
|Inline|Default. Opens in the current page.|`"navigationTarget": "inline"` |
|newWindow|Opens in the new browser tab.|`"navigationTarget": "newWindow"` |

### Managing security for notifications

The in-app notification feature uses three tables, and a user needs to have the correct security roles to receive notifications and send notifications to themselves, or other users.  

|Usage|Needed table privileges|
|------------|----------------|
|User has no in-app notification bell and receives no in-app notifications toasts |None: Read privilege on app notification table. |
|User can receive in-app notifications|- Basic: Read privilege on app notification table.<br/> - Create and read privilege on model-driven app user setting.|
|User can send in-app notifications to self |- Basic: Create privilege on app notification table. <br/> - Write and append privilege on model-driven app user setting. <br/> - Append privilege on setting definition. |
|User can send in-app notifications to others |Read privilege with Local, Deep, or Global access level on app notification table based on the receiving user's business unit. |


### Notification storage

The app notification table uses the organization's database storage capacity. Because of this, it is important to consider the volume of notifications sent and the expiration setting. More information: [Microsoft Dataverse storage capacity](/power-platform/admin/capacity-storage)

## Examples

### Notification with action link

The following examples show how to create notifications with actions, custom body, and custom icons.

#### Action with title and URL

This example shows how to create a notification by adding title and URL to the **actions** parameter.

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

This example shows how to create a notification by adding one action to the **actions** parameter.

> [!div class="mx-imgBorder"] 
> ![App notification with single action](../media/app-notification-with-single-action.png "App notification with single action")

```JavaScript
var systemuserid = "<user-guid>";
var notificationRecord = 
{
    "title": "Congratulations",
	  "body": "Your customer rating is now an A. You resolved 80% of your cases within SLA thi week and average customer rating was A+",
	  "ownerid@odata.bind": "/systemusers(" + systemuserid + ")",
    "icontype": 100000001, // success
    "data": JSON.stringify({
	 "actions": [
	  {
        "title": "View cases",
        "data": {
		"url": "?pagetype=entitylist&etn=incident&viewid=00000000-0000-0000-00aa-000010001028&viewType=1039"
		}		
	  }
	 ]
	})
}
Xrm.WebApi.createRecord("appnotification", notificationRecord).
  then(
      function success(result) {
          console.log("notification created with single action: " + result.id);
      },
      function (error) {
          console.log(error.message);
          // handle error conditions
      }
  );
``` 

### Notification with multiple actions 

This example shows how to create a notification with multiple actions.

> [!div class="mx-imgBorder"] 
> ![App notification with multiple actions](../media/app-notification-with-multiple-actions.png "App notification with multiple actions")


```JavaScript
// Notification with multiple actions as center dialog 
var systemuserid = "<user-guid>";
var notificationRecord = 
{
    "title": "Upcoming Service Reminder",
	  "body": "This is to inform you that you have an upcoming service request for your vehicle.",
	  "ownerid@odata.bind": "/systemusers(" + systemuserid + ")",
    "icontype": 100000000, // info
    "data": JSON.stringify({
	   "actions": [
	    {
        "title": "Cohor Winery",
        "data": {
		    "url": "?pagetype=entityrecord&etn=account&id=b0a19cdd-88df-e311-b8e5-6c3be5a8b200",
		    "navigationTarget": "dialog"
		       }		
	    },
	    {
	      "title": "Service Appointment",
        "data": {
		    "url": "?pagetype=entityrecord&etn=appointment&id=96db3cf0-e605-ec11-94ef-000d3a36469a",
		    "navigationTarget": "dialog"
	        }
	    }
	 ]
	})
}
Xrm.WebApi.createRecord("appnotification",notificationRecord).
  then(
      function success(result) {
          console.log("notification created with multiple actions: " + result.id);
      },
      function (error) {
          console.log(error.message);
          // handle error conditions
      }
  );
``` 

### Notification with custom body 

This example shows how to create a notification by adding custom body with an inline link and bold styling. 

> [!div class="mx-imgBorder"] 
> ![Notification ith custom body](../media/app-notification-with-custom-body.png "Notification with custom body")

```javascript
var systemuserid = "<user-guid>";
var notificationRecord = 
{
    "title": "SLA critical",
	"body": "Records assigned to you is critically past SLA.",
	"ownerid@odata.bind": "/systemusers(" + systemuserid + ")",
    "icontype": 100000002, // failure
    "data": JSON.stringify({
	 "body": "Case record [Complete overhaul required (sample)](?pagetype=entityrecord&etn=incident&id=0a9f62a8-90df-e311-9565-a45d36fc5fe8) assigned to you is critically past SLA and has been escalated to your manager."
	 })
}
Xrm.WebApi.createRecord("appnotification",notificationRecord).
  then(
      function success(result) {
          console.log("notification created with custom body: " + result.id);
      },
      function (error) {
          console.log(error.message);
          // handle error conditions
      }
  );
```

This is another example with a custom body with an inline link and bold styling. 

> [!div class="mx-imgBorder"] 
> ![Notification with bold text](../media/app-notification-with-custom-body-and-bold-text.png "Notification with bold text")


```JavaScript
var systemuserid = "<user-guid>";
var notificationRecord = 
{
    "title": "SLA Missed",
	"body": "Records assigned to you is critically past SLA.",
	"ownerid@odata.bind": "/systemusers(" + systemuserid + ")",
    "icontype": 100000003, // warning
    "data": JSON.stringify({
	 "body": "Case record [Average order shipment time (sample)](?pagetype=entityrecord&etn=incident&id=0a9f62a8-90df-e311-9565-a45d36fc5fe8) **assigned** to you just went out of SLA."
	 })
}
Xrm.WebApi.createRecord("appnotification",notificationRecord).
then(
      function success(result) {
          console.log("notification created with custom body and bold styling: " + result.id);
      },
      function (error) {
          console.log(error.message);
          // handle error conditions
      }
  );
```

### Notification with custom icon

This example shows how to create a notification by adding custom icons. Within the notification, set **iconType** to **Custom** and in the body include **iconUrl** with a value pointing to a web resource.  The notification work with either SVG or PNG file types.

> [!div class="mx-imgBorder"] 
> ![Notification with custom icon](../media/app-notification-with-custom-icon.png "Notification with custom icon")

```JavaScript
var systemuserid = "<user-guid>";
var notificationRecord = 
{
  "title": "Welcome",
  "body": "Welcome to the world of app notifications!",
  "ownerid@odata.bind": "/systemusers(" + systemuserid + ")",
  "icontype": 100000005, // custom
  "data": "{ 'data': { 'iconUrl': '/WebResources/cr245_AlertOn' } }"
}
Xrm.WebApi.createRecord("appnotification", notificationRecord).
  then(
      function success(result) {
          console.log("notification created with custom icon: " + result.id);
      },
      function (error) {
          console.log(error.message);
          // handle error conditions
      }
  );
```

### Notification with custom title and body

This notification example adds custom title and body definition, which allow multiple links, bold, and italics. 

> [!div class="mx-imgBorder"] 
> ![Notification with custom title and body ](../media/app-notification-with-custom-title-body.png "Notification with custom title and body")

```JavaScript
var systemuserid = "<user-guid>";
var notificationRecord = 
{
    "title": "Complete overhaul required (sample)",
	"body": "Maria Campbell mentioned you in a post.",
	"ownerid@odata.bind": "/systemusers(" + systemuserid + ")",
    "icontype": 100000004, // mention
    "data": JSON.stringify({
	 "title": "[Complete overhaul required (sample)](?pagetype=entityrecord&etn=incident&id=0a9f62a8-90df-e311-9565-a45d36fc5fe8)",
	 "body": "[Maria Campbell](?pagetype=entityrecord&etn=contact&id=43m770h2-6567-ebm1-ob2b-000d3ac3kd6c) mentioned you in a post: _\"**[@Paul](?pagetype=entityrecord&etn=contact&id=03f770b2-6567-eb11-bb2b-000d3ac2be4d)** we need to prioritize this over due case, [@Robert](?pagetype=entityrecord&etn=contact&id=73f970b2-6567-eb11-bb2b-000d3ac2se4h) will work with you to engage with engineering team ASAP.\"_",
	  "actions": [
	   {
	     "title": "View record",
		 "data": {
		 "url": "?pagetype=entityrecord&etn=incident&id=0a9f62a8-90df-e311-9565-a45d36fc5fe8"
		 }
	   }
	  ]
	 })
}
Xrm.WebApi.createRecord("appnotification",notificationRecord).
  then(
      function success(result) {
          console.log("notification created with custom title and body: " + result.id);
      },
      function (error) {
          console.log(error.message);
          // handle error conditions
      }
  );
```

## In-app notifications vs push notifications

Power Apps Notification Connector is for push notifications and is separate from the in-app notification. Push notification only appears on the mobile device notifications list to open the app.  The in-app notification appears when the app is open.  We recommend limiting the use of push notification to higher priority items to avoid overwhelming the user.

- [Power Apps Notification Connector](https://docs.microsoft.com/connectors/powerappsnotification)
- [Power Apps Notification Connector V2](https://docs.microsoft.com/connectors/powerappsnotificationv2/)
- [Create push notifications for the Power Apps mobile app](../../../mobile/power-apps-mobile-notification.md)

## Related articles

- [Create an entity record using the Web API](../../data-platform/webapi/create-entity-web-api.md)
- [Create an entity record with Client API](reference/xrm-webapi/createrecord.md)
- [Use in-app notifications](../../../user/notifications.md)
