---
title: "Power Apps component framework overview | Microsoft Docs"
description: "Use the Power Apps component framework to create code components to provide enhanced experiences for people to view and work with data in forms, views, and dashboards."
keywords: "Component Framework, code components, Power Apps controls"
author: nkrb 
manager: kvivek
ms.date: 09/05/2019
ms.service: "powerapps"
ms.custom:
  - "dyn365-a11y"
  - "dyn365-developer"
ms.topic: article
ms.assetid: 7923e36d-3640-49f7-9f2f-c97358a632db
ms.author: nabuthuk
---

# Power Apps component framework overview

Power Apps component framework empowers professional developers and app makers to create code components for model-driven and canvas apps (public preview) to provide enhanced user experience for the users to work with data on forms, views, and dashboards. For example:

- Replace a field that displays a numeric text value with a `dial` or `slider` code component.
- Transform a list into an entirely different visual experience bound to the data set like a `Calendar` or `Map`.

> [!IMPORTANT]
> - PowerApps component framework is in public preview for canvas apps, and is generally available for model-driven apps. This implies that all the APIs that are supported for model-driven apps might not be supported on canvas apps yet.
> - By default Power Apps component framework is enabled for model-driven apps. To enable this feature for canvas apps, see [Code components for canvas apps](component-framework-for-canvas-apps.md).
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]
> - Power Apps component framework works only on Unified Interface and not on the web client. 
> - Power Apps component framework doesn't work for on-premises instances. 

## How is it different from web resources

Unlike HTML web resources, code components are rendered as a part of the same context, load at the same time as any other components, providing a seamless experience for the users. 

Developers can bundle all the HTML, CSS, and TypeScript files into a single [solution](https://docs.microsoft.com/dynamics365/customer-engagement/customize/solutions-overview) package file and move across environments and also shipped via [AppSource](https://appsource.microsoft.com/marketplace/apps?page=1&product=dynamics-365). 

Code components can be reused many times across different entities and forms. Use Power Apps component framework to create code components that can be used across the full breadth of Power Apps capabilities.

## Advantages 

- Access to a rich set of framework APIs that expose capabilities like component lifecycle management, contextual data, and metadata. 
- Seamless server access via Web API, utility and data formatting methods, device features like camera, location and microphone, along with easy-to-invoke UX elements like dialogs, lookups, and full-page rendering.  
- Support for modern web practices.
- Optimizes for performance.
- Reusability
- Bundle all files into a single solution file.

## Licensing

Power Apps component framework licensing requirements are inline with existing connectors and components and is based on the type of data and connections used in your app. More information: [Power Apps pricing](https://powerapps.microsoft.com/en-us/pricing/). To align with the licensing requirements, we will be classifying code components into two types:

- Code components that connect to external services or data directly and not through connectors. When these components are used in an app, the app becomes premium, and end users are required to have **Power Apps** licenses.
- Code components that don't connect to external services or data. When these components are used in an app that uses standard features, the app remains standard, and end users are required to have minimum **Power Apps for Office 365** licenses.

> [!NOTE]
> If you are currently using code components in model-driven apps connected to Common Data Service, end users will require **Power Apps** licenses.

With the general availability of the framework, code component developers will be able to classify components as part of the component manifest to allow makers to see which components are premium.

## Related topics

[What are code components](custom-controls-overview.md)<br/>
[Code components for canvas apps](component-framework-for-canvas-apps.md)<br/>
[Create and build a code component](create-custom-controls-using-pcf.md)<br/>
[Power Apps for developers](https://docs.microsoft.com/powerapps/#pivot=home&panel=developer)

