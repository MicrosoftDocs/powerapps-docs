---
title: Build Apps and take action with insights from Microsoft Fabric
description: Build Apps and drive action by creating virtual tables in dataverse with insights from Microsoft Fabric.
author: MilindaV2
ms.author: Milindav
ms.reviewer: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 11/14/2023
ms.custom: template-how-to
---
# Build Apps and automations, drive action with insights from Microsoft Fabric 

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Link to Microsoft Fabric feature in Dataverse eables extending your data and insights in Dynamics 365 and Power Apps in into Microsoft Fabric. You can also bring your own data into Fabric and combine, reshape, and aggregate data with data from Dataverse. You can use Fabric tools such as SQL, Spark, and dataflows to work with your data within Fabric. For example:
	• Combine financial data from Dynamics 365 with financial data from other systems to derive consolidated insights.
	• Merge historical data, ingested into OneLake from legacy systems, with current business data from Dynamics 365 and Dataverse.
	• Combine weblogs and telemetry data from your website with product and order details from Dynamics 365.
	• Apply machine learning and detect anomalies and exceptions within your data.

Insights aren't complete unless you can drive action and business processes. Now you can bring insights you found in Microsoft Fabric to build apps, drive business processes with Power Automate without data copy, no-ETL or third party integration tools. 

With Dataverse virtual tables over Microsoft Fabric, your low code App builders can connect to data in Microsoft OneLake and build Power Apps and drive business actions. 
Additionally, with Power Pages, low code makers can build external facing websites and drive action from OneLake insights with partners, suppliers, and customers

## Pre requisites
You can use an existing Dataverse environment or create a new developer environment. More information: [Create a developer environment](https://learn.microsoft.com/en-us/power-platform/developer/create-developer-environment)

You need to have contrinutor or administrator access to a Microsoft Fabric workspace with data. 
- If you don’t have Power BI premium license or Fabric capacity, you can sign up for a Free [Fabric trial capacity](https://learn.microsoft.com/en-us/fabric/get-started/fabric-trial)
- If you do not have a workspace with data, you can easily create a workspace with sample data using the [lakehouse tutorial here](https://learn.microsoft.com/en-us/fabric/data-engineering/tutorial-build-lakehouse)

## Create a virtual table with Microsoft Fabric data
You can follow the process below to create a Virtual table using Microsoft Fabric data.

>[Note]
> 
> This feature is enabled by default on all environments. Admins can disable this feature in the Power Platform admin center in the environment feature settings.
>

1. Sign into [Power Apps](https://make.powerapps.com) and then select **Tables** on the left navigation pane
2. On the command bar, select **New table > Create a virtual table** or select the **Create Virtual table** tile.
3. Select SQL Server as the connection, and then select Next.



