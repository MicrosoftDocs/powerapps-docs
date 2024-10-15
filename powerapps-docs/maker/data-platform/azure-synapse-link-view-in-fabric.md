---
title: Link your Dataverse environment to Microsoft Fabric and unlock deep insights
description: Link your Microsoft Dataverse data from Power Apps and Dynamics 365 with Microsoft Fabric and unlock advanced insights.
author: MilindaV2
ms.author: Milindav
ms.reviewer: matp
ms.service: powerapps
ms.topic: how-to
ms.date: 10/15/2024
ms.custom: template-how-to
---
# Link your Dataverse environment to Microsoft Fabric and unlock deep insights

Microsoft Dataverse direct link to Microsoft Fabric enables organizations to extend their Power Apps and Dynamics 365 enterprise applications, and business processes into Fabric. The **Link to Microsoft Fabric** feature built into Power Apps makes all your Dynamics 365 and Power Apps data available in Microsoft OneLake, the built-in data lake for Microsoft Fabric.

- No need to export data, build extract, transform, load (ETL) pipelines, or use our partner integration tools.
- With shortcuts from Dataverse directly into OneLake, your data stays in Dataverse while authorized users get to work with data in Fabric.
- Link data from all Dynamics 365 apps, including Dynamics 365 Finance and Operations apps.
- Build Power Apps and automations to drive action from insights in OneLake.

[Microsoft OneLake](/fabric/onelake/onelake-overview), a data lake built into Fabric, helps eliminate data silos. Combine data from your applications and devices web sites, mobile apps, sensors, and signals from your warehouse and factories with data from your business processes in Dynamics 365, such as sales, cases, inventory, and orders, to predict potential delays or shortages that affect keeping your promises to customers. Dataverse creates shortcuts to OneLake, which enables you to work with data without making multiple copies.

Dataverse also generates an enterprise-ready [Synapse lakehouse and SQL endpoint](/fabric/data-engineering/lakehouse-overview) and a Power BI dataset for your Power Apps and Dynamics 365 data. This makes it easier for data analysts, data engineers, and database admins to combine business data with data already present in OneLake using Spark, Python, or SQL. As data gets updated, changes are reflected in lakehouse automatically.

Low-code makers can build apps and automations to orchestrate business processes and react to insights found in Fabric. By adding those insights back to Dataverse as virtual tables connected to OneLake, makers build low-code apps with Power Apps, Power Pages, or Power Automate using the design tools already available. Using connectors to over 1,000 apps, makers create business processes that span Dynamics 365 as well as many other enterprise applications.

