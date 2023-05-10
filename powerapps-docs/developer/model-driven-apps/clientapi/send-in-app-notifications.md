---
title: "Send in-app notifications within model-driven apps" 
description: Learn how to configure notifications in model-driven apps by using a client API.
ms.date: 05/10/2023
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

This article outlines the steps for how to send in-app notifications to a specific user. To see how these notifications appear in applications, see [In-app notifications in model-driven apps](/powerapps/user/notifications).

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

Notifications can be sent using the `SendAppNotification` API. See [SendAppNotification Action](xref:Microsoft.Dynamics.CRM.SendAppNotification) for information on the API and parameters. 

The following basic examples show how to use the API to send in-app notifications.

> [!div class="mx-imgBorder"] 
> ![Screenshot of a Welcome notification.](../media/welcome-notification.png "Welcome notification")


# [Web API](#tab/webapi)

In-app notifications can be sent by using the Web API. More information: [Use Web API actions](../../data-platform/webapi/use-web-api-actions.md).

```http
POST [Organization URI]/api/data/v9.0/SendAppNotification 
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

# [SDK for .NET](#tab/sdk)

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

<!-- # [Power Fx](#tab/powerfx)

In-app notifications can be sent from Power Apps using Power Fx. More information: [Microsoft Power Fx overview](/power-platform/power-fx/overview).

```powerapps-dot
XSendAppNotification(
  "Welcome",
  LookUp(Users,'Primary Email'="<User email address>"),
  "Welcome to the world of app notifications!"
)
``` -->

---

## Notification polling

In-app notifications use polling to retrieve notifications periodically when the app is running.  New notifications are retrieved at start of the model-driven app and when a page navigation occurs as long as the last retrieval is more than one minute ago.  If a user stays on a page for a long duration, new notifications won't be retrieved until the user navigates to another page.

## Notification table

Notifications sent using the `SendAppNotification` API are stored in the [Notification (appnotification)  table](../../data-platform/reference/entities/appnotification.md). The following are the columns for the table.

|Column Label|Column Schema Name|Description|
|---|---|---|
|Title|`Title`|The title of the notification.|
|Owner|`OwnerId`|The user who receives the notification.|
|Body|`Body`|Details about the notification.|
|IconType|`IconType`|The list of predefined icons. The default value is `Info`. For more information, go to [Changing the notification icon](#changing-the-notification-icon) later in this article.|
|Toast Type|`ToastType`|The list of notification behaviors. The default value is `Timed`. For more information, go to [Changing the notification behavior](#changing-the-notification-behavior) later in this article.|
|Priority | `Priority` |Enables prioritization of notifications, which determines the order in which the notifications are displayed in the notification center. For more information, see [Changing the notification behavior](#changing-the-notification-behavior) later in this article. |
|Expiry (seconds)|`TTLInSeconds`|The number of seconds from when the notification should be deleted if not already dismissed.|
|Data|`Data`|JSON that's used for extensibility and parsing richer data into the notification. The maximum length is 5,000 characters.|

  > [!NOTE]
  > The `appmoduleid` field is not used in the table.

## Customizing the notifiction

In addition to the basic properties of the notification, there are options for customizing the notification delivered to the user. This includes changing the styles in the **Title** and **Body** of the notification, customizing the notification icon, and changing the behavior of the notification.

### Using markdown in Title and Body

The **Title** and **Body** attributes of the `SendAppNotification` API do not support markdown defined within the properties. You can adjust the styles of these properties using markdown in the **OverrideContent** property. This field supports overriding the `Title` and `Body` simple strings with a limited subset of markdown styles.

The following is the supported markdown.

|Text Style|Markdown|
|---|---|
|Bold|`**Bold**`|
|Italic|`_Italic_`|
|Bullet list|`- Item 1\r- Item 2\r- Item 3`|
|Numbered list|`1. Green\r2. Orange\r3. Blue`|
|Hyperlinks|`[Title](url)`|

Newlines can be included with the body using `\n\n\n\n`.

This example shows how to create a notification by adding a custom body definition that includes an inline link.

> [!div class="mx-imgBorder"] 
> ![Notification with a block of text that includes an inline link.](../media/app-notification-with-custom-body.png "Notification with an inline link")

# [Web API](#tab/webapi)

```http
POST [Organization URI]/api/data/v9.0/SendAppNotification 
HTTP/1.1
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json

