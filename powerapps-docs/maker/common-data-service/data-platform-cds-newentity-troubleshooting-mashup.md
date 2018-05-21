---
title: Troubleshooting Power Query | Microsoft Docs
description: Resolve issues using Power Query to create a custom entity in Common Data Service (CDS) for Apps. 
author: mllopis
manager: kfile
ms.service: powerapps
ms.component: cds
ms.topic: conceptual
ms.date: 05/16/2018
ms.author: millopis
---

# Troubleshooting Power Query
When you use Power Query to create a custom entity that contains data from external sources, this error might appear:

`Your Azure Active Directory administrator has set a policy that prevents you from using this feature. Please contact your administrator, who can grant permissions for this feature on your behalf.`

The error appears if Power Query can't access the organization's data in PowerApps or Common Data Service (CDS) for Apps. This situation arises under two sets of circumstances:

* An Azure Active Directory (AAD) tenant administrator has disallowed users' ability to consent to apps that access company data on their behalf.
* Using an unmanaged Active Directory tenant. An unmanaged tenant is a directory without a global administrator that was created to complete a self-service signup offer. To fix this scenario, users must first convert to a managed tenant and then follow one of the two solutions to this issue, described in the following section.

To resolve this issue, the Azure Active Directory administrator must follow the steps in either of the procedures later in this topic.

## Allow users to consent to apps that access company data
This approach is perhaps easier than the next, but it allows for broader permissions.

1. In [https://portal.azure.com](https://portal.azure.com), open the **Azure Active Directory** blade, and then select **User settings**.
2. Select **Yes** next to **Users can consent to apps accessing company data on their behalf**, and then select **Save**.

## Allow Power Query to access company data
As an alternative, the tenant administrator can give consent to Power Query without modifying tenant-wide permissions.

1. Install [Azure PowerShell](https://docs.microsoft.com/powershell/azure/install-azurerm-ps).
2. Run the following PowerShell commands:
   * Login-AzureRmAccount (and sign in as the tenant admin)
   * New-AzureRmADServicePrincipal -ApplicationId f3b07414-6bf4-46e6-b63f-56941f3f4128

The advantage of this approach (versus the tenant-wide solution) is that this solution is very targeted. It provisions only the **Power Query** service principal, but no other permission changes are made to the tenant.

## Updating personal data

Users can update mashups and other information (such as query names and mashup metadata) through the Query Editor and through the `Options` dialog accessible from the Query Editor.

In PowerApps, the Query Editor can be accessed by going to the Data pane, expanding it, then clicking on the Entities pane menu item. Once there, click on the "..." menu and choose Edit Queries. Then click on the `Options` button in the ribbon and click on the `Export Diagnostics` button.


## Deleting personal data

Most data is deleted automatically within 30 days. For data and metadata around mashups, the user needs to remove all of their mashups through PowerApps. All of the associated data and metadata will be deleted within 30 days.

Mashups can be removed from Power Apps by removing the Data Integrator projects, which can be removed from the namesake tab, clicking on the "..." button, and choosing the `Delete` option.

If you created a mashup through the "New entities from data (Technical Preview)" feature, then you can remove it by clicking on the "..." button, choosing Edit queries, then choosing Options in the ribbon, and finally clicking on the "Remove all queries" button. Once you confirm that you want to delete your queries they will be deleted.


## Exporting personal data

Users can open the Query Editor, click on the `Options` button in the ribbon, and click on the `Export Diagnostics` button.

In PowerApps, the Query Editor can be accessed by going to the Data pane, expanding it, then clicking on the Entities pane menu item. Once there, click on the "..." menu and choose Edit Queries. Then click on the `Options` button in the ribbon and click on the `Export Diagnostics` button.

System generated logs regarding user actions in the user interface (UI) can be accessed in the Azure Portal.


