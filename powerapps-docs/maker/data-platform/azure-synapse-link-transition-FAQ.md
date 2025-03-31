---
title: Frequently asked questions when transitioning from legacy data integration services to Fabric link and Azure Synapse Link for Dataverse
description: Learn how to transition from export to data lake, BYOD, and data export service to link to Microsoft Fabric and Azure Synapse Link for Microsoft Dataverse.
ms.date: 03/31/2025
ms.reviewer: matp 
ms.topic: "how-to"
applies_to: 
  - "powerapps"
author: Milindav
ms.subservice: dataverse-maker
ms.author: Milindav
search.audienceType: 
  - maker
ms.custom: bap-template
---
# Frequently asked questions when transitioning from legacy data integration services

This article discusses the frequently asked questions with transition from legacy data integration services to Fabric link or Azure Synapse Link for Dataverse.

Data export service, [bring your own database (BYOD)](/dynamics365/fin-ops-core/dev-itpro/analytics/export-entities-to-your-own-database), and [export to data lake](/dynamics365/fin-ops-core/dev-itpro/data-entities/azure-data-lake-ga-version-overview) were features introduced in Dynamics 365 apps to export data for analytics and data integration scenarios. These services enabled IT admins and specialists to export data into external databases or data lakes and build data integration pipelines. While we improved these services over the years with updates, as part of unification of Dynamics 365 with the Power Platform, the same capabilities are rearchitected for these disparate services into simpler, unified experiences built into Power Apps (make.powerapps.com). The unified and improved service is called link to Azure Synapse. 

Also available is a service named link to Microsoft Fabric where you can directly integrate Microsoft Dataverse, the data platform behind Dynamics 365 as well as Power Apps with Microsoft Fabric with no-copy, no-ETL required. Whether you link to Microsoft Fabric or upgrade to Azure Synapse Link, the rearchitected services provide you with an easy ramp to benefit from AI and Copilot investments in Dataverse and Fabric.

## What is the difference between Link to Azure Synapse and link to Fabric?

Link to Azure Synapse and link to Fabric services are built into Dataverse, the platform powering Power Apps and all Dynamics 365 products.

Azure Synapse Link continuously exports data from Dynamics 365 and Power Apps to your own storage account, allowing IT professionals to build and manage data integration pipelines with Azure Synapse Analytics as well as other tools.

In contrast, link to Fabric offers a no-copy, no-ETL integration directly with Microsoft Fabric, keeping data within the Dataverse governance boundary for enhanced security. Fabric Link uses Dataverse managed storage, removing the need to configure and manage your own storage. When using link to Fabric, you might notice an increase in Dataverse storage consumption.

Both these services operate across PowerApps, Dynamics 365 customer engagement apps like Dynamics 365 Sales, Dynamics 365 Customer Service, as well as Dynamics 365 finance and operations apps.

| Link to Fabric  |  Azure Synapse Link |
|-------------------------------|------------------------------------|
| No copy, no extract, transform, load (ETL) direct integration with Fabric. | Export data to your own storage account and integrate with Azure Synapse, Fabric, and other tools. |
| Data stays in Dataverse. Users get secure access in Microsoft Fabric. | Data stays in your own storage. You manage access to users.|
| All tables chosen by default.| System administrators can choose required tables. |
| Consumes additional Dataverse storage.| Consumes your own storage and other compute and integration tools.|

## What option should I consider if I want to use Microsoft Fabric?

