---
title: Troubleshooting Power Query | Microsoft Docs
description: Resolve issues using Power Query to create a custom entity in the Common Data Service for Apps 
services: ''
suite: powerapps
documentationcenter: na
author: mllopis
manager: kfile
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 08/18/2017
ms.author: millopis

---
# Troubleshooting Power Query
When you use Power Query to create a custom entity that contains data from external sources, this error might appear:

`Your Azure Active Directory administrator has set a policy that prevents you from using this feature. Please contact your administrator, who can grant permissions for this feature on your behalf`.

The error appears if Power Query can't access the organization's data in PowerApps or the Common Data Service. This situation arises under two sets of circumstances:

* An Azure Active Directory (AAD) tenant administrator has disallowed users' ability to consent to apps accessing company data on their behalf.
* Using an unmanaged Active Directory tenant. An unmanaged tenant is a directory without a global administrator that was created to complete a self-service signup offer. To fix this scenario, users must first convert to a managed tenant and then follow one of the two solutions to this issue, described in the following section.

To resolve this issue, the AAD administrator must follow the steps in either of the procedures later in this topic.

## Allow users to consent to apps that access company data
This approach is perhaps easier than the next, but it allows for broader permissions.

1. In [https://portal.azure.com](https://portal.azure.com), open the **Azure Active Directory** blade, and then select **User settings**.
1. Select **Yes** next to **Users can consent to apps accessing company data on their behalf**, and then select **Save**.

## Allow Power Query to access company data
As an alternative, the tenant administrator can give consent to Power Query without modifying tenant-wide permissions.

1. Install [Azure PowerShell](https://docs.microsoft.com/powershell/azure/install-azurerm-ps).
2. Run the following PowerShell commands:
   * Login-AzureRmAccount (and sign in as the tenant admin)
   * New-AzureRmADServicePrincipal -ApplicationId f3b07414-6bf4-46e6-b63f-56941f3f4128

The advantage of this approach (versus the tenant-wide solution) is that this solution is very targeted. It provisions only the **Power Query** service principal, but no other permission changes are made to the tenant.

