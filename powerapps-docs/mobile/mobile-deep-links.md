---
title: Use deep links with the Power Apps mobile app
description: How to configure deep links for Power Apps mobile.
author: vamseedillimsft
ms.component: pa-user
ms.topic: quickstart
ms.date: 06/14/2024
ms.subservice: mobile
ms.author: vamseedilli
ms.custom: ""
ms.reviewer: smurkute
ms.assetid: 
search.audienceType: 
  - enduser
searchScope:
  - "Power Apps"
contributors:
- anuitz
- sitarampemmaraju
- vamseedilli
- smurkute
---

# Use deep links with the Power Apps mobile app

Deep links let users move from one application to another on computers and mobile devices. Simple examples include a mobile app deep-linking to Facebook to sign in, an email address deep-linking to a mail app to compose a message, or a website deep-linking to an app store to download a related mobile app. 

## Supported deep links in the Power Apps mobile app

You can open an `entityrecord` or an `entitylist` view in the Power Apps mobile app by using deep-link URLs from other apps. When you follow the link from an external app, the target element opens in Power Apps mobile

If you're already signed in to your instance in the app, the target record is displayed when you follow the link from an external app. Otherwise, you're prompted to sign in to your instance in the mobile app; after you're signed in, the target element is displayed. You must have the Power Apps mobile app installed on your mobile device to use this feature.

## Supported Urls parameters for a model-driven app

Use the following application handler and query string parameters to compose the URL.

Deep links for the Power Apps mobile app should start with the following:

```ms-apps://<org-url>_<app-id>?tenantId=<tenant-id>&environmentId=<environment-id>&appLogicalName=<appLogicalName>&appType=AppModule&openApp=true&restartApp=true&forceOfflineDataSync=true```

> [!IMPORTANT]
> The org-url can't contain **https://**. The following is an example of a model-driven app deep link: <br>
> ms-apps://contoso.onmicrosoft.com_e6429eba-2204-40e8-b9dd-fc74791ff2c2?tenantId=aaaabbbb-0000-cccc-1111-dddd2222eeee&environmentId=g67tfyufhkjfg&appLogicalName=cr12_e567

| **Parameter**        | **Description**                                                              | **Required**|
|----------------------|------------------------------------------------------------------------------|-------------|
| &lt;targeted-app&gt; | <ul><li>`ms-dynamicsxrm` -> Dynamics 365 for phones</li><li> `ms-apps-fs` -> Field Service</li><li>`ms-apps` -> Power Apps</li><li>`ms-mobile-apps` -> wrapped native mobile apps</li>                                                                     | Yes|
| &lt;org-url&gt;      | Connects to the correct org URL.                                              | Yes|
| &lt;app-id&gt;       | Opens the correct app module.                                                 | Yes|
| tenantId=&lt;tenand-id&gt;             | Connects to the correct tenant.                                               | Yes|
| *environmentId=&lt;environment-id&gt;             | Uniquely identifies the environment within a tenant.                                               | Yes|
| *appLogicalName=&lt;app-logical-name&gt;             | Unique Name of the app. For more information on how to find this unique name of the app in modern studio, refer [Manage model-driven app settings in the app designer](/power-apps/maker/model-driven-apps/app-properties) and for classic editor, refer [Manage model-driven app properties in the app designer (classic)](/power-apps/maker/model-driven-apps/manage-app-properties)                     | Yes|
|appType=AppModule     | Indicates that the targeted app is a model-driven app.                                                 | Yes|
| restartApp=true      | Restarts the model-driven app. Required to ensure parameters are passed when the app is already open. | No |
| autoLoginUpn=&lt;e-mail&gt;      | Autopopulates e-mail and triggers sign-in. <br><br>**Note**: This parameter will be ignored if a user is already signed into the app. | No|
| forceOfflineDataSync=true | Ensures that data sync is triggered so that all the latest data is available. | No|

***Considerations**

- The environment ID and appLogicalName are mandatory for all new deep links.
- Existing deep links without an environment ID or appLogicalName will experience slower performance until December 2025, after which they won't be supported.  
- Update all existing deep links to include the environment ID and appLogicalName to improve performance and reduce wait time.

