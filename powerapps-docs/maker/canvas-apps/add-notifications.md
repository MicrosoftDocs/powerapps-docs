---
title: Send a push notification from a canvas app. | Microsoft Docs
description: Learn how to send push notifications from a canvas app in Power Apps.
author: kavishi
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 10/23/2020
ms.author: kaagar
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Send notification from an app

You can send a push notification from one app to another or to the same app. In canvas apps, you can send notifications by using the Power Apps Notification connector.

In this article, the sample app used for notifications is built from the default **Case Management** app template.

> [!NOTE]
> Before you begin, create push notifications for the Power Apps mobile app. More information: [Create push notifications for the Power Apps mobile app](../../mobile/power-apps-mobile-notification).

1. In [Power Apps](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), go to the app to which you want to send push notifications.

1. Copy the app ID. More information: [Get an app ID](get-sessionid.md#get-an-app-id)

1. In the left pane, select **Data** - **Connections**.

1. Edit the app. More information: [Edit an app](edit-app.md)

1. Select **View** - **Data sources**.

1. Select **Add data source**.

1. Select **New Connection**.

1. Select **Power Apps Notification**.

    ![Select Power Apps Notification](./media/add-notifications/select-powerapps-notification.png "Select Power Apps Notification")

1. Paste the app ID copied from the previous step.

    ![Paste the app ID](./media/add-notifications/paste-app-id.png "Paste the app ID")

1. Select **Connect**.

1. Add the push notification connection to the trigger app using the similar steps.

    In our example, we use the same app as the trigger app. The user who reassigns the case also triggers a push notification to the new case owner.

    ![Add connection](./media/add-notifications/add-connection.png)

1. From the push notification connection, call the **SendPushNotification** method.

    In our example, we trigger this notification by using the **OnSuccess** property in a form.

    ![Power Apps formula](./media/add-notifications/powerapps-function.png)

## Perform an action when a user taps the notification

### Pass parameters

Your push notification can pass specific parameters to the app. For example, to read the **CaseID** value, use *Param("CaseID")*. To quickly identify this parameter, add a **Label** control to your app. Set the **Text** property of that control to **Param("CaseID")**. If the user opens the app from the **All apps** list, the value is empty. If the user opens the app from another location on the device, the value is populated with the **CaseID** value.

### Set the start page

You can set your app to open, for example, the **Case details** page as soon as the app opens:

1. Add a **Timer** control, and set its **OnTimerEnd** property to this formula:

    `Navigate(EditCase, ScreenTransition.None)`

1. (optional) Hide the **Timer** control by setting its **Visible** property to **false**.

1. Set the **OnVisible** property of the screen to **Timer.Start()**.

> [!TIP]
> It's a good idea to create a unique first page in the app for the notification:
> 
> 1. Create an empty page that your app doesn't already open, add a **Text Input** control, and set its **timer.Duration** value.
> 2. When you create the app, set the timer to a non-zero value. When you're ready to publish the app, set the value to **0** to immediately trigger the timer.

## Syntax

| Name | Description |
| --- | --- |
| SendPushNotification |Sends a push notification to the app that's specified in the connection settings for the notification. |

### Parameters

| Name | Type | Description |
| --- | --- | --- |
| recipients |String array, required |A list of: <ul> <li>Email addresses for users or security groups</li> <li>Object IDs for users or security groups in Azure Active Directory</li></ul> |
| message |String, required |The message body of the push notification. |
| openApp |Boolean, optional |Whether to open the app when the user taps the push notification. |
| params |Parameters, optional |Key-value parameters to pass with the notification. These can be further processed in the app to open a specific page and load a specific state. |

### Sample formulas
Send a basic notification.

```powerapps-dot
PowerAppsNotification.SendPushNotification(
	{
		recipients: ["f60ccf6f-7579-4f92-967c-2920473c966b", "72f988bf-86f1-41af-91ab-2d7cd011db47"],
		message: "A new case was assigned to you."
	}
)
```

Send a notification that opens an app and passes along specific parameters.

```powerapps-dot
PowerAppsNotification.SendPushNotification(
	{
		recipients: ["email1@contoso.com", "email2@contoso.com"],
		message: "message in the notif toast",
		params: Table({key:"notificationKey", value:"The value for notificationKey"}),
		openApp: true
 	}
)
```

### See also

- [Create push notifications for the Power Apps mobile app](../../mobile/power-apps-mobile-notification)
- [Power Apps Notification reference](https://docs.microsoft.com/connectors/powerappsnotification/)
