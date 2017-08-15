<properties
	pageTitle="Add push notifications | Microsoft PowerApps"
	description="Learn how to send native push notifications to a PowerApps app."
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="jamesol-msft"
	manager="anneta"
	editor=""
	tags=""
	/>

<tags
	ms.service="powerapps"
	ms.devlang="na"
	ms.topic="article"
	ms.tgt_pltfrm="na"
	ms.workload="na"
	ms.date="08/08/2017"
	ms.author="jamesol"/>

# Add a push notification to a PowerApps app

Push notifications for mobile apps primarily are used in consumer and business applications, to engage app users, and help them prioritize key tasks. In Microsoft PowerApps, you can send notifications by using the PowerApps Notification connector. You can send native push notifications to all apps that you created by using PowerApps. We plan to add more notification types in the future.

![Option to send native push notification][1]

## When to use push notifications in your app

- You have critical content that you need to make your users aware of immediately.
- You have important tasks for your users to act on via your app, in a preloaded context.
- You want to engage your users on a specific interval, or you need users to enter the app in a specific context.


## Choose your app

Choose the app that you want to receive the push notification. For detailed steps on how to quickly create an app from a template, see the [Create an app from a template tutorial](https://powerapps.microsoft.com/tutorials/get-started-test-drive/). In the tutorial, and in this article, we use the Case Management PowerApps app template. 

## Set up permissions

### Admin permissions

To add push notifications to an app, first you create a connection to the app. To create a connection, you must have Contributor permission for the app.

### App user permissions

To receive notifications, the app must be in **My apps** on the user's device. The app user must either open the app in the user's PowerApps iOS, Android, or Windows phone client application view, or get the app from the organization's AppSource gallery at [Dynamics 365](https://home.dynamics.com/). These measures prevent the app from being shared with the entire organization. When the user accesses the app from one of these locations, the user can choose to receive app push notifications when they install the app.


## Trigger a push notification from a flow

**Note**: Currently, if you use a flow to trigger a push notification, you can send the notification to only one user or one security group at a time.

1. Create a flow. In our example, a flow is triggered when a new record is added to the Case entity in Common Data Service.
	![Option to send native push notification][4]
2. Search for and then select the **PowerApps Notification** connector. You also have the option to rename the connection to reflect your scenario.
	![Option to send native push notification][5]
3. Enter the App ID of the PowerApps app that you want to send notifications to.
4. (Optional) You can pass parameters to the app when the app opens, after the user taps the push notification. In our example, we pass along the **Case ID** and **Initial Owner** fields for the selected contact.
	![Option to send native push notification][6]

## Trigger a push notification directly from an app

You can use PowerApps to send a push notification directly from one app to another app, or to the same app.

1. In [PowerApps](https://web.powerapps.com/), go to the app that you want to send push notifications to. On the **Details** tab, copy the App ID of the app that will receive the push notification.
	![Get App ID][8]
2. Select the **Connections** tab, and then complete the steps to create a connection to the PowerApps Notification connector. You'll paste in the App ID from step 1.
	![Create connection][9]
3. Add the connection to the trigger app. In our example, we use the same app as the trigger app. The user that reassigns the case is the one that triggers the push notification. The new case owner is the one who receives the push notification.
	![Add connection][10]
4. From the push notification connection, call the **SendPushNotification** method. In our example, we trigger this notification by using the **OnSuccess** property in a Form control.
	![PowerApps formula][11]


## Load a specific page and context when a user taps the notification

### Pass parameters

Your push notification can pass specific parameters to the app. For example, to read the **CaseID** value, use *Param("CaseID")*. To help you quickly identify this parameter, you can add a label to your app. In the label, set the text to **Param("CaseID")**. If the user opens the app from the All apps list, the value is empty. If the user opens the app from another location on the device, the value is populated with the **CaseID** value.

### Set the start page

You can set your app to go directly to the **Case details** page (in our example):

1. Add a Timer control to the app.
2. Under the **OnVisible** property of the page element, call **Timer.Start()**.
3. Select the Timer control, and then set its **OnTimerEnd** value to **Navigate(EditCase, ScreenTransition.None)**.
	
	**Note**: To hide the Timer control, set the **Visible** property of the Timer control to **false**.

**Tip**: It's a good idea to create a unique first page in the app for the notification:

1. Create an empty page that your app does not already go to.
2. On the page, add a Text Input control.
3. In the Text Input control, set the **timer.Duration** value.
4. When you create the app, set the timer to a non-zero value. When you are ready to publish the app, set the value to **0** to immediately trigger the timer.

## Syntax

| Name                 | Description                                                                                  |
|----------------------|------------------------------------------------------------------------------------------|
| SendPushNotification | Sends a push notification to the app that is specified in the push notification connection settings. |

### Parameters
| Name       | Type                      | Description                                                                                                                                                             |
|------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| recipients | String array, required | A list of: <ul> <li>User emails</li> <li>User Azure Active Directory (Azure AD) object IDs</li> <li>Security group emails</li> <li>Security group Azure AD object IDs </li></ul>                |
| message    | String, required          | The push notification message body.                                                                                                                             |
| openApp    | Boolean, optional         | Whether to open the app when the user taps the push notification.                                                                                             |
| params     | Parameters, optional      | Key-value parameters to pass with the notification. These can be further processed in the app to go to a specific page and load a specific state. |

### PowerApps formula samples

```
//Send a basic notification.
PowerAppsNotification.SendPushNotification(
 {
  recipients: [""f60ccf6f-7579-4f92-967c-2920473c966b", 72f988bf-86f1-41af-91ab-2d7cd011db47],
  message: "A new case was assigned to you."
 }
)

//Send a notification that opens the targeted PowerApps app, and passes along specific parameters.
PowerAppsNotification.SendPushNotification(
{
  recipients:["email1@contoso.com", "email2@contoso.com"],
  message:"message in the notif toast",
  params:Table({key:"notificationKey", value:"The value for notificationKey"}),
  openApp:true
 }
)
```

## Known limitations for the PowerApps Notification connector

* Currently, notifications are not displayed on the Windows phone client.
* Currently, we don't provide push notifications for users who run apps only in a web browser.
* Notifications show the generic PowerApps icon instead of a specific app icon.
* When you use Microsoft Flow, you can send a push notification to only one recipient at a time.

For reference information, see [PowerApps Notification reference](https://docs.microsoft.com/en-us/connectors/powerappsnotification/).



[1]: ./media/add-notifications/pic1-send-notif.jpg
[2]: ./media/add-notifications/pic2-diagramoverview.jpg
[3]: ./media/add-notifications/pic3-select-app-id.jpg
[4]: ./media/add-notifications/pic4-step1-flowupdated.jpg
[5]: ./media/add-notifications/pic5-step2-create-connection.jpg
[6]: ./media/add-notifications/pic6-step3-configure-notif.jpg
[7]: ./media/add-notifications/pic7-case-table.jpg
[8]: ./media/add-notifications/grab-id.png
[9]: ./media/add-notifications/create-connection.png
[10]: ./media/add-notifications/add-connection.png
[11]: ./media/add-notifications/powerapps-function.png