If opening an `entityrecord` form or creating a new `entityrecord`, use the following parameters:

| **Parameter**                       | **Description**                                                                                            | **Required**|
|---------------------------------|--------------------------------------------------------------------------------------------------------|-------------|
| etn=&lt;entity-logical-name&gt; | Designates which table to go to.                                                                 | Yes|
| pagetype=entityrecord           | Indicates that the target is a form.    | Yes|
| id=&lt;record-id&gt;            | Designates which specific record to go to; if left blank, the created form for the table opens. | Yes|
| extraqs=&lt;form-id&gt;         | Designates which form to open for the `entityrecord`; if not specified, the default form opens. The `extraqs` parameter can also be used to default field values.        |  No|

If the link goes to an `entitylist` view, add the following parameters:

| **Parameter**                                                | **Description**                                                     | **Required**|
|--------------------------------------------------------------|---------------------------------------------------------------------|-------------|
| etn=&lt;entity-logical-name&gt;                              | Designates which table to go to.                              | Yes|
| pagetype=entitylist                                          | Indicates that we're going to a view.                               | Yes|
| viewid=&lt;view-id&gt;                                       | Designates which view to open.                                       | No|
| Viewtype= &lt;1039 if system view, 4230 if personal view&gt; | Indicates whether the targeted view is a system view or a personal view. | No|

## Supported Urls parameters for a canvas app
  
```ms-apps:///providers/Microsoft.PowerApps/apps/<appID>?tenantId=<tenantId>&environmentId=<environment-id>&restartApp=true```

| **Parameter**        | **Description**                                                                              | **Required**|
|----------------------|----------------------------------------------------------------------------------------------|-------------|
| &lt;app-id&gt;       | Opens the correct app module.                                                                 | Yes|
| tenantId=&lt;tenantId&gt;     | Connects to the correct tenant.                                                               | Yes|
| *environmentId=&lt;environment-id&gt; | Uniquely identifies the environment within a tenant. | Yes|
| restartApp=true      |  Restarts the Canvas app. Required to ensure parameters are passed when the app is already open. | No|
| autoLoginUpn=&lt;e-mail&gt;      | Autopopulates e-mail and triggers sign-in. <br><br>**Note**: This parameter will be ignored if a user is already signed into the app. | No|

***Considerations**
- The environment ID is mandatory for all new deep links.
- Existing deep links without an environment ID will experience slower performance until December 2025, after which they won't be supported.  
- Update all existing deep links to include the environment ID to improve performance and reduce wait time.

  ## Supported Urls parameters for a wrapped native mobile app
  
 ```ms-mobile-apps:///providers/Microsoft.PowerApps/apps/<appID>?tenantId=<tenantId>&restartApp=true```
 > [!IMPORTANT]
> The deep link URL for wrapped apps works when there's ONLY one wrapped app installed on the mobile device and will NOT work when there are more than one wrapped apps installed. 

| **Parameter**        | **Description**                                                                              |**Required**|
|----------------------|----------------------------------------------------------------------------------------------|-------------|
| &lt;app-id&gt;       | Opens the correct app module.                                                                 | Yes|
| tenantId=&lt;tenantId&gt;     | Connects to the correct tenant.                                                              | Yes|
| restartApp=true      |  Restarts the model-driven app. Required to ensure parameters are passed when the app is already open. | No|
| autoLoginUpn=&lt;e-mail&gt;      | Autopopulates e-mail and triggers sign-in. <br><br>**Note**: This parameter will be ignored if a user is already signed into the app.|   No|

## Troubleshooting

Deep links can open in your browser depending on the company's organizational policies and the user's device settings. Mobile Device Management (MDM) tools and device operating systems have different options and settings that affect how deep links are handled. If deep links are opening in a browser instead of directly in Power Apps mobile, make sure your MDM policies and device settings are appropriately configured. 

As an example, on some Android devices, go to **Settings** > **Apps** > **Power Apps** > **Open by default** and add **apps.powerapps.com** to make deep links open directly in Power Apps mobile.

### See also

[Important upcoming changes (deprecations) in canvas apps](/power-apps/maker/canvas-apps/important-changes-deprecations)
