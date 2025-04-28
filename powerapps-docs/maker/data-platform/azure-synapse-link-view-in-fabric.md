---
title: Link your Dataverse environment to Microsoft Fabric and unlock deep insights
description: Link your Microsoft Dataverse data from Power Apps and Dynamics 365 with Microsoft Fabric and unlock advanced insights.
author: MilindaV2
ms.author: Milindav
ms.reviewer: matp
ms.service: powerapps
ms.subservice: dataverse-maker
ms.topic: how-to
ms.date: 01/15/2025
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
> [!VIDEO https://learn-video.azurefd.net/vod/player?id=ddd288c6-e47a-4bc6-974b-4fe0f1a49362]

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

Once the link is set up, you can grant other users access to the Fabric workspace so that they can work with Dataverse data using all Fabric workloads. The lakehouse, SQL endpoint, and Power BI dataset are updated with new data as changes occur in Dataverse. More information: [Link to Microsoft Fabric](fabric-link-to-data-platform.md)

### Direct access to your data in Microsoft OneLake

Link to Fabric creates a direct and secure Link between your data in Dataverse and a Fabric workspace. There's no need to provide a storage account or Synapse workspaces. When you link to Fabric from Power Apps, the system creates an optimized replica of your data in delta parquet format, the native format of Fabric and OneLake, using Dataverse storage such that your operational workloads aren't impacted. This replica is governed and secured by Dataverse and stays within the same region as your Dataverse environment while enabling Fabric workloads to operate on this data.

Admins can manage tables linked to OneLake from the **Azure Synapse Link for Dataverse** page. By opening the **Microsoft OneLake** link, admins view tables added by makers, add more tables, and migrate the link to other environments. Tables added to OneLake consume Dataverse storage and admins can see storage consumption in the Power Platform admin center.

> [!NOTE]
>
> By selecting **Link to Microsoft Fabric**, the system adds all nonsystem Dataverse tables that have the **Track changes** property enabled. You can add more tables later.
>
> If you used this feature during public preview, you can continue to use the tables selected earlier. If you choose the **Link to Fabric** option in new environments (or unlink and relink existing environments), all tables are added.  
>
> Enabling this feature results in an increase in **Dataverse database** storage consumption. You can view additional storage consumption in the [environment storage capacity details view](/power-platform/admin/capacity-storage#environment-storage-capacity-details) in Power Platform admin center. For an example, you notice an additional file `Account-Analytics` if you selected the `Account` table for Fabric link. Also note that the chart only displays tables consuming hightest storage. You can get a list of tables using the menu on top right of the chart.

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

## Next steps

[Link to Microsoft Fabric](fabric-link-to-data-platform.md)