{
  "Title": "SLA critical",
  "Body": "Record assigned to yo uis critically past SLA.",
  "Recipient": "/systemusers(<Guid of the user>)",
  "IconType": 100000003, // warning
  "ToastType": 200000000, // timed
  "OverrideContent": {
    "@odata.type": "#Microsoft.Dynamics.CRM.expando",
    "title": "**SLA critical**",
    "body": "Case record [Complete overhaul required (sample)](?pagetype=entityrecord&etn=incident&id=0a9f62a8-90df-e311-9565-a45d36fc5fe8) assigned is critically past SLA and has been escalated to your manager."
  }
}
```

# [SDK for .NET](#tab/sdk)

```csharp

OrganizationRequest request = new OrganizationRequest()
{
    RequestName = "SendAppNotification",
    Parameters = new ParameterCollection
    {
        ["Title"] = "SLA critical",
        ["Recipient"] = new EntityReference("systemuser", <Guid of the user>),
        ["Body"] = "Record assigned to you is critically past SLA.",
        ["IconType"] = new OptionSetValue(100000003), //warning
        ["ToastType"] = new OptionSetValue(200000000), //timed
        ["OverrideContent"] = new Entity()
        {
          Attributes = 
          {
            ["title"] = "**SLA critical**",
            ["body"] = "Case record [Complete overhaul required (sample)](?pagetype=entityrecord&etn=incident&id=0a9f62a8-90df-e311-9565-a45d36fc5fe8) assigned to you is critically past SLA and has been escalated to your manager."
          }
        }
     }
};

OrganizationResponse response = currentUserService.Execute(request);
Guid appNotificationId = (Guid)response.Results["NotificationId"];
```
---

This example adds a custom title and a body definition that allows multiple links, bold formatting, and italic formatting.

> [!div class="mx-imgBorder"] 
> ![Notification that includes a custom title, multiple links, bold text, and italic formatting.](../media/app-notification-with-custom-title-body.png "Notification with a custom title and body")

# [Web API](#tab/webapi)

```http
POST [Organization URI]/api/data/v9.0/SendAppNotification
HTTP/1.1
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json

{
  "Title": "Complete overhaul required (sample)",
  "Body": "Maria Campbell mentioned you in a post.",
  "Recipient": "/systemusers(<Guid of the user>)",
  "IconType": 100000004, // mention
  "OverrideContent": {
    "@odata.type": "#Microsoft.Dynamics.CRM.expando",
    "title": "[Complete overhaul required (sample)](?pagetype=entityrecord&etn=incident&id=0a9f62a8-90df-e311-9565-a45d36fc5fe8)",
    "body": "[Maria Campbell](?pagetype=entityrecord&etn=contact&id=43m770h2-6567-ebm1-ob2b-000d3ac3kd6c) mentioned you in a post: _\"**[@Paul](?pagetype=entityrecord&etn=contact&id=03f770b2-6567-eb11-bb2b-000d3ac2be4d)** we need to prioritize this overdue case, [@Robert](?pagetype=entityrecord&etn=contact&id=73f970b2-6567-eb11-bb2b-000d3ac2se4h) will work with you to engage with engineering team ASAP.\"_"
  }
}
```

# [SDK for .NET](#tab/sdk)

```csharp

OrganizationRequest request = new OrganizationRequest()
{
    RequestName = "SendAppNotification",
    Parameters = new ParameterCollection
    {
        ["Title"] = "Complete overhaul required (sample)",
        ["Recipient"] = new EntityReference("systemuser", <Guid of the user>),
        ["Body"] = "Maria Campbell mentioned you in a post.",
        ["IconType"] = new OptionSetValue(100000004), //mention
        ["OverrideContent"] = new Entity()
        {
          Attributes = 
          {
            ["title"] = "[Complete overhaul required (sample)](?pagetype=entityrecord&etn=incident&id=0a9f62a8-90df-e311-9565-a45d36fc5fe8)",
            ["body"] = "[Maria Campbell](?pagetype=entityrecord&etn=contact&id=43m770h2-6567-ebm1-ob2b-000d3ac3kd6c) mentioned you in a post: _\"**[@Paul](?pagetype=entityrecord&etn=contact&id=03f770b2-6567-eb11-bb2b-000d3ac2be4d)** we need to prioritize this overdue case, [@Robert](?pagetype=entityrecord&etn=contact&id=73f970b2-6567-eb11-bb2b-000d3ac2se4h) will work with you to engage with engineering team ASAP.\"_"
          }
        }
     }
};

