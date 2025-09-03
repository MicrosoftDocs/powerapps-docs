---
title: "Power Apps code apps overview"
description: "Use Power Apps code apps"
ms.author: alaug
author: alaug
ms.date: 09/10/2025
ms.reviewer: jdaly
ms.topic: overview
ms.subservice: code-apps  #requested new value
contributors:
 - JimDaly
---
# Power Apps code apps overview

[!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

Power Apps empowers developers of all skillsets—including those building web apps in IDEs like Visual Studio Code—to efficiently build and run business apps on a managed platform.

**Code apps** let developers bring Power Apps capabilities into custom web apps built in a code‑first IDE. You can develop locally and run the same app in Power Platform. Build with popular frameworks (React, Angular, Vue, etc.) while keeping full control over your UI and logic.

**Key features include:**

- Out-of-the-box Microsoft Entra authentication and authorization
- Access to Power Platform data sources and 1,500+ connectors, callable directly from JavaScript
- Easy publishing and hosting of line-of-business web apps in Power Platform
- Adherence to your organization's Managed Platform policies (app sharing limits, Conditional Access, Data Loss Prevention, etc.)
- Simplified deployment and ALM

The managed platform accelerates safe, rapid innovation, and when ready, apps can be deployed to dedicated production environments.

## Prerequisites

Code apps require several developer tools like Visual Studio Code, git, dotnet, node.js, and npm to be available on the command line.  

### Install the following developer tools

- [Visual Studio Code](https://code.visualstudio.com/)
- [Node.js](https://nodejs.org/) (LTS version)
- [Git](https://git-scm.com/)
- [Power Apps CLI](/power-platform/developer/cli/introduction)

### Enable code apps on a Power Platform environment

Code apps can be enabled via environment setting which can be set by Power Platform Admins and environment admins. The environment setting respects groups and rules set by Power Platform Admins.

1. As an admin, go to https://admin.powerplatform.microsoft.com
1. Navigate to **Manage** > **Environments** > select the environment where you will use code apps
1. Navigate to **Settings** >  Expand the **Product** subsection > Select **Features**

   :::image type="content" source="media/enable-settings-products-features.png" alt-text="Enable features":::

1. Navigate to the feature **Power Apps Code Apps** and use the **Enable code apps** toggle for enablement.

   :::image type="content" source="media/enable-code-apps.png" alt-text="Enable code apps":::

1. Click **Save** in the settings experience.

> [!NOTE]
> If the Power Apps Code Apps setting doesn't appear in the admin center UI it is because a UI update hasn't reached your environment yet. You can get the setting to appear by appending `?ecs.ShowCodeAppSetting=true` to the admin center URI.
> For example, if this is the URL to the admin settings:
> `https://admin.powerplatform.microsoft.com/manage/environments/1c137ea4-049e-ef11-8a66-000d3a106833/settings/Features`
> Append the query string to the end.
> `https://admin.powerplatform.microsoft.com/manage/environments/1c137ea4-049e-ef11-8a66-000d3a106833/settings/Features?ecs.ShowCodeAppSetting=true`

### License end-users with Power Apps Premium

End-users that run code apps need a [Power Apps Premium license](https://www.microsoft.com/power-platform/products/power-apps/pricing).

## Limitations

1. Code apps can invoke APIs outside of Power Platform connectors. Code apps do not yet support [Content Security Policy](/power-platform/admin/content-security-policy) (CSP).
1. Code apps do not yet support [Storage Shared Access Signature (SAS) IP restriction](/power-platform/admin/security/data-storage#advanced-security-features ).
1. Code apps don't support Power Platform Native source code integration.
1. Code apps don't support Dataverse solutions and therefore cannot use Power Platform pipelines for deployments.
1. Code apps don't have a Power Platform native integration with Azure Application Insights. Azure Application Insights can be added as it would be to a generic web app but it will not include information recognized in the platform layer, such as app open events (to measure success/failure)

## Managed Platform capability support

This table enumerates Power Platform management capabilities that work for code apps.

|Capability|Notes|
|---|---|
| End-users see consent dialog for connector permissions | [Learn more](/power-apps/maker/canvas-apps/add-manage-connections#consent-dialog-fine-grained-permssions)|
| Sharing limits | Code apps respect canvas app sharing limits. [Learn more](/power-platform/admin/managed-environment-sharing-limits)  |
| App Quarantine | [Learn more](/power-platform/admin/admin-manage-apps?tabs=new#manage-app-quarantine-state) |
| Data Loss policy enforcement during app launch | [Learn more](/power-platform/admin/wp-data-loss-prevention) |
| Conditional Access on an individual app | [Learn more](/power-platform/admin/admin-manage-apps?tabs=new#managed-environments-conditional-access-on-individual-apps) |
| Admin consent dialog suppression | Consent suppression is supported for both Microsoft connecters that use OAuth as well as custom connectors that use OAuth. [Learn more](/power-apps/maker/canvas-apps/add-manage-connections#suppress-consent-dialog-for-apps-that-use-custom-connectors-using-microsoft-entra-id-oauth)  |
| Tenant isolation | [Learn more](/power-platform/admin/cross-tenant-restrictions) |
| Azure B2B (external user access) | Code apps may be shared with and access by end-users using Azure B2B to access resources in a tenant, similar to canvas apps. [Learn more](/power-apps/maker/canvas-apps/share-app-guests) |
