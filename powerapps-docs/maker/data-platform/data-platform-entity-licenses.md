---
title: License requirements for tables| Microsoft Docs
description: An explanation of license requirements for tables with complex business logic and restricted tables in Microsoft Dataverse.
author: MicroSri
ms.service: powerapps
ms.topic: conceptual
ms.date: 08/28/2020
ms.subservice: dataverse-maker
ms.author: sriknair
ms.reviewer: kvivek
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# License requirements for tables

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

App makers can use most of the tables available within Microsoft Dataverse (including custom tables and tables that are part of the Common Data Model) to create apps and flows for users who have a Power Apps or Power Automate license. 

In some cases, tables contain complex business logic or are tied to customer engagement apps in Dynamics 365 (Dynamics 365 Sales, Customer Service, Field Service, Marketing, or Project Service Automation) that require app users to have a specific license. This topic provides licensing information for tables with complex business logic and tables that are tied to Dynamics 365 apps (termed as restricted tables).

## Tables with complex business logic
Tables that include the following complex server-side logic require users of an app or flow that uses these tables to have a [Power Apps](https://powerapps.microsoft.com/pricing/) or [Power Automate](https://flow.microsoft.com/pricing/) license:

- Code plug-ins (for more information, see [Plug-in development](../../developer/data-platform/plug-ins.md))
- Real-time workflows (for more information, see [Workflow processes](/flow/workflow-processes))

    > [!NOTE]
    >  Only workflows that are converted to a real-time workflow are considered real-time and synchronous. Workflows that are run in the background can still be used with the appropriate Power Apps plan and do not require additional licenses.

To know whether or not you added complex business logic to your tables, review the list of plug-in assemblies and workflows configured in your environment. For the list of tables which may contain server side logic after installing a Dynamics 365 app (such as Dynamics 365 Sales or Dynamics 365 Customer Service), see [Complex tables requiring Power Apps or Power Automate licenses](data-platform-complex-entities.md)  

### Impacting license requirements when adding complex business logic

App makers can add code plug-ins and real-time workflows to tables within Dataverse, but doing so could change the license requirements for users of apps already deployed. App makers should be cautious when adding complex business logic to a table and should first check which apps use the table and whether users of those apps have the appropriate licenses.

## Restricted tables

Restricted tables are not standard tables within Dataverse, but are included in one of the customer engagement apps in Dynamics 365 (Dynamics 365 Sales, Customer Service, Field Service, Marketing, or Project Service Automation) or a third-party solution. For example, the knowledge article, goal, and entitlement tables.

> [!NOTE]
> Apps and flows that use these tables require the app and flow user to be licensed appropriately-not the maker or developer of the app or flow.

tables that are tied to the functionality of Dynamics 365 apps (such as Dynamics 365 Sales or Dynamics 365 Customer Service) require app users to have the corresponding license for that application if they want to create, update, or delete rows within the tables. For a full list of restricted tables, see [Restricted tables requiring Dynamics 365 licenses](data-platform-restricted-entities.md).

## Licensing examples
Barb and Isaac are creating apps in Power Apps using Dataverse to store their data.

### Table creation

-	No user can create a new restricted table; Microsoft reserves the right to create and define them for Dynamics 365 apps (such as Dynamics 365 Sales or Dynamics 365 Customer Service)

-	Users can create custom tables with Dynamics 365, Power Apps, or Power Automate license

-	For existing restricted tables, a user can add rows with the appropriate Dynamics 365 app license

### Create apps using Power Apps

-	Barb and Isaac can create a canvas or model-driven app accessing restricted tables with a Dynamics 365 license

-	Barb and Isaac can create a canvas or model driven app accessing custom tables with either Dynamics 365 or Power Apps license

### Use apps

Barb wants to use two canvas apps:
-	App 1 &ndash; uses the Appointment table along with a custom table that stores related information

-	App 2 &ndash; uses the Appointment table along with the Work Order table, which is a restricted table

Isaac wants to use two model-driven apps:
-	App 3 &ndash; uses the Appointment table along with a custom table that stores related information

-	App 4 &ndash; uses the Appointment table along with the Work Order table, which is a restricted table

Barb and Isaac need the following licenses:
- Barb can use App 1 with a Dynamics 365 app license or a Power Apps license.

-	Barb can use App 2 only with a Dynamics 365 app license because there is a restricted table accessed by the app.

-	Isaac can use App 3 with a Dynamics 365 app license or a Power Apps license. 

-	Isaac can use App 4 only with a Dynamics 365 app license because there is a restricted table accessed by the app.

### Create flows using Power Automate

Now, let's see what happens when Isaac adds a real-time workflow to the custom table that both Barb and Isaac are using in their apps.
-	Isaac can create a workflow accessing restricted tables with a Dynamics 365 app license

-	Barb and Isaac can create a workflow accessing custom tables with either Dynamics 365 app or Power Automate license 

### Use flows
-	Barb or Isaac can run the workflow accessing restricted tables with a Dynamics 365 app license

-	Barb or Isaac can run the workflow accessing custom tables with either Dynamics 365 app or Power Automate license


## More about licensing

For more information about licensing, see [Licensing overview](/power-platform/admin/pricing-billing-skus).

For the latest information on licensing requirements for tables, see the [Power Apps licensing guide](https://go.microsoft.com/fwlink/p/?linkid=2085130).


[!INCLUDE[footer-include](../../includes/footer-banner.md)]