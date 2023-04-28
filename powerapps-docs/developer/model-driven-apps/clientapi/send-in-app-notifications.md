---
title: "Send in-app notifications within model-driven apps" 
description: Learn how to configure notifications in model-driven apps by using a client API.
ms.date: 02/22/2023
ms.reviewer: jdaly
ms.service: powerapps
ms.subservice: mda-developer
ms.topic: article
author: adrianorth
ms.author: aorth 
search.audienceType: 
  - maker
  - developer
contributors: 
  - JimDaly
  - caburk
---

# Send in-app notifications within model-driven apps

Developers of model-driven apps can configure notifications to be displayed to app users as a toast or within the notification center. Your model-driven app automatically polls the system for new notifications and displays them to the user. The notification sender or your system administrator can configure how the notification is shown and how it can be dismissed. Notifications appear in the notification center until the recipient dismisses them or they expire. By default, a notification expires after 14 days but your administrator can override this setting.

Notifications are user-specific. Each notification is intended for a single user, identified as the recipient when the notification is sent. If a notification needs to be sent to multiple users, individual notifications must be created and sent for each recipient.

This article outlines the steps for how to send in-app notifications to a specific user by using a [client API](reference.md). To see how these notifications appear in applications, see [In-app notifications in model-driven apps](/powerapps/user/notifications).

## Enable the in-app notification feature

To use the in-app notification feature, you need to enable the **In-app notifications** setting.  This setting is stored within the model-driven app.

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Open the solution that contains the model-driven app.  

1. Select the model-driven app and click **Edit** split menu to open using the modern app designer.

1. Open **Settings** and switch to **Features**.

1. Enable "In-app notifications".

    > [!div class="mx-imgBorder"]
    > ![Custom page as main page](media/send-in-app-notifications/app-designer-settings-enable-in-app-notifications.png "Custom page as main page")

1. Click **Save** to save the settings change.

1. Click **Publish** on the model-driven app.


## Send basic in-app notifications

Notifications can be sent using the `SendAppNotification` API. The following basic examples show how to use the API to send in-app notifications.

> [!div class="mx-imgBorder"] 
> ![Screenshot of a Welcome notification.](../media/welcome-notification.png "Welcome notification")

# [Client API](#tab/clientapi)

In-app notifications can be sent by using the [createRecord](reference/xrm-webapi/createrecord.md) API.

```javascript
//THIS NEEDS TO BE UPDATED WITH CORRECT SYNTAX FOR SENDAPPNOTIFICATION

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

# [Web API](#tab/webapi)

In-app notifications can be sent by using the Web API. More information: [Use Web API actions](../../data-platform/webapi/use-web-api-actions.md).

```http
POST [Organization URI]/api/data/v9.0/sendappnotification 
HTTP/1.1
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json

{
  "Title": "Welcome",
  "Body": "Welcome to the world of app notifications!",
  "Recipient": "/systemusers(<Guid of the user>)",
  "IconType": 100000000, // info
  "ToastType": 200000000 // timed
}
```

# [Dataverse SDK](#tab/sdk)

In-app notifications can be sent by using the Dataverse SDK with the organization service. More information: [IOrganizationService Interface](../../data-platform/org-service/iorganizationservice-interface.md)

```csharp

OrganizationRequest request = new OrganizationRequest()
{
    RequestName = "SendAppNotification",
    Parameters = new ParameterCollection
    {
        ["Title"] = "Welcome",
        ["Recipient"] = new EntityReference("systemuser", <Guid of the user>),
        ["Body"] = "Welcome to the world of app notifications!",
        ["IconType"] = new OptionSetValue(100000000), //info
        ["ToastType"] = new OptionSetValue(200000000) //timed
     }
};

