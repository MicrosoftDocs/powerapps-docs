---
title: Troubleshoot Power Query | Microsoft Docs
description: Resolve issues by using Power Query to create a custom table in Microsoft Dataverse.
author: mllopis
manager: kfile
ms.service: powerapps
ms.component: cds
ms.topic: conceptual
ms.date: 05/16/2018
ms.author: millopis
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Troubleshoot Power Query
[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

When you use Power Query for Excel to create a custom table that contains data from external sources, this error might appear:

>"Your Azure Active Directory administrator has set a policy that prevents you from using this feature. Please contact your administrator, who can grant permissions for this feature on your behalf."

The error appears if Power Query can't access the organization's data in Power Apps or Microsoft Dataverse. This situation arises under two sets of circumstances:

* An Azure Active Directory (Azure AD) tenant administrator has disallowed users' ability to consent to apps that access company data on their behalf.
* Using an unmanaged Active Directory tenant. An unmanaged tenant is a directory without a global administrator that was created to complete a self-service signup offer. To fix this scenario, users must first convert to a managed tenant and then follow one of the two solutions to this issue. The solutions are described in the next section.

To resolve this issue, the Azure Active Directory administrator must follow either of the procedures that are presented later in this article.

## Allow users to consent to apps that access company data
This approach is perhaps easier than the next, but it allows for broader permissions.

1. In the [Azure portal](https://portal.azure.com), open the **Azure Active Directory** pane, and then select **User settings**.
2. Next to **Users can consent to apps accessing company data on their behalf**, select **Yes**, and then select **Save**.

## Allow Power Query to access company data
As an alternative, the tenant administrator can give consent to Power Query without modifying tenant-wide permissions.

1. Install [Azure PowerShell](/powershell/azure/install-azurerm-ps).
2. Run the following PowerShell commands:
   * Login-AzureRmAccount (and sign in as the tenant admin)
   * New-AzureRmADServicePrincipal -ApplicationId f3b07414-6bf4-46e6-b63f-56941f3f4128

The advantage of this approach (versus the tenant-wide solution) is that this solution is very targeted. It provisions only the **Power Query** service principal, but no other permission changes are made to the tenant.

## Update personal data

Users can update mashups and other information (such as query names and mashup metadata) through the Query Editor and through the **Options** dialog box that's accessible from the Query Editor.

In Power Apps, you access the Query Editor by doing the following:
1. Go to the **Data** pane, expand it, and then select **Tables**. 
2. Select the ellipsis (...), and then select **Edit Queries**.
3. In the ribbon, select the **Options** button, and then select the **Export Diagnostics** button.


## Delete personal data

Most data is deleted automatically within 30 days. For data and metadata around mashups, users must remove all their mashups through Power Apps. All of the associated data and metadata will be deleted within 30 days.

To remove mashups from Power Apps:
1. Remove the Data Integrator projects, which can be removed from the namesake tab.
2. Select the ellipsis (...), and then select the **Delete** option.

If you created a mashup through the "New tables from data (Technical Preview)" feature, you can remove it by doing the following:
1. Select the ellipsis (...), and then select **Edit queries**.
2. In the ribbon, select the **Options** button.
3. Select the **Remove all queries** button.  
    After you confirm that you want to delete your queries, they are deleted.

## Export personal data

To export personal data, users can do the following:
1. Open the Query Editor.
2. In the ribbon, select the **Options** button.
3. Select the **Export Diagnostics** button.

In Power Apps, you can access the Query Editor by doing the following:
1. Go to the **Data** pane, expand it, and then select **Tables**.
2. Select the ellipsis (...), and then select **Edit Queries**. 
3. In the ribbon, select the **Options** button, and then select the **Export Diagnostics** button.

System-generated logs about user actions on the user interface (UI) can be accessed in the Azure portal.





[!INCLUDE[footer-include](../../includes/footer-banner.md)]