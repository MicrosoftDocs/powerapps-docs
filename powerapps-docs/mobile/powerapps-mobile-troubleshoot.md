---
title: Troubleshoot issues in the Power Apps mobile app
description: Troubleshooting and known issues for the Power Apps mobile app 
author: trdehove
ms.component: pa-user
ms.topic: conceptual
ms.date: 08/01/2023
ms.subservice: mobile
ms.author: trdehove
ms.reviewer: sericks
search.audienceType: 
  - enduser
contributors:
- makolomi 
---

# Troubleshoot issues in the Power Apps mobile app

This troubleshooting article helps fix common issues for the [Power Apps mobile app](../mobile/run-powerapps-on-mobile.md).

> [!NOTE]
> If you are having an issue with Power Apps for iOS or Android and you don't find a solution on this page, please send a description of your issue with a screenshot and session ID to [pamobsup@microsoft.com](mailto:pamobsup@microsoft.com?subject=Power%20Mobile%20issues). Comments on this page are not received by the support team.

## Error: A major update is available. Upgrade your app to the latest version to keep your app working. If you are unable to upgrade, contact your administrator.

A major update to the Power Apps offline sync engine has been made. To keep your app working, [upgrade to the latest version of the Power Apps mobile app](run-powerapps-on-mobile.md). You must be running one of the following versions or later:

-   Android: 3.23031.18
-   iOS: 13.23031.18
-   Windows: 3.23024.21

If you are unable to upgrade, contact your administrator.

## Diagnose mobile apps with Monitor