Fabric Link provides a seamless, no-copy integration with Dataverse and Microsoft Fabric, eliminating the need to manage complex data export processes. With link to Microsoft Fabric, your data stays securely within your Dataverse environment, while authorized users in Microsoft Fabric can access the data, making it easier for your team to leverage data for insights without the hassle of managing separate storage and integration solutions. This streamlined approach can lead to cost savings and more efficient data utilization, especially if you’re already using Power BI. [Go to this article](/powerapps-docs/maker/data-platform/azure-synapse-link-transition-from-FnO.md#Simplification with Fabric link) for a comparison of total cost of ownership (TCO) between link to Microsoft Fabric and link to Azure Synapse. 

Using the [Fabric Link transition tool provided by Dynamics 365 FastTrack team](https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets/tree/master/Analytics/DataverseLink/FabricLink_SQLAnalyticsEndpoint), you can create a Fabric data warehouse with the same data shapes as export to data lake feature and minimize the effort to transition your existing reports and data pipelines.

## What option should I consider if I want to keep the data export solution?

Upgrading from export to data lake to Azure Synapse Link enables you to preserve your investments with minimal changes. While Azure Synapse Link simplifies data integration by continuously exporting data in a more efficient Delta Parquet format, it provides similar outputs as export to data lake service therefore reducing the effort to switch. You can use Power BI, Microsoft Fabric as well as many non-Microsoft tools that support Delta Parquet format to work with your Dynamics 365 data. You can also secure your storage account with firewalls and enable restricted access via managed identities, ensuring secure data access and compliance. [Go to this article](/power-apps/maker/data-platform/azure-synapse-link-transition-from-fno#example-2-upgrade-to-azure-synapse-link) for a comparison of total cost of ownership (TCO) between link to Fabric and link to Azure Synapse.

Using the [Synapse Link transition tool provided by Dynamics 365 FastTrack team](https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets/tree/master/Analytics/DataverseLink/VirtualDatawarehouse) you can create a Synapse workspace with similar data shapes as export to data lake feature and reduce the effort to transition your existing reports and data pipelines.

## We don’t use Power BI or Fabric with Dynamics 365 data, can I extract change data?

If you use Power BI or Microsoft Fabric to gain insights from your Dynamics 365 or Power Apps data, Fabric Link provides the most benefits while simplifying data integration efforts. However, if you're using non-Microsoft tools and/or use export to data lake change feeds to incrementally export data to your downstream data warehouse, you can use Synapse Link incremental data exports instead. [More information](/power-apps/maker/data-platform/azure-synapse-link-transition-from-fno#understanding-benefits--more-real-time-reporting)

Using the [The Data integration tool provided by Dynamics 365 FastTrack team](https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets/tree/master/Analytics/DataverseLink/DataIntegration) you can create a pipeline to incrementally copy change data into an Azure SQL database, Synapse dedicated pool or an on-premises database.

## Are there differences in columns/schema between Export to Data Lake and Fabric Link or Synapse Link?

Fabric Link and Synapse Link represent a unification of legacy services built into Dynamics 365. The same capabilities are rearchitected to transform these disparate services into simpler, unified experiences built into Power Apps (make.powerapps.com). In the process, to avoid conflicts, minor changes are made to the schema. The underlying data engine behind Fabric Link and Synapse Link is the same so the changes apply both to Fabric Link and Synapse Link options:

- Renaming SQL reserved words such as `Level_, Resource_`.
- ID field in export to data lake tables become `FnO_Id`.
- Deleted rows are included. For example, Synapse Link and Fabric Link perform what is referred to as a "soft delete." You can use the `isDelete` flag to identify deleted rows and remove them.
- TimeZoneID (TZID) fields are removed because these are legacy fields no longer used in finance and operations apps.
- Fields that contain binary data are removed.
- `nVarChar(max)` fields are included but data is truncated at 2,000 characters.

For more information, go to [working with Finance and Operations data and metadata](/power-apps/maker/data-platform/azure-synapse-link-select-fno-data#working-with-data-and-metadata).

Using the [Fabric Link transition tool provided by Dynamics 365 FastTrack team](https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets/tree/master/Analytics/DataverseLink/FabricLink_SQLAnalyticsEndpoint), you can create a Fabric data warehouse with the same data shapes as export to data lake feature and minimize the effort to transition your existing reports and data pipelines.

Using the [Synapse Link transition tool provided by Dynamics 365 FastTrack team](https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets/tree/master/Analytics/DataverseLink/VirtualDatawarehouse) you can create a Synapse workspace with similar data shapes as export to data lake feature and reduce the effort to transition your existing reports and data pipelines.

Using the [data integration tools provided by Dynamics 365 FastTrack team](https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets/tree/master/Analytics/DataverseLink/DataIntegration) you can create a pipeline to incrementally copy change data into an Azure SQL database, Synapse dedicated pool or an on-premises database.

## Why are all Dataverse tables auto selected with Fabric Link, why can’t I select only the Dataverse tables I need?

By selecting **Link to Microsoft Fabric**, the system adds all nonsystem Dataverse tables that have the **Track changes** property enabled. You can’t remove these tables as some of these tables might be used by Dynamics 365 as well as partner applications and removing them can cause the applications to fail.

Enabling link to Fabric feature (or a Dynamics 365 application that contains insights features) might result in an increase in Dataverse database storage consumption. You can view additional storage consumption as additional files in the environment storage capacity details view in the Power Platform admin center. For example, you might notice an additional file "Account-Analytics" if you selected the "Account" table for Fabric link. Also note that the chart only displays tables consuming highest storage. You can get a list of tables using the menu on top right of the chart.

## Export to data lake service is working well for us. Why did you retire these services?

As part of the Dynamics 365 platform unification project, we consolidated several services that “exported data” in Dynamics 365 applications to a single service under the brand name Synapse Link for Dataverse. Using our learnings, many shortcomings of existing services were addressed in Synapse Link while maintaining same data formats – so that you can upgrade your investments with minimal disruptions. Fabric link service is a new, no-copy, no-ETL solution, which enables you to leverage innovations in Fabric without having to invest in data pipelines. It’s a “read-replica” of your data for authorized users in Fabric.

## Why can't I find some Tables and Entities from Finance and Operations in tables in Link to Fabric or Link to Azure Synapse  

Azure Synapse Link or Fabric link enables tables where the "change tracking" property is enabled. Currently, change tracking can't be enabled for all finance and operations entities. The **Track changes** option is unavailable for entities created in finance and operations in the past for data migration. In some entities, enabling change tracking might fail with the error message **chosen entity doesn't pass the validation rules** or the **Track changes** checkbox is disabled for some entities.

For more information about entity validation rules and how you can fix them, go to [Enable row version change tracking for data entities](/dynamics365/fin-ops-core/dev-itpro/data-entities/rowversion-change-track#enable-row-version-change-tracking-for-data-entities). You might need developer assistance to complete the steps. If the chosen entity is unavailable because of the change tracking limitation, choose the tables that comprise the data from that entity. 

You can use the [EntityUtil](https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets/tree/master/Analytics/DataverseLink/DataIntegration/EntityUtil) solution provided by the FastTrack team to create entity shapes using tables.

## Is BYOD service retired? Is there a retirement date?

As part of the Dynamics 365 platform unification project, several services that exported data in Dynamics 365 applications are consolidated. [BYOD](/dynamics365/fin-ops-core/dev-itpro/analytics/export-entities-to-your-own-database) is a service that exports entity data into a customers own Azure SQL database. While a retirement date for BYOD service hasn't been determined, we recommend that you transition to Synapse Link or Fabric link services. Fabric link service is a new, no-copy, no-ETL solution, which enables you to query your data with SQL similar to a “read-replica” of your data in Fabric.

### Will you retire Synapse Link in the future?

As part of the platform unification project, we have consolidated several services that exported data in Dynamics 365 applications to a service under the brand name Synapse Link for Dataverse. Fabric link, a no-copy, no-ETL solution, which enables you to leverage innovations in Fabric without having to invest in data pipelines is also available. Link to Fabric is a “read-replica” of your data for authorized users in Fabric. 

While many customers are excited to adopt Fabric, we also understand some customers want to continue to export data and build their own integration pipelines. As such, we want to enable you to export data well into the future.

## Will export to data lake service stop since it's deprecated after November 1, 2024?

Export to data lake service is deprecated as of November 1, 2024 and support will be limited. You can reduce the risk by beginning the transition process now. We plan to decommission export to data lake service beginning March 25, 2025 as customers transition to Synapse Link and Fabric link services. We plan to start the decommissioning process with customers who have completed the transition as well as customers who aren't actively using the service. You'll be notified before the decommission process begins and have the option to ask for a past due extension via the link [aka.ms/SynapseLinkPastDue](https://aka.ms/SynapseLinkPastDue).

## My transition might run beyond deprecation date, is there a process to get an extension?

Export to data lake service is deprecated as of November 1, 2024, but will continue to operate under limited support until March 25, 2025. If you haven't done so already, you should begin the transition process now.

To help customers who might need more time to complete their transition, we introduced an in-product “past due extend” option. You can apply for a one-time “past due extension” by taking the survey the Azure Synapse Link area in Power Apps (make.powerapps.com) or the link [aka.ms/SynapseLinkPastDue](https://aka.ms/SynapseLinkPastDue). This option is available only to customers who are currently validating either Synapse Link or Fabric Link services.

If a past due extension is approved, you receive a confirmation e-mail and the extended date is shown within the product. You can join the community and stay in touch via the forum or weekly office hours at [aka.ms/SynapseLinkforDynamics](https://aka.ms/SynapseLinkforDynamics).

## I have completed the transition, how can I uninstall export to data lake feature?

If you aren't using this feature in your environment, ask your finance and operations apps administrator to uninstall this feature. To uninstall, visit the environment page in life cycle services (LCS), navigate to the **Environment Add-ins** section, and then select the **Uninstall** option in the **Export to Data lake** environment add-in.

## Related articles

[What is Azure Synapse Link for Dataverse?](export-to-data-lake.md)

[Link your Dataverse environment to Microsoft Fabric and unlock deep insights](azure-synapse-link-view-in-fabric.md)
