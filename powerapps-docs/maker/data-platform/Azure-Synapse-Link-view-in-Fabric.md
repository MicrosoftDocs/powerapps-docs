---
title: Dataverse direct integration with Microsoft Fabric
description: Use Azure Synapse Link for Dataverse to export your Microsoft Dataverse data to Azure Synapse Analytics in Delta Lake format to explore your data and accelerate time to insight.
author: MilindaV2
ms.author: Milindav
ms.reviewer: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 09/05/2023
ms.custom: template-how-to
---
# View Dataverse data in Microsoft Fabric (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Microsoft Dataverse direct integration with Microsoft Fabric enables organizations to extend their Dynamics 365 enterprise applications and business processes into Fabric. The **View in Microsoft Fabric** feature built into Power Apps makes all your Dynamics 365 and other data from Power Apps available for analysis in Fabric.

- No need to export data, build ETL pipelines, or use third-party integration tools.
- Link data from Dataverse directly into Fabric, no need to bring your own storage.
- Link existing Azure Synapse Link for Dataverse links to Fabric.

> [!IMPORTANT]
> - This is a preview feature.
>
> - [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]
>

With just one click, you get more insights from your business data stored in Dataverse. :::image type="content" source="media/fabric/azure-synapse-link-two-experiences.png" alt-text="Azure Synapse link with Dataverse data in Microsoft Fabric" lightbox="media/fabric/azure-synapse-link-two-experiences.png":::

As data gets updated, changes are reflected in Fabric automatically. Dataverse also generates an enterprise-ready [lakehouse and SQL endpoint](/fabric/data-engineering/lakehouse-overview) for your Dynamics 365 data. This makes it easier for data engineers and database admins to combine data from multiple sources and build custom analytics with Spark, Python, or SQL.

[Microsoft OneLake](/fabric/onelake/onelake-overview), built into Fabric, helps to eliminate data silos. Combine data from your applications and devices—web sites, mobile apps, sensors, and signals from your warehouse and factories—with data from your business processes in Dynamics 365—sales, cases, inventory, and orders—to predict potential delays or shortages that affect keeping your promises to customers.

Makers can build low-code apps and automations to orchestrate business processes and react to insights found in Fabric. Add those insights back to Dataverse as virtual tables connected to Fabric OneLake. Makers can turn them into low-code apps with Power Apps, Power Pages, or Power Automate using the design tools already available. Using connectors to over 1,000 apps, makers can create business processes that span Dynamics 365 as well as many other enterprise applications.

## Prerequisites

A Power BI premium license or Fabric capacity. 

If you don’t have Power BI premium license or Fabric capacity, you can sign up for a Free Fabric trial capacity. More information: [Fabric (preview) trial](/fabric/get-started/fabric-trial)

## Open Microsoft Fabric from Power Apps

Low code makers can use make.powerapps.com to work with their data and build new apps and automations using Power Apps, Power Automate and other tools already available in the Power Platform.

Makers choose one or more tables from Dataverse and launch Fabric by selecting **View in Microsoft Fabric**. When you select the command for the first time, a workspace is created in your Power BI subscription with shortcuts in Fabric to Dataverse tables. A Fabric Lakehouse and a default data warehouse are also created, enabling makers to explore data with SQL, Spark, or other Fabric tools.

Makers can continue to add more data and open Fabric from Power Apps (make.powerapps.com). The default Fabric Lakehouse and the data warehouse are updated with new data as changes occur in Dataverse.

## Add more data and manage your link

When makers choose to view in Fabric from Power Apps, optimized replicas of your data are created in Dataverse storage such that your operational workloads aren't impacted. This replica is governed and secured by Dataverse while enabling Fabric workloads to operate on this data.

IT admins can manage this replica from the Azure Synapse Link for Dataverse page shown as **Managed Store** or **Microsoft OneLake**. IT admins can view tables added by makers, add or remove tables, and migrate the link to other environments. Admins can also see storage consumption in the Power platform admin center.

> [!NOTE]
>
> - Currently, you can’t add Dynamics finance and operations tables into the **Managed Store** link that's created with this feature.

## Link existing Azure Synapse Link for Dataverse profiles to Fabric

Azure Synapse Link for Dataverse enables IT admins to simplify their data integrations by provisioning and configuring Azure resources such as Azure datalake storage and Azure Synapse. Now, you can enable Fabric links for your existing links in Azure Synapse Link without any additional efforts or copying data. Fabric links simplify downstream data pipelines and you can use new features like Power BI DirectLake mode reports. Fabric Lakehouse and Lakehouse SQL endpoint contain improved query engines that let you work with Spark or SQL within an integrated environment.

