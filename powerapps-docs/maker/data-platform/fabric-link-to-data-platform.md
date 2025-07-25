---
title: Configure your environment and link to Microsoft Fabric
description: This article shows you how to configure your Power Platform environment and link it to Microsoft Fabric.
author: MilindaV2
ms.author: Milindav
ms.reviewer: matp
contributors: saviegas
ms.service: powerapps
ms.subservice: dataverse-maker
ms.topic: how-to
ms.date: 06/23/2025
ms.custom: template-how-to
---
# Link to Microsoft Fabric

Microsoft Fabric integration with Microsoft Dataverse allows you to seamlessly link your Power Platform environment to Microsoft Fabric, enabling advanced data analysis and reporting capabilities. This guide provides step-by-step instructions on configuring your environment, linking it to Microsoft Fabric, and managing linked tables.

You can use an existing Dataverse environment or create a new developer environment if you want to try this feature. More information: [Create a developer environment](/power-platform/developer/create-developer-environment)

## Prerequisites

- You must have the Systems Administrator security role in the Power Platform environment to enable **Link to Fabric** or **Synapse Link**. 
- You must be an administrator of the Power BI workspace. 
- If you want the system to create a Power BI workspace, you need to have Power BI Capacity Administrator access to a capacity within the same region as the Dataverse environment.
- A Power BI premium license or Fabric capacity within the same Azure geographical region as your Dataverse environment is required. If you don’t have Power BI premium license or Fabric capacity within the same geographical region, you can buy a capacity or sign up for a free Fabric trial capacity. More information: [Fabric (preview) trial](/fabric/get-started/fabric-trial)
- Your administrator needs to grant you access to create Fabric lakehouses and artifacts. You can find these settings in the  Fabric admin portal. Go to **Tenant Settings** > **Microsoft Fabric** > **Users can create Fabric items**, **Tenant settings** > **Workspace settings** > **Create workspaces** as well as **Tenant settings** > **oneLake settings** > **Users can access data stored in OneLake with apps external to Fabric**.
- To confirm whether you have access to the required premium capacity, go to [Power BI](https://app.powerbi.com), open the workspace, and select **Workspace settings** > **Premium**. Make sure that **Trial** or **Premium capacity** is selected.
   :::image type="content" source="media/fabric/fabric-trial-capacity.png" alt-text="You need either Trial or Premium capacity for your Power BI workspace." lightbox="media/fabric/fabric-trial-capacity.png":::

## Create a link to Fabric

Link to Microsoft Fabric from the Power Apps **Tables** area: Select **Analyze** > **Link to Microsoft Fabric** on the command bar.

1. Sign into [Power Apps](https://make.powerapps.com).
2. Select the environment you want, select **Tables** on the left navigation pane, and then select **Analyze** > **Link to Microsoft Fabric** on the command bar.
3. If you're linking to Fabric for the first time, a wizard appears. You can launch Fabric with the same option in subsequent runs.
4. The wizard validates your Fabric subscription settings the first time. In the event you don't have a Fabric capacity in the same geography or region as your Dataverse environment, the wizard notifies you to get a capacity in the required geography. 
5. If needed, the wizard asks you to create a one time connection to Microsoft Fabric within the same step. This connection is needed to enable Fabric and Dataverse services to securely access data. You need to sign in and then save the connection to proceed.
6. The wizard asks you to select an existing Fabric workspace or to create a new one. You can expect to see shortcuts to all your tables within this workspace.
7. If you don't see workspaces, ask the system to create a workspace. Go to [Troubleshooting common issues](fabric-troubleshoot.md) if you don't see the desired workspace.  
8. All Dataverse tables where the "Change tracking" property is enabled are linked to Fabric. If this environment is linked to finance and operations apps, you can add finance and operations tables later using the **Manage tables** option. More information: [Manage link to Fabric](#manage-link-to-fabric).
9. When done, select **Create** in the wizard to create the workspace, create shortcuts, and to perform the initialization for the first time.
10. When complete, Fabric lakehouse opens in a separate browser tab. 

> [!NOTE]
>
> It might take up to 60 minutes to update data in OneLake including the conversion to delta parquet format. If you selected a table that contains a lot of data, the initial load time might take longer. When you open Fabric lakehouse, the links appear as **unidentified** until the initial sync is completed. More information: [Troubleshooting common issues](fabric-troubleshoot.md)
>
> When the initial sync is complete, the system continuously refreshes updates in Dataverse in the lakehouse. It might take up to 60 minutes for the data to be refreshed especially during peak load periods.
>
> If you have more than 2,000 active Dataverse tables, Link to Fabric can fail with an error. Go to [Troubleshooting common issues](fabric-troubleshoot.md) for help resolving issues.

## Manage link to Fabric

Admins can manage tables linked to OneLake from the **Azure Synapse Link for Dataverse** page. If this environment is linked to Fabric, you see a link called **Microsoft OneLake**.

1. Sign into [Power Apps](https://make.powerapps.com). 
   > [!NOTE]
   >
   > This feature is enabled by default on all environments. Power Platform admins can disable this feature in the Power Platform admin center in the environment feature settings.

2. Select **Azure Synapse Link** from the left navigation pane, and the select **Microsoft OneLake**.
3. Open Fabric by selecting **View in Microsoft Fabric**.
4. Add more table links to Fabric by selecting **Manage tables**.
5. When you add a table, the system performs an initial sync and indexes the data. When the initial sync is completed, a shortcut to OneLake is created. View the status of tables by selecting **Manage tables**. Use the **Refresh Fabric tables** option to add the newly enabled table in Fabric. You might need to review the report and downstream data flows to see that they aren't impacted by the change.

   > [!NOTE]
   > If your environment is linked to a Dynamics 365 finance and operations environment, the add tables option enables you to include tables from finance and operations apps. Learn more: [Choose finance and operations data in Azure Synapse Link for Dataverse](azure-synapse-link-select-FnO-data.md)

6. When the sync status is **Active**, as data gets updated, your data changes are shown in reports created in Fabric.
7. If a new column is added to a table that’s already part of the profile (also known as a metadata change), you can use the **Refresh Fabric tables** option, from the command bar, to update the change in Fabric. The update occurs after the next table data change is triggered. You might need to review the report and downstream data flows to confirm that they aren't impacted by the change.
8. You can also **Unlink**, which removes the Fabric link to your Dataverse environment. When unlinking, the Fabric lakehouse is also removed.

> [!NOTE]
> If you've installed Dynamics 365 apps such as Customer Insights, the tables required for the app are also included in the **Microsoft OneLake** link.
> 
> Removing already added tables has been disabled since it might impact already built reports.

### Share the data connection with other users

The system creates a data connection between the Power Platform environment and Fabric workspace using the credentials of the user at the time of link creation. If you use the **Fabric link** option from the Power Apps **Tables** area, the system creates the connection and asks you to save it. If you use the **Synapse Link** option, you must create a data connection yourself before enabling the link. 

The system uses this connection to enable Fabric users to connect to Dataverse - the data store behind the Power Platform environment. If you want to enable other users to add or remove tables to Fabric link, you need to share this data connection with other users. 

1. Go to [Fabric.Microsoft.com](https://fabric.microsoft.com) and select the gear icon on top left (next to the user icon).
2. On the **Settings** menu, select **Data connections and Gateways**. The available data connections are displayed.
3. Select the **Connections** tab, and then choose the data connection you created with the connection type **Dataverse**. You might notice a connection that is named similar to **org...crm.dynamics.com**. In case you have multiple connections like this, you need to select the connection that links to the specific Power Platform environment.
4. Once you select the correct data connection, select **...** > **manage users**. Then you're shown users who have access to this connection.
5. Enter the name or email of other users who need access to data. When you select a user, specify either the **Owner** role or **Reader** role. You only need to provide reader role to enable them to consume data. The users you specify receive an e-mail confirming access to data.

You might need to grant access to other users to this workspace so that they can work with data. Depending on the need for data access, you might need to secure the data in this workspace before you share this data with others. You can secure the lakehouse as well as tables within the lakehouse using OneLake security. More information: [OneLake security overview](/fabric/onelake/security/get-started-security)

You can only create user based connections at this time.

## Link existing Azure Synapse Link for Dataverse links with Fabric

You can link your existing Azure Synapse Link for Dataverse profiles with Fabric from the **Azure Synapse Link for Dataverse** area. You need to select the **Enable Parquet/Delta lake** option to enable the view in the Fabric feature for Azure Synapse Link for Dataverse profiles.

To enable an existing link, follow these steps:

1. Sign into [Power Apps](https://make.powerapps.com).
1. Select **Azure Synapse Link** from the left navigation.
1. Select an existing Azure Synapse Link for Dataverse profile, and then select **Link to Microsoft Fabric**.
1. You're prompted to choose a Power BI premium workspace to continue. A list of workspaces in the same region as your environment are displayed. If you don’t see a workspace in the drop-down list, you might need to create one, and then return to this task. More information [Link to Microsoft Fabric](#link-to-microsoft-fabric)
1. Select **OK**. Validations are performed and the required artifacts are created in Fabric.  
1. Select **View in Microsoft Fabric** open Fabric lakehouse.
1. You can add or remove tables using by selecting **Manage tables**. When you add a table, an initial sync is performed. When the initial sync is completed, select **Refresh Fabric tables** to refresh the Dataverse shortcut added to your Fabric lakehouse.

> [!NOTE]
>
> - Select **Enable Parquet/Delta lake** to enable the view in Fabric.
> - Existing Azure Synapse Link for Dataverse profiles where the data is saved as CSV files can't be linked to Microsoft Fabric.
> - Azure Synapse Link profiles secured with managed identities, formerly Managed Service Identity (MSI), can't be linked to Microsoft Fabric at this point in time.  

## Next steps

[Work with Dataverse data and generate Power BI reports](fabric-work-data-and-power-bi.md)
