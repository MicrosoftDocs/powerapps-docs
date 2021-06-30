---
title: "Power Apps component framework overview in Microsoft Dataverse| Microsoft Docs"
description: "Use the Power Apps component framework to create code components to provide an enhanced experiences for people to view and work with data in forms, views, and dashboards."
keywords: "Component Framework, code components, Power Apps controls"
author: nkrb 
manager: kvivek
ms.date: 06/08/2021
ms.service: "powerapps"
ms.custom:
  - "dyn365-a11y"
  - "dyn365-developer"
  - "intro-internal"
ms.topic: article
ms.assetid: 7923e36d-3640-49f7-9f2f-c97358a632db
ms.author: nabuthuk
---

# Power Apps component framework overview

Power Apps component framework empowers professional developers and app makers to create code components for model-driven and canvas apps.   These code components can be used to enhance the user experience for users working with data on forms, views, dashboards, and canvas app screens.  For example:

- Replace a column on a form that displays a numeric text value with a `dial` or `slider` code component.
- Transform a list into an entirely different visual experience bound to the dataset like a `Calendar` or `Map`.

> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RE4slRe]


> [!IMPORTANT]
> - Power Apps component framework works only on Unified Interface and not on the legacy web client. 
> - Power Apps component framework is currently not supported for on-premises environments. 

## How is it different from web resources

Unlike HTML web resources, code components are rendered as a part of the same context, load at the same time as any other components, providing a seamless experience for the users. 

Developers can bundle all the HTML, CSS, and TypeScript files into a single [solution](../../maker/data-platform/solutions-overview.md) package file and move across environments and also shipped via [AppSource](https://appsource.microsoft.com/marketplace/apps?page=1&product=dynamics-365). 

Code components can be reused many times across different tables and forms. Use Power Apps component framework to create code components that can be used across the full breadth of Power Apps capabilities.

## Advantages 

- Access to a rich set of framework APIs that expose capabilities like component lifecycle management, contextual data, and metadata. 
- Seamless server access via Web API, utility and data formatting methods, device features like camera, location, and microphone, along with easy-to-invoke UX elements like dialogs, lookups, and full-page rendering.  
- Support for modern web practices.
- Optimizes for performance.
- Reusability
- Bundle all files into a single solution file.

## Licensing

Power Apps component framework licensing requirements are inline with existing connectors and components and is based on the type of data and connections used in your app. More information: [Power Apps pricing](https://powerapps.microsoft.com/pricing/). To align with the licensing requirements, we will be classifying code components into two types:

- Code components that connect to external services or data directly via the user's browser client and not through connectors are considered as premium. When these components are used in an app, the app becomes premium, and end-users are required to have **Power Apps** licenses.
- Code components that don't connect to external services or data. When these components are used in an app that uses standard features, the app remains standard, and end- users are required to be licensed at minimum for **Office 365**. More information: [Power Apps pricing](https://powerapps.microsoft.com/pricing/)
- Code components can be declared as premium components by adding a `<external-service-usage>` node to the component's manifest file with all the external service domains this component is connecting to.
   ```xml
    <external-service-usage enabled="true">
     <domain>www.microsoft.com</domain>
    </external-service-usage>
    ```

> [!NOTE]
> If you are currently using code components in model-driven apps connected to Microsoft Dataverse, end-users will require **Power Apps** licenses.

## Related topics

[What are code components](custom-controls-overview.md)<br/>
[Code components for canvas apps](component-framework-for-canvas-apps.md)<br/>
[Create and build a code component](create-custom-controls-using-pcf.md)<br/>
[Learn Power Apps component framework](/learn/paths/use-power-apps-component-framework)<br/>
[Use code components in Power Apps portals](../../maker/portals/component-framework.md)



[!INCLUDE[footer-include](../../includes/footer-banner.md)]