OrganizationResponse response = currentUserService.Execute(request);
Guid appNotificationId = (Guid)response.Results["NotificationId"];
```
---

>[!NOTE]
>OverrideContent is not supported in Power Fx with the `SendAppNotification` API.




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
POST [Organization URI]/api/data/v9.0/SendAppNotification 
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
  "OverrideContent": {
    "@odata.type": "#Microsoft.Dynamics.CRM.expando",
    "iconUrl": "/WebResources/cr245_AlertOn" //URL of the image file to be used for the notification icon
  }
}
```

### Setting the notification priority

You can change the order in which notifications display in the notification center by setting the priority. The following are the optional values:

|Priority | Value |
|---------|-------|
|Normal |`200000000`|
|High |`200000001`|

The default value is `Normal`. Notifications are sorted in the notification center by Priority and Created On date, descending. High priority notifications will display at the top of the list in the notification center.

## Notification actions

In-app notifications support zero to many actions on the notification card. There are three supported action types:

- **URL**: When the action is selected the web browser navigates to the defined URL.
- **Side Pane**: When the action is selected, a side pane is opened in the app and loads the defined context in the pane.
- **Teams Chat**: When the action is selected, a Teams chat is initiated with defined users in the context of a Dynamics 365 record.

### Defining a URL action

The URL action type enables navigation from the action on the app notification to a defined URL. The following are the parameters for this action type:

|Parameter | Required | Data type | Description |
|-------------|-------------|-------------|-------------|
|url | Yes | String | This is the URL of the web address to be opened when the action is selected. |
|navigationTarget | No | String | This parameter controls where a navigation link opens. The options are:<br><ul><li>`dialog`: Opens in the center dialog.</li><li>`inline`: Default. Opens in the current page.</li><li>`newWindow`: Opens in a new browser tab.</li><ul> |

The following example shows how to create a notification with a single URL action.

> [!div class="mx-imgBorder"] 
> ![App notification with a single action.](../media/app-notification-with-single-action.png "App notification with a single action")
  
# [Web API](#tab/webapi)

```http
POST [Organization URI]/api/data/v9.0/SendAppNotification 
HTTP/1.1
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json

{
  "Title": "Congratulations",
  "Body": "Your customer rating is now an A. You resolved 80% of your cases within SLA thi week and average customer rating was A+",
  "Recipient": "/systemusers(<GUID of user>)",
  "IconType": 100000001, // success
  "ToastType": 200000000, // timed
  "Actions": {
      "@odata.type":"Microsoft.Dynamics.CRM.expando",
      "actions@odata.type":"#Collection(Microsoft.Dynamics.CRM.expando)",
      "actions": [
        {
            "title": "View cases",
            "data": {
                "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                "type": "url",
                "url": "?pagetype=entitylist&etn=incident&viewid=00000000-0000-0000-00aa-000010001028&viewType=1039",
                "navigationTarget": "newWindow"
            }
        }
      ]
  }
}
```

# [SDK for .NET](#tab/sdk)

```csharp

OrganizationRequest request = new OrganizationRequest()
{
    RequestName = "SendAppNotification",
    Parameters = new ParameterCollection
    {
        ["Title"] = "Congratulations",
        ["Recipient"] = new EntityReference("systemuser", <Guid of the user>),
        ["Body"] = "Your customer rating is now an A. You resolved 80% of your cases within SLA thi week and average customer rating was A+",
        ["IconType"] = new OptionSetValue(100000000), //info
        ["ToastType"] = new OptionSetValue(200000000), //timed
        ["Actions"] = new Entity()
        {
          Attributes = 
          {
            ["actions"] = new EntityCollection()
            {
              Entities = 
              {
                new Entity()
                {
                  Attributes =
                  {
                    ["title"] = "View cases",
                    ["data"] = new Entity()
                    {
                      Attributes =
                      {
                        ["type"] = "url",
                        ["url"] = "?pagetype=entitylist&etn=incident&viewid=00000000-0000-0000-00aa-000010001028&viewType=1039",
                        ["navigationTarget"] = "newWindow"
                      }
                    }
                  }
                }
              }
            }
          }
        }
     }
};

OrganizationResponse response = currentUserService.Execute(request);
Guid appNotificationId = (Guid)response.Results["NotificationId"];
```