You can add or removing tables from existing Azure Synapse Link for Dataverse links and/or create new Fabric links within a single experience. You can also use Azure Synapse Link for Dataverse to choose [tables and entities from Dynamics 365 Finance and Operations](/power-apps/maker/data-platform/azure-synapse-link-select-fno-data).

> [!NOTE]
> You need to create a Azure Synapse Link for Dataverse profile and enable the **Delta parquet conversion for Fabric link** option. This option isn't available for  Azure Synapse Link for Dataverse profiles that use the CSV output format.

Makers can build Apps and automations with enterprise-wide data available in Microsoft OneLake – the data store behind Microsoft Fabric. Makers define virtual tables using the Lakehouse SQL endpoint available for Fabric data and work with the data as if they were native Dataverse tables.

## Configure your environment

You can use an existing Dataverse environment or create a new developer environment. More information: [Create a developer environment](/power-platform/developer/create-developer-environment)

## Create a connection to your Dataverse environment

> [!IMPORTANT]
> You need the system administrator security role for your environment to complete this task.

Perform this one time operation in your Power BI environment for each Power Apps environment that will view Dataverse data in Fabric. This connection is used by Fabric to connect to the Dataverse environment to access data.

1. Sign in to [Microsoft Power BI](https://app.powerbi.com).
1. Select Power BI settings (**Gear icon** on top right), and then select **Manage connections and gateways**.
1. On the **Data (preview)** page, select **+ New** to create a new connection.
1. Select **Cloud**, and then select **Connection type** as **Dataverse**
1. Provide the following information: 
   - **Connection name**. Enter the environment URL that is also to be provided in the **Environment domain** field below.
   - **Environment domain**. Enter the environment domain, such as *contoso.crm.dynamics.com*. You can find the environment domain (URL) from the Power Platform admin center. Go to **Environments** > open the environment you want, and then copy the **Environment URL**.
   > [!IMPORTANT]
   > You must enter the **Environment URL** into both the **Connection name** and **Data source path** fields. Don't include the *https://* and the trailing */*.
   > 
   > :::image type="content" source="media/fabric/fabric-setting-up-connection.png" alt-text="Create a one time connectiong in Power BI" lightbox="media/fabric/fabric-setting-up-connection.png":::
   - Select **OAuth 2.0** as the **Authentication method**.
   - Select Edit credentials, and then confirm your credentials.
1. Review the connection information, and then select **Create**.

## Open Fabric

After you [Create a connection to your Dataverse environment](#create-a-connection-to-your-dataverse-environment), you can launch Fabric from Power Apps in two ways:

- **Tables** area: Select a table from the **Tables** area and then select **View in Microsoft Fabric**. This is the quickest way to get started.
- **Azure Synapse Link for Dataverse** area: From the **Azure Synapse Link for Dataverse** area you can choose your own Power BI workspace. From here you can also enable monitoring and managing options.

1. Sign in to Power Apps using the below URL.
   > [!IMPORTANT]
   > You must use this URL to access the preview. https://make.preview.Powerapps.com?athena.shortcuts=true&athena.mdl=true&athena.cds2=true

1. Select the environment you want, select **Tables** on the left navigation pane, and then select the table you want, such as the **Account** table.
1. On the command bar, select **View in Microsoft Fabric**.
1. If you're viewing a table in Fabric for the first time, you see a dialog box confirming the name of the Power BI workspace. Select **OK** to continue. Subsequent table selections are added to the same workspace so you aren't asked to confirm again.

Fabric Lakehouse opens in a separate browser tab.

During preview, it might take up to 30 minutes to update data in the managed lake including the conversion to Delta parquet format. If you've selected a table that contains a lot of data, the initial load time might take even longer. When you open Fabric Lakehouse, you see the links as **unidentified** until the initial sync is completed. More information: [Troubleshooting common issues](#troubleshooting-common-issues)

## Manage Fabric links

You can add or remove tables in the default Fabric link or create new links from the **Azure Synapse Link for Dataverse** area of Power Apps (make.powerapps.com). You can also link existing Azure Synapse Link for Dataverse profiles with Fabric using this option. You must have the system administrator security role in the environment to manage Fabric links.

### Manage the default link

If you or someone else signed in to Power Apps (make.powerapps.com) and linked tables previously, notice a default Fabric link called **Managed Store** or **Microsoft OneLake**. All tables chosen are included in the **Managed Store** Azure Synapse Link for Dataverse link.

You can add more tables or remove tables included in the default **Managed Store** link.

Managed store uses Dataverse provisioned file storage. When you purchase Power Apps or Dynamics 365 licenses, you receive a storage quota for your organization. When you add more tables to the managed store, this quota is consumed depending on the size of the table. You can purchase additional storage as required to expand the quota. You can view storage consumption in the Power Platform admin center.

1. Sign in to Power Apps using the below URL.
   > [!IMPORTANT]
   > You must use this URL to access the preview. https://make.preview.Powerapps.com?athena.shortcuts=true&athena.mdl=true&athena.cds2=true

1. Select **Azure Synapse Link** from the left navigation pane.
1. Notice the default Azure Synapse Link for Dataverse profile named **Managed store** or **Microsoft OneLake**. Select **Managed store** or **Microsoft OneLake**, and then select **View in Microsoft Fabric**.
1. If you or a user in this environment opened make.powerapps.com and linked tables earlier, notice all tables chosen.
1. You can add and remove tables linked to Fabric by selecting **Manage tables**.
1. When you add a table, the system performs an initial sync and replicates data in Dataverse storage. When the initial sync is completed, a Dataverse shortcut to Fabric is created. You can view the status of tables added from the **Tables** area in make.powerapps.com or tables added by selecting **Manage tables**.
1. When the sync status is **Active**, as data gets updated, your data changes are shown in reports created in Fabric.
1. If a new column is added to a table that’s already added (also known as a metadata change), you can use the **Refresh Fabric tables** option to update the change in Fabric. You might need to review the report and downstream data flows to see that they aren't impacted by the change.
1. Open Fabric by selecting **View in Microsoft Fabric**. You can also **Unlink**, which removes Fabric links. When unlinking, the Fabric workspace or the lakehouse created aren't removed since you might have added your own tables and links. However, to remove go to [Azure](https://portal.azure.com) and open Fabric to remove the lakehouse and workspace.

> [!NOTE]
> During preview, depending on the size of data, the initial copy might take more than 30 minutes to complete. For subsequent updates, it might take  about 30 minutes to update data in the managed store including the conversion to Delta parquet format. When you open Fabric Lakehouse you'll see the links as **unidentified** until the initial sync is completed. More information: [Troubleshooting common issues](#troubleshooting-common-issues)

## Link existing Azure Synapse Link for Dataverse links with Fabric

You can link your existing Azure Synapse Link for Dataverse profiles with Fabric from the Azure Synapse Link for Dataverse area. You need to select the **Enable Parquet/Delta lake** option to enable the view in Microsoft Fabric feature for Azure Synapse Link for Dataverse profiles.

To enable an existing link, follow these steps:

1. Sign in to Power Apps using the below URL.
   > [!IMPORTANT]
   > You must use this URL to access the preview. https://make.preview.Powerapps.com?athena.shortcuts=true&athena.mdl=true&athena.cds2=true

1. Select **Azure Synapse Link** from the left navigation.
1. Select an existing Azure Synapse Link for Dataverse profile, and then select **Link to Microsoft Fabric**.
1. You're prompted to choose a Power BI premium workspace to continue. A list of workspaces in the same region as your environment are displayed. If you don’t see a workspace in the drop down list, you might need to create one, and then return to this task. More information: [Create a Fabric workspace](#create-a-fabric-workspace)
1. Select **OK**. Validations are performed and the required artifacts are created in Fabric.  
1. Select **View in Microsoft Fabric** open Fabric Lakehouse.
1. You can add or remove tables using by selecting **Manage tables**. When you add a table, an initial sync is performed. When the initial sync is completed, select **Refresh Fabric tables** to refresh the Dataverse shortcut added to your Fabric Lakehouse.

> [!NOTE]
> - Select **Enable Parquet/Delta lake** to enable view in Microsoft Fabric.
> - Existing Azure Synapse Link for Dataverse profiles where the data is saved as CSV files can't be linked to Microsoft Fabric.

## Create a Fabric workspace

You need to create a new Fabric workspace or choose an existing workspace to link with an existing Azure Synapse Link for Dataverse. We recommend that you create a new workspace to direct link to Dataverse.

To confirm that you can create a premium workspace, go to [Power BI](https://app.powerbi.com), open the workspace, select **Workspace settings** > **Premium**. Make sure that **Trial** or **Premium capacity** is selected. The workspace you choose to link with Dataverse must be assigned to a premium capacity in the same region as your Dataverse environment.

:::image type="content" source="media/fabric/fabric-trial-capacity.png" alt-text="You need either Trial or Premium capacity for your Power BI workspace." lightbox="media/fabric/fabric-trial-capacity.png":::

Open Fabric with the URL shown below (notice the new URL, you can also get to preview by launching PowerBI.com):
https://fabric.microsoft.com

Contact your Power BI administrator if you don't have permissions to create workspaces.

## Work with Dataverse data and generate Power BI reports

This section describes the different ways you can work with Dataverse data in Fabric and generate reports in Power BI.

### Work with Dataverse data in Fabric

You can view the Azure Synapse Analytics lakehouse, SQL endpoint, and the default dataset generated by Dataverse in the Fabric workspace you chose earlier.

When you select **View in Microsoft Fabric**, a Dataverse generated Azure Synapse Analytics lakehouse opens. You can go to other Fabric features and work with Fabric and Power BI.

### Explore the Dataverse generated Azure Synapse Analytics lakehouse

The tables you selected are added to the Azure Synapse Analytics lakehouse and displayed in Power BI as shown below. These tables are linked to your Power Platform environment using **Dataverse shortcuts**. As data changes in Dataverse, the Dataverse shortcuts in Fabric reflect the latest data.

![Dataverse generated Synapse lakehouse](media/fabric/fabric-with-dv-shortcuts-shown.png)

Note that Dataverse manages these shortcuts. You shouldn't delete or remove these shortcuts in Fabric. If you accidentally delete a link, you can go to the Azure Synapse Link for Dataverse area in Power Apps and select **Refresh Fabric links** to re-create the links.

> [!NOTE]
> During preview, it can take 30 minutes or more to reflect the tables. You might see tables named as **undefined** during that time.

### Explore data with SQL endpoint

You can open SQL endpoint and query Dataverse data with SQL and generate views in Fabric.

In Power BI, select **SQL endpoint** from the top right context menu. The data is displayed in a SQL friendly experience where you can create SQL queries and views.

![SQL endpoint with Dataverse generated shortcuts](media/fabric/fabric-sql-endpoint-shortcuts-shown.png)

### Auto create a Power BI report

Choose the default dataset generated by Dataverse, and then select **Auto-create report**. A Power BI report with the data you have selected is created.

:::image type="content" source="media/fabric/fabric-autocreated-report.png" alt-text="Power BI auto-created report from Dataverse data in Fabric":::

## Secure data in the workspace

When you've linked Dataverse with Fabric workspaces, secure the data in this workspace before you share this data with others. More information: [OneLake security guidelines](/fabric/onelake/get-started-security)

## Build apps and automations with Fabric data

You might have explored Dataverse data with the Synapse lakehouse, SQL endpoint, or Power BI. You can also bring your own data into Fabric and combine, reshape, and aggregate data with data from Dataverse. You can use Fabric tools such as SQL, Spark, and dataflows to work with your data within Fabric. For an example;

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
| You need to create a Dataverse connection in Fabric with the connection name < your domain URL>. | Go to [Create a connection to your Dataverse environment](#create-a-connection-to-your-dataverse-environment)  | 
| You need to get a Power BI premium of Fabric capacity. You can also get a Fabric trial | You need a Power BI premium of a Fabric capacity. Power BI premium per user capacity won't be sufficient. You can get a free trial capacity by visiting the link here: [Fabric (preview) trial](/fabric/get-started/fabric-trial)  | 
| Creation of Fabric workspace failed. Consider creating a Fabric workspace first and linking using the **Azure Synapse Link for Dataverse** area | Go to [Manage Fabric links](#manage-fabric-links) |
| Creation of Fabric workspace failed. You can try again. If this issue persists contact Microsoft Customer Support with the corelation ID | Ensure that you have admin permissions to your Power BI workspace. If the issue isn't resolved after several retries, contact Microsoft Customer Support with the provided reference ID |
| Creation of Fabric lakehouse failed. You can try again. If this issue persists contact Microsoft Customer Support with the corelation ID | Ensure that you have admin permissions to your Power BI workspace. If the issue isn't resolved after several retries, you may contact Microsoft Customer Support with the provided reference ID |
| You need to add one or more tables before linking to Microsoft Fabric. | If you're using Managed store (the default link), add one or more tables using **Manage tables** in the **Azure Synapse Link for Dataverse** area in Power Apps (make.powerapps.com) and try to link to Fabric again.  |
| Your organization doesn't appear to have Microsoft Fabric. You can get a Trial | Contact your administrator or get a Trial version of Microsoft Fabric. |
|You need to get a Trial version of Fabric to get stated | You need a Power BI premium of a Fabric capacity. Power BI premium per user capacity won't be sufficient. You can get a free trial capacity by visiting: [Fabric (preview) trial](/fabric/get-started/fabric-trial) |
| You need to be a System administrator to link to Fabric | You need the system administrator security role in Dataverse to perform this operation. More information: [Security roles and privileges](/power-platform/admin/security-roles-privileges)  |

## See also

[Create virtual tables using the virtual connector provider](create-virtual-tables-using-connectors.md)
