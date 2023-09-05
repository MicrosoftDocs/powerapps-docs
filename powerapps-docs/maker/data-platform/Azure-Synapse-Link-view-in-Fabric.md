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

Microsoft Dataverse direct integration with Microsoft Fabric enables organizations to extend their Dynamics 365 enterprise applications and business processes into Fabric. The **View in Microsoft Fabric** feature built into Power Apps makes all your Dynamics 365 data available for analysis in Fabric. <!-- Why limit this to D365? This could also include any Dataverse data independent of D365 apps right? -->

- No need to export data, build ETL pipelines, or use third-party integration tools.
- Link data from Dataverse directly into Fabric, no need to bring your own storage.
- Link existing Azure Synapse Link for Dataverse links or new links created with your own Azure storage. <!-- Throughout I assumed "Synapse Link" referred to "Azure Synapse Link for Dataverse". If it is something else, let me know what the correct naming is, such as Azure Synapse Link. -->

> [!IMPORTANT]
> This is a preview feature.
>
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

With just one click, you’ll get more insights from your business data stored in Dataverse. :::image type="content" source="media/fabric/azure-synapse-link-two-experiences.png" alt-text="Azure Synapse link with Dataverse data in Microsoft Fabric" lightbox="media/fabric/azure-synapse-link-two-experiences.png":::

As data gets updated, changes are reflected in Fabric automatically. Dataverse also generates an enterprise-ready Azure Synapse Analytics lakehouse and SQL endpoint for your Dynamics 365 data. This makes it easier for data engineers and database admins to combine data from multiple sources and build custom analytics with Spark, Python, or SQL.

Fabric’s lake-centric approach helps to eliminate data silos. Combine data from your applications and devices—web sites, mobile apps, sensors, and signals from your warehouse and factories—with data from your business processes in Dynamics 365—sales, cases, inventory, and orders—to predict potential delays or shortages that affect keeping your promises to customers.

Makers can build low-code apps and automations to orchestrate business processes and react to insights found in Fabric using connectors to over 1,000 apps. Add those insights back to Dataverse as virtual tables connected to the external source <!-- Since virtual tables always connect via an external source I've revised --> through the SQL endpoint. Makers can turn them into low-code apps with Power Apps, Power Pages, or Power Automate using the design tools already available.

## Prerequisites

A Power BI premium license or Fabric capacity. If you don’t have Power BI premium license or Fabric capacity, you can sign-up for a Free Fabric trial capacity. More information: [Fabric (preview) trial](/fabric/get-started/fabric-trial) <!-- Moved this here to make more discoverable since I was blocked when selecting a table > View in Microsoft Fabric with a message that a Power BI premium license was required -->

## Open Fabric from Power Apps

Low code makers can use make.powerapps.com to work with their data and build new apps and automations using Power Apps, Power Automate and other tools already available in the Power platform. 

<!-- Removing this since it should be easily discoverable from the maker portal for users so no need to image it
![View in Microsoft Fabric built into Power Apps Maker portal](media/Fabric/Maker-portal-view-in-fabric-2.png) -->

Makers choose one or more tables from Dataverse and open Fabric by selecting **View in Microsoft Fabric**. When selecting for the first time, the system creates a workspace in your Power BI subscription and creates shortcuts in Fabric to Dataverse tables. An Azure Synapse Analytics lakehouse and a default data warehouse are also created, enabling makers to explore data with SQL, Spark, or other Fabric tools.

Makers can continue to add more data and open Fabric from the make.powerapps.com. The default Azure Synapse Analytics lakehouse and the data warehouse are updated with new data as changes occur in Dataverse.

## Add more data and manage your link

When makers choose to view in Fabric from Power Apps, optimized replicas of your data in Dataverse storage are created such that your operational workloads aren't impacted. This replica is governed and secured by Dataverse while enabling Fabric workloads to operate on this data.

IT admins manage this replica from the Synapse Link for Dataverse page shown as **Managed Store** or **Microsoft OneLake**. IT admins can view tables added by makers, add or remove tables, and migrate the link to other environments. Admins can also see storage consumption in the Power platform admin center.

