---
title: Troubleshooting - Unable to create or retrieve a mashup for this database | Microsoft Docs
description: Resolve issues creating a Custom Entity using CDS and Power Query, by administrator changes to AAD restrictions.
services: ''
suite: powerapps
documentationcenter: na
author: mllopis
manager: kfend
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
# Troubleshooting - Unable to create or retrieve a mashup for this database
When using the **New Entities from Data (Technical Preview)** feature, you might run into an error that looks like the following:

    *Unable to create or retrieve a mashup for the current database*

This can occur when you're using the feature to create *Custom Entities* in the **Common Data Service (CDS)** based on data from external data sources using **Power Query**. The error is triggered when **Power Query** cannot access the organization's data in **PowerApps or CDS**. There are two scenarios when this can happen:

* An **Azure Active Directory** (AAD) tenant administrator has disallowed users' ability to consent to apps accessing company data on their behalf.
* Using an unmanaged Active Directory tenant. An unmanaged tenant is a directory without a global administrator that was created to complete a self-service signup offer. To fix this scenario, users must *first* convert to a managed tenant, then follow one of the two solutions to this issue, described in the following section.

There are two ways to fix the issue described above:

* Have the AAD administrator follow the steps necessary for users to consent to apps accessing company data
* Have the AAD administrator allow **Power Query** to access data

Each of the steps necessary for these solutions are described next.

## Allowing users to give apps consent to access company data

You can contact the AAD tenant administrator, and have him or her perform the following steps, which enables users to consent to any app accessing company data:

1. Visit [https://portal.azure.com](https://portal.azure.com)
2. Open the **Azure Active Directory** blade.
3. Select **User settings**.
4. Select **Yes** next to **Users can consent to apps accessing company data on their behalf**, and then select **Save**.
5. Once that process is completed, the issue will be resolved.

This is perhaps the easiest approach, but it allows for broader permissions than the next option.

## Allowing Power Query to access company data
Another solution is to have the tenant administrator give consent to **Power Query** without modifying tenant-wide permissions. Have the tenant administrator take the following steps achieve this:

1. Install [Azure PowerShell](https://docs.microsoft.com/powershell/azure/install-azurerm-ps)
2. Run the following PowerShell commands:
   * Login-AzureRmAccount (and sign in as the tenant admin)
   * New-AzureRmADServicePrincipal -ApplicationId f3b07414-6bf4-46e6-b63f-56941f3f4128

The advantage of this approach (versus the tenant-wide solution) is that this solution is very targeted. It provisions only the **Power Query** service principal, but no other permission changes are made to the tenant.

