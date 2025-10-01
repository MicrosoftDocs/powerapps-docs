---
title: "Power Apps code apps overview (preview)"
description: "Use Power Apps code apps"
ms.author: alaug
author: alaug
ms.date: 09/10/2025
ms.reviewer: jdaly
ms.topic: overview
contributors:
 - JimDaly
---
# Power Apps code apps overview (preview)

> [!NOTE]
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

Power Apps empowers developers of all skill sets, including those building web apps in integrated developer environments (IDEs) like Visual Studio Code, to efficiently build and run business apps on a managed platform.

**Code apps** let developers bring Power Apps capabilities into custom web apps built in a code‑first IDE. You can develop locally and run the same app in Power Platform. Build with popular frameworks (React, Vue, and others) while keeping full control over your UI and logic.

**Key features include:**

- Microsoft Entra authentication and authorization
- Access to Power Platform data sources and 1,500+ connectors, callable directly from JavaScript
- Easy publishing and hosting of line-of-business web apps in Power Platform
- Adherence to your organization's Managed Platform policies (app sharing limits, Conditional Access, Data Loss Prevention, and so on)
- Simplified deployment and ALM

The managed platform accelerates safe, rapid innovation, and when ready, apps can be deployed to dedicated production environments.

## Prerequisites

Code apps require several developer tools like Visual Studio Code, git, dotnet, node.js, and npm to be available on the command line.  

### Install the following developer tools

Use these tools while creating code apps:

- [Visual Studio Code](https://code.visualstudio.com/)
- [Node.js](https://nodejs.org/) (LTS version)
- [Git](https://git-scm.com/)
- [Power Apps CLI](/power-platform/developer/cli/introduction)

### Enable code apps on a Power Platform environment

Code apps can be enabled via an environment setting that Power Platform Admins and environment admins can set. The environment setting respects groups and rules set by Power Platform Admins.

1. As an admin, go to [Power Platform admin center](https://admin.powerplatform.microsoft.com)
1. Navigate to **Manage** > **Environments** > select the environment where you'll use code apps
1. Navigate to **Settings** >  Expand the **Product** subsection > Select **Features**

   :::image type="content" source="media/enable-settings-products-features.png" alt-text="Enable features":::

1. Navigate to the feature **Power Apps code apps** and use the **Enable code apps** toggle for enablement.

   :::image type="content" source="media/enable-code-apps.png" alt-text="Enable code apps":::

1. Select **Save** in the settings experience.

### License end-users with Power Apps Premium

End-users that run code apps need a [Power Apps Premium license](https://www.microsoft.com/power-platform/products/power-apps/pricing).

## Limitations

- Code apps can invoke APIs outside of Power Platform connectors. Code apps don't yet support [Content Security Policy](/power-platform/admin/content-security-policy) (CSP).
- Code apps don't yet support [Storage Shared Access Signature (SAS) IP restriction](/power-platform/admin/security/data-storage#advanced-security-features ).
- Code apps don't support [Power Platform Git integration](/power-platform/alm/git-integration/overview).
- Code apps don't support Dataverse solutions and therefore can't use Power Platform pipelines for deployments.
- Code apps don't have a Power Platform native integration with Azure Application Insights. Azure Application Insights can be added as it would be to a generic web app but it doesn't include information recognized in the platform layer, such as app open events (to measure success/failure).

## Managed Platform capability support

This table enumerates Power Platform management capabilities that work for code apps.

|Capability|Notes|
|---|---|
| End-users see consent dialog for connector permissions | [Learn more](/power-apps/maker/canvas-apps/add-manage-connections#consent-dialog-fine-grained-permssions)|
| Sharing limits | Code apps respect canvas app sharing limits. [Learn more](/power-platform/admin/managed-environment-sharing-limits)  |
| App Quarantine | [Learn more](/power-platform/admin/admin-manage-apps?tabs=new#manage-app-quarantine-state) |
| Data Loss policy enforcement during app launch | [Learn more](/power-platform/admin/wp-data-loss-prevention) |
| Conditional Access on an individual app | [Learn more](/power-platform/admin/admin-manage-apps?tabs=new#managed-environments-conditional-access-on-individual-apps) |
| Admin consent dialog suppression | Consent suppression is supported for both Microsoft connecters that use OAuth and custom connectors that use OAuth. [Learn more](/power-apps/maker/canvas-apps/add-manage-connections#suppress-consent-dialog-for-apps-that-use-custom-connectors-using-microsoft-entra-id-oauth)  |
| Tenant isolation | [Learn more](/power-platform/admin/cross-tenant-restrictions) |
| Azure B2B (external user access) | Code apps might be shared with and accessed by end-users using Azure B2B to access resources in a tenant, similar to canvas apps. [Learn more](/power-apps/maker/canvas-apps/share-app-guests) |
| Health metrics | Operational health metrics for code apps are available in both the Power Platform admin center and the maker portal. [Learn more](https://learn.microsoft.com/en-us/power-platform/admin/monitoring/monitor-power-apps?branch=main) |

## Related information

- [Code apps architecture (preview)](architecture.md)  
- [System limits and configuration](system-limits-configuration.md)
