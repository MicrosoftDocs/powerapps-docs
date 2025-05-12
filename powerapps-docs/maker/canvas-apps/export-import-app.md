---
title: Overview of exporting and importing canvas apps
description: Overview of exporting and importing canvas apps.
author: caburk

ms.topic: concept-article
ms.date: 10/1/2024
ms.subservice: canvas-maker
ms.author: caburk
ms.reviewer: mkaur
search.audienceType: 
  - maker
contributors:
  - mduelae
  - caburk
---

# Overview of exporting and importing canvas apps

In this article, you'll learn about the different options available to export and import canvas apps in the form of singular app file, app package, and considerations from the application lifecycle management (ALM) perspective. To effectively manage ALM, it's recommended to use solutions. Canvas apps packages don’t support ALM and should only be used for basic import and export capabilities when Dataverse isn’t accessible.

You can export and import canvas apps using one of the following options:

- [Export and import canvas apps as app packages](export-import-app-package.md)
- [Export and import canvas apps as part of solutions](../data-platform/solutions-overview.md)
- [Export and import a canvas app as a single app file](export-import-single-app.md)


> [!IMPORTANT]
> - Canvas app packages can't be used with [Dataverse solution packages](../data-platform/solutions-overview.md) because of the package incompatibility.
> - Canvas apps that have Dataverse dependencies, such as flows, connection references, etc. are not supported for canvas app packages. For ALM capabilities in Microsoft Power Platform environments, use Microsoft Dataverse and solutions instead of the canvas app package export and import. More information: [ALM overview](/power-platform/alm/overview-alm)
> - An App Insights instrumentation key may be present in imported canvas apps. Inspect the instrumentation key after importing an app to ensure it corresponds to the desired App Insights resource.

## Export and import canvas apps as app packages

You can export and import canvas apps by using packages. This feature allows you to export an app from one environment and import it to another.

## Resources included in canvas apps packages

An app can consume different resources. For example, most apps use connections. Other apps might use Power Automate, have custom connectors, or connect by using gateways to on-premises resources. Some apps might also use Dataverse customizations

The following table explains different resource types, supportability, and import options.

| Resource type | Supported | Import options |
| --- | --- | --- |
| App |Yes, for canvas apps |There are two options to import an app into an environment: <ul><li><b>Create new</b>: The app is created as a new app in the environment where the package is imported.</li> <li><b>Update</b>: The app already exists in the environment and will be updated when this package is imported.</li></ul> |
| Power Automate |Yes |There are two options to import a flow into an environment: <ul><li><b>Create new</b>: The flow is created as a new flow in the environment where the package is imported.</li> <li><b>Update</b>: The flow already exists in the environment and will be updated when this package is imported.</li></ul><br> <b>Note: </b>All resources that the flow depends on will also be included in the app package that's exported and will need to be configured when the package is imported. <br> <br> You can also export and import flows by using solutions. More information: [Power Automate solutions](/power-automate/overview-solution-flows) |
| Custom connectors |No |Exporting a custom connector isn't supported. You need to re-create the custom connector on the target environment. |
| Connections |No |Exporting a connection isn't supported. You need to re-create connections on the target environment. |
| Dataverse customizations |No |Exporting Dataverse customizations as a part of a canvas app package isn't supported. You need to use Dataverse solutions instead. More information: [Dataverse solutions](../../developer/data-platform/introduction-solutions.md) |
| Gateways |No | You can't export or import gateways. You need to re-create gateways on the target environment. |

## Permissions

Only the **Owner** or **Co-owner** of an app can export a canvas app package. To import an app, the **Environment Maker** permission is required on the destination environment.

### See also

- [Save and publish an app](save-publish-app.md)
- [Edit an app](edit-app.md)
- [Delete an app](delete-app.md)
- [Share an app](share-app.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
