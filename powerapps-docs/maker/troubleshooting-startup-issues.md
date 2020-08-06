---
title: Troubleshooting startup issues for Power Apps | Microsoft Docs
description: This troubleshooting guide helps fix common configuration problems that prevent Power Apps from starting.
author: matthewbolanos
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 08/06/2020
ms.author: mabolan
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Troubleshooting startup issues for Power Apps

This troubleshooting article helps fix common configuration problems that prevent Power Apps from starting.

## Common errors

- When you sign in to Power Apps - especially using the *InPrivate* or *incognito* experience, you receive the following error:

    ```
    Sign in required
    Please select sign in to continue.
    Session ID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    
    AADSTS50058: A silent sign-in request was sent but no user is signed in. The cookies used to represent the user's session were not sent in the request to Azure AD. This can happen if the user is using Internet Explorer or Edge, and the web app sending the silent sign-in request is in different IE security zone than the Azure AD endpoint (login.microsoftonline.com).
    Trace ID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    Correlation ID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    Timestamp: xxxx-xx-xx xx:xx:xxZ

    ```

    **Resolution**: [Don't block third-party cookies](#resolution-4-allow-third-party-cookies).

- When you receive a “Hmmm … We couldn’t sign you in” error message and identifier that resembles the following image:

    ![Hmmm … We couldn’t sign you in. The information below may be helpful](./media/troubleshooting-startup-issues/error.png "Hmmm … We couldn’t sign you in. The information below may be helpful")

    **Resolution**: Check [Resolutions for common errors](#resolutions-for-common-errors) for different error variations and resolutions.
    
- When you try to create an app from a SharePoint list, you receive the following "abnormal termination" error message
    ```
    WebAuthoring abnormal termination.

    Client date/time: <Client Time>Thh:mm:ss.sssZ
    Version: 2.0.602
    Session ID: xxxx-xxxxx-xxxxxxx--xxxxxxxx
    description: {"error":{"detail":{"exception":{}},"colno":0,"filename":"https://paaeuscdn.azureedge.net/v2.0.602.0/studio/openSource/modified/winjs/js/base.js?v=39de0f2edf1...",
    "lineno":0,"message":"Script error","initErrorEvent":"[function]","bubbles":false,"cancelBubble":false,"cancelable":false,"currentTarget":"[window]","defaultPrevented":true,
    "eventPhase":2,"isTrusted":true,"srcElement":"[window]","target":"[window]","timeStamp":1490711965955,"type":"error","initEvent":"[function]","preventDefault":"[function]",
    "stopImmediatePropagation":"[function]","stopPropagation":"[function]","AT_TARGET":2,"BUBBLING_PHASE":3,"CAPTURING_PHASE":1},"errorLine":0,"errorCharacter":0,
    "errorUrl":"https://paaeuscdn.azureedge.net/v2.0.602.0/studio/openSource/modified/winjs/js/base.js?v=39de0f2edf1... error","setPromise":"[function]","exception":{}}
    stack: null
    errorNumber: 0
    errorMessage: Script error
    ```

To resolve the issues listed above, read [Resolutions for common errors](#resolutions-for-common-errors), and try one of the listed resolutions.

## Resolutions for common errors

| Error identifier                                                              | Microsoft Internet Explorer 11          | Microsoft Edge (Legacy)                         | Google Chrome                        |
|-------------------------------------------------------------------------------|-------------------------------|-------------------------------|-------------------------------|
| Sign in required | [Allow third-party cookies](#resolution-4-allow-third-party-cookies) | [Allow third-party cookies](#resolution-4-allow-third-party-cookies) | [Allow third-party cookies](#resolution-4-allow-third-party-cookies) |
| UserInterventionNeeded_CookiesBlocked <br> UserInterventionNeeded_StorageBlocked   | [Enable storage of local data](#resolution-1-enable-storage-of-local-data-in-your-browser)  | [Enable storage of local data](#resolution-1-enable-storage-of-local-data-in-your-browser)  | [Enable storage of local data](#resolution-1-enable-storage-of-local-data-in-your-browser)  |
| UserInterventionNeeded_NavigateToAadTimeout                                   | Possible network problem      | [Configure Trust Zones](#resolution-2-configure-trust-zones-for-internet-explorer-and-microsoft-edge-legacy)         | Possible network problem      |
| UserInterventionNeeded_NavigateToAadDenied <br> UserInterventionNeeded_StorageLost | [Configure Trust Zones](#resolution-2-configure-trust-zones-for-internet-explorer-and-microsoft-edge-legacy)         | [Configure Trust Zones](#resolution-2-configure-trust-zones-for-internet-explorer-and-microsoft-edge-legacy)         | Not applicable                |
| AadError                                                                      | [Azure Active Directory Errors](#resolution-3-azure-active-directory-errors) | [Azure Active Directory Errors](#resolution-3-azure-active-directory-errors) | [Azure Active Directory Errors](#resolution-3-azure-active-directory-errors) |

### new table

| Error | Microsoft Edge | Microsoft Edge Legacy | Microsoft Internet Explorer 11 | Google Chrome |
| - | - | - | - | - |
| Sign in required | [Allow third-party cookies](#resolution-4-allow-third-party-cookies) | [Allow third-party cookies](#resolution-4-allow-third-party-cookies) | [Allow third-party cookies](#resolution-4-allow-third-party-cookies) | [Allow third-party cookies](#resolution-4-allow-third-party-cookies) | [Allow third-party cookies](#resolution-4-allow-third-party-cookies) |
| UserInterventionNeeded_CookiesBlocked <br> UserInterventionNeeded_StorageBlocked | [Enable storage for local data](#instructions-for-microsoft-edge) | [Enable storage for local data](#instructions-for-microsoft-edge-legacy) | [Enable storage for local data](#instructions-for-internet-explorer-11) | [Enable storage for local data](#instructions-for-google-chrome) |
| UserInterventionNeeded_NavigateToAadTimeout | Possible network problem | [Configure Trust Zones](#resolution-2-configure-trust-zones-for-internet-explorer-and-microsoft-edge-legacy)  | Possible network problem | Possible network problem |
| UserInterventionNeeded_NavigateToAadDenied <br> UserInterventionNeeded_StorageLost | Not applicable | [Configure Trust Zones](#resolution-2-configure-trust-zones-for-internet-explorer-and-microsoft-edge-legacy) | [Configure Trust Zones](#resolution-2-configure-trust-zones-for-internet-explorer-and-microsoft-edge-legacy) | Not applicable |
| AadError | [Azure Active Directory Errors](#resolution-3-azure-active-directory-errors) | [Azure Active Directory Errors](#resolution-3-azure-active-directory-errors) | [Azure Active Directory Errors](#resolution-3-azure-active-directory-errors) | [Azure Active Directory Errors](#resolution-3-azure-active-directory-errors) |

## Resolution 1: Enable storage of local data in your browser
Power Apps stores some data locally in your browser, including user identity and preferences. Power Apps can’t function if the browser is configured to disallow storage of local data.

### Instructions for Internet Explorer 11

- **Option 1: Enable local data for all sites**

    1. Close all Internet Explorer and Microsoft Edge windows.
    2. Select **OK** to close the **Internet Options** dialog box.
    3. Select **OK**.
    4. Remove any entries for **powerapps.com**.
    5. In the **Settings** section, select **Sites**.
    6. Select **OK**.
    7. Select **Accept** for third-party cookies.
    8. Select **Accept** for first-party cookies.
    9. In the **Settings** section, select **Advanced**.
    10. Select the **Privacy** tab.
    11. Select **Internet Options**.
    12. On the browser toolbar, select the gear icon.
    13. Open Internet Explorer.

- **Option 2: Create exceptions to enable local data for Power Apps and associated services**
    1. Open Internet Explorer.
    2. On the browser toolbar, select the gear icon.
    3. Select **Internet Options**.
    4. Select the **Privacy** tab.
    5. In the **Settings** section, select **Sites**.
    6. Add an entry to “Allow” **powerapps.com**.
    7. Select **OK**.
    8. Select **OK** to close the Internet Options dialog box.
    9. Close all Internet Explorer and Microsoft Edge windows.

### Instructions for Microsoft Edge
1. Open Microsoft Edge.
2. On the Microsoft Edge toolbar, select **Settings and more**.
1. Select **Site permissions** from the left pane.
1. Select **Cookies and site data**.
1. Turn On **Allow sites to save and read cookie data (recommended)**.
1. Close all Internet Explorer and Microsoft Edge windows.

### Instructions for Microsoft Edge Legacy
1. Open Microsoft Edge.
2. On the Microsoft Edge toolbar, select **More** > **Settings**.
3. Near the bottom of the panel, select **View advanced settings**.
4. Near the bottom of the panel, find the **Cookies** drop-down options list.
5. Select **Don’t block cookies**.
6. Close all Internet Explorer and Microsoft Edge windows.

### Instructions for Google Chrome
    
- **Option 1: Enable local data for all sites**
    1. On your browser toolbar, select **More**.
    2. Select **Settings**.
    3. Near the bottom of the page, select **Show advanced settings**.
    4. In the "Privacy" section, select **Content settings**.
    5. Select **Allow local data to be set (recommended)**.
    6. Make sure that **Block third-party cookies and site data** isn't selected.
    7. Select Manage exceptions and make sure that there are no exceptions for **https://create.powerapps.com**, **https://\*.create.powerapps.com**, **https://make.\*.powerapps.com**, **https://make.powerapps.com**, and **https://login.microsoftonline.com**. If there are such exceptions, remove them by clicking on the x sign for the corresponding rows.
    8. Select **Done**.
    
- **Option 2: Create exceptions to allow local data for Power Apps and associated services**
      
    1. On the browser toolbar, select **More**.
    2. Select **Settings**.
    3. Near the bottom of the page, select **Show advanced settings**.
    4. In the Privacy section, select **Content settings**.
    5. Select **Manage exceptions** and create exceptions to “Allow” data storage for **https://create.powerapps.com**, **https://\*.create.powerapps.com**, **https://make.\*.powerapps.com**, **https://make.powerapps.com**, and **https://login.microsoftonline.com**.
    6. Select **Done**.


## Resolution 2: Configure Trust Zones for Internet Explorer and Microsoft Edge Legacy

Internet Explorer and Microsoft Edge Legacy use *Trust Zones*. Problems can occur if services on which Power Apps relies are in different Trust Zones in your browser settings. While these settings apply to both Internet Explorer and Microsoft Edge Legacy, the easiest way to access them is from Internet Explorer. (You might need assistance from your IT administrator to change some of these settings.)

- **Option 1: Add the required Power Apps domains to the Trusted Sites zone**
    1. On the browser toolbar, select the gear icon.
    2. Select **Internet Options**.
    3. Select the **Security** tab.
    4. Select **Trusted sites**.
    5. Select **Sites**.
    6. Add the following sites by typing the address and selecting **Add** for each:
        - **https://login.microsoftonline.com**
        - **https://create.powerapps.com**
        - **https://*.create.powerapps.com** (the asterisk is part of the address, don't replace it)
        - **https://make.powerapps.com**
        - **https://make.*.powerapps.com** (the asterisk is part of the address, don't replace it)
        - **https://*.powerapps.com** (the asterisk is part of the address, don't replace it)
    7. Select **Close**.
    8. Select **OK**.
    9. Close all Internet Explorer and Microsoft Edge Legacy windows.

- **Option 2: Remove all the Power Apps domains from the Trusted Sites zone**
    1. On the browser toolbar, select the gear icon.
    2. Select **Internet Options**.
    3. Select the **Security** tab.
    4. Select **Trusted sites**.
    5. Select **Sites**.
    6. Remove all existing entries for the following sites:
        - **https://login.microsoftonline.com**
        - **https://create.powerapps.com**
        - **https://*.create.powerapps.com**
        - **https://make.powerapps.com**
        - **https://make.*.powerapps.com** 
        - Any other address that ends in **powerapps.com** or **create.powerapps.com**.
  7. Select **Close**.

## Resolution 3: Azure Active Directory Errors

Azure Active Directory (Azure AD) is the technology on which the Power Apps relies for user authentication and authorization.

The error page that you see might contain additional information that can help diagnose and fix the problem.

To resolve Azure AD errors, you might need assistance from your IT department.

## Resolution 4: Allow third-party cookies

To disable the **Block third-party cookies** setting in your browser:

| Browser | Steps |
| - | - |
| Microsoft Edge | **Settings and more**  > **Settings**  > **Site permissions**  > **Cookies and site data** > Turn off **Block third-party cookies**. |
| Microsoft Edge Legacy | **More** > **Settings** > **View advanced settings** > **Cookies** > Turn off **Block third-party cookies**. |
| Google Chrome | **More** > scroll down to **Privacy and security** > **Cookies and other site data** > Select an option to allow third-party cookies. For example,  **Allow all cookies** for always, or **Block third-party cookies in incognito** for only blocking in *incognito*. <br> **Note**: You can also start *incognito* session and turn **Block third-party cookies** in the browser window before enter you URL in the address bar. 
| Internet Explorer 11 | **Tools** > **Internet Options** > **Advanced** > Select **Allow** under **Third-party Cookies**.

Most browsers allow settings to reflect the changes immediately. You may also close all the browser windows and reopen instead.

### See also

- [Common issues and resolutions](canvas-apps/common-issues-and-resolutions.md)
- [Power Apps Support](https://powerapps.microsoft.com/support/)
