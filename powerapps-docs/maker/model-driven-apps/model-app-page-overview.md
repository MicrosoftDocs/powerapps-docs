---
title: "Converge model-driven and canvas apps using the custom page"
description: "Add a custom page to use canvas as a page in your model-driven app" 
ms.date: 06/20/2021
ms.reviewer: "matp"
ms.service: powerapps
ms.topic: "overview"
author: "adrianorth"
ms.author: "aorth"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
---
# Overview of custom pages for model-driven apps

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

The custom page is a new page type within a model-driven app, which brings in the power of canvas apps. Custom pages is a huge step towards the convergence of model-driven and canvas apps. Custom pages can be used to add full pages, dialogs, or panes to the model-driven app utilizing the power of the canvas designer. Custom page also includes support for low-code page authoring experiences with Power Fx expressions, canvas components and custom code components. 

This new page is more flexible than the current model-driven application form, view, or dashboard page. For example, it lets you include one or more tables on a single page. Maker can then define data and component interactions using expressions. The custom page is a separate solution element supporting co-authoring at a page level. Like other model-driven app pages, the custom page state can be governed either from the parameters passed or retrieved from persisted tables.
Images below shows inline rendering of a custom page within the model-driven app. This custom page utilizes all of the available space while maintaining header and navigation areas from the main model-driven app. 

Custom page as main page.

  > [!div class="mx-imgBorder"]
  > ![Custom page as main page](media/model-app-page-overview/page-inline-model-app.png "Custom page as main page")

Custom page as a center dialog.

  > [!div class="mx-imgBorder"]
  > ![Custom page as center dialog](media/model-app-page-overview/page-center-dialog-model-app.png "Custom page as center dialog")

Custom page as a side dialog.

  > [!div class="mx-imgBorder"]
  > ![Custom page as side dialog](media/model-app-page-overview/page-side-dialog-model-app.png "Custom page as side dialog")
  > 

Custom page must be created from a solution either from the modern app designer or the Solution area in Power Apps using New > Page. See [add a custom page to your model-driven app](add-page-to-model-app.md) for details.

  > [!IMPORTANT]
  > - This is a preview feature, and isn't available in all regions.
  > - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

Custom pages is a new feature with significant product changes and currently has a number of known limitations outlined in [Custom Page Known Issues](model-app-page-issues.md).

## Custom pages are different than embedded canvas apps

A custom page enables makers to create a new page experience using the canvas app capabilities. This provides a low-code authoring experience with more flexible layouts, better control with styling options, ability to add connector data, use expressions, custom UX components and so on. Custom page authoring happens in the canvas app designer which has  added context of the model-driven app that the page runs in.

While embedded canvas apps can utilize limited canvas capabilities with the full app hosting approach, embedding is not deeply integrated. The direct use of embedded canvas app also implies that the current limitation on number of embedded canvas apps hasn't changed. The advanced integration of the custom page addresses those limits and is much more performant. Additionally, the embedded canvas app can only be placed within a model-driven form which is not the case with the custom page. For more information, see [Embed a canvas app on a model-driven form](embed-canvas-app-in-form.md).

Think of a custom page in your model-driven app like a table, form or a dashboard page. This page can consist of any set of controls that are supported on the page. Custom page can interact and seamlessly navigate between other model-driven app page types and other custom pages. A custom page is truly a single page and is not like a canvas app that can have multiple screens or pages inside of it. 

In most cases, we recommend that you use custom pages instead of embedded canvas apps for tighter integration and better performance. 


## Migrating standalone canvas app content to custom pages

Existing standalone canvas apps aren't supported for use as a custom page and the expected app structure is different. A standalone canvas app often has many screens with global access to all controls and variables. The custom page is expected to typically be a single screen with loose coupling to provide performance and co-development capabilities.

To migrate an existing standalone canvas app, first start by identify a mapping of screens to separate custom pages. For each separate custom page do the following steps:

1. Create a blank custom page from the model-driven app designer. More information: [Add a custom page to your model-driven app](add-page-to-model-app.md)
1. Add a canvas app data source for data used by the screen.
1. Copy the screen from the canvas app in the original canvas app designer.
1. Paste the screen into the new custom page in the model-driven app designer.
1. Change the navigate calls to use the custom page name instead of the screen name.
1. Add the custom page into the model-driven app designer sitemap.

## Frequently asked questions

* What data can the custom page use?

  A custom page can use Dataverse and some of the most common connectors for Power Apps. The list of verified connectors is listed in [Add connectors into custom pages](page-data-connector.md).

* What interactions can the custom page have with the model-driven app?

  Custom pages can be added to the site map for direct navigation using [Add custom page to sitemap](add-page-to-model-app.md#add-existing-custom-page-into-model-driven-app-sitemap). Model pages can open a custom page using the `navigateTo` Client API. Custom pages can navigate to other custom pages or to a model-driven app page like form, view, or dashboard with the PowerFx navigate function. More information: [Navigating to and from a custom page in your model-driven app](navigate-page-examples.md)

* How is the custom page made responsive?

  The recently released responsive container controls enables building a responsive app page without formulas. More information: [Building responsive pages](../canvas-apps/build-responsive-apps.md).  More custom page design guidance can also be found in [Design a custom page for your model-driven app](design-page-for-model-app.md).

* How is the custom page managed in a solution?

  Each custom page is a separate component in the solution, which allows one maker to edit a custom page at a time.  Most custom pages will have a single screen. Instead of multiple screens, they will use the custom page's navigation functions to move to another custom page or model-driven app page. When a custom page has multiple screens, it's still a single solution component so only one maker can be working on the contained set of screens.

* What licenses are allowed to use a custom page and does a custom page impact app counts?

  The custom page uses a special canvas app type, which allows it to be managed differently. The custom page is considered part of the model-driven app infrastructure and can only be used within a model-driven app. So, it follows the license for the model-driven app. Also, custom pages don't count toward the app limits because they're treated as a page instead of an app.

* Do custom pages need to be shared like standalone canvas apps?

  The custom page is aligned with the model-driven app page sharing, which relies on the model-driven app sharing without sharing individual pages for app users. Makers may need to share the custom page to allow editing.

### See also

[Add a custom page to your model-driven app](add-page-to-model-app.md)

[Design a custom page for your model-driven app](design-page-for-model-app.md)

[Navigating to and from a custom page in your model-driven app](navigate-page-examples.md)

[Using PowerFx in custom page](page-powerfx-in-model-app.md)

[Add connectors into custom pages](page-data-connector.md)

[Use Monitor to troubleshoot custom page](monitor-page-checker.md)

[Model-driven app custom page known issues](model-app-page-issues.md)
