---
title: Use deep links with the Power Apps mobile app
description: How to configure deep links for Power Apps mobile.
author: trdehove
ms.component: pa-user
ms.topic: quickstart
ms.date: 11/16/2023
ms.subservice: mobile
ms.author: trdehove
ms.custom: ""
ms.reviewer: sericks
ms.assetid: 
search.audienceType: 
  - enduser
searchScope:
  - "Power Apps"
contributors:
- anuitz
- sitarampemmaraju
---

# Use deep links with the Power Apps mobile app

Deep links let users move from one application to another on computers and mobile devices. Simple examples include a mobile app deep-linking to Facebook to sign in, an email address deep-linking to a mail app to compose a message, or a website deep-linking to an app store to download a related mobile app. 

## Supported deep links in the Power Apps mobile app

You can open an `entityrecord` or an `entitylist` view in the Power Apps mobile app by using deep-link URLs from other apps. When you follow the link from an external app, the target element opens in Power Apps mobile

If you're already signed in to your instance in the app, the target record is displayed when you follow the link from an external app. Otherwise, you're prompted to sign in to your instance in the mobile app; after you're signed in, the target element is displayed. You must have the Power Apps mobile app installed on your mobile device to use this feature.

## Supported Urls parameters for a model-driven app

Use the following application handler and query string parameters to compose the URL.

Deep links for the Power Apps mobile app should start with the following:

```ms-apps://<org-url>_<app-id>?tenantId=<tenant-id>&isShortcut=true&appType=AppModule&openApp=true&restartApp=true&forceOfflineDataSync=true```

> [!IMPORTANT]
> The org-url can't contain **https://**. The following is a example of a model-driven app deeplink: <br>
> ms-apps://contoso.onmicrosoft.com_e6429eba-2204-40e8-b9dd-fc74791ff2c2?tenantId=219f9bd4-8c16-4dfa-b87e-f4a33764f1dd

| **Parameter**        | **Description**                                                              |
|----------------------|------------------------------------------------------------------------------|
| &lt;targeted-app&gt; | <ul><li>`ms-dynamicsxrm` -> Dynamics 365 for phones</li><li> `ms-apps-fs` -> Field Service</li><li>`ms-apps` -> Power Apps</li><li>`ms-mobile-apps` -> wrapped native mobile apps</li>                                                                     |
| &lt;org-url&gt;      | Connects to the correct org URL.                                              |
| &lt;app-id&gt;       | Opens the correct app module.                                                 |
| tenantId             | Connects to the correct tenant.                                               |
| forceOfflineDataSync | Ensures that data sync is triggered so that all the latest data is available. |


If opening an `entityrecord` form or creating a new `entityrecord`, use the following parameters:

| **Parameter**                       | **Description**                                                                                            |
|---------------------------------|--------------------------------------------------------------------------------------------------------|
| etn=&lt;entity-logical-name&gt; | Designates which table to go to.                                                                 |
| pagetype=entityrecord           | Indicates that the target is a form.    |
| extraqs=&lt;form-id&gt;         | Designates which form to open for the `entityrecord`; if not specified, the default form opens. The `extraqs` parameter can also be used to default field values.        |
| id=&lt;record-id&gt;            | Designates which specific record to go to; if left blank, the create form for the table opens. |

If the link goes to an `entitylist` view, add the following parameters:

| **Parameter**                                                | **Description**                                                     |
|--------------------------------------------------------------|---------------------------------------------------------------------|
| etn=&lt;entity-logical-name&gt;                              | Designates which table to go to.                              |
| pagetype=entitylist                                          | Indicates that we're going to a view.                               |
| viewid=&lt;view-id&gt;                                       | Designates which view to open.                                       |
| Viewtype= &lt;1039 if system view, 4230 if personal view&gt; | Designates whether we're going to a system view or a personal view. |

## Supported Urls parameters for a canvas app
  
```ms-apps:///providers/Microsoft.PowerApps/apps/<appID>?tenantId=<tenantId>&restartApp=true```

| **Parameter**        | **Description**                                                                              |
|----------------------|----------------------------------------------------------------------------------------------|
| &lt;app-id&gt;       | Opens the correct app module.                                                                 |
| &lt;tenantId&gt;     | Connects to the correct tenant.                                                               |
| restartApp=true      | Restarts the canvas app, needed to ensure parameters are passed when the app is already open. |
| autoLoginUpn=&lt;e-mail&gt;      | Autopopulates e-mail and triggers sign-in. | 

  ## Supported Urls parameters for a wrapped native mobile app
  
 ```ms-mobile-apps:///providers/Microsoft.PowerApps/apps/<appID>?tenantId=<tenantId>&restartApp=true```

| **Parameter**        | **Description**                                                                              |
|----------------------|----------------------------------------------------------------------------------------------|
| &lt;app-id&gt;       | Opens the correct app module.                                                                 |
| &lt;tenantId&gt;     | Connects to the correct tenant.                                                              |
| restartApp=true      | Restarts the canvas app to ensure parameters are passed when the app is already open. |
| autoLoginUpn=&lt;e-mail&gt;      | Autopopulates e-mail and triggers sign-in. |  

## Troubleshooting

Deeplinks may open in your browser depending on the company's organizational policies and the user's device settings. Mobile Device Management (MDM) tools and device operating systems have different options and settings that impact how deeplinks are handled. If deeplinks are opening in a browser instead of directly in Power Apps mobile, make sure your MDM policies and device settings are appropriately configured. 

As an example, on some Android devices, go to **Settings** > **Apps** > **Power Apps** > **Open by default** and add **apps.powerapps.com** to make deeplinks open directly in Power Apps mobile.
