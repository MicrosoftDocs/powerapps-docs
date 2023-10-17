---
title: Dataverse direct integration with Microsoft Fabric
description: Link your data from Power Apps and Dynamics 365 in Dataverse with Microsoft Fabric Link and unlock advanced insights.
author: MilindaV2
ms.author: Milindav
ms.reviewer: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 10/09/2023
ms.custom: template-how-to
---
# Link your Dataverse environment to Microsoft Fabric and unlock deep insights (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Microsoft Dataverse direct link with Microsoft Fabric enables organizations to extend their Power Apps, Dynamics 365 enterprise applications, and business processes into Fabric. The **Link to Microsoft Fabric** feature built into Power Apps makes all your Dynamics 365 and Power Apps data available in OneLake.

- No need to export data, build ETL pipelines, or use third-party integration tools.
- With shortcuts from Dataverse directly into OneLake, your data stays in Dataverse while authorized users get to work with data in Fabric.
- Link existing Azure Synapse Link for Dataverse links to Fabric.
- Link data from all Dynamics 365 apps, including Dynamics 365 Finance and Operations apps.


> [!IMPORTANT]
> - This is a preview feature.
>
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]
>

With a few clicks, you can link your Dataverse environment with Fabric. Your tables in Dataverse appear in OneLake. Your data remains within the Dataverse governance boundary while authorized Fabric users get to work with your data using Power BI, SQL, Spark, and many other tools.

[OneLake](/fabric/onelake/onelake-overview), a data lake built into Fabric, helps eliminate data silos. Combine data from your applications and devices—web sites, mobile apps, sensors, and signals from your warehouse and factories—with data from your business processes in Dynamics 365—sales, cases, inventory, and orders—to predict potential delays or shortages that affect keeping your promises to customers. Dataverse creates shortcuts to OneLake, which enables you to work with data without making multiple copies.

Dataverse also generates an enterprise-ready [Synapse lakehouse and SQL endpoint](/fabric/data-engineering/lakehouse-overview) and a Power BI dataset for your Power Apps and Dynamics 365 data. This makes it easier for Data analysts, Data engineers, and Database admins to combine business data with data already present in OneLake using Spark, Python, or SQL. As data gets updated, changes are reflected in lakehouse automatically.

Low-code makers can build apps and automations to orchestrate business processes and react to insights found in Fabric. By adding those insights back to Dataverse as virtual tables connected to OneLake, makers can build low-code apps with Power Apps, Power Pages, or Power Automate using the design tools already available. Using connectors to over 1,000 apps, makers can create business processes that span Dynamics 365 as well as many other enterprise applications.

## Prerequisites

A Power BI premium license or Fabric capacity. 

If you don’t have Power BI premium license or Fabric capacity, you can sign up for a Free Fabric trial capacity. More information: [Fabric (preview) trial](/fabric/get-started/fabric-trial)

## Open Fabric from Power Apps

From the **Tables** area in Power Apps (make.powerapps.com), makers choose one or more tables, then launch Fabric by selecting **Export** > **Link to Microsoft Fabric** on the command bar. When you select the command for the first time, your Dataverse environment is linked to a Fabric workspace. A Synapse lakehouse, SQL endpoint, a Power BI dataset, and shortcuts to your tables are all created in Microsoft OneLake within the workspace. You see the tables selected in Dataverse as shortcuts and you can work with Dataverse data linked via shortcuts.

Makers can continue to choose more data and open Fabric from Power Apps. The lakehouse, SQL endpoint, and the Power BI dataset are updated with new data as changes occur in Dataverse.

## Link to Microsoft OneLake overview

When you link to Fabric from Power Apps, the system creates an optimized replica of your data in delta parquet format, the native format of Fabric and OneLake, using Dataverse storage such that your operational workloads aren't impacted. This replica is governed and secured by Dataverse and stays within the same region as your Dataverse environment while enabling Fabric workloads to operate on this data.

Admins can manage tables linked to OneLake from the **Azure Synapse Link for Dataverse** page. By opening the **Microsoft OneLake** link, admins can view tables added by makers, add or remove tables, and migrate the link to other environments. Tables added to OneLake consume Dataverse storage and admins can see storage consumption in the Power Platform admin center.

> [!NOTE]
>
> Dataverse might add related tables to OneLake to enable better experiences for Fabric users. Also you might see tables added by Dynamics 365 apps.
>
> Currently, you can’t add Dynamics 365 Finance and Operations (F&O) tables into the **Microsoft OneLake** link that's created with this feature. You can add F&O tables using the Synapse Link feature. More information: [Choose finance and operations data in Azure Synapse Link for Dataverse](azure-synapse-link-select-FnO-data.md)

## Link existing Azure Synapse Link for Dataverse profiles to Fabric

