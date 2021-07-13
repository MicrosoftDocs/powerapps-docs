---
title: "Step 2: Create a managed solution for your app (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn about how to create a managed solution for your app to include all the components. This is required for publishing an app to Appsource." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 12/20/2019
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "KumarVivek" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "kvivek" # MSFT alias of Microsoft employees only
manager: "annbe" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Step 2: Create a managed solution for your app

Create a managed solution to include all the components for your app. You might find these topics helpful as you plan and create a managed solution to package your app components:
- [Introduction to solutions](introduction-solutions.md)
- [Plan for solution development](/dynamics365/customer-engagement/developer/plan-solution-development) 
- [Create, export, or import an unmanaged solution](/power-platform/alm/solution-api#create-export-or-import-an-unmanaged-solution)

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

## Display name and description of your solution

While creating a solution to package your app components, make sure you provide appropriate values in the **Display Name** and **Description** columns for your new solution that you want to be displayed to your customers.

![Create a solution.](media/appsource-new-solution.png)

The **Display Name** and **Description** values for a solution are displayed to the customers in the **Dynamics 365 Administration Center** portal.

![Solutions.](media/appsource-solution-names.png)

## Supporting data for your solution

If your solution requires supporting or demo data:
1. Create supporting/demo data in your test environment.
2. Use the [Configuration Migration tool](/dynamics365/customer-engagement/admin/manage-configuration-data) to create a schema to include your supporting/demo data. 
3. Save the schema file so that you can reuse it later to update the data in case your demo data changes.
4. Use the schema to export the data. Ensure that you provide a meaningful name to your export file. The data is exported and as a .zip file.

For detailed information about using the Configuration Migration tool to create a schema and export your data, see [Create a schema to export configuration data](/dynamics365/customer-engagement/admin/create-schema-export-configuration-data)

## At the end of this step

You will have a solution file (example: *SampleSolution.zip*) and optionally a demo data file (example: *SampleData.zip*) for your app.

**Optional licensing information:** If you wish to add licensing information to your solution, see [Appendix: Add licensing information to your solution](appendix-add-license-information-to-your-solution.md).

> [!div class="nextstepaction"]
> [Step 3: Create an AppSource package for your app](create-package-app-appsource.md) 
  


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
