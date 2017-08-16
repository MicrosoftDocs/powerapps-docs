<properties
	pageTitle="Add notifications | Microsoft PowerApps"
	description="Sends native push notifications to a PowerApp."
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

# Send a push notification to a PowerApp #
Notifications are ubiquitous today to increase usage and retention of mobile apps. They are largely used across consumer and business applications to help engage users and prioritize towards their key tasks. In PowerApps sending notifications is done via the “PowerApps Notification connector”. Today I can send native push notifications to all app created with PowerApps. Additional types of notifications are to be added in the future.

![Option to send native push notification][1]

## When to use push notifications in your app ##
-	You have critical content that your users need to pay immediate attention
-	You have important tasks for them to act on via your app with all context pre-loaded.
-	You want to re-engage your users on a given cadence/ trigger and bring them in a particular app context.


## Before getting started ##
Choose an app that would be receiving the push notification. For the tutorial below, I’ve chosen the "Case Management" app from the PowerApps templates. Please look at [Create an app from template tutorial](https://powerapps.microsoft.com/tutorials/get-started-test-drive/) for detailed steps on how to quickly create an app from template.

## Setting up permissions ##

### Contributor permissions ###
 In order to target an app with push notifications you have to have contributor permissions when you create the connection.

### App user permissions ###
Your app user needs to have the app showing under "My apps". They need to either open the app from their PowerApps iOS/Android/WinPhone client application view or pull it from the AppSource org gallery in [home.dynamics.com](https://home.dynamics.com/).

This protects users from having an app shared with the entire company and directly have that app send push notifications before they become users of it.


## Trigger a push notification from a Flow ##

> **NOTE**  There is a known limitation today where you can only send a push notification to a single user or security group at a time from a Flow.

1. First create a flow, in this example we are triggering a flow when a new record is added to the Case entity in CDS.
![Option to send native push notification][4]

1. Now that you’ve configured the trigger, you can move to the second step where the push notification is sent. Search for the PowerApps Notification connector and select it. You can optionally choose to rename the connection to match your scenario.
![Option to send native push notification][5]

1. Next enter the app ID for the PowerApp that you want to send notifications to.

1. You may optionally choose to pass parameters to the app when it is launched from the user clicking the push notifications.  In this example, we are passing along the **Case ID** and **Initial Owner** fields for the selected contact.
![Option to send native push notification][6]

## Trigger a push notification directly from an App ##
PowerApps enables you to directly send a push notification from an app to another (or target the very same one).

1. Go to **[web.powerapps.com](https://web.powerapps.com/)** and navigate to the app you want to send push notifications to. From here, let's grab the ID of the app receiving push notifications as shown below.
![Grab app id][8]

1. Go to Connections tab and follow steps below to create a connection to the PowerApps Notification connector, pasting in the app ID from step 1.
![Create connection][9]

1. Add the connection to the trigger app. In this example, we use the very same app as trigger. The user that re-assigns the case is the one to trigger the push notification. The new case owner is the one to receive the push notification.
![Add connection][10]

1. Call the SendPushNotificaiton method from PushNotification connection. In this example we trigger this notification OnSuccess trigger in a form control.
![PowerApps formula][11]


### Configure your app to load to a specific screen and context when a user taps on the notification ##
The notification can pass in parameters to the app, for example to read the “CaseID” value you can read this via ``Param("CaseID")`` at any time. To quickly see this you can add a label to your app and set the text to be ``Param("CaseID")``. The value is empty if the app is opened from the app list and is populated with the CaseID value otherwise.

Next step is to configure your app to directly navigate to the Case details screen.
To do that, add a Timer to the app, and call ``Timer.Start()`` under OnVisible property of the screen element. Now select the Timer and set its OnTimerEnd to ``Navigate(EditCase, ScreenTransition.None)``.
#### Tip #1 ####
 Hide the timer: Set the Visible property of the Timer to false.
#### Tip #2 ####
 Control the app behavior so you can edit the first screen: Create an empty screen that your app does not navigate to. In there add a Text Input control. Now set the timer.Duration to be the value in the control. As you are creating the app set the timer to a non-0 value. When you are ready publish the app set the value to 0 for immediate triggering of the timer.

## Syntax ##

| Name                 | Summary                                                                                  |
|----------------------|------------------------------------------------------------------------------------------|
| SendPushNotification | Send a push notification to the app specified in the Push Notification connection setup. |

### Parameters ###
| Name       | Type                      | Summary                                                                                                                                                             |
|------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| recipients | Array of string, required | List of <ol> <li>user emails</li> <li>user Azure AD object Ids</li> <li>security group emails</li> <li>security group Azure AD object Ids </li></ol>                |
| message    | String, required          | Message body for the push notification.                                                                                                                             |
| openApp    | Boolean, optional         | Whether to open or not the app when user taps on the push notification.                                                                                             |
| params     | Parameters, optional      | Key-value parameters to pass with the notification.,These can be further processed in the app in order to navigate to the desired screen and load the state needed. |

### PowerApps Formula Samples ###
```
//Send a basic notification
PowerAppsNotification.SendPushNotification(
 {
  recipients: [""f60ccf6f-7579-4f92-967c-2920473c966b", 72f988bf-86f1-41af-91ab-2d7cd011db47],
  message: "A new case was assigned to you."
 }
)

//Send a different notification that will open the targeted PowerApps and pass along the specific parameters
PowerAppsNotification.SendPushNotification(
{
  recipients:["email1@contoso.com", "email2@contoso.com"],
  message:"message in the notif toast",
  params:Table({key:"notificationKey", value:"The value for notificationKey"}),
  openApp:true
 }
)
```

## Known limitations for PowerApps Notification Connector ##
1. For Windows Phone client the notifications don't show currently.

1. We do not provide push notifications yet for users who only run apps in the web browser.

1. The notifications shows the PowerApps generic icon instead of showing the specific icon of the app.

1. With Flow you can only have one recipient at a time.

For a connection refrence documentation please refer to: [PowerApps connector reference](https://docs.microsoft.com/en-us/connectors/powerappsnotification/)



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
