---
title: "Add code components to a custom page for your model-driven app" 
description: "This article outlines the use of code components built by professional developers using the Power Apps component framework within a custom page."
ms.custom: ""
ms.date: 07/14/2021
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "hemantg"
ms.author: "matp"
manager: "kvivek"
search.audienceType: 
  - maker
search.app: 
  - "PowerApps"
  - D365CE
---

# Add code components to a custom page for your model-driven app (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This article outlines the use of code components built by professional developers using [Power Apps component framework](../../developer/component-framework/overview.md) within a custom page. For low-code custom UX extensibility, see [add canvas components to a custom page for your model-driven app.](/powerapps/maker/model-driven-apps/page-canvas-components) 

  > [!IMPORTANT]
  > - This is a preview feature, and may not be available in all regions.
  > - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]

  > [!NOTE]
  > - Custom pages support all the component framework APIs that are currently supported for canvas apps. 
  > - Certain model-driven app specific APIs like [WebAPI](../../developer/component-framework/reference/webapi.md) and [Navigation](../../developer/component-framework/reference/navigation.md) have published app support for custom pages. These APIs can be used in the code component for custom pages and works on the final published app. 
  > - For individual API support status on each platform, see [Power Apps component framework API reference](/powerapps/developer/component-framework/reference/)

Code components provide professional developers the ability to create custom code components for use within an app. This pro-code extensibility mechanism provides first-class application lifecycle management (ALM) to seamlessly extend the components available to all the app makers across the organization. Code components can be reused across custom pages, canvas, and model-driven apps. They can be centrally updated, packaged, and moved using standard Microsoft Dataverse solutions. More information: [Power Apps component framework overview](/powerapps/developer/component-framework/overview) 

## Enabling Power Apps component framework for custom pages

To use code components inside a custom page, you need to enable Power Apps component framework feature. More information: [Enable the Power Apps component framework feature](/powerapps/developer/component-framework/component-framework-for-canvas-apps#enable-the-power-apps-component-framework-feature) 

:::image type="content" source="../../developer/component-framework/media/enable-pcf-feature.png" alt-text="Enable Power Apps component framework." lightbox="../../developer/component-framework/media/enable-pcf-feature.png":::

## Create code components for use in a custom page

This section outlines how to create, import, and test code components.

### Creating and importing code components in Dataverse

Code components for custom pages follow the same pattern as they do with canvas app. Code components need to be implemented first before they can be added to a custom page. To create a code component, see [Create your first component](/powerapps/developer/component-framework/implementing-controls-using-typescript).

You can also try [OOB sample components](/powerapps/developer/component-framework/use-sample-components#try-the-sample-components) to jump start. Once you are done implementing your code component, it can be packaged into a solution and added to Dataverse, making it available for use in all the custom pages in line with model-driven and canvas apps. More information: [Code components application lifecycle management (ALM)](/powerapps/developer/component-framework/code-components-alm).

### Importing and using code component in a custom page

In an environment, custom pages can use all the code components previously imported into Dataverse using solutions. On the left pane, select **Add (+)**, and then select **Get more components** at the bottom of the page. You will see a code tab on the **Import components** pane showing all code components present in the environment.

:::image type="content" source="media/add-component-to-model-app/get-code-components-for-custom-page.png" alt-text="Get code components for a custom page." lightbox="media/add-component-to-model-app/get-code-components-for-custom-page.png":::

  > [!NOTE]
  > - If the code tab doesn't show up in the **Import component** pane, verify that the Power Apps component framework feature setting for canvas apps is enabled. More information: [Enable Power Apps component framework feature](../../developer/component-framework/component-framework-for-canvas-apps.md) 
  > - Also, ensure that you are working on the latest canvas app studio authoring version. 

The newly added code components are now available under the **Code components** section. It can be added to a custom page.

:::image type="content" source="media/add-component-to-model-app/add-web-api-component-to-custompage.png" alt-text="Add Web API code components for a custom page." lightbox="media/add-component-to-model-app/add-web-api-component-to-custompage.png":::

### Testing the code component inside the studio and published app

Like canvas apps, code components are interactive and can be tested in the custom page studio authoring environment. However, specific APIs like `Web APIs` and `Navigation`, which only have the custom page runtime support when invoked, will show the error message "Method not implemented".

:::image type="content" source="media/add-component-to-model-app/create-record-not-implmented-custom-page-studio.png" alt-text="Create record Web API not implemented." lightbox="media/add-component-to-model-app/create-record-not-implmented-custom-page-studio.png":::

You can dismiss this error and publish the custom page. Then, add this custom page to the model-driven app and publish the app to see the custom page web API in action.

The image below shows the standard [Web API sample control](/powerapps/developer/component-framework/sample-controls/webapi-control) and [Navigation API control](/powerapps/developer/component-framework/sample-controls/navigation-api-control) added to custom page working inside a published model-driven app.

### Additional code component resources

You can also use other [sample components](/powerapps/developer/component-framework/use-sample-components#try-the-sample-components) from Microsoft.

![Add standard sample controls to a custom page.](media/add-component-to-model-app/add-sample-code-components-to-custom-page.png "Add standard sample controls to a custom page.")

Or try some from the [Power Apps community gallery](/powerapps/developer/component-framework/community-resources).

 ![Component gallery.](../../developer/component-framework/media/pcf-gallery.PNG "Components gallery")

### See also

[Model-driven app custom page overview](model-app-page-overview.md)

[Add a custom page to your model-driven app](add-page-to-model-app.md)

[Using PowerFx in custom page](page-powerfx-in-model-app.md)

[Overview of Power Apps connectors](../canvas-apps/connections-list.md)

[Add data connection in canvas designer](../canvas-apps/add-data-connection.md)
