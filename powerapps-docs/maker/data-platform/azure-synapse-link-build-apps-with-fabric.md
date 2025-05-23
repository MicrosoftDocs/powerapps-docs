---
title: Build apps and take action with insights from Microsoft Fabric
description: Build apps and drive action by creating virtual tables in Microsoft Dataverse with insights from Microsoft Fabric.
author: MilindaV2
ms.author: Milindav
ms.reviewer: matp
ms.service: powerapps
ms.subservice: dataverse-maker
ms.topic: how-to
ms.date: 03/10/2025
ms.custom: template-how-to
---
# Build apps and automations, drive action with insights from Microsoft Fabric 

Link to Microsoft Fabric feature in Microsoft Dataverse enables extending your data and insights in Dynamics 365 and Power Apps in Fabric. Bring your own data into Fabric and combine, reshape, and aggregate data with data from Dataverse. Use Fabric tools such as SQL, Spark, and dataflows to work with your data within Fabric. For example:

- Combine financial data from Dynamics 365 with financial data from other systems to derive consolidated insights.
- Merge historical data ingested into OneLake from legacy systems with current business data from Dynamics 365 and Dataverse.
- Combine weblogs and telemetry data from your website with product and order details from Dynamics 365.
- Apply machine learning and detect anomalies and exceptions within your data.

Insights aren't complete unless you can drive action and business processes. Bring insights you found in Fabric to build apps, drive business processes with Power Automate without data copy, no-ETL, or non-Microsoft integration tools.

With Dataverse virtual tables sourced with Fabric, your low-code app builders connect to data in Microsoft OneLake and build Power Apps and drive business actions. Additionally, with Power Pages, low-code makers can build external facing websites and drive action from OneLake insights with partners, suppliers, and customers.

![Virtual table with insights from Microsoft Fabric](media/Fabric/Fabric_to_App_GIF_demo.gif)

## Prerequisites

- An existing Dataverse environment or you can create a new developer environment. More information: [Create a developer environment](/power-platform/developer/create-developer-environment)
- Contributor or administrator access to a Fabric workspace with data.

If you don’t have Power BI premium license or Fabric capacity, you can sign up for a free [Fabric trial capacity](/fabric/get-started/fabric-trial).

If you don't have a workspace with data, create a workspace with sample data using the [lakehouse tutorial](/fabric/data-engineering/tutorial-build-lakehouse).

## Create a virtual table with Fabric data

Follow these steps to create a virtual table using Fabric data.

> [!NOTE]
>
> This feature is enabled by default with all environments. Admins can disable this feature in the Power Platform admin center in the environment feature settings. 

1. Sign into [Power Apps](https://make.powerapps.com), and then select **Tables** on the left navigation pane.
2. On the command bar, select **New table** > **Create a virtual table**.
3. Select **Microsoft Fabric** as the connection, and then select **Next**.
4. Select a **Microsoft Fabric workspace** from the available list of workspaces. All workspace where you have access are available in the list.
5. Choose a **Microsoft Fabric Lakehouse** from the drop-down list. All lakehouses and data warehouses within the workspace selected previously are available to choose.
6. On the **Data** page, select a table from the list of tables shown from the lakehouse. Select **Configure table and column names that will be used in Dataverse** if you want to rename any of the fields or tables in Dataverse or to specify additional properties available for you in Dataverse. Select **Next**.
7. If you selected the **Configure table and column names that will be used in Dataverse** checkbox, you're shown the table and column properties and you can modify them here. When you're done modifying them select **Next**.
8. Verify that the field chosen for **primary key field** is a unique field. You might need to verify the default field selected by the system as the primary key.

> [!NOTE]
>
> While the table you selected from Fabric Lakehouse might not have a primary key defined, you need to select a field that is unique to continue. If you don't select a unique field, the table might not show all the records. While the wizard selects a field based on metadata available, the selection might not be accurate.


9. Review the information shown, and then select **Finish**.

A new Dataverse virtual table is created with data from Fabric.

## Building apps and taking action with insights

You can build an app with the virtual table sourced with Fabric data in Power Apps (make.powerapps.com). From the Home page, select **Start with data** > **Select an existing table**, select the virtual table created earlier, and then select **Create app**. Provide a name for your app and build the app by following the wizard.

> [!NOTE]
>
> Virtual tables created with data from Microsoft Fabric OneLake are read-only. Currently, you can't modify the data in Fabric OneLake with Power Apps.

## See also

[Create and edit virtual tables that contain data from an external data source](create-edit-virtual-entities.md)
