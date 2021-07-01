---
title: "Converge model-driven and canvas apps using the custom page"
description: "Use a custom page to add a canvas app as a page to your model-driven app" 
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
# Overview of canvas app custom pages for model-driven apps

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

The custom page is a new page type within a model-driven app, which brings in the power of canvas apps. Custom pages increase the convergence of model-driven and canvas apps. Custom pages can be used to add full pages, dialogs, or panes with the power of the canvas app designer. It also includes a low-code page authoring experience with expressions and custom PCF controls.  

This new page can be more flexible than a modeled form, view, or dashboard page. It lets you include one or more tables. Then, the maker can define the data and component interactions. The custom page is a separate solution element supporting co-authoring at a page level. Like other model-driven app pages, the page state is either from the parameters passed or retrieved from persisted tables.

Below shows the custom page inline within the model-driven app having the full-page space other than header and navigation.

Custom page as main page.

  > [!div class="mx-imgBorder"]
  > ![Custom page as main page](media/model-app-page-overview/page-inline-model-app.png "Custom page as main page")

Custom page as a center dialog.

  > [!div class="mx-imgBorder"]
  > ![Custom page as center dialog](media/model-app-page-overview/page-center-dialog-model-app.png "Custom page as center dialog")

Custom page as a side dialog.

  > [!div class="mx-imgBorder"]
  > ![Custom page as side dialog](media/model-app-page-overview/page-side-dialog-model-app.png "Custom page as side dialog")

Custom pages are added through a solution using either the modern app designer or the **Solutions** area in Power Apps. More information: [Add a custom page to your model-driven app](add-page-to-model-app.md) for details.

  > [!IMPORTANT]
  > - This is a preview feature, and isn't available in all regions.
  > - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

## Custom pages are different than embedded canvas apps

A custom page enables makers to create a new page experience using the canvas app capabilities.  This provides a low-code authoring experience with more flexible layouts, more control with styling options, ability to add connector data, use expressions, and so on. Custom page authoring happens in the canvas app designer with increasing context of the model-driven app that the page runs in. 

Embedded canvas apps also use the canvas capabilities with a hosting approach that not as integrated as a custom page. The simpler integration of an embedded canvas app means the current limitation on number of embedded canvas apps hasn't changed. The advanced integration of the custom page addresses those limits.  The embedded canvas app can only be placed with a model-driven form acting like a low code component. For more information, see [Embed a canvas app on a model-driven form](embed-canvas-app-in-form.md).

Think of a custom page in your model-driven app like a table form or a dashboard page. The page can consist of any set of controls that are supported on the page and can interact and navigate between other model-driven app page types and a canvas page. A custom page isn't a canvas app that has multiple screens or pages inside of it. It truly is a single page, not a series or set of canvas pages like an embedded canvas app.

In most cases, we recommend that you use custom pages instead of embedded canvas apps.

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

<!-- If these are already documented in the separate known issue topic we don't need to repeat them here. Otherwise, move them to the separate topic.
## Known limitations

Custom pages have a few known limitations.  Below are the most common and the full list is in [Custom Page Known Issues](model-app-page-issues.md).

* Supports the most common canvas controls and custom pro-dev components. For more information on what is available, see [Design a custom page for your model-driven app](design-page-for-model-app.md)

* Canvas component library or canvas component control support is coming soon

* Native player support (for example, iOS, Android) is coming soon for online-only. Offline support will be coming in 2022

* Custom pages require third-party cookie to be enabled which is required by the canvas runtime

Custom pages will not work on premise since it requires the online service for canvas apps. Custom pages also will notwork with IE 11 because it depends on capabilities not available in that browser. -->

### See also

[Add a custom page to your model-driven app](add-page-to-model-app.md)

[Design a custom page for your model-driven app](design-page-for-model-app.md)

[Navigating to and from a custom page in your model-driven app](navigate-page-examples.md)

[Using PowerFx in custom page](page-powerfx-in-model-app.md)

[Add connectors into custom pages](page-data-connector.md)

[Use Monitor to troubleshoot custom page](monitor-page-checker.md)

[Model-driven app custom page known issues](model-app-page-issues.md)