> [!NOTE]
>
> - Currently, you can’t add Dynamics finance and operations tables into the **Managed Store** Azure Synapse Link for Dataverse link that's created with this feature. <!-- Do you mean the managed store link that's created? -->
> - Dataverse environment life cycle operations, such as environment move operations, might impact reports built using this feature. More information: [Troubleshooting common issues](#troubleshooting-common-issues)

## Link existing Azure Synapse Link for Dataverse profiles to Fabric

Azure Synapse Link for Dataverse enables IT admins to simplify their data integrations by provisioning and configuring Azure resources such as Azure datalake storage and Azure Synapse. Now, you can enable Fabric links for your existing Azure Synapse Link for Dataverse links and benefit from the innovations in Fabric without any additional efforts or copying data. Fabric integration further simplifies data integration efforts with features like Power BI Direct Lake mode reports as well as query engine improvements in next generation Azure Synapse data warehouse.

<!-- Removing this since it should be easily discoverable from the maker portal for users so no need to image it
![View in Microsoft Fabric in Synapse Link](media/Fabric/Azure-Syunapse-Link-with-View-In-Fabric.png) -->

You can add or removing tables from existing Azure Synapse Link for Dataverse links and/or create new Fabric links within a single experience. You can also use Azure Synapse Link for Dataverse to choose tables and entities from Dynamics 365 Finance and Operations (F&O). <!-- Is there a link to more information for this??? --> See <…>>

> [!NOTE]
> You need to create a Azure Synapse Link for Dataverse profile and enable the **Delta parquet conversion for Fabric link** option. This option isn't available for  Azure Synapse Link for Dataverse profiles that use the CSV output format.

Makers can build Apps and automations with enterprise-wide data available in One Lake – the data store behind Microsoft Fabric. Makers define external tables <!-- Do you mean virtual tables here? -->using the SQL endpoint available for Fabric data and work with the data as if they were native Dataverse tables.

## Configure your environment

You can use an existing PowerApps environment or create a new developer environment. More information: [Create a developer environment](/power-platform/developer/create-developer-environment)

## Create a connection to your PowerApps environment

> [!IMPORTANT]
> You need the system administrator security role for your environment to complete this task.

You need to perform this one time operation in your Power BI environment for each Power Apps environment. This connection is used by Fabric to connect to the Dataverse environment to access data.

1. Sign in to [Power BI](https://app.powerbi.com).
1. Select Power BI settings (**Gear icon** on top right), and then select **Manage connections and gateways**.

<!-- common UI not necessary to have a screenshot ![](media/Fabric/Fabric-launch-connections-and-gateways.png) -->
1. On the **Data (preview)** page, select **+ New** to create a new connection.
1. Select **Cloud**, and then select **Connection type** as **Dataverse**
1. Provide the following information: 
   - **Connection name**. Enter the environment URL that is also to be provided in the **Environment domain** field below.
   - **Environment domain**. Enter the environment domain, such as *contoso.crm.dynamics.com*. You can find the environment domain (URL) from the Power Platform admin center. Go to **Environments** > open the environment you want, and then copy the **Environment URL**.
   > [!IMPORTANT]
   > You must enter the **Environment URL** into both the **Connection name** and **Environment domain** fields. Don't include the *https://* and the trailing */*.
   > 
   > :::image type="content" source="media/fabric/fabric-setting-up-connection.png" alt-text="Create a one time connectiong in Power BI" lightbox="media/fabric/fabric-setting-up-connection.png"::: <!-- This screenshot UI doesn't match what's current. Instead of "Environment domain" it has "Data source path". Do you have a current screenshot that has the correct UI and doesn't include your name?-->
   - Select **OAth2** as the **Authentication method**.
   - Select Edit credentials, and then confirm your credentials.
1. Review the connection information, and then select **Create**.

## Open Fabric

After you [Create a connection to your PowerApps environment](#create-a-connection-to-your-powerapps-environment), you can open Fabric from Power Apps in two ways:

- **Tables** area: Select a table from the **Tables** area and then select **View in Microsoft Fabric**. This is the quickest way to get started.
- **Azure Synapse Link for Dataverse** area: From the **Azure Synapse Link for Dataverse** area you can choose your own Power BI workspace. From here you can also enable monitoring and managing options.

<!-- This is the same as the Tables area isn't it? So removing  Alternatively, you can create a link by choosing tables from Power Apps. System creates a Power BI workspace, a link and launches Microsoft Fabric with default settings. You can add more tables to this link later from Tables menu in PowerApps maker portal.

![View in Microsoft Fabric built into Power Apps Maker portal](media/Fabric/Maker-portal-view-in-fabric-2.png)   -->

1. Sign in to Power Apps using the below URL.
   > [!IMPORTANT]
   > You must use this URL to access the preview. https://make.preview.Powerapps.com?athena.shortcuts=true&athena.mdl=true&athena.cds2=true

1. Select the environment you want, select **Tables** on the left navigation pane, and then select the table you want, such as the **Account** table.
1. On the command bar select **View in Microsoft Fabric**.
1. If your viewing a table in Fabric for the first time, you'll see a dialog box confirming the name of the Power BI workspace. Select **OK** to continue. Subsequent table selections will be added to the same workspace so you won't be asked to confirm again.

Azure Synapse lakehouse opens in a separate browser tab.

It might take 15 minutes to update data in the managed lake including the conversion to Delta parquet format. If you've selected a table that contains a lot of data, the initial load time might take even longer. When you open Fabric lakehouse, you'll see the links as **unidentified** until the initial sync is completed. More information: [Troubleshooting common issues](#troubleshooting-common-issues)

## Manage Fabric links

You can add or remove tables in the default Fabric link or create new links using the Synapse Link menu. <!-- What's "Synapse Link menu"? Do you mean the Azure Synapse Link for Dataverse area in the maker portal? -->You can also link existing Synapse Link profiles with Fabric using this option. You must have the system administrator security role the environment to manage Fabric links.

### Manage the default link

If you or someone else signed in to Power Apps (make.powerapps.com) and linked tables previously, you'll notice a default Fabric link called **Managed Store** or **Microsoft OneLake**. All tables chosen are included in the **Managed Store** Azure Synapse Link for Dataverse link.

You can add more tables or remove tables included in the default **Managed Store** link.

Managed store uses Dataverse provisioned file storage. When you purchase Power Apps or Dynamics 365 licenses, you receive a storage quota for your organization. When you add more tables to the managed store, this quota is consumed depending on the size of the table. You can purchase additional storage as required to expand the quota. You can view storage consumption in the Power Platform admin center.

1. Sign in to Power Apps using the below URL.
   > [!IMPORTANT]
   > You must use this URL to access the preview. https://make.preview.Powerapps.com?athena.shortcuts=true&athena.mdl=true&athena.cds2=true

1. Select **Azure Synapse Link** from the left navigation pane.
1. You'll notice the default Azure Synapse Link for Dataverse profile named **Managed store** or **Microsoft OneLake**. Select **Managed store** or **Microsoft OneLake**, and then select **View in Microsoft Fabric**.
1. If you or a user in this environment opened make.powerapps.com and linked tables earlier, you'll notice all tables chosen.
1. You can add and remove tables linked to Fabric by selecting **Manage tables**.
1. When you add a table, the system performs an initial sync and replicates data in Dataverse storage. When the initial sync is completed, a Dataverse shortcut to Fabric is created. You can view the status of tables added from the **Tables** area in make.powerapps.com or tables added by selecting **Manage tables**.
1. When the sync status is **Active**, as data gets updated, your data changes are shown in reports created in Fabric.
1. If a new column is added to a table that’s already added to Managed Lake <!-- What is Managed Lake? Do you mean Managed Store? -->(also known as a metadata change), you can use the **Refresh Fabric tables** option to update the change in Fabric. You might need to review the report and downstream data flows to see that they aren't impacted by the change.
1. Open Fabric by selecting **View in Microsoft Fabric**. You can also **Unlink**, which removes Fabric links. When unlinking, the Fabric workspace or the lakehouse created aren't removed since you might have added your own tables and links. However, to remove go to [Azure](https://portal.azure.com) and open Fabric to remove the lakehouse and workspace.

> [!NOTE]
> Depending on the size of data, the initial copy might take more than 15 minutes to complete. For subsequent updates, it might take  about 15 minutes to update data in the managed lake including the conversion to Delta parquet format. When you launch Fabric lakehouse you'll see the links as **unidentified** until the initial sync is completed. More information: [Troubleshooting common issues](#troubleshooting-common-issues)

## Link existing Azure Synapse Link for Dataverse links with Fabric

You can link your existing Azure Synapse Link for Dataverse profiles with Fabric from the Azure Synapse Link for Dataverse area. You need to select the **Enable Parquet/Delta lake** option to enable the view in Microsoft Fabric feature for Azure Synapse Link for Dataverse profiles. 

To enable an existing link, follow these steps:

1. Sign in to Power Apps using the below URL.
   > [!IMPORTANT]
   > You must use this URL to access the preview. https://make.preview.Powerapps.com?athena.shortcuts=true&athena.mdl=true&athena.cds2=true

1. Select **Azure Synapse Link** from the left navigation.
1. Select an existing Azure Synapse Link for Dataverse profile, and then select **Link to Microsoft Fabric**.
1. You're prompted to choose a Power BI premium workspace to continue. A list of workspaces in the same region as your environment are displayed. If you don’t see a workspace in the drop down list, you might need to create a one and then return to this task. More information: [Create a Fabric workspace](#create-a-fabric-workspace)
1. Select **OK**. Validations are performed and the required artifacts are created in Fabric.  
1. Click **View in Microsoft Fabric** open Fabric lakehouse.
1. You can add or remove tables using by selecting **Manage tables**. When you add a table, an initial sync is performed. When the initial sync is completed, select **Refresh Fabric tables** to refresh the Dataverse shortcut added to your Fabric lakehouse.

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

## Working with Dataverse data in Fabric
<!-- start here -->
You can view the Synapse Lakehouse, SQL endpoint and the default dataset generated by Dataverse in the Microsoft Fabric workspace you have chosen earlier.

When you choose **View in Microsoft Fabric** option PowerApps maker portal or in Synapse Link, Dataverse generated Synapse lake house will be launched. You can navigate into other Fabric features yourself and work with Fabric and Power BI.

## Explore Dataverse generated Synapse Lakehouse

You will notice the tables you have selected being added to the Synapse Lakehouse as shown below. These tables are linked to your PowerApps environment using **Dataverse shortcuts**. As data changes in Dataverse, the Dataverse shortcuts in Fabric will reflect the latest data. 
Also note that Dataverse manages these shortcuts. You should not delete or remove these shortcuts in Microsoft fabric. If you delete them inadvertently, you can revisit the Synapse Link menu in PowerApps and choose **Refresh Fabric Links** option to recreate the links.


![Dataverse generated Synapse Lakehouse](media/Fabric/Fabric-with-DV-shortcuts-shown.png)

**NOTE**: During preview, the system make take \~15minute or more to reflect the tables. You may see table names as **undefined** during that time.

## Explore data with SQL endpoint
You can launch SQL endpoint and query Dataverse data with SQL and generate views in Microsoft Fabric

![Choose SQL endpoint](media/Fabric/Fabric-choose-SQL-endpoint.png)

Select SQL endpoint from the top right context menu and the same data will be shown in a SQL friendly experience where you can create SQL queries and views.

![SQL endpoint with Dataverse generated shortcuts](media/Fabric/Fabric-SQL-endpoint-shortcuts-shown.png)


## Auto create a Power BI report

You can choose the default dataset generated by Dataverse and choose Auto create a report. The system generates a PowerBI report with the data you have selected as shown below.

![](media/Fabric/Fabric-autocreated-PBI-report.png)

## Secure data in the workspace 
You have linked PowerApps and Fabric workspaces as a system administrator. You need to secure the data in this workspace before you share this data with others. 
>
> **NOTE:**
>
> In the future, you will be able to apply security definitions in PowerApps to data in the workspace.
>

## Build Apps and automations with Fabric data in Maker portal

By now, you may have explored Dataverse data with the Synapse Lakehouse, SQL endpoint as well as Power BI. You can also bring your own data into Microsoft Fabric and combine, re-shape and aggregate data with data from Dataverse. You can use Fabric tools such as SQL, Spark, Data flows to work with your data within Microsoft Fabric. For an example;

-	Combine financial data from Dynamics 365 with financial data from other systems to derive consolidated insights
-	Merge historical data (ingested into OneLake from legacy systems) with current business data from Dynamics and PowerApps
-	Combine weblogs and telemetry data from your web site with product and order details from Dynamics 
-	Apply machine learning and detect anomalies and exceptions within your data.
  
Insights are not complete unless you can drive action and business processes. You can bring data in OneLake into Dataverse as external tables and use that data to build PowerApps or create business automations.

### Choose data from Microsoft Fabric
1.	You can bring data in a Lakehouse into Dataverse by choosing the corresponding SQL endpoint. Choose the SQL endpoint corresponding to the Lakehouse
2.	You can also bring data from a data warehouse into Dataverse.
3.	In either the SQL endpoint or the data warehouse, Select the gear icon on top left to launch the properties window.
4.	Copy the (1) SQL connection string and the (2) name from the properties window

![Choose SQL endpoint](media/Fabric/Fabric-SQL-endpoint-for-defining-virtual-tables.png)


### Define Dataverse external tables
5.	Launch PowerApps maker portal and select Tables menu. Choose **Create a virtual table** 

![Create virtual table](media/Fabric/Fabric-choose-SQL-endpoint-new-experience.png)

6.	Select SQL server as the connection. 
7.	Paste the SQL connection string you copied in step (1) above. 
8.	Enter the name of the data warehouse or SQL endpoint you copied (2) above. 
9.	Choose tables from the Fabric. When complete, you can continue to work with the tables and build Apps.


## Troubleshooting common issues

> NOTE
> - This feature is in preview. Preview features are not ready for production use and are provided to validate and to provide feedback to product team. You can join the preview yammer group [https://aka.ms/SynapseLinkforDynamics](https://aka.ms/SynapseLinkforDynamics) to provide feedback and stay in touch with product team
>  - You need to have a Power BI premium capacity, Fabric premium capacity or Trial capacity in the same region as your Dataverse environment. Power BI premium per user capacity will not be sufficient. You can get a free trial capacity by visiting the link here: [Fabric (preview) trial - Microsoft Fabric \| Microsoft Learn](https://learn.microsoft.com/en-us/fabric/get-started/fabric-trial)
>  - Depending on the size of data, initial sync may take 15min or more. In case of very large tables, initial sync may take much longer before you can consume data in Microsoft Fabric. 
> 	- After the initial sync, data changes in Dataverse will be reflected in Microsoft Fabric upto 60 mins later.
>

If you are seeing an error message. see suggestions to resolve below 

| Error message                      | How to resolve                | 
|:-----------------------------------|:------------------------------|
| You need to create a Dataverse connection in Fabric with the connection name < your domain URL>. | See configure data connection section  | 
| You need to get a Power BI premium of Fabric capacity. You can also get a Fabric trial | You need a Power BI premium of a Fabric capacity. Power BI premium per user capacity will not be sufficient. You can get a free trial capacity by visiting the link here: [Fabric (preview) trial - Microsoft Fabric \| Microsoft Learn](https://learn.microsoft.com/en-us/fabric/get-started/fabric-trial)  | 
| Creation of Fabric workspace failed. Consider creating a Fabric workspace first and linking using Synapse Link menu | See Manage Microsoft Fabric Links section for details |
| Creation of Fabric workspace failed. You can try again, If this issue persists contact support with corelation ID | Ensure that you have admin permissions to your Power BI workspace. If the issue is not resolved after several retrys, you may contact support with the provided reference ID |
| Creation of Fabric Lakehouse failed. You can try again, If this issue persists contact support with corelation ID | Ensure that you have admin permissions to your Power BI workspace. If the issue is not resolved after several retrys, you may contact support with the provided reference ID |
| You need to add one or more tables before linking to Microsoft Fabric. | If you are using Managed store (ie. the default link), you can add one or more tables using the Manage tables option in Synapse Link menu and try to Link to the Fabric again |
| Your organization does not appear to have Microsoft Fabric. You can get a Trial | You can contact your administrator or get a Trial version of Microsoft Fabric |
|You need to get a Trial version of Fabric to get stated | You need a Power BI premium of a Fabric capacity. Power BI premium per user capacity will not be sufficient. You can get a free trial capacity by visiting the link here: [Fabric (preview) trial - Microsoft Fabric \| Microsoft Learn](https://learn.microsoft.com/en-us/fabric/get-started/fabric-trial) |
| You need to be a System administrator to link to Fabric | You need system administrator permissions in PowerApps to perform this operation |