Monitor is a tool that offers makers a deep view of what an app does and how it does it by logging all key activities that occur in the app as it runs. You can [connect a mobile app session to Monitor](../maker/monitor-canvasapps.md#for-apps-running-on-power-apps-mobile-preview) to better diagnose and troubleshoot issues faster.

## Debug JavaScript web resources in mobile apps

While developing JavaScript web resources for mobile scenarios, you can use your Android device to debug your mobile-specific code and ensure it works as expected. More information: [Debug JavaScript in mobile apps on Android](../developer/model-driven-apps/clientapi/debug-JavaScript-code.md#debug-javascript-in-mobile-apps-on-android).

## Error: There was a problem signing you in

You are unable to sign in due to issues with the Microsoft Authenticator app.

If you don't have the Microsoft Authenticator app, download the app from the App Store or Play Store and then sign in to Power Apps mobile again.

If you already have the Microsoft Authenticator app installed and you're having sign in issues, then try these steps:

1. Back up your Microsoft Authenticator account. For more information, see [Back up and recover account credentials using the Microsoft Authenticator app](/azure/active-directory/user-help/user-help-auth-app-backup-recovery)
2. Uninstall the Microsoft Authenticator app.
3. Uninstall Power Apps mobile.
4. Reinstall the Microsoft Authenticator app and add your back up account.
5. Reinstall [Power Apps mobile](../mobile/run-powerapps-on-mobile.md).
6. Open Power Apps mobile and then sign in.

## Error: Your device configuration is preventing sign in

If you get this error messages, it means your company's IT department requires Microsoft Intune or an authentication app to sign in securely. However, your device setup is blocking Power Apps mobile from launching the authentication app that's installed on your device.

Microsoft authentication apps are Authenticator and Company Portal. Your company may use a third-party authentication app. If you're not sure, ask your IT department or help desk which authentication app to use. Once you have the correct authentication app, then follow the steps below.

 > [!NOTE]
 > Power Apps requires a valid license to sign in. For more information, see [Licensing overview](/power-platform/admin/pricing-billing-skus).

Sometimes, updating and manually opening the authentication app on your device before signing in to Power Apps mobile can fix the problem. If this doesn't fix the issue, then follow the next steps depending on your device manufacturer and authentication app.

### Huawei or Honor device

1. Go to **Settings** > **Battery** > **App launch**.

    > [!NOTE]
    > The **App launch** menu can have different names depending on the model and the operating version of your mobile device. If you   don't see the **App launch** menu option, then look for one of the following menu options:
    > - **Close apps after screen lock** 
    > - **Applications**
    > - **Background applications**

2. Under **Manage automatically**, on the authenticator app set the toggle switch to **OFF**.
3. On the **Manage manually** screen, ensure that **Secondary launch / Can be launched by other apps** is enabled. To allow the Power Apps mobile app to launch the app.

### Vivo device

1. Go to **Settings** > **More Settings** > **Applications** > **Autostart**.
2. Set the toggle switch to **ON** for the authenticator app.

If the issue is still not fixed, then try these steps:

1. Back up your Microsoft Authenticator accounts. For more info, see [Back up and recover account credentials using the Microsoft Authenticator app](/azure/active-directory/user-help/user-help-auth-app-backup-recovery) 
2. Uninstall the Microsoft Authenticator app.
3. Uninstall Power Apps mobile.
4. Install Microsoft Authenticator again and add your back up accounts again.
5. Install [Power Apps mobile](../mobile/run-powerapps-on-mobile.md).
6. Open Power Apps mobile and sign in.

If you still can't sign in, then email us at pamobsup@microsoft.com and include your device make and model, session ID, and provide the exact error message that you get.

## App list is empty

The app list in the Power Apps mobile app may appear empty when you lose internet connection before the app list has downloaded. This can happen in any of the following scenarios:

- It's the first time you're signing in to the mobile app.
- When you pull down to refresh the app list.
- When you come back online after a period of being offline. The app list is automatically refreshed.

To resolve connection related issues, ensure you remain connected to the internet while the app list is fully downloaded.

## Pin to Home does not work on iOS 14

**iOS device running iOS 14**: The Safari browser no longer supports the **Pin to Home** functionality for Power Apps mobile. You need to use the Siri Shortcuts app to pin an app to the Home screen. For more information, see [Use Siri Shortcuts (iOS 14 or later)](../mobile/run-powerapps-on-mobile.md#use-siri-shortcuts-to-add-a-shortcut-to-the-home-screen-ios-14-or-later).

**iOS 13**: You can still use the Safari browser to pin an app to the Home screen. For more information, see [Pin an app to the home screen](../mobile/run-powerapps-on-mobile.md#use-safari-to-add-a-shortcut-ios-13-or-earlier)

## App resets when running it on Power Apps mobile

When you run a canvas or model-driven app on Power Apps mobile, it can reset if the app is using too many resources. If the app uses more resources than are available on your device, the app resets. This is similar to when you visit a large, complex webpage and the web browser suspends the page because it is consuming too much power.

On Android devices, this app restart can look like a crash because the app is closed and the user is taken to the home screen of the device.

If you experience a reset while using a canvas app, contact your app developer, and see [Prevent canvas app restarts](../mobile/power-apps-mobile-canvas-app-restarts.md).

## Unable to download SharePoint attachment in the mobile app

The Power Apps platform does not support accessing authenticated URLs, including SharePoint attachments. If you run a Power Apps application in a web browser and it tries to access a SharePoint attachment, it may work if you are signed-in to SharePoint in another tab. This is because web browsers support multiple signed-in users, and sign-ins are valid across browser tabs. However, the Power Apps mobile app is not a web browser, so does not benefit from this browser-based behavior.

## Flows created in a solution are not supported on Power Apps mobile

The Flow action menu in Power Apps mobile doesn't support flows created in a solution.

## Error: Contact your administrator for access to your organizations mobile apps

When using the Dynamics 365 mobile app, you encounter the following message: **Contact your administrator for access to your organizations mobile apps**. 

To check for recently added apps, select Refresh. If you can’t find your app, change your search criteria and try again.**

 For more information see, [Troubleshoot "We can’t find any apps for your role"  error message](https://support.microsoft.com/help/4486472/we-can-t-find-any-apps-for-your-role-message-in-dynamics-365-for-phone).
 
## The list of apps is empty

Make sure the user has a [default security role](/power-platform/admin/security-roles-privileges) assigned to them such as **Basic**. This is in addition to any custom security role assigned to the user. For more information, see [Setup overview for mobile apps](/dynamics365/mobile-app/set-up-dynamics-365-for-phones-and-dynamics-365-for-tablets#requirements).

## Error message: This record is unavailable
If this message appears when a user starts the mobile app, and then selects the **Home** button, or **Dashboards** from the menu, the user likely doesn’t have access to the expected dashboards.  

## Flows created in a solution is not supported 
The Flow action menu in Dynamics 365 for phones and tablets app doesn't support flows created in a solution.

## Error message: Your server is not available or does not support this application  
 **Cause 1**: The Microsoft Dataverse or Dynamics 365 Customer Engagement (on-premises) server is down. Verify that the server is on and connected to your network.  
 
 **Cause 2**: Your Microsoft Dataverse or Dynamics 365 Customer Engagement (on-premises) app version is not supported. For supported version information, see [What's supported](/dynamics365/mobile-app/support-phones-tablets). 
  
 **Cause 3**: This error can also occur if you enter an invalid URL. Make sure the same URL you have provided works to access Dynamics 365 apps in your browser on your device.  

## Error message: You haven't been authorized to use this app. Check with your system administrator to update your settings

 **Cause 1**: Verify that your security role includes the **Use [!INCLUDE[pn_moca_short](../includes/pn-moca-short.md)]** privilege. See "Required privileges" in [Setup overview for mobile apps](/dynamics365/mobile-app/set-up-dynamics-365-for-phones-and-dynamics-365-for-tablets#requirements).  
  
 **Cause 2**: This error can occur if you have a Microsoft Dataverse or Dynamics 365 Customer Engagement (on-premises) organization and your user has not been assigned a license for the organization. If you add a Microsoft Dataverse or Dynamics 365 Customer Engagement (on-premises) subscription to an existing [!INCLUDE[pn_MS_Office_365](../includes/pn-ms-office-365.md)] tenant, your user may not have a  license assigned. 
 
 If the user has the Global Administrator or Service Administrator role and you’re able to sign in to on the web app to perform certain administrative actions, but you can’t perform end user tasks, such as creating records (for example, accounts, contacts, and leads) or configuring Dynamics 365 for mobile. When you sign in to the web app, you may notice that not all areas appear within the navigation (for example, Sales and Marketing are missing):  
 
Access the **Active** users section in the admin center and verify you have a **Dynamics 365 Customer Engagement Plan** license assigned to your user record.  
  
## Error message: Sorry, something went wrong while initializing the app. Please try again, or restart the app  

 **Cause 1**: Permissions might not be set properly. See "Required privileges" in [Setup overview for mobile apps](/dynamics365/mobile-app/set-up-dynamics-365-for-phones-and-dynamics-365-for-tablets#requirements).  
  
 **Cause 2**: See the following KB article:  
  
 An error occurs in the [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] app for users in child business units. For more information, see [Sorry, something went wrong while initializing the app](https://support.microsoft.com/kb/2899860).  
  
 **Sample Trace Message for Cause 2**:  
  
 `Error Message:System.NullReferenceException: Object reference not set to an instance of an object.`   
 `Microsoft.Crm.Application.WebServices.ApplicationMetadataService.<>c__DisplayClass30.<UserRolesChanged>b__2d(Entity role)`   
  `at System.Linq.Enumerable.Any[TSource](IEnumerable`1 source, Func`2 predicate)`   
  `at Microsoft.Crm.Application.WebServices.ApplicationMetadataService.UserRolesChanged(Guid[] clientUserRoles, DateTime syncTime, ExecutionContext context)`   
 `at Microsoft.Crm.Application.WebServices.ApplicationMetadataService.RetrieveUserContext(UserContextRetrieveRequest userContextRetrieveRequest)`  
 
## Error message: The language installed on your company’s system isn’t available on the app. Please contact your system administrator to set up a supported language
 **Cause**: This error occurs if one of the supported languages is not enabled in Microsoft Dataverse or Dynamics 365 Customer Engagement (on-premises). For more information on the supported languages, see [Supported languages for Dynamics 365 for phones and Dynamics 365 for tablets](/dynamics365/mobile-app/support-phones-tablets#supported-languages-for--and-).

## Error message: The process assigned to this record is unavailable or has been deleted 
 If you receive this message for a record which has a nondeleted process assigned to it, you should manually synchronize Dynamics 365 mobile app data with Microsoft Dataverse or Dynamics 365 Customer Engagement (on-premises) app data. Close the mobile app, reopen it, and then choose to download the latest customizations. This procedure forces the mobile app to check for updated customizations. Recently viewed data while you were connected is cached and synched. Record data like Accounts or Contacts are not synched.
 
## Event 10001 messages appear in the Event Log when you run Dynamics 365 for mobile. 
 The following event may be recorded multiple times to the Event Log, when **Show Analytic and Debug Logs** is enabled, on the device where Dynamics 365 for mobile is running. Notice that, by default, **Show Analytic and Debug Logs** is disabled in [!INCLUDE[pn_Event_Viewer](../includes/pn-event-viewer.md)] and these messages won’t be recorded. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Enable Analytic and Debug Logs](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc749492(v=ws.11))  
  
- Event Id: 10001  
  
- Message: `SEC7131 : Security of a sandboxed iframe is potentially compromised by allowing script and same origin access.`  
  
  Verify the source of the messages. If the source is Microsoft Dataverse or Dynamics 365 Customer Engagement (on-premises), these events don’t pose a security threat and can be ignored.  
  
## Data cached for offline viewing remains after the entity is no longer enabled for Dynamics 365 for mobile
 In  Dynamics 365 for mobile, record data is cached as the user visits the record so the user can access the data when going offline.  
  
 This cached data persists after the entity is no longer enabled for Dynamics 365 for mobile (**Settings** > **Customizations** > **Customize the System** > [select an entity] > under **Outlook & Mobile**, deselect **[!INCLUDE[pn_moca_short](../includes/pn-moca-short.md)]**).  
  
 To remove the cached data, the user must sign out of mobile app, or the app must be reconfigured or uninstalled.  
    
 ## Customization changes do not appear in the mobile app
 **Cause 1**: The customizations (metadata) from Microsoft Dataverse or Dynamics 365 Customer Engagement (on-premises) organization are cached on your device. The app checks for updated metadata after 24 hours or anytime you reopen the app. For customization changes to become available immediately, you must completely close and then reopen the app. If new metadata is found, you are prompted to download it. For more information on how to completely close an app, refer to the help for your operating system or reference one of the articles provided:  
  
- **Windows 10**: [How do I close an app?](https://support.microsoft.com/help/4027154/windows-close-an-app-in-windows-10)  
  
- **iPad**: [Force an app to close](https://support.apple.com/kb/ht5137)  
  
- **Android**: [How to force close Android apps](https://support.google.com/android/answer/9079646?hl=en#close_apps)  
  
**Cause 2**: You may be seeing a different form than the one you customized. If you have multiple forms for an entity, you see the first form in the form order that you have access to. This is different than the web application where you see the last form you used and have the ability to change between forms. 

 ## Native Android or iOS links are not supported
The Dynamics 365 mobile app does not support universal links on iOS and Android app links on Android.
  
 
 
## Error message: in Android, AUTH_FAILED_INTUNE_POLICY_REQUIRED AADSTS53005: Application needs to enforce Intune protection policies

Contact your administrator or help desk and make sure that your user is under Intune app protection policies.

On your device, go to **Settings** > **General** > **Accounts** and remove any accounts that are connected with Microsoft 365.

## Error message: Access Denied. This app must be protected with an Intune policy before you can access company data

Contact your administrator or help desk and verify that Intune app protection policies are applied for your user account.

### Admin instructions to resolve the issue

If you're an admin, you can avoid users getting this error by making sure all mobile users have access to the sales dashboard:  
  
1. In the web app, go to **Settings > Customizations > Customize the System**.  
  
2. Select **Dashboards**.  
  
3. Select **Sales Dashboard**.  
  
4. Select **Enable Security Roles**.  
  
5. Select **Display to everyone** and then select **OK**. If you prefer to display only to select security roles, be sure to select your user’s security role.  
  
6. Select **Publish**.  
  
7. Have your user close and open the mobile app so your dashboard changes download.  
  
### End-user instructions to resolve the issue
   
#### You can choose a different dashboard and set it as your home page:  
  
1. From the mobile app, select the menu and then select **Dashboards**.  
  
2. On the command bar, select **Select Dashboard** and then select the dashboard you would like to use as your home page.  
  
3. On the command bar, select **Set as Home**.  
  

#### Or, you can create a personal dashboard through the web app and enable it for mobile:  
  
1. In the web app, go to **Sales > Dashboards**.  
  
2. Select **New**.  
  
3. Select **Properties**.  

4. Enter a name for your dashboard and select **Enable for mobile**.  
  
5. Add the components you want on your dashboard and select **Save**.  
  
6. In the mobile app, follow the previous procedure to select your new dashboard and set it as your home page.
   

## Network requests fail when Power Apps mobile app is running in the background

When the Power Apps mobile app is running in the background and a canvas or model-driven app makes a network request, a mobile operating system could deprioritize or cancel this network request. This can cause an error message to appear in the mobile app when it returns from the background. 

If you experience a failed network request when the Power Apps mobile app is running in the background, contact your app developer.

## App does not appear in the app list offline 
New and recently republished apps might not appear in the offline app list right away. To make your app appear in the app list offline, open the app on your device when it is online and keep it open for 1-2 minutes.

## Not able to zoom in to input elements in the app
Pinch to zoom is not supported by HTML input elements by deafult. More information on HTML input control default behavior: [HTML Input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input).

## Issue still not resolved?  
If the information provided previously doesn’t resolve your issue, either [Post your issue in the Power App Community](https://powerusers.microsoft.com/t5/Power-Apps-Community/ct-p/PowerApps1) or [Contact Technical Support](https://powerapps.microsoft.com/support/).

 The following are some suggested details to provide:

- What are the specific symptoms you encounter? For example, if you encounter an error, what is the exact error message?

- Does the issue only occur for users with certain [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] security roles?

- Does the issue only occur on certain devices but works correctly for the same user on another device?

- If you attempt to connect to a different [!INCLUDE[pn_microsoftcrm](../includes/pn-microsoftcrm.md)] organization that does not include your customizations, does the same issue occur? If the issue only occurs with your customizations, provide a copy of the customizations if possible.

- Does the issue still occur after uninstalling the app and reinstalling it?

- What type of device are you using, such as iPad 4th Generation, Microsoft Surface. What is the version of the operating system, such as iOS 10.0 or Windows 10.


### See also
[Setup overview for mobile apps](/dynamics365/mobile-app/set-up-dynamics-365-for-phones-and-dynamics-365-for-tablets)
 
[Power Pages known issues](/power-pages/known-issues)

[Power Automate known issues](/power-automate/process-advisor-issues)

[!INCLUDE[footer-include](../includes/footer-banner.md)]