Azure Synapse Link for Dataverse enables admins to simplify their data integrations by provisioning and configuring Azure resources such as Azure datalake storage and Azure Synapse. Now, you can enable Fabric links for your existing links in Azure Synapse Link without any additional effort or copying data. Fabric links simplify downstream data pipelines and you can use features like Power BI DirectLake mode reports. Fabric lakehouse and lakehouse SQL endpoint contain improved query engines that let you work with Spark or SQL within an integrated environment.

You can add or remove tables from existing Azure Synapse Link for Dataverse links and create new Fabric links within a single experience. You can also use Azure Synapse Link for Dataverse to choose [tables and entities from Dynamics 365 Finance and Operations](/power-apps/maker/data-platform/azure-synapse-link-select-fno-data).

> [!NOTE]
> You need to create a Azure Synapse Link for Dataverse profile and enable the **Delta parquet conversion for Fabric link** option. This option isn't available for  Azure Synapse Link for Dataverse profiles that use the CSV output format.

## Configure your environment

You can use an existing Dataverse environment or create a new developer environment. More information: [Create a developer environment](/power-platform/developer/create-developer-environment)

## Create a connection to your Dataverse environment

Perform this one time operation in your Power BI environment for each Power Apps environment that will view Dataverse data in Fabric. This connection is used by Fabric to connect to the Dataverse environment to access data.

> [!IMPORTANT]
> You need the system administrator security role for your environment to complete this task.

