---
title: "Converge model-driven and canvas apps using the custom page"
description: "Add a custom page to use canvas as a page in your model-driven app" 
ms.date: 06/20/2021
ms.reviewer: "matp"

ms.subservice: mda-maker
ms.topic: overview
author: "adrianorth"
ms.author: "aorth"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
---
# Overview of custom pages for model-driven apps

The custom page is a new page type within a model-driven app, which brings the power of canvas apps into model-driven apps. Custom pages increase the convergence of model-driven and canvas apps and can be used to add full pages, dialogs, or panes with the flexibility of the canvas designer. It also includes a low-code page authoring experience with expressions and custom Power Apps component framework controls.  

This new page can be more flexible than a model-driven app form, view, or dashboard page. It lets you include one or more tables. Then, the maker can define the data and component interactions. The custom page is a separate solution element, which allows one maker to edit one custom page at a time. Like other model-driven app pages, the page state is either from the parameters passed or retrieved from persisted tables.

> [!IMPORTANT]
> - The base functionality of custom pages has moved to general availability in all regions.  However some specific or new capabilities are still in public preview and are marked with _(preview)_.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)] 
> - Custom pages are a new feature with significant product changes and currently have a number of known limitations outlined in [Custom Page Known Issues](model-app-page-issues.md).

| Capability | Status | Notes |
| -- | -- | -- |
| Runtime for custom pages | General Availability |
| Solution and ALM for custom pages | General Availability |
| Connectors in custom pages | General Availability | [List of all Power Apps connectors](/connectors/connector-reference/connector-reference-powerapps-connectors) |
| Modern controls in custom pages | General Availability | [List of supported controls](design-page-for-model-app.md#supported-controls-in-a-custom-page)
| Code components in custom pages | General Availability |
| Monitor support for custom pages | General Availability |
| Authoring custom pages | Public Preview | Modern app designer and canvas designer are expected to be used to author custom page that are supported at runtime |
| Canvas components in custom pages | Public Preview |
| Custom page in Teams model-driven app | Public Preview |
| Custom page in mobile online | Public Preview | iOS must allow enabling “Allow cross site tracking” that can be prevented by device management |

## Examples of custom pages

Below shows the custom page inline within the model-driven app. The model-driven app has the full-page space in the images without the header and navigation.

[Custom page as main page](add-page-to-model-app.md).

  > [!div class="mx-imgBorder"]
  > ![Custom page as main page](media/model-app-page-overview/page-inline-model-app.png "Custom page as main page")

[Custom page as a center dialog](/powerapps/developer/model-driven-apps/clientapi/navigate-to-custom-page-examples#open-as-a-centered-dialog).

  > [!div class="mx-imgBorder"]
  > ![Custom page as center dialog](media/model-app-page-overview/page-center-dialog-model-app.png "Custom page as center dialog")

[Custom page as a side dialog](/powerapps/developer/model-driven-apps/clientapi/navigate-to-custom-page-examples#open-as-a-side-dialog).

  > [!div class="mx-imgBorder"]
  > ![Custom page as side dialog](media/model-app-page-overview/page-side-dialog-model-app.png "Custom page as side dialog")
  > 

[Custom page as an app side pane](/powerapps/developer/model-driven-apps/clientapi/create-app-side-panes) allows opening a custom page within the new app side pane on the right side of the app.

  > [!div class="mx-imgBorder"]
  > ![Custom page as app side pane](media/model-app-page-overview/page-app-side-pane-model-app.png "Custom page as app side pane")
  > 

Custom pages must be created from a solution either from the modern app designer or the **Solution** area in Power Apps using **New** > **Page**. More information: [Add a custom page to your model-driven app](add-page-to-model-app.md)

## Custom pages are different than embedded canvas apps

A custom page enables makers to create a new page experience using the canvas app capabilities. This provides a low-code authoring experience with more flexible layouts, more control with styling options, the ability to add connector data, use expressions, and so on. Custom page authoring happens in the canvas app designer with increasing context of the model-driven app that the page runs in.

Embedded canvas apps also use the canvas capabilities with a hosting approach that isn't as integrated as a custom page. The simpler integration of an embedded canvas app means the current limitation on number of embedded canvas apps hasn't changed. The advanced integration of the custom page addresses those limits. The embedded canvas app can only be placed on a model-driven form acting like a low-code component. More information: [Embed a canvas app on a model-driven form](embed-canvas-app-in-form.md).

In most cases, we recommend that you use custom pages instead of embedded canvas apps for tighter integration and better performance. 

## Migrating standalone canvas app content to custom pages

Existing standalone canvas apps aren't supported for use as a custom page and the expected app structure is different. A standalone canvas app often has many screens with global access to all controls and variables. The custom page is expected to typically be a single screen with loose coupling to provide performance and co-development capabilities.

To migrate an existing standalone canvas app, first start by identifying a mapping of screens to separate custom pages. For each separate custom page complete the following steps:

1. Create a blank custom page from the model-driven app designer. More information: [Add a custom page to your model-driven app](add-page-to-model-app.md)
1. Add a canvas app data source for data used by the screen.
1. Copy the screen from the canvas app in the original canvas app designer.
1. Paste the screen into the new custom page in the model-driven app designer.
1. Change the navigate calls to use the custom page name instead of the screen name.
1. Add the custom page into the model-driven app designer site map.

## Frequently asked questions

* What data can the custom page use?

  A custom page can use Microsoft Dataverse and all of the connectors for Power Apps. More information: [List of all Power Apps connectors](/connectors/connector-reference/connector-reference-powerapps-connectors).

* What interactions can the custom page have with the model-driven app?

  Custom pages can be added to the site map for direct navigation using [Add custom page to sitemap](add-page-to-model-app.md#add-an-existing-custom-page-into-a-site-map). Model-driven app pages can open a custom page using the `navigateTo` Client API. Custom pages can navigate to other custom pages or to a model-driven app page such as a form, view, or dashboard with the Power Fx navigate function. More information: [Navigating to a custom page](page-powerfx-in-model-app.md#navigating-to-a-custom-page)

* How is the custom page made responsive?

  The responsive container controls enable building a responsive app page without formulas. More information: [Building responsive pages](../canvas-apps/build-responsive-apps.md).  More custom page design guidance can also be found in [Design a custom page for your model-driven app](design-page-for-model-app.md).

* How is the custom page managed in a solution?

  Each custom page is a separate component in the solution, which allows one maker to edit one custom page at a time. Most custom pages will have a single screen. Instead of multiple screens, they will use the custom page's navigation functions to move to another custom page or model-driven app page. When a custom page has multiple screens, it's still a single solution component so only one maker can be working on the contained set of screens.

* What licenses are allowed to use a custom page and does a custom page impact app counts?

  The custom page uses a special canvas app type, which allows it to be managed differently. The custom page is considered part of the model-driven app infrastructure and can only be used within a model-driven app. So, it follows the license for the model-driven app. Also, custom pages don't count toward the app limits because they're treated as a page instead of an app.

* Do custom pages need to be shared like standalone canvas apps?

  The custom page is aligned with the model-driven app page sharing, which relies on the model-driven app sharing without sharing individual pages for app users. Makers may need to share the custom page to allow editing.

### See also

[Add a custom page to your model-driven app](add-page-to-model-app.md)

[Design a custom page for your model-driven app](design-page-for-model-app.md)

[Using PowerFx in custom page](page-powerfx-in-model-app.md)

[Add connectors into custom pages](../canvas-apps/add-data-connection.md)

[Use Monitor to troubleshoot custom page](monitor-page-checker.md)

[Model-driven app custom page known issues](model-app-page-issues.md)
