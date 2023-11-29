---
title: Dataverse direct integration with Microsoft Fabric
description: Link your data from Power Apps and Dynamics 365 in Dataverse with Microsoft Fabric and unlock advanced insights.
author: MilindaV2
ms.author: Milindav
ms.reviewer: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 11/14/2023
ms.custom: template-how-to
---
# Link your Dataverse environment to Microsoft Fabric and unlock deep insights

Microsoft Dataverse direct link with Microsoft Fabric enables organizations to extend their Power Apps, Dynamics 365 enterprise applications, and business processes into Fabric. The **Link to Microsoft Fabric** feature built into Power Apps makes all your Dynamics 365 and Power Apps data available in Microsoft OneLake, the built-in data lake for Microsoft Fabric.

- No need to export data, build ETL pipelines, or use third-party integration tools.
- With shortcuts from Dataverse directly into OneLake, your data stays in Dataverse while authorized users get to work with data in Fabric.
- Link data from all Dynamics 365 apps, including Dynamics 365 Finance and Operations apps.
- Build Power Apps and automations to drive action from insights in OneLake

[Microsoft OneLake](/fabric/onelake/onelake-overview), a data lake built into Fabric, helps eliminate data silos. Combine data from your applications and devices—web sites, mobile apps, sensors, and signals from your warehouse and factories—with data from your business processes in Dynamics 365—sales, cases, inventory, and orders—to predict potential delays or shortages that affect keeping your promises to customers. Dataverse creates shortcuts to OneLake, which enables you to work with data without making multiple copies.

Dataverse also generates an enterprise-ready [Synapse lakehouse and SQL endpoint](/fabric/data-engineering/lakehouse-overview) and a Power BI dataset for your Power Apps and Dynamics 365 data. This makes it easier for Data analysts, Data engineers, and Database admins to combine business data with data already present in OneLake using Spark, Python, or SQL. As data gets updated, changes are reflected in lakehouse automatically.

Low-code makers can build apps and automations to orchestrate business processes and react to insights found in Fabric. By adding those insights back to Dataverse as virtual tables connected to OneLake, makers can build low-code apps with Power Apps, Power Pages, or Power Automate using the design tools already available. Using connectors to over 1,000 apps, makers can create business processes that span Dynamics 365 as well as many other enterprise applications.