1. Sign in to [Microsoft Power BI](https://app.powerbi.com).
1. Select Power BI settings (**Gear icon** on top right), and then select **Manage connections and gateways**.
1. On the **Data** page, select **+ New** to create a new connection.
1. Select **Cloud**, and then select **Connection type** as **Dataverse**
1. Provide the following information: 
   - **Connection name**. Enter the environment URL that is also to be provided in the **Environment domain** field below.
   - **Environment domain**. Enter the environment domain, such as *contoso.crm.dynamics.com*. You can find the environment domain (URL) from the Power Platform admin center. Go to **Environments** > open the environment you want, and then copy the **Environment URL**.
      > [!IMPORTANT]
      > You must enter the **Environment URL** into both the **Connection name** and **Data source path** fields. Don't include the *https://* and the trailing */*.
      > 
      > :::image type="content" source="media/fabric/fabric-setting-up-connection.png" alt-text="Create a one time connectiong in Power BI" lightbox="media/fabric/fabric-setting-up-connection.png":::
   - Select **OAuth 2.0** as the **Authentication method**.
   - Select **Edit credentials**, and then confirm your credentials.
1. Review the connection information, and then select **Create**.

## Link to Microsoft Fabric

After you [Create a connection to your Dataverse environment](#create-a-connection-to-your-dataverse-environment), you can link Fabric from Power Apps in two ways:

- **Tables** area: Select a table from the **Tables** area and then select **Export** > **Link to Microsoft Fabric**. This is the quickest way to get started.

- **Azure Synapse Link for Dataverse** area: From the Azure Synapse Link for Dataverse area link an existing Synapse Link profile or, select **Microsoft OneLake**.

1. Sign into [Power Apps](https://make.powerapps.com).
   > [!NOTE]
   >
   > This feature is enabled by default on all environments. Admins can disable this feature in the Power Platform admin center in the environment feature settings.

2. Select the environment you want, select **Tables** on the left navigation pane, and then select the table you want, such as the **Account** table.
3. On the command bar, select **Export > Link to Microsoft Fabric**.
4. If you're viewing a table in Fabric for the first time, a dialog box confirming the name of the Power BI workspace appears. Select **OK** to continue. Subsequent table selections are added to the same workspace so you aren't asked to confirm again.

Fabric lakehouse opens in a separate browser tab.

During preview, it might take up to 60 minutes to update data in OneLake including the conversion to delta parquet format. If you've selected a table that contains a lot of data, the initial load time might take even longer. When you open Fabric lakehouse, you see the links as **unidentified** until the initial sync is completed. More information: [Troubleshooting common issues](#troubleshooting-common-issues)

## Manage link to Microsoft OneLake

If you or someone else signed into Power Apps and linked tables to Fabric, they're shown under **Microsoft OneLake**.

1. Sign into [Power Apps](https://make.powerapps.com). 
   > [!NOTE]
   >
   > This feature is enabled by default on all environments. Admins can disable this feature in the Power Platform admin center in the environment feature settings.

2. Select **Azure Synapse Link** from the left navigation pane, and the select **Microsoft OneLake**.
3. Open Fabric from here by selecting **View in Microsoft Fabric**.
4. Add and remove tables linked to Fabric by selecting **Manage tables**.
5. When you add a table, the system performs an initial sync and indexes the data. When the initial sync is completed, a shortcut to OneLake is created. View the status of tables by selecting **Manage tables**.
6. When the sync status is **Active**, as data gets updated, your data changes are shown in reports created in Fabric.
7. If a new column is added to a table that’s already added (also known as a metadata change), you can use the **Refresh Fabric tables** option to update the change in Fabric. You might need to review the report and downstream data flows to see that they aren't impacted by the change.
8. You can also **Unlink**, which removes the Fabric link to your Dataverse environment. When unlinking, the Fabric workspace or the lakehouse created aren't removed since you might have added your own tables and links.

> [!NOTE]
> During preview, depending on the size of data, initialization may take up to 60 minutes to complete. Subsequent updates to data may also take up to 60 minutes to update. When you open Fabric lakehouse you'll see the links as **unidentified** until the initial sync is completed. More information: [Troubleshooting common issues](#troubleshooting-common-issues)

## Link existing Azure Synapse Link for Dataverse links with Fabric

You can link your existing Azure Synapse Link for Dataverse profiles with Fabric from the **Azure Synapse Link for Dataverse** area. You need to select the **Enable Parquet/Delta lake** option to enable the view in the Fabric feature for Azure Synapse Link for Dataverse profiles.

To enable an existing link, follow these steps:

1. Sign into [Power Apps](https://make.powerapps.com).
1. Select **Azure Synapse Link** from the left navigation.
1. Select an existing Azure Synapse Link for Dataverse profile, and then select **Link to Microsoft Fabric**.
1. You're prompted to choose a Power BI premium workspace to continue. A list of workspaces in the same region as your environment are displayed. If you don’t see a workspace in the drop-down list, you might need to create one, and then return to this task. More information: [Create a Fabric workspace](#create-a-fabric-workspace)
1. Select **OK**. Validations are performed and the required artifacts are created in Fabric.  
1. Select **View in Microsoft Fabric** open Fabric lakehouse.
1. You can add or remove tables using by selecting **Manage tables**. When you add a table, an initial sync is performed. When the initial sync is completed, select **Refresh Fabric tables** to refresh the Dataverse shortcut added to your Fabric lakehouse.

> [!NOTE]
> - Select **Enable Parquet/Delta lake** to enable the view in Fabric.
> - Existing Azure Synapse Link for Dataverse profiles where the data is saved as CSV files can't be linked to Microsoft Fabric.

## Create a Fabric workspace

You need to create a new Fabric workspace or choose an existing workspace to link with an existing Azure Synapse Link for Dataverse. We recommend that you create a new workspace to direct link to Dataverse.

To confirm that you can create a premium workspace, go to [Power BI](https://app.powerbi.com), open the workspace, select **Workspace settings** > **Premium**. Make sure that **Trial** or **Premium capacity** is selected. The workspace you choose to link with Dataverse must be assigned to a premium capacity in the same region as your Dataverse environment.

:::image type="content" source="media/fabric/fabric-trial-capacity.png" alt-text="You need either Trial or Premium capacity for your Power BI workspace." lightbox="media/fabric/fabric-trial-capacity.png":::

Open [Fabric](https://fabric.microsoft.com). You can also get there by going to [PowerBI.com](https://PowerBI.com).

Contact your Power BI administrator if you don't have permissions to create workspaces.

## Work with Dataverse data and generate Power BI reports

This section describes the different ways you can work with Dataverse data in Fabric and generate reports in Power BI.

### Work with Dataverse data in Fabric

You can view the Azure Synapse Analytics lakehouse, SQL endpoint, and the default dataset generated by Dataverse in the Fabric workspace you chose earlier.

When you select **View in Microsoft Fabric**, a Dataverse generated Azure Synapse Analytics lakehouse opens. You can go to other Fabric features and work with Fabric and Power BI.

### Explore the Dataverse generated Azure Synapse Analytics lakehouse

The tables you selected are added to the Azure Synapse Analytics lakehouse and displayed in Power BI as shown below. These tables are linked to your Power Platform environment using **Dataverse shortcuts**. As data changes in Dataverse, the Dataverse shortcuts in Fabric reflect the latest data.

![Dataverse generated Synapse lakehouse](media/fabric/fabric-with-dv-shortcuts-shown.png)

Note that Dataverse manages these shortcuts. You shouldn't delete or remove these shortcuts in Fabric. If you accidentally delete a link, you can go to the **Azure Synapse Link for Dataverse** area in Power Apps and select **Refresh Fabric links** to re-create the links.

### Explore data with SQL endpoint

You can open SQL endpoint and query Dataverse data with SQL and generate views in Fabric.

In Power BI, select **SQL endpoint** from the top right context menu. The data is displayed in a SQL friendly experience where you can create SQL queries and views.

![SQL endpoint with Dataverse generated shortcuts](media/fabric/fabric-sql-endpoint-shortcuts-shown.png)

### Auto-create a Power BI report

Choose the default dataset generated by Dataverse, and then select **Auto-create report**. A Power BI report with the data you have selected is created.

:::image type="content" source="media/fabric/fabric-autocreated-report.png" alt-text="Power BI auto-created report from Dataverse data in Fabric":::

## Secure data in the workspace

When you've linked Dataverse with Fabric workspaces, secure the data in this workspace before you share this data with others. More information: [OneLake security guidelines](/fabric/onelake/get-started-security)

## Build apps and automations with Fabric data

You might have explored Dataverse data with the Synapse lakehouse, SQL endpoint, or Power BI. You can also bring your own data into Fabric and combine, reshape, and aggregate data with data from Dataverse. You can use Fabric tools such as SQL, Spark, and dataflows to work with your data within Fabric. For example:

- Combine financial data from Dynamics 365 with financial data from other systems to derive consolidated insights.
- Merge historical data, ingested into OneLake from legacy systems, with current business data from Dynamics 365 and Dataverse.
- Combine weblogs and telemetry data from your website with product and order details from Dynamics 365.
- Apply machine learning and detect anomalies and exceptions within your data.
  
Insights aren't complete unless you can drive action and business processes. Bring data in OneLake into Dataverse as virtual tables and use that data to build apps in Power Apps or create business automations with Power Automate.

### Choose data from Fabric

1. In Power BI, bring data in a lakehouse into Dataverse by choosing the corresponding SQL endpoint. Select the SQL endpoint corresponding to the lakehouse. You can also bring data from a data warehouse into Dataverse.
1. In either the SQL endpoint or the data warehouse, select **Settings** (gear icon) on top left to launch the properties window.
1. Copy the (1) SQL connection string and the (2) name from the properties page.

   :::image type="content" source="media/fabric/fabric-sql-endpoint-for-defining-virtual-tables.png" alt-text="Select the SQL endpoint to use for creating virtual tables":::

### Define Dataverse virtual tables using Fabric data

1. Sign in to Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc), and then select **Tables** on the left navigation pane.
1. On the command bar, select **New table** > **Create a virtual table**.
1. Select **SQL Server** as the connection, and then select **Next**.
1. Paste the SQL connection string you copied earlier with [Choose data from Fabric](#choose-data-from-fabric), (1) into the **SQL Server name** field.
1. Enter the name of the data warehouse or SQL endpoint you copied earlier (2) into the **SQL database name** field.
1. Select tables from Fabric. When complete, you can continue to work with the tables and build apps.

## Troubleshooting common issues

If you experience an error message, here are suggestions to resolve the issue. 

| Error message                      | How to resolve                | 
|:-----------------------------------|:------------------------------|
| You need to create a Dataverse connection in Fabric with the connection name &lt;your domain URL&gt;. | Go to [Create a connection to your Dataverse environment](#create-a-connection-to-your-dataverse-environment)  | 
| You need to get a Power BI premium of Fabric capacity. You can also get a Fabric trial. | You need a Power BI premium of a Fabric capacity. Power BI premium per user capacity won't be sufficient. You can get a free trial capacity by visiting the link here: [Fabric (preview) trial](/fabric/get-started/fabric-trial)  | 
| Creation of Fabric workspace failed. Consider creating a Fabric workspace first and linking using the **Azure Synapse Link for Dataverse** area. | Go to [Manage link to Microsoft OneLake](#manage-link-to-microsoft-onelake) |
| Creation of Fabric workspace failed. You can try again. If this issue persists contact Microsoft Customer Support with the corelation ID. | Ensure that you have admin permissions to your Power BI workspace. If the issue isn't resolved after several retries, contact Microsoft Customer Support with the provided reference ID |
| Creation of Fabric lakehouse failed. You can try again. If this issue persists contact Microsoft Customer Support with the corelation ID. | Ensure that you have admin permissions to your Power BI workspace. If the issue isn't resolved after several retries, you may contact Microsoft Customer Support with the provided reference ID |
| You need to add one or more tables before linking to Microsoft Fabric. | If you're using Managed store (the default link), add one or more tables using **Manage tables** in the **Azure Synapse Link for Dataverse** area in Power Apps (make.powerapps.com) and try to link to Fabric again.  |
| Your organization doesn't appear to have Microsoft Fabric. You can get a Trial | Contact your administrator or get a Trial version of Microsoft Fabric. |
|You need to get a Trial version of Fabric to get started. | You need a Power BI premium of a Fabric capacity. Power BI premium per user capacity won't be sufficient. You can get a free trial capacity by visiting: [Fabric (preview) trial](/fabric/get-started/fabric-trial) |
| You need to be a System administrator to link to Fabric. | You need the system administrator security role in Dataverse to perform this operation. More information: [Security roles and privileges](/power-platform/admin/security-roles-privileges)  |

## See also

[Create virtual tables using the virtual connector provider](create-virtual-tables-using-connectors.md)
