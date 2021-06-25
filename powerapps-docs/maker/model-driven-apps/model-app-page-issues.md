---
title: "Known issues with custom pages in a model-driven app (preview)"
description: "" 
ms.custom: ""
ms.date: 04/03/2020
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "adrianorth"
ms.assetid: b4098c96-bce1-4f57-804f-8694e6254e81
ms.author: "aorth"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---
# Known issues with custom pages in a model-driven app (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

The custom page is a new page type within model-driven app, which brings in the power of canvas.  Below are the known issues to be aware of.

* When a custom page is modified (for example saved and published), the model-driven app is not aware of the change and will continue to use the last version of the custom page when the model-driven app was published.  A model-driven app publish through app designer or solution explorer will update all custom pages in the model-driven app. This also applies to **Publish all**.

* When navigating back to a custom page from another page, the page state is not restored so the page is like a new navigation.  We are looking at enabling page state to be saved before navigating away and restored on reload.

* Deleting a model-driven app with a custom page from the make.powerapps.com Apps list fails with an error.  The work-around is to delete from the solution explorer list.

* Layout or control support for Right to Left (RTL) is coming before GA

* Ability to get the current users settings including Locale, Language is coming before GA

* Custom pages use a canvas hosting session that can time out after 8 hours where the Unified Interface session has a longer timeout.  When this timeout happens an error message bar will appear to prompt the user to refresh the browser

  > [!div class="mx-imgBorder"]
  > ![Custom page session timeout app message bar error](media/model-app-page-overview/page-session-timeout-app-message-error.png "Custom page session timeout app message bar error")

* Deleting a custom page that is referenced by a model-driven app will be blocked until the reference is removed from the model-driven app Pages and the sitemap. See more on [Managing dependencies](/power-platform/alm/removing-dependencies)

* Under some cases, loading a custom page when there is a change can take longer and no page loading spinner is shown.

* When a custom page with code component is opened for editing, a security dialog is shown.  On this dialog, clicking on **Go back** button does not navigate back to parent context.  User can close the browser tab to leave the canvas designer.  

* When a user is prompted for consent with connectors and clicks "Don't allow", the custom page will render but without data.  The user does not get notified that data retrieval is skipped.

## Related topics

[Model-driven app custom page overview](model-app-page-overview.md)