Watch this video to learn about accessing Dataverse data in Fabric:
> [!VIDEO https://www.microsoft.com/videoplayer/embed/RW1dP9v]

## Prerequisites

A Power BI premium license or Fabric capacity.

If you don’t have Power BI premium license or Fabric capacity, you can sign up for a Free Fabric trial capacity. More information: [Fabric (preview) trial](/fabric/get-started/fabric-trial)

## Link to Fabric from Power Apps

From the **Tables** area in Power Apps (make.powerapps.com), makers can link to Fabric by selecting **Analyze** > **Link to Microsoft Fabric** on the command bar. When you select the command for the first time, your Dataverse environment is linked to a Fabric workspace. A Synapse lakehouse, SQL endpoint, a Power BI dataset are created and Dataverse tables are linked to the lakehouse via shortcuts. Authorized users can work with Dataverse data with all Fabric workloads linked via shortcuts. The lakehouse, SQL endpoint, and the Power BI dataset are updated with new data as changes occur in Dataverse.

## Access your data in Microsoft OneLake

When you link to Fabric from Power Apps, the system creates an optimized replica of your data in delta parquet format, the native format of Fabric and OneLake, using Dataverse storage such that your operational workloads aren't impacted. This replica is governed and secured by Dataverse and stays within the same region as your Dataverse environment while enabling Fabric workloads to operate on this data.

Authorized users get access to Dataverse data in this replica from Microsoft OneLake. 

Admins can manage tables linked to OneLake from the **Azure Synapse Link for Dataverse** page. By opening the **Microsoft OneLake** link, admins can view tables added by makers, add more tables, and migrate the link to other environments. Tables added to OneLake consume Dataverse storage and admins can see storage consumption in the Power Platform admin center.

> [!NOTE]
>
> By selecting **Link to Microsoft Fabric**, the system adds all non-system Dataverse tables that have the **Track changes** property enabled.
>
> If you used this feature during public preview, you can continue to use the tables selected earlier. If you choose the **Link to Fabric** option in new environments (or unlink and re-link existing environments), all tables will be added.  
>  
> System administrators can add Dynamics 365 finance and operations tables into the **Microsoft OneLake** link that's created with this feature by selecting **Synapse Link**. These tables aren't automatically added at this time.
>
> Enabling this feature might result in an increase in Dataverse storage consumption. View additional storage consumption in Power Platform admin center.
>

## Link existing Azure Synapse Link for Dataverse profiles to Fabric

Azure Synapse Link for Dataverse enables IT admins with provisioning, configuring Azure resources as well as automating data exports to your own storage and enabling you to build your own integration pipelines. Link to Fabric feature enables direct connectivity between your data in Dataverse with Microsoft Fabric without data export enabling low code makers to easily work with their data. This table provides a quick comparison between the options.

| Link to Fabric                      | Azure Synapse Link                | 
|:-----------------------------------|:------------------------------|
| No copy, no ETL direct integration with Microsoft Fabric.  |  Export data to your own storage account and integrate with Synapse, Microsoft Fabric, and other tools. |
| Data stays in Dataverse - secure access in Microsoft Fabric. | Data stays in your own storage. You manage access. |
| All tables chosen by default.<sup>1</sup>  | System administrators can choose required tables. |
| Consumes additional Dataverse storage.  | Consumes your own storage as well as other compute and integration tools. | 

<sup>1</sup>You must create an Azure Synapse Link for Dataverse profile and enable the **Delta parquet conversion for Fabric link** option. This option isn't available for  Azure Synapse Link for Dataverse profiles that use the CSV output format.

We have also made it possible to connect existing Azure Synapse Links with Microsoft Fabric and benefit from Fabric innovations like Power BI DirectLake mode reports and integrated Spark and Data pipelines. You can add or remove tables from existing Azure Synapse Link for Dataverse links and create new Fabric links within a single experience. You can also use Azure Synapse Link for Dataverse to choose [tables and entities from Dynamics 365 Finance and Operations](/power-apps/maker/data-platform/azure-synapse-link-select-fno-data).

## Configure your environment

You can use an existing Dataverse environment or create a new developer environment if you want to try this feature. More information: [Create a developer environment](/power-platform/developer/create-developer-environment)

## Link to Microsoft Fabric

Link to Microsoft Fabric from the Power Apps **Tables** area: Select **Analyze** > **Link to Microsoft Fabric** on the command bar. 

1. Sign into [Power Apps](https://make.powerapps.com).
   > [!NOTE]
   >
   > This feature is enabled by default on all environments. Admins can disable this feature in the Power Platform admin center in the environment feature settings.
   > 
   > This option has moved from the **Export** menu since public preview. You can no longer select this option from the context menu for specific tables because this option applies to all tables.
   >

2. Select the environment you want, select **Tables** on the left navigation pane, and then select **Analyze** > **Link to Microsoft Fabric** on the command bar
3. If you're linking to Fabric for the first time, a wizard appears. You can launch Fabric with the same option in subsequent runs.
4. The wizard validates your Fabric subscription settings the first time. If needed, the wizard asks you to create a one time connection to Microsoft Fabric within the same step.
5. The wizard asks you to select an existing Fabric workspace or to create a new one. You can expect to see shortcuts to all your tables within this workspace.
6. When done, select **Create** in the wizard to create the workspace, create shortcuts, and to perform the initialization for the first time.

When complete, Fabric lakehouse opens in a separate browser tab.

It might take up to 60 minutes to update data in OneLake including the conversion to delta parquet format. If you selected a table that contains a lot of data, the initial load time might take longer. When you open Fabric lakehouse, the links appear as **unidentified** until the initial sync is completed. More information: [Troubleshooting common issues](#troubleshooting-common-issues)

The workspace you choose to link with Dataverse must be assigned to a premium capacity in the same region as your Dataverse environment. If you choose to create a new workspace, the system requires that you have access to a Power BI / Fabric premium capacity within the same region as your Dataverse environment. The wizard might detect missing prerequisites including insufficient capacity at the beginning.

Currently, the system supports these premium capacity SKUs: "P1", "P2", "P3", "P4", "P5", "F2", "F4", "F8", "F16", "F32", "F64", "F128", "F256", "F512", "F512", "F1024", "F2048", "DCT1", "FT1"

To confirm whether you have access to the required premium capacity, go to [Power BI](https://app.powerbi.com), open the workspace, and select **Workspace settings** > **Premium**. Make sure that **Trial** or **Premium capacity** is selected.

:::image type="content" source="media/fabric/fabric-trial-capacity.png" alt-text="You need either Trial or Premium capacity for your Power BI workspace." lightbox="media/fabric/fabric-trial-capacity.png":::

Open [Fabric](https://fabric.microsoft.com). You can also get there by going to [PowerBI.com](https://PowerBI.com).

Contact your Power BI administrator if you don't have permissions to create workspaces.

## Manage link to Microsoft OneLake

Admins can manage tables linked to OneLake from the **Azure Synapse Link for Dataverse** page. If an authorized user signed into Power Apps and linked tables to Fabric, they're shown under a link called **Microsoft OneLake**.

1. Sign into [Power Apps](https://make.powerapps.com). 
   > [!NOTE]
   >
   > This feature is enabled by default on all environments. Power Platform admins can disable this feature in the Power Platform admin center in the environment feature settings.

2. Select **Azure Synapse Link** from the left navigation pane, and the select **Microsoft OneLake**.
3. Open Fabric by selecting **View in Microsoft Fabric**.
4. Add more table links to Fabric by selecting **Manage tables**.
5. When you add a table, the system performs an initial sync and indexes the data. When the initial sync is completed, a shortcut to OneLake is created. View the status of tables by selecting **Manage tables**.
6. When the sync status is **Active**, as data gets updated, your data changes are shown in reports created in Fabric.
7. If a new column is added to a table that’s already added (also known as a metadata change), you can use the **Refresh Fabric tables** option to update the change in Fabric. You might need to review the report and downstream data flows to see that they aren't impacted by the change.
8. You can also **Unlink**, which removes the Fabric link to your Dataverse environment. When unlinking, the Fabric workspace or the lakehouse created aren't removed since you might have added your own tables and links.

> [!NOTE]
> 
> Depending on the size of data, initialization might take up to 60 minutes to complete. Subsequent updates to data might also take up to 60 minutes to update. When you open Fabric lakehouse you'll see the links as **unidentified** until the initial sync is completed. More information: [Troubleshooting common issues](#troubleshooting-common-issues)
>
> If you've installed Dynamics 365 apps such as Customer Insights, the tables required for the app are also included in the **Microsoft OneLake** link.
> 
> Removing already added tables has been disabled since it might impact already built reports.

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
> - Select **Enable Parquet/Delta lake** to enable the view in Fabric.
> - Existing Azure Synapse Link for Dataverse profiles where the data is saved as CSV files can't be linked to Microsoft Fabric.

## Work with Dataverse data and generate Power BI reports

This section describes the different ways you can work with Dataverse data in Fabric and generate reports in Power BI.

### Work with Dataverse data in Fabric

You can view the Azure Synapse Analytics lakehouse, SQL endpoint, and the default dataset generated by Dataverse in the Fabric workspace you chose earlier.

When you select **Link to Microsoft Fabric**, a Dataverse generated Azure Synapse Analytics lakehouse opens. You can go to other Fabric features and work with Fabric and Power BI.

### Explore the Dataverse generated Azure Synapse Analytics lakehouse

The tables you selected are added to the Azure Synapse Analytics lakehouse and displayed in Power BI as shown below. These tables are linked to your Power Platform environment using **Dataverse shortcuts**. As data changes in Dataverse, the Dataverse shortcuts in Fabric reflect the latest data.

![Dataverse generated Synapse lakehouse](media/fabric/fabric-with-dv-shortcuts-shown.png)

Note that Dataverse manages these shortcuts. You shouldn't delete or remove these shortcuts in Fabric. If you accidentally delete a link, you can go to the **Azure Synapse Link for Dataverse** area in Power Apps and select **Refresh Fabric links** to re-create the links.

### Explore data with SQL endpoint

You can open SQL endpoint and query Dataverse data with SQL and generate views in Fabric.

In Power BI, select **SQL endpoint** from the top right context menu. The data is displayed in a SQL friendly experience where you can create SQL queries and views.

![SQL endpoint with Dataverse generated shortcuts](media/fabric/fabric-sql-endpoint-shortcuts-shown.png)

### Autocreate a Power BI report

Choose the default dataset generated by Dataverse, and then select **Auto-create report**. A Power BI report with the data you have selected is created.

:::image type="content" source="media/fabric/fabric-autocreated-report.png" alt-text="Power BI auto-created report from Dataverse data in Fabric":::

## Secure data in the workspace

When you've linked Dataverse with Fabric workspaces, secure the data in this workspace before you share this data with others. More information: [OneLake security guidelines](/fabric/onelake/get-started-security)

## Troubleshooting common issues

If you experience an error message, here are suggestions to resolve the issue. 

| Error message                      | How to resolve                | 
|:-----------------------------------|:------------------------------|
| You need to get a Power BI premium of Fabric capacity. You can also get a Fabric trial. | You need a Power BI premium of a Fabric capacity. Power BI premium per user capacity won't be sufficient. You can get a free trial capacity by visiting the link here: [Fabric (preview) trial](/fabric/get-started/fabric-trial)  | 
| Creation of Fabric workspace failed. You can try again. If this issue persists contact Microsoft Customer Support with the correlation ID. | Ensure that you have admin permissions to your Power BI workspace. If the issue isn't resolved after several retries, contact Microsoft Customer Support with the provided reference ID |
| Creation of Fabric lakehouse failed. You can try again. If this issue persists contact Microsoft Customer Support with the correlation ID. | Ensure that you have admin permissions to your Power BI workspace. If the issue isn't resolved after several retries, you can contact Microsoft Customer Support with the provided reference ID. |
| Your organization doesn't appear to have Microsoft Fabric. You can get a trial. | Contact your administrator or get a trial version of Microsoft Fabric. |
|You need to get a trial version of Fabric to get started. | You need a Power BI premium of a Fabric capacity. Power BI premium per user capacity won't be sufficient. You can get a free trial capacity by visiting: [Fabric (preview) trial](/fabric/get-started/fabric-trial) |
| You need to be a system administrator to link to Fabric. | You need the system administrator security role in Dataverse to perform this operation. More information: [Security roles and privileges](/power-platform/admin/security-roles-privileges)  |

## See also

[Create virtual tables using the virtual connector provider](create-virtual-tables-using-connectors.md)
