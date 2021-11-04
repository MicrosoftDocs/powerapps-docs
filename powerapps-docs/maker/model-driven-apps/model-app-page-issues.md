---
title: "Known issues with custom pages in a model-driven app"
description: "Find the known issue that might occur when you create a custom page" 
ms.custom: ""
ms.date: 09/02/2021
ms.reviewer: ""
ms.service: powerapps
ms.subservice: mda-maker
ms.topic: "article"
author: "adrianorth"
ms.author: "aorth"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Known issues with custom pages in a model-driven app

The custom page is a new page type within model-driven apps. Custom pages bring the power of canvas apps into model-driven apps. Below are the known issues to be aware of.

> [!IMPORTANT]
> - The base functionality of custom pages has moved to General Availability in all regions.  However there are some specific or new capabilities that are still in public preview and are marked with _(preview)_.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)] 

## Maker-related issues

* When a custom page is modified, such as saved and published, the model-driven app isn't aware of the change. The model-driven app will continue to use the last version of the custom page when the model-driven app was published. A model-driven app publish through app designer, solution explorer, or **Publish all** will update all custom pages in the model-driven app.

* Layout or control support for Right to Left (RTL) is currently unavailable but coming soon.

* The ability to get the current users settings including locale and language is currently unavailable but coming soon.

* Custom pages use a canvas app hosting session that can time out after 8 hours.  However, the Unified Interface session has a longer timeout. When the timeout happens an error message bar appears that prompts the user to refresh the browser.

  > [!div class="mx-imgBorder"]
  > ![Custom page session timeout app message bar error](media/model-app-page-overview/page-session-timeout-app-message-error.png "Custom page session timeout app message bar error")

* When a custom page with code component is opened for editing, a security dialog is shown. Selecting **Go back** on the security dialog doesn't navigate back to the parent context. The user can close the browser tab to leave the canvas app designer.

* Not all canvas app controls are available with custom pages. However, custom pages support the most common canvas app controls and custom pro-dev components. For more information about what is available, see [Design a custom page for your model-driven app](design-page-for-model-app.md)

* Makers need to share custom pages to allow another maker to make changes, which is a different behavior than the typical model-driven app components. If a custom page can't be shared from the **Solutions** area, open the environment in Power Platform admin center, and then open **Resources** > **Power Apps** > **Page** > **Share**. Similarly to reuse the canvas app components inside the custom page, the corresponding canvas app component library also needs to be shared with the custom page makers.

* The maker experience for the custom page doesn't have support for certain Power Apps component framework APIs like `Navigation` and Web APIs which is inline with the stand alone canvas apps. However, these APIs are available in the published app where the custom page is added to model-driven apps. More information: [add code components to a custom page for your model-driven app.](/powerapps/maker/model-driven-apps/page-code-components)

* The maker experience for the custom page is currently not enabled in sovereign clouds. If you would like to enable it for a maker session, append "powerappsPortalApps.enableEditInShellAppDesigner=true" as a query parameter to the https://make.powerapps.com/ url.

## User-related issues

* When a user with no Power Apps user privileges opens a custom page in the model-driven app, they will see an error mentioning no active entitlements to use PowerApps.  More information: [Licensing overview for Microsoft Power Platform](/power-platform/admin/pricing-billing-skus) and the associated licensing guide.

* Custom pages require third-party cookies to be enabled, which is required by the canvas app runtime.

* When a user is prompted for consent with connectors and selects **Don't allow**, the custom page will render but without data.  The user doesn't get notified that data retrieval is skipped.

* After a model-driven app or custom page is changed and published, loading a custom page can take longer than normal and no page loading spinner is shown.

* When navigating back to a custom page from another page, the page state isn't restored so the page appears like a new navigation.

* Native player support is available for iOS and Android in online-only mode. Offline support will come later. The preview Dynamics 365 Windows player displays a blank page when a custom page is opened.

* When a user running Internet Explorer opens a custom page, an error message will appear indicating Internet Explorer isn't supported.

* While attempting to sign in, the current behavior caused by a user selecting anywhere away from the sign in box causes the pop out window for sign in to shift behind the app browser.

* When a user runs an app that isn't compliant with their organization's [Data Loss Prevention (DLP) policies](/power-platform/admin/wp-data-loss-prevention), they'll see an error dialog and the 'Technical details' reflects the app isn't DLP compliant. 

   ![Data Loss Prevention error dialog](media/model-app-page-issues/power_apps_unified_app_dlp_error.png "Data Loss Prevention error dialog")


## See also

[Model-driven app custom page overview](model-app-page-overview.md)
