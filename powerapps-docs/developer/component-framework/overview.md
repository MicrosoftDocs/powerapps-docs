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

Power Apps component framework empowers professional developers and app makers to create code components for model-driven and canvas apps (experimental preview) to provide enhanced user experience for the users to work with data on forms, views, and dashboards. For example:

- Replace a field that displays a numeric text value with a `dial` or `slider` code component.
- Transform a list into an entirely different visual experience bound to the data set like a `Calendar` or `Map`.

> [!IMPORTANT]
> - Power Apps component framework is in experimental preview for canvas apps, and in GA for model-driven apps. This implies that all the APIs that are supported for model-driven apps might not be supported on canvas apps yet.
> - By default Power Apps component framework is enabled for model-driven apps. To enable this feature for canvas apps, see [Code components for canvas apps](component-framework-for-canvas-apps.md).
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)]
> - Canvas apps only support the *field* type of code components, and not the *dataset* type.
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

## Related topics

[What are code components](custom-controls-overview.md)<br/>
[Code components for canvas apps](component-framework-for-canvas-apps.md)<br/>
[Create and build a code component](create-custom-controls-using-pcf.md)<br/>
[Power Apps for developers](https://docs.microsoft.com/powerapps/#pivot=home&panel=developer)