<!-- # [Power Fx](#tab/powerfx)

```powerapps-dot
XSendAppNotification(
    "Congratulations",
    LookUp(Users,'Primary Email'="<User email address>"),
    "Your customer rating is now an A. You resolved 80% of your cases within SLA thi week and average customer rating was A+",
    [XCreateUrlAction
        ("View cases","?pagetype=entitylist&etn=incident&viewid=00000000-0000-0000-00aa-000010001028&viewType=1039", "newWindow")
    ]
)
``` -->

---
  
### Defining a side pane action

A side pane action enables opening a side pane to load a defined page when the action is selected from the app notification. See [Creating side panes by using a client API](./create-app-side-panes.md) for more information.

When using the side pane action type, you have control over the options of the side pane itself, and the page that loads in the side pane.
- See [createPane](./reference/xrm-app/xrm-app-sidepanes/createpane.md) for the optional parameters for the pane that is created.
- See [navigateTo (Client API reference)](./reference/xrm-navigation/navigateto.md) for the parameters to be defined for the page that will be loaded in the side pane.
  
The following example shows creating an app notification with a two side pane actions.
  
# [Web API](#tab/webapi)

```http
POST [Organization URI]/api/data/v9.0/SendAppNotification 
HTTP/1.1
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json

{
  "Title": "New task",
  "Body": "A new task has been assigned to you to follow up on the Contoso account",
  "Recipient": "/systemusers(<User ID>)",
  "IconType": 100000000, // info
  "ToastType": 200000000, // timed
  "Actions": {
      "@odata.type":"Microsoft.Dynamics.CRM.expando",
      "actions@odata.type":"#Collection(Microsoft.Dynamics.CRM.expando)",
      "actions": [
        {
          "title": "View task",
          "data" : {
                "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                "type": "sidepane",
                "paneOptions": {
                    "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                    "title": "Task Record",
                    "width": 400
                },
                "navigationTarget": {
                    "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                    "pageType": "entityrecord",
                    "entityName": "task",
                    "entityId": "<Task ID>"
                }
           }
        },
        {
          "title": "View account",
          "data" : {
                "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                "type": "sidepane",
                "paneOptions": {
                    "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                    "title": "Account Record",
                    "width": 400
                },
                "navigationTarget": {
                    "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                    "pageType": "entityrecord",
                    "entityName": "account",
                    "entityId": "<Account ID>"
                }
           }
        }
      ]
  }
}
```

# [SDK for .NET](#tab/sdk)

```csharp

OrganizationRequest request = new OrganizationRequest()
{
    RequestName = "SendAppNotification",
    Parameters = new ParameterCollection
    {
        ["Title"] = "New task",
        ["Recipient"] = new EntityReference("systemuser", <Guid of the user>),
        ["Body"] = "A new task has been assigned to you to follow up on the Contoso account",
        ["IconType"] = new OptionSetValue(100000000), //info
        ["ToastType"] = new OptionSetValue(200000000), //timed
        ["Actions"] = new Entity()
        {
          Attributes = 
          {
            ["actions"] = new EntityCollection()
            {
              Entities = 
              {
                new Entity()
                {
                  Attributes =
                  {
                    ["title"] = "View task",
                    ["data"] = new Entity()
                    {
                      Attributes =
                      {
                        ["type"] = "sidepane",
                        ["paneOptions"] = new Entity
                        {
                          Attributes = 
                          {
                            ["title"] = "Task",
                            ["width"] = 400
                          }
                        },
                        ["navigationTarget"] = new Entity
                        {
                          Attributes = 
                          {
                            ["pageType"] = "entityrecord",
                            ["entityName"] = "task",
                            ["entityId"] = "<GUID of the table record>"
                          }
                        }
                      }
                    }
                  }
                },
                new Entity()
                {
                  Attributes =
                  {
                    ["title"] = "View account",
                    ["data"] = new Entity()
                    {
                      Attributes =
                      {
                        ["type"] = "sidepane",
                        ["paneOptions"] = new Entity
                        {
                          Attributes = 
                          {
                            ["title"] = "Account",
                            ["width"] = 400
                          }
                        },
                        ["navigationTarget"] = new Entity
                        {
                          Attributes = 
                          {
                            ["pageType"] = "entityrecord",
                            ["entityName"] = "account",
                            ["entityId"] = "<GUID of the table record>"
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
     }
};

OrganizationResponse response = currentUserService.Execute(request);
Guid appNotificationId = (Guid)response.Results["NotificationId"];
```

