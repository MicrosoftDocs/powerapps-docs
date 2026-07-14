---
title: "Known issues with custom pages in a model-driven app"
description: "Find the known issue that might occur when you create a custom page." 
ms.custom: ""
ms.date: 04/16/2025
ms.reviewer: ""
ms.subservice: mda-maker
ms.topic: troubleshooting-known-issue
author: "adrianorth"
ms.author: "aorth"
search.audienceType: 
  - maker
---
# Known issues with custom pages in a model-driven app

The custom page is a new page type within model-driven apps. Custom pages bring the power of canvas apps into model-driven apps. Below are the known issues to be aware of.

> [!IMPORTANT]
> Using custom pages with mobile devices is currently in public preview. Offline and device capability controls like barcode scanning, capturing photos from device, or attaching files isn't supported.
>
> Custom pages aren't supported within **App for Outlook** and return an error on loading.

## Maker-related issues

* When a custom page is modified, such as saved and published, the model-driven app isn't aware of the change. The model-driven app continues to use the last version of the custom page when the model-driven app was published. A model-driven app published through app designer, solution explorer, or **Publish all** updates all custom pages in the model-driven app.

* Images, icons, and shapes aren't currently supported with Right-To-Left (RTL) languages.
  
* The [App.ConfirmExit](/power-platform/power-fx/reference/object-app#confirmexit) property isn't supported in custom pages. 

* The ability to get the current data formats from users settings including date, time, numbers, and currency isn't supported.

* Custom pages use a canvas app hosting session that can time out after 8 hours.  However, the Unified Interface session has a longer timeout. When the timeout happens, an error message bar appears that prompts the user to refresh the browser.

  > [!div class="mx-imgBorder"]
  > ![Custom page session timeout app message bar error](media/model-app-page-overview/page-session-timeout-app-message-error.png "Custom page session timeout app message bar error")

* When a custom page with code component is opened for editing, a security dialog is shown. Selecting **Go back** on the security dialog doesn't navigate back to the parent context. The user can close the browser tab to leave Power Apps Studio.

* Not all canvas app controls are available with custom pages. However, custom pages support the most common canvas app controls and custom pro-dev components. For more information about what is available, see [Design a custom page for your model-driven app](design-page-for-model-app.md)

* Makers need to share custom pages to allow another maker to make changes, which is a different behavior than the typical model-driven app components. If a custom page can't be shared from the **Solutions** area, open the environment in Power Platform admin center, and then open **Resources** > **Power Apps** > **Page** > **Share**. Similarly, to reuse the canvas app components inside the custom page, the corresponding canvas app component library also needs to be shared with the custom page makers.

* The maker experience for the custom page doesn't have support for certain Power Apps component framework APIs like `Navigation` and Web APIs, which is in line with the stand-alone canvas apps. However, these APIs are available in the published app where the custom page is added to model-driven apps. More information: [Add code components to a custom page for your model-driven app.](/powerapps/maker/model-driven-apps/page-code-components)

* The maker experience for the custom page is currently not enabled in sovereign clouds. If you would like to enable it for a maker session, append "powerappsPortalApps.enableEditInShellAppDesigner=true" as a query parameter to the https://make.powerapps.com/ url.

* Makers can't use cross-environment Dataverse references in a custom page.

## User-related issues

* When a user with no Power Apps user privileges opens a custom page in the model-driven app, they see an error mentioning no active entitlements to use Power Apps. More information: [Licensing overview for Microsoft Power Platform](/power-platform/admin/pricing-billing-skus) and the associated licensing guide.

* Custom pages require third-party cookies to be enabled, which is required by the canvas app runtime.

* When a user is prompted for consent with connectors and selects **Don't allow**, the custom page renders but without data.  The user doesn't get notified that data retrieval is skipped.

* After a model-driven app or custom page is changed and published, loading a custom page can take longer than normal, and no page loading spinner is shown.

* Native player support is available for iOS, Android, and Windows in online-only mode. Offline support currently isn't supported.

* When you go back to a custom page from another page, the page state isn't restored so the page appears like a new navigation. State is also not persisted when switching between multi-session tabs in multi-session apps. For more information about multi-session support with model-driven apps, go to [Customer Service workspace sessions and tabs](/dynamics365/customer-service/csw-overview?tabs=customerserviceadmincenter).

* While attempting to sign in, the current behavior caused by a user selecting anywhere away from the sign in box causes the pop out window for sign in to shift behind the app browser.

* When a user runs an app that isn't compliant with their organization's [Data Loss Prevention (DLP) policies](/power-platform/admin/wp-data-loss-prevention), they see an error dialog and the 'Technical details' reflects the app isn't DLP compliant. 

   ![Data Loss Prevention error dialog](media/model-app-page-issues/power_apps_unified_app_dlp_error.png "Data Loss Prevention error dialog")

* When there are multiple custom pages in an app, the consent dialog asks for data permissions for all of the connectors in all the custom pages even if they haven't yet been opened.

## Connections

* All custom pages share the connection infrastructure, as if they were part of the same canvas app. For instance, if a model-driven app has two custom pages and one is connected to SQL Server while the other isn't, the consent dialog will still appear and require permission for SQL access even if the page being opened doesn't require it.
* Custom pages in model-driven apps don't support connection detection through the *Connected.connected* property.
* The number of connectors in a model-driven app, across all custom pages, shouldn't exceed 10. The number of connection references, across all custom pages, shouldn't exceed 20. The number of connectors and connection references can increase the wait time an app user experiences when the user plays an app with custom pages.
* The **App Permissions** dialog is not opened when a custom page is first opened by a user in the Power Apps mobile app.  This behavior can cause the page to appear frozen, but is expected behavior.  To resolve this issue, open the app in a browser to approve the permissions before playing it in the Power Apps mobile app. You can also run the [AdminPowerAppApisToBypassConsent](/powershell/module/microsoft.powerapps.administration.powershell/set-adminpowerappapistobypassconsent?view=pa-ps-latest&preserve-view=true) PowerShell command to bypass the need for the permissions dialog by a Power Platform administrator.

## See also

[Model-driven app custom page overview](model-app-page-overview.md)