OrganizationResponse response = currentUserService.Execute(request);
Guid appNotificationId = (Guid)response.Results["NotificationId"];
```

# [Power Fx](#tab/powerfx)

In-app notifications can be sent from Power Apps using Power Fx. More information: [Microsoft Power Fx overview](https://learn.microsoft.com/en-us/power-platform/power-fx/overview).

```powerapps-dot
XSendAppNotification(
  "Welcome",
  LookUp(Users,'Primary Email'="<User email address>",
  "Welcome to the world of app notifications!"
)
```

---

## Notification polling

In-app notifications use polling to retrieve notifications periodically when the app is running.  New notifications are retrieved at start of the model-driven app and when a page navigation occurs as long as the last retrieval is more than one minute ago.  If a user stays on a page for a long duration, new notifications won't be retrieved until the user navigates to another page.

## Notification table

Notifications are stored in the **Notification** (`appnotification`) table. The following are the columns for the table.

|Column display|Column name|Description|
|---|---|---|
|Title|`title`|The title of the notification.|
|Owner|`ownerid`|The user who receives the notification.|
|Body|`body`|Details about the notification.|
|IconType|`icontype`|The list of predefined icons. The default value is `Info`. For more information, go to [Changing the notification icon](#changing-the-notification-icon) later in this article.|
|Toast Type|`toasttype`|The list of notification behaviors. The default value is `Timed`. For more information, go to [Changing the notification behavior](#changing-the-notification-behavior) later in this article.|
|Expiry (seconds)|`ttlinseconds`|The number of seconds from when the notification should be deleted if not already dismissed.|
|Data|`data`|JSON that's used for extensibility and parsing richer data into the notification. The maximum length is 5,000 characters.|

  > [!IMPORTANT]
  > - The `appmoduleid` field is not used.

## Customizing the notifiction
In addition to the basic properties of the notification, there are options for customizing the notification delivered to the user. This includes changing the styles in the **Title** and **Body** of the notification, customizing the notification icon, and changing the behavior of the notification.

### Using markdown in Title and Body

The **Title** and **Body** attributes of the `SendAppNotification` API do not support markdown defined within the properties. You can adjust the styles of these properties using markdown in the **OverrideContent** property. This field supports overriding the Title and Body simple strings with a limited subset of markdown styles.

The following is the supported markdown.

|Text Style|Markdown|
|---|---|
|Bold|`**Bold**`|
|Italic|`_Italic_`|
|Bullet list|`- Item 1\r- Item 2\r- Item 3`|
|Numbered list|`1. Green\r2. Orange\r3. Blue`|
|Hyperlinks|`[Title](url)`|

Newlines can be included with the body using `\n\n\n\n`.

The following are examples of overriding the title and body properties with markdown.

# [Client API](#tab/clientapi)

```javascript
//THIS NEEDS TO BE UPDATED WITH CORRECT SYNTAX FOR SENDAPPNOTIFICATION

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

# [Web API](#tab/webapi)

```http
POST [Organization URI]/api/data/v9.0/sendappnotification 
HTTP/1.1
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json

{
  "Title": "Welcome",
  "Body": "Welcome to the world of app notifications!",
  "Recipient": "/systemusers(<Guid of the user>)",
  "IconType": 100000000, // info
  "ToastType": 200000000 // timed,
  "OverrideContent": {
    "@odata.type": "#Microsoft.Dynamics.CRM.expando",
    "title": "**Welcome**",
    "body": "Welcome to the world of [app notifications](https://www.bing.com/search?q=app+notifications)!"
  }
}
```

# [Dataverse SDK](#tab/sdk)

```csharp

OrganizationRequest request = new OrganizationRequest()
{
    RequestName = "SendAppNotification",
    Parameters = new ParameterCollection
    {
        ["Title"] = "Welcome",
        ["Recipient"] = new EntityReference("systemuser", <Guid of the user>),
        ["Body"] = "Welcome to the world of app notifications!",
        ["IconType"] = new OptionSetValue(100000000), //info
        ["ToastType"] = new OptionSetValue(200000000) //timed
        ["OverrideContent"] = new Entity()
        {
          Attributes = 
          {
            ["title"] = "**Welcome**",
            ["body"] = "Welcome to the world of [app notifications](https://www.bing.com/search?q=app+notifications)!"
          }
        }
     }
};

OrganizationResponse response = currentUserService.Execute(request);
Guid appNotificationId = (Guid)response.Results["NotificationId"];
```

>[!NOTE]
>OverrideContent is not supported in Power Fx with the `SendAppNotification` API.


---

### Changing the notification behavior

You can change in-app notification behavior by setting **Toast Type** to one of the following values.

|Toast Type|Behavior|Value|
|---|---|---|
|Timed|The notification appears for a brief duration (the default is four seconds) and then disappears.|`200000000`|
|Hidden|The notification appears only in the notification center and not as a toast notification.|`200000001`|

### Changing the notification icon

You can change the in-app notification icon by setting **Icon Type** to one of the following values. When using a custom icon, specify the `iconUrl` parameter within the `OverrideContent` parameter.

|Icon Type|Value|Image|
|---|---|---|
|Info|`100000000`|:::image type="content" source="media/send-in-app-notifications/app-notification-info-icon.png" alt-text="Info Icon":::|
|Success|`100000001`|:::image type="content" source="media/send-in-app-notifications/app-notification-success-icon.png" alt-text="Success Icon":::|
|Failure|`100000002`|:::image type="content" source="media/send-in-app-notifications/app-notification-failure-icon.png" alt-text="Failure Icon":::|
|Warning|`100000003`|:::image type="content" source="media/send-in-app-notifications/app-notification-warning-icon.png" alt-text="Warning Icon":::|
|Mention|`100000004`|:::image type="content" source="media/send-in-app-notifications/app-notification-mention-icon.png" alt-text="Mention Icon":::|
|Custom|`100000005`||

The following example demonstrates using Web API to send a notification with a custom icon.

```http
POST [Organization URI]/api/data/v9.0/sendappnotification 
HTTP/1.1
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json

{
  "Title": "Welcome",
  "Body": "Welcome to the world of app notifications!",
  "Recipient": "/systemusers(<Guid of the user>)",
  "IconType": 100000005, // custom
  "ToastType": 200000000 // timed,
  "OverrideContent": {
    "@odata.type": "#Microsoft.Dynamics.CRM.expando",
    "title": "**Welcome**",
    "body": "Welcome to the world of [app notifications](https://www.bing.com/search?q=app+notifications)!",
    "iconUrl": "https://<web address>/<file name>" //URL of the image file to be used for the notification icon
  }
}
```

## Notification actions

In-app notifications support zero to many actions on the notification card. There are three supported action types:

- **URL**: When the action is selected the web browser navigates to the defined URL.
- **Side Pane**: When the action is selected, a side pane is opened in the app and loads the defined context in the pane.
- **Teams Chat**: When the action is selected, a Teams chat is initiated with defined users in the context of a Dynamics 365 record.

### Defining a URL action type

You can control where a navigation link opens by setting the `navigationTarget` parameter. 

|Navigation target|Behavior|Example|
|----------|-----------|-----------|
|`dialog`|Opens in the center dialog.|`"navigationTarget": "dialog"` |
|`inline`|Default. Opens in the current page.|`"navigationTarget": "inline"` |
|`newWindow`|Opens in a new browser tab.|`"navigationTarget": "newWindow"` |

### Defining a side pane action

A side pane action enables opening a side pane to load a defined page when the action is selected from the app notification. See [Creating side panes by using a client API](./create-app-side-panes.md) for more information.

When using the side pane action type, you have control over the options of the side pane itself, and the page that loads in the side pane.
- See [createPane](./reference/xrm-app/xrm-app-sidepanes/createpane.md) for the optional parameters for the pane that is created.
- See [navigateTo (Client API reference](./reference/xrm-navigation/navigateto.md) for the parameters to be defined for the page that will be loaded in the side pane.

### Defining a Teams chat action

A Teams chat action enables scenarios where a Teams chat is initiated from the app notification. This uses the embedded Teams feature for Dynamics 365 apps, which provides sellers and agents the ability to chat in Microsoft Teams from within the customer engagement apps, such as Sales Hub, Customer Service Hub, and custom apps. 

>[!NOTE]
>Microsoft Teams chat in Dynamics 365 must be enabled to use the Teams chat action type. See [Work with Microsoft Teams chat in Dynamics 365](/dynamics365/teams-integration/enable-teams-chat.md) for more information.

The action type provides the following options:
- Create a new chat session or open an existing chat session.
- Link the chat session to a Dynamics 365 record or create an unlinked chat.

The following are the parameters for defining a Teams chat action on the app notification.

|Parameter | Data type | Description | 
|----------|-----------|-------------|
|chatId    |GUID       |Define a value for the chat ID to open an existing chat. This is the **Teams Chat Id** property of the **Microsoft Teams chat association entity (msdyn_teamschatassociation)** table for chats linked to a Dynamics 365 record, or the **id** property of the **chat** entity from Microsoft Graph. See [Get chat](https://learn.microsoft.com/graph/api/chat-get) for more information.<br><br> If a value is not defined for this parameter then a new chat session will be initiated. |
|memberIds |GUID       |This is an array of the AAD user ID values of each of the participants that will be included in a new chat session. Member ID values should not be defined if a value has been defined for the **chatId** parameter. If the **chatId** has been defined, then the existing chat will be opened, and the members of the existing chat will be included in the chat when opened. |
|entityContext | Expando |The entity context provides the Dynamics 365 record to which the chat session should be linked. For example, if the chat session is regarding a specific customer account record, define the account record in this parameter to have the chat session linked to the account and display in the account's timeline. <br><br>The entity context includes the **entityName** and **recordId** parameters, which must be defined to identify the record for the entity context.<br><br> An entity context should not be defined if a value has been defined for the **chatId** parameter. If the **chatId** has been defined, then the existing chat will be opened, and the entityContext, whether linked or unlinked, will already have been defined for the existing chat. If the action is creating a new chat session (i.e. the **chatId** parameter has not been provided), and the the entity context is not defined, then the new chat session will not be linked to a Dynamics 365 record. |
|entityName | String | Part of the entity context, this is the logical name of the Dataverse table for the record to which the chat will be linked. |
|recordId | GUID | Part of the entity context, this is the ID property of the table defined in the **entityName** parameter for the record to which the chat will be linked. |
|chatTitle | String | The title of the Teams chat. |
|initialMessage | String | The text of an introduction message you may optionally provide that will be automatically sent when the chat is created. |

## Managing security for notifications

The in-app notification feature uses three tables. A user needs to have the correct security roles to receive notifications and to send notifications to themselves or other users.  

|Usage|Required table privileges|
|------------|----------------|
|User has no in-app notification bell and receives no in-app notification |None: Read privilege on the app notification table. |
|User can receive in-app notifications|<ul><li>Basic: Read privilege on the app notification table.</li><li>Create, Read, Write, and Append privileges on the model-driven app user setting.</li><li>Read and AppendTo privileges on setting definition.</li></ul> |
|User can send in-app notifications to self |Basic: Create and Read privileges on the app notification table. |
|User can send in-app notifications to others |Read privilege with Local, Deep, or Global access level on the app notification table based on the receiving user's business unit. |


### Notification storage

Because the app notification table uses the organization's database storage capacity, it's important to consider the volume of notifications sent and the expiration setting. More information: [Microsoft Dataverse storage capacity](/power-platform/admin/capacity-storage)

## Examples

The following examples show how to create notifications that include actions, custom body definitions, and custom icons.

### Notification with an action that has a title and URL

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
> ![App notification with a single action.](../media/app-notification-with-single-action.png "App notification with a single action")

```javascript
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

This example shows how to create a notification that includes multiple actions.

> [!div class="mx-imgBorder"] 
> ![App notification with multiple actions.](../media/app-notification-with-multiple-actions.png "App notification with multiple actions")


```javascript
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
        "title": "Coho Winery",
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

### Notification with a custom body definition

This example shows how to create a notification by adding a custom body definition that includes an inline link.

> [!div class="mx-imgBorder"] 
> ![Notification with a block of text that includes an inline link.](../media/app-notification-with-custom-body.png "Notification with an inline link")

<!--note from editor: Please note that in lines 309 and 339, it should be "records... are critically" or "record... is critically". I assume it's okay to have two "body" definitions in these code blocks?-->

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

The following is another example of a custom body definition. This one includes an inline link and bold formatting.

> [!div class="mx-imgBorder"] 
> ![Notification with a block of text that includes an inline link and bold text.](../media/app-notification-with-custom-body-and-bold-text.png "Notification with bold text")

```javascript
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

### Notification with a custom icon

This example shows how to add a custom icon to a notification<!--note from editor: Edit okay?-->. Within the notification, set **iconType** to **Custom** and in the body, include **iconUrl** with a value pointing to a web resource. The icon can be either an SVG or PNG file type.

> [!div class="mx-imgBorder"] 
> ![Notification with a custom icon.](../media/app-notification-with-custom-icon.png "Notification with a custom icon")

```javascript
var systemuserid = "<user-guid>";
var notificationRecord = 
{
  "title": "Welcome",
  "body": "Welcome to the world of app notifications!",
  "ownerid@odata.bind": "/systemusers(" + systemuserid + ")",
  "icontype": 100000005, // custom
  "data": "{ 'iconUrl': '/WebResources/cr245_AlertOn'}"
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

### Notification with a custom title and body

This example adds a custom title and a body definition that allows multiple links, bold formatting, and italic formatting.

> [!div class="mx-imgBorder"] 
> ![Notification that includes a custom title, multiple links, bold text, and italic formatting.](../media/app-notification-with-custom-title-body.png "Notification with a custom title and body")

```javascript
var systemuserid = "<user-guid>";
var notificationRecord = 
{
    "title": "Complete overhaul required (sample)",
   "body": "Maria Campbell mentioned you in a post.",
   "ownerid@odata.bind": "/systemusers(" + systemuserid + ")",
    "icontype": 100000004, // mention
    "data": JSON.stringify({
    "title": "[Complete overhaul required (sample)](?pagetype=entityrecord&etn=incident&id=0a9f62a8-90df-e311-9565-a45d36fc5fe8)",
    "body": "[Maria Campbell](?pagetype=entityrecord&etn=contact&id=43m770h2-6567-ebm1-ob2b-000d3ac3kd6c) mentioned you in a post: _\"**[@Paul](?pagetype=entityrecord&etn=contact&id=03f770b2-6567-eb11-bb2b-000d3ac2be4d)** we need to prioritize this overdue case, [@Robert](?pagetype=entityrecord&etn=contact&id=73f970b2-6567-eb11-bb2b-000d3ac2se4h) will work with you to engage with engineering team ASAP.\"_",
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

## In-app notifications vs. push notifications

The Power Apps Notification connector is for push notifications, which are separate from in-app notification. Push notifications only appear on the mobile device notifications list to open the app. In-app notifications appear when the app is open. We recommend limiting the use of push notifications to high-priority items, to avoid overwhelming the user. For more information, go to:

- [Power Apps Notification connector](/connectors/powerappsnotification)
- [Power Apps Notification V2 connector](/connectors/powerappsnotificationv2/)
- [Create push notifications for Power Apps Mobile](../../../mobile/power-apps-mobile-notification.md)

## Related articles

- [Create a table row using the Web API](../../data-platform/webapi/create-entity-web-api.md)
- [createRecord (Client API reference)](reference/xrm-webapi/createrecord.md)
- [In-app notifications in model-driven apps](/powerapps/user/notifications)
- [appnotification EntityType](/power-apps/developer/data-platform/webapi/reference/appnotification)
- [Notification (appnotification) table/entity reference](../../data-platform/reference/entities/appnotification.md)