<!-- # [Power Fx](#tab/powerfx)

```powerapps-dot
XSendAppNotification(
  "You have a new task!",
  AsType(ThisRecord.Owner, Users),
  "A new task has been assigned to you to follow up with your customer",
  [XCreateSidePaneActionForEntity
    ("View task","taskRecord","Task","task",ThisRecord.Task),
  XCreateSidePaneActionForEntity
    ("View account","accountRecord","Account","account",AsType(ThisRecord.Regarding, Accounts).Account)
  ]
)
``` -->

---

### Defining a Teams chat action

A Teams chat action enables scenarios where a Teams chat is initiated from the app notification. This uses the embedded Teams feature for Dynamics 365 apps, which provides sellers and agents the ability to chat in Microsoft Teams from within the customer engagement apps, such as Sales Hub, Customer Service Hub, and custom apps. 

>[!NOTE]
>Microsoft Teams chat in Dynamics 365 must be enabled to use the Teams chat action type. See [Work with Microsoft Teams chat in Dynamics 365](/dynamics365/teams-integration/enable-teams-chat) for more information.

The action type provides the following options:
- Create a new chat session or open an existing chat session.
- Link the chat session to a Dynamics 365 record or create an unlinked chat.

The following are the parameters for defining a Teams chat action on the app notification.

|Parameter | Data type | Description |
|----------|-----------|-------------|
|chatId    |String     |Define a value for the chat ID to open an existing chat. This is the ID of the Teams chat session, which can be obtained from the **id** property of the **chat** entity in Microsoft Graph. See [Get chat](/graph/api/chat-get) for more information. For Teams chat sessions that have been linked to Dynamics 365 records, the association is stored in the **Microsoft Teams chat association entity (msdyn_teamschatassociation)** table in Dataverse. The ID for the chat session is stored in the **Teams Chat Id** property of this table.<br><br> Leave this parameter blank to initiate a new chat session. |
|memberIds |GUID       |This is an array of the AAD user ID values of each of the participants that will be included in a new chat session. Member ID values should not be defined if a value has been defined for the **chatId** parameter. If the **chatId** has been defined, then the existing chat will be opened, and the members of the existing chat will be included in the chat when opened. |
|entityContext | Expando |The entity context provides the Dynamics 365 record to which the chat session should be linked. For example, if the chat session is regarding a specific customer account record, define the account record in this parameter to have the chat session linked to the account and display in the account's timeline. <br><br>The entity context includes the **entityName** and **recordId** parameters, which must be defined to identify the record for the entity context.<br><br> An entity context should not be defined if a value has been defined for the **chatId** parameter. If the **chatId** has been defined, then the existing chat will be opened, and the entityContext, whether linked or unlinked, will already have been defined for the existing chat. If the action is creating a new chat session (i.e. the **chatId** parameter has not been provided), and the the entity context is not defined, then the new chat session will not be linked to a Dynamics 365 record. |
|entityName | String | Part of the entity context, this is the logical name of the Dataverse table for the record to which the chat will be linked. |
|recordId | GUID | Part of the entity context, this is the ID property of the table defined in the **entityName** parameter for the record to which the chat will be linked. |
|chatTitle | String | The title of the Teams chat. |
|initialMessage | String | The text of an introduction message you may optionally provide that will be automatically sent when the chat is created. |

The following example shows creating an app notification with a single Teams chat action.
  
# [Web API](#tab/webapi)