Watch this video to learn about accessing Dataverse data in Fabric:
> [!VIDEO https://www.microsoft.com/videoplayer/embed/RW1dP9v]

## Prerequisites

- A Power BI premium license or Fabric capacity within the same Azure geographical region as your Dataverse environment is required. Currently, the system supports these premium capacity SKUs: "P1", "P2", "P3", "P4", "P5", "F2", "F4", "F8", "F16", "F32", "F64", "F128", "F256", "F512", "F512", "F1024", "F2048", "DCT1", "FT1."
- If you don’t have Power BI premium license or Fabric capacity within the same geographical region, you buy a capacity or sign up for a free Fabric trial capacity. More information: [Fabric (preview) trial](/fabric/get-started/fabric-trial)

- Your administrator can grant you access to create Fabric lakehouses and artifacts. You can find these settings in the  Fabric admin portal. Go to **Tenant Settings** > **Microsoft Fabric** > **Users can create Fabric items**, **Tenant settings** > **Workspace settings** > **Create workspaces** as well as **Tenant settings** > **oneLake settings** > **Users can access data stored in OneLake with apps external to Fabric**.
- You must have the system administrator security role in the Dataverse environment.
- You must be an administrator of the Power BI workspace. You also need to be a Power BI capacity administrator to a capacity within the same geographic location as the Dataverse environment.
- To confirm whether you have access to the required premium capacity, go to [Power BI](https://app.powerbi.com), open the workspace, and select **Workspace settings** > **Premium**. Make sure that **Trial** or **Premium capacity** is selected.
   :::image type="content" source="media/fabric/fabric-trial-capacity.png" alt-text="You need either Trial or Premium capacity for your Power BI workspace." lightbox="media/fabric/fabric-trial-capacity.png":::

## Link to Fabric from Power Apps

From the **Tables** area in Power Apps (make.powerapps.com), makers link to Fabric by selecting **Analyze** > **Link to Microsoft Fabric** on the command bar. 

When you select the command for the first time, a wizard driven experience links your Dataverse environment to a Fabric workspace. A Synapse lakehouse, SQL endpoint, a Power BI dataset are created and Dataverse tables are linked to the lakehouse via shortcuts.

Once the link is set up, you can grant other users access to the Fabric workspace so that they can work with Dataverse data using all Fabric workloads. The lakehouse, SQL endpoint, and Power BI dataset are updated with new data as changes occur in Dataverse.

## Direct access to your data in Microsoft OneLake

Link to Fabric creates a direct and secure Link between your data in Dataverse and a Fabric workspace. There's no need to provide a storage account or Synapse workspaces. When you link to Fabric from Power Apps, the system creates an optimized replica of your data in delta parquet format, the native format of Fabric and OneLake, using Dataverse storage such that your operational workloads aren't impacted. This replica is governed and secured by Dataverse and stays within the same region as your Dataverse environment while enabling Fabric workloads to operate on this data.

Admins can manage tables linked to OneLake from the **Azure Synapse Link for Dataverse** page. By opening the **Microsoft OneLake** link, admins view tables added by makers, add more tables, and migrate the link to other environments. Tables added to OneLake consume Dataverse storage and admins can see storage consumption in the Power Platform admin center.

> [!NOTE]
>
> By selecting **Link to Microsoft Fabric**, the system adds all non-system Dataverse tables that have the **Track changes** property enabled. You can add more tables later.
>
> If you used this feature during public preview, you can continue to use the tables selected earlier. If you choose the **Link to Fabric** option in new environments (or unlink and re-link existing environments), all tables will be added.  
>  
> Enabling this feature might result in an increase in *Dataverse database* storage consumption. View additional storage consumption in Power Platform admin center.
>

## Comparing Link to Fabric with Azure Synapse Link for Dataverse

Azure Synapse Link for Dataverse enables IT admins to export data to their own storage and build data integration pipelines. Azure Synapse Link assists with provisioning and configuring Azure resources within an integrated experience.

Link to Fabric feature enables direct connectivity between your data in Dataverse with Microsoft Fabric without the need to bring your own storage and Synapse workspaces. Link to Fabric leverages storage built into Dataverse and removes the need to provision and manage your own storage.  

This table provides a comparison between the options.

| Link to Fabric                      | Azure Synapse Link                | 
|:-----------------------------------|:------------------------------|
| No copy, no ETL direct integration with Microsoft Fabric.  |  Export data to your own storage account and integrate with Synapse, Microsoft Fabric, and other tools. |
| Data stays in Dataverse - users get secure access in Microsoft Fabric. | Data stays in your own storage. You manage access to users. |
| All tables chosen by default.  | System administrators can choose required tables. |
| Consumes additional Dataverse storage. | Consumes your own storage as well as other compute and integration tools. | 

You can connect existing Azure Synapse Links with Microsoft Fabric and benefit from Fabric innovations like Power BI DirectLake mode reports and integrated Spark and data pipelines. You must create an Azure Synapse Link for Dataverse profile and enable the **Delta parquet conversion for Fabric link** option. This option isn't available for Azure Synapse Link for Dataverse profiles that use the CSV output format.

## Configure your environment

You can use an existing Dataverse environment or create a new developer environment if you want to try this feature. More information: [Create a developer environment](/power-platform/developer/create-developer-environment)

## Link to Microsoft Fabric

Link to Microsoft Fabric from the Power Apps **Tables** area: Select **Analyze** > **Link to Microsoft Fabric** on the command bar. 

1. Sign into [Power Apps](https://make.powerapps.com).
2. Select the environment you want, select **Tables** on the left navigation pane, and then select **Analyze** > **Link to Microsoft Fabric** on the command bar.
   > [!NOTE]
   >
   > This feature is enabled by default on all environments. Admins can disable this feature in the Power Platform admin center in the environment feature settings.
   > 
   > This option has moved from the **Export** menu since public preview. You can no longer select this option from the context menu for specific tables because this option applies to all tables.
   >

3. If you're linking to Fabric for the first time, a wizard appears. You can launch Fabric with the same option in subsequent runs.
4. The wizard validates your Fabric subscription settings the first time. In the event you don't have a Fabric capacity in the same geography or country as your Dataverse environment, the wizard notifies you to get a capacity in the required geography. 
5. If needed, the wizard asks you to create a one time connection to Microsoft Fabric within the same step. This connection is needed to enable Fabric and Dataverse services to securely access data. You need to sign in and then save the connection to proceed.
6. The wizard asks you to select an existing Fabric workspace or to create a new one. You can expect to see shortcuts to all your tables within this workspace.
7. If you don't see workspaces, ask the system to create a workspace. Go to [Troubleshooting common issues](#troubleshooting-common-issues) if you don't see the desired workspace.  
8. All Dataverse tables where the "Change tracking" property is enabled are linked to Fabric. If this environment is linked to finance and operations apps, you can add finance and operations tables later using the **Manage tables** option. More information: [Manage link to Fabric](#manage-link-to-fabric).
9. When done, select **Create** in the wizard to create the workspace, create shortcuts, and to perform the initialization for the first time.
10. When complete, Fabric lakehouse opens in a separate browser tab. 

> [!NOTE]
>
> It might take up to 60 minutes to update data in OneLake including the conversion to delta parquet format. If you selected a table that contains a lot of data, the initial load time might take longer. When you open Fabric lakehouse, the links appear as **unidentified** until the initial sync is completed. More information: [Troubleshooting common issues](#troubleshooting-common-issues)
>
> Go to [Troubleshooting common issues](#troubleshooting-common-issues) for help resolving issues.

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
7. If a new column is added to a table that’s already added (also known as a metadata change), you can use the **Refresh Fabric tables** option to update the change in Fabric. You might need to review the report and downstream data flows to see that they aren't impacted by the change.
8. You can also **Unlink**, which removes the Fabric link to your Dataverse environment. When unlinking, the Fabric lakehouse is also removed.

> [!NOTE]
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
>
> - Select **Enable Parquet/Delta lake** to enable the view in Fabric.
> - Existing Azure Synapse Link for Dataverse profiles where the data is saved as CSV files can't be linked to Microsoft Fabric.
> - Azure Synapse Link profiles secured with managed identities, formerly Managed Service Identity (MSI), can't be linked to Microsoft Fabric at this point in time.  

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

## Secure data and grant access to other users

You must have the Systems Administrator security role in the Power Platform environment to enable **Link to Fabric** or **Synapse Link**. You must be an administrator of the Power BI workspace. If you want the system to create a Power BI workspace, you need to have Power BI Capacity Administrator access to a capacity within the same region as the Dataverse environment.

The system creates a data connection between the Power Apps environment and Fabric workspace using the credentials of the user at the time of link creation. If you use the **Fabric link** option from the Power Apps **Tables** area, the system creates the connection and asks you to save. If you use the **Synapse Link** option, you must create a data connection yourself before enabling the link.

The system uses this connection to enable Fabric users to connect to Dataverse - the data store behind the Power Platform environment. If you want to enable other users to add or remove tables to Fabric link, you need to share this data connection with other users. To share the data connection with other users:

1. Go to Fabric.Microsoft.com and select the gear icon on top left (next to user icon).
2. On the **Settings** menu, select **Data connections and Gateways**. The available data connections are displayed.
3. Select the **Connections** tab, and then choose the data connection you created with the connection type **Dataverse**. You might see a connection that is named like **org...crm.dynamics.com**. In case you have multiple connections like this, you need to select the connection that links to the specific Power Platform environment.
4. Once you select the correct data connection, select **...** > **manage users**. Then you're shown users who have access to this connection.
5. Enter the name or email of other users who need access to data. When you select a user, specify either the **Owner** role or **Reader** role. You only need to provide reader role to enable them to consume data. The users you specify receive an e-mail confirming access to data.

You might need to grant access to other users to this workspace so that they can work with data. Depending on the need for data access, you might need to secure the data in this workspace before you share this data with others. You can secure the lakehouse as well as tables within the lakehouse using OneLake security. More information: [OneLake security overview](/fabric/onelake/security/get-started-security)

## Troubleshooting common issues

If you experience an error message, here are suggestions to resolve the issue. 

| Error message                      | How to resolve                | 
|:-----------------------------------|:------------------------------|
| You must have Power BI premium or Fabric capacity in the same region {Region}. You can also get a Fabric trial. <br><br> You won't receive this error after April 30, 2024. Instead, you're shown an error if you don't have capacity in the same geography. | You need a Power BI premium of a Fabric capacity in the same region as your Dataverse environment. Power BI premium per user capacity isn't sufficient. You can get a free trial capacity by visiting [Fabric (preview) trial](/fabric/get-started/fabric-trial). <br> More information: [Prerequisites](#prerequisites)  | 
| Creation of Fabric workspace failed. You can try again. If this issue persists contact [Microsoft customer support](/power-platform/admin/get-help-support) with the corelation ID. | You must be a Power BI Capacity Administrator or have contributor access to a capacity within the same geography  as your Dataverse environment. <br> Currently, the system supports these premium capacity SKUs described in the [Prerequisites](#prerequisites). <br> Verify with your Power BI Tenant admin that you have permissions to create workspaces. You can find this setting in Power BI Admin portal under **Tenant settings > workspace settings > Create workspaces**. <br> If the issue isn't resolved, contact [Microsoft customer support](/power-platform/admin/get-help-support) with the provided reference ID |
| Creation of Fabric lakehouse failed. You can try again. If this issue persists contact [Microsoft customer support](/power-platform/admin/get-help-support) with the corelation ID. | Verify with your Power BI Tenant admin that you have permissions to create OneLake shortcuts. You can find this setting in Power BI Admin portal under  **Admin Portal > Tenant Settings > Microsoft Fabric > Users can create Fabric items**. <br> More information: [Prerequisites](#prerequisites) <br> If the issue isn't resolved after several retries, you can contact [Microsoft customer support](/power-platform/admin/get-help-support) with the provided reference ID. |
| We ran into an issue, Creaton of Fabric Lakehouse failed. | Verify with your Power BI tenant admin that you have permissions to create artifacts in Fabric. You can find this setting in Power BI admin portal under **Tenant settings > oneLake settings > Users can access data stored in OneLake with apps external to Fabric**. <br> More information: [Prerequisites](#prerequisites) <br> If the issue isn't resolved after several retries, you can contact [Microsoft customer support](/power-platform/admin/get-help-support) with the provided reference ID. |
| Your organization doesn't appear to have Microsoft Fabric. You can get a trial. | Contact your administrator or get a trial version of Microsoft Fabric. |
|You need to get a trial version of Fabric to get started. | You need a Power BI premium of a Fabric capacity. Power BI premium per user capacity isn't sufficient. You can get a free trial capacity by visiting: [Fabric (preview) trial](/fabric/get-started/fabric-trial) |
| You need to be a system administrator to link to Fabric. | You need the system administrator security role in Dataverse to perform this operation. More information: [Security roles and privileges](/power-platform/admin/security-roles-privileges)  |
| Newly added fields in tables aren't reflected in Fabric Lakehouse. | When a new field is added to a Dataverse table, the newly added column isn't added to Fabric Linked workspaces automatically. To include newly added columns, select **Synapse Link** in Power Apps (make.powerapps.com), select the Microsoft OneLake or the Azure Synapse Link profile and select **Refresh Fabric tables**. This action refreshes the table metadata in Fabric Lakehouse. |
| Error message "Unauthorized. Access to target location https://[...].crm3.dynamics.com/ denied" when accessing Dataverse tables in Fabric Lakehouse. | This error message indicates that the user accessing tables in Fabric doesn't have the required permissions to access Dataverse tables. This error might be shown even if the same user has access to the tables in Dataverse. <br> The Link to Fabric wizard in Power Apps creates a data connection at the time of creating the Link to Fabric. This data connection uses credentials of the user, it's possible that: <br> - The password of the user who created the connection has changed or has expired. <br> - The user account of the user who created the Fabric link is inactive. <br> - Other users who need to access Dataverse tables in Fabric Lakehouse don't have access to the data connection. More information: [Secure data and grant access to other users](#secure-data-and-grant-access-to-other-users) |
| Error message "A back end error occurred. The Fabric to Dataverse connection ID ... is not valid for this user. Please check that you have access to this connection, and that the connection is connected to this organization, with URL ... You can try again, if this issue persists please contact support. | This error message indicates that the user selecting the **Refresh Fabric tables** option in the Azure Synapse Link page doesn't have the required permissions. This error might be shown even when the user has access to the tables in Dataverse and is a system administrator. <br> The link to Fabric wizard in Power Apps creates a data connection at the time of creating the link to Fabric. This data connection uses credentials of the user, it's possible that: <br> - The password of the user who created the connection has changed or has expired. <br> - The user account of the user who created the Fabric link is inactive. <br> - The user performing the **Refresh Fabric tables** option doesn't have access to the data connection. More information: [Secure data and grant access to other users](#secure-data-and-grant-access-to-other-users) |
|All tables from Dataverse show as **Unidentified** in Fabric Lakehouse. | You might see this error message while your data is being initialized for the first time. If this issue persists for more than several hours, go to **Synapse Link** in Power Apps (make.powerapps.com), choose the Microsoft OneLake or the Azure Synapse Link profile and select **Refresh Fabric Links**. This refreshes the table metadata in Fabric Lakehouse. | 
| Tables from Dynamics 365 finance and operations apps are missing. | System auto selects nonsystem tables with **Change tracking** property set to **Yes** when creating a Fabric Link. To select more tables, open **Microsoft OneLake** profile in **Synapse Link** and select **Manage Tables**. If you have a finance and operations environment linked to this Power Platform environment, you can also select tables from finance and operations apps. Finance and operations apps tables aren't autoselected with Fabric Link. <br> More information: [Add Finance and Operations tables](/power-apps/maker/data-platform/azure-synapse-link-select-fno-data#add-finance-and-operations-tables-in-azure-synapse-link) |
| There are {.. #tables} tables enabled for change tracking in your environment. Addition of more than one thousand tables isn't supported. | Fabric link feature currently can't be enabled on environments with more than 1,000 change tracking enabled tables. <br> As a workaround, select **Synapse Link** in Power Apps (make.powerapps.com) and create multiple profiles with less than 1,000 tables each. |     

## See also

[Create virtual tables using the virtual connector provider](create-virtual-tables-using-connectors.md)