```http
POST [Organization URI]/api/data/v9.0/SendAppNotification 
HTTP/1.1
Content-Type: application/json; charset=utf-8
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json

{
  "Title": "New order posted",
  "Body": "A new sales order has been posted for Contoso",
  "Recipient": "/systemusers(<Guid of the user>)",
  "IconType": 100000000, // info
  "ToastType": 200000000, // timed
  "Actions": {
      "@odata.type":"Microsoft.Dynamics.CRM.expando",
      "actions@odata.type":"#Collection(Microsoft.Dynamics.CRM.expando)",
      "actions": [
        {
            "title": "Chat with sales rep",
            "data": {
                "@odata.type":"#Microsoft.Dynamics.CRM.expando",
                "type": "teamsChat",
                "memberIds@odata.type": "#Collection(String)",
                "memberIds": ["<AAD user ID 1>","<AAD user ID 2>"],
                "entityContext": {
                  "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                  "entityName": "account",
                  "recordId": "<Account ID value>"
                }
            }
        }
      ]
  }
}
```

# [SDK for .NET](#tab/sdk)

```csharp

OrganizationRequest request = new OrganizationRequest()
{
    RequestName = "SendAppNotification",
    Parameters = new ParameterCollection
    {
        ["Title"] = "New order posted",
        ["Recipient"] = new EntityReference("systemuser", <Guid of the user>),
        ["Body"] = "A new sales order has been posted for Contoso",
        ["IconType"] = new OptionSetValue(100000000), //info
        ["ToastType"] = new OptionSetValue(200000000), //timed
        ["Actions"] = new Entity()
        {
          Attributes = 
          {
            ["actions"] = new EntityCollection()
            {
              Entities = 
              {
                new Entity()
                {
                  Attributes =
                  {
                    ["title"] = "Chat with sales rep",
                    ["data"] = new Entity()
                    {
                      Attributes =
                      {
                        ["type"] = "teamsChat",
                        ["memberIds"] = new string[]{ "<AAD user ID 1>","<AAD user ID 2>" },
                        ["entityContext"] = new Entity
                        {
                          Attributes = 
                          {
                            ["entityName"] = "account",
                            ["recordId"] = "<Account ID value>"
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
     }
};

OrganizationResponse response = currentUserService.Execute(request);
Guid appNotificationId = (Guid)response.Results["NotificationId"];
```

<!-- # [Power Fx](#tab/powerfx)

```powerapps-dot
  
XSendAppNotification(
   "New order posted",
   AsType(ThisRecord.Owner, Users),
   "A new sales order has been posted for Contoso",
   [XCreateTeamsChatAction(
      "Chat with sales rep",
      [AsType(ThisRecord.Owner, Users).'Azure AD Object ID',ThisRecord.'Created By'.'Azure AD Object ID'],
      AsType(ThisRecord.Customer, Accounts).Account,
      "account",
      ThisRecord.Description
      )
   ]
)
``` -->

---

## Managing security for notifications

The in-app notification feature uses three tables. A user needs to have the correct security roles to receive notifications and to send notifications to themselves or other users.  

In addition to the appropriate table permissions, a user must be assigned the **Send In-App Notification (prvSendAppNotification)** privilege to execute the `SendAppNotification` API. The privilege is granted to the **Environment Maker** role by default. This privilege is required for sending app notifications. It is not required to receive notifications.

|Usage|Required table privileges|
|------------|----------------|
|User has no in-app notification bell and receives no in-app notification |None: Read privilege on the app notification table. |
|User can receive in-app notifications|<ul><li>Basic: Read privilege on the app notification table.</li><li>Create, Read, Write, and Append privileges on the model-driven app user setting.</li><li>Read and AppendTo privileges on setting definition.</li></ul> |
|User can send in-app notifications to self |Basic: Create and Read privileges on the app notification table, and Send In-App Notification privilege. |
|User can send in-app notifications to others |Read privilege with Local, Deep, or Global access level on the app notification table based on the receiving user's business unit, and Send In-App Notification privilege. |


## Notification storage

Because the app notification table uses the organization's database storage capacity, it's important to consider the volume of notifications sent and the expiration setting. More information: [Microsoft Dataverse storage capacity](/power-platform/admin/capacity-storage)

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

