---
title: Frequently asked questions when transitioning from legacy data integration services to Fabric link and Azure Synapse Link for Dataverse
description: Learn how to transition from Export to Data Lake, BYOD, and data export service to link to Microsoft Fabric and Azure Synapse Link for Microsoft Dataverse.
ms.date: 29/03/2025
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

## Frequently asked questions

### Transition from legacy data integration services
Data export service, [bring your own database (BYOD)](/dynamics365/fin-ops-core/dev-itpro/analytics/export-entities-to-your-own-database), and [Export to Data Lake](/dynamics365/fin-ops-core/dev-itpro/data-entities/azure-data-lake-ga-version-overview) were features introduced in Dynamics 365 apps to export data for analytics and data integration scenarios. These services enabled IT admins and specialists to export data into external databases or data lakes and build data integration pipelines. While we improved these services over the years with updates, as part of unification of Dynamics 365 with the power platform, we rearchitected the same capabilities of these disparate services into simpler, unified experiences built into Power Apps (make.powerapps.com). The unified (and improved) service is called Link to Azure Synapse. 

We have also introduced a new service namely, Link to Microsoft Fabric where you can directly integrate Dataverse, the data platform behind Dynamics 365 as well as Power Apps with Microsoft Fabric with no-xopy, no-ETL required. Whether you Link to Microsoft Fabric or upgrade to Azure Synapse Link, the rearchitected services provide you with an easy ramp to benefit from AI and Copilot investments in Microsoft Dataverse and Fabric.

### What is the difference between Link to Fabric and Link to Azure Synapse  
Link to Azure synapse and Link to Fabric services are built into Dataverse, the platform powering PowerApps and all Dynamics products.

Azure Synapse Link continuously exports data from Dynamics 365 and PowerApps to your own storage account, allowing IT professionals to build and manage data integration pipelines with Azure Synapse Analytics as well as other tools. 

In contrast, Link to Fabric offers a no-copy, no-ETL integration directly with Microsoft Fabric, keeping data within the Dataverse governance boundary for enhanced security. Fabric Link leverages Dataverse managed storage, removing the need to configure and manage your own storage. You may notice an increase in Dataverse storage consumption.

Both these services operate across PowerApps, Dynamics 365 customer engagement apps like Sales, Service as well as Dynamics 365 ERP.

| Link to Fabric  |  Azure Synapse Link |
|-------------------------------|------------------------------------|
| No copy, no ETL direct integration with Fabric. | Export data to your own storage account and integrate with Azure Synapse, Fabric, and other tools. |
| Data stays in Dataverse. Users get secure access in Microsoft Fabric. | Data stays in your own storage. You manage access to users.|
| All tables chosen by default.| System administrators can choose required tables. |
| Consumes additional Dataverse storage.| Consumes your own storage and other compute and integration tools.|

### What option should I consider if I want to use Microsoft Fabric 
Fabric Link provides a seamless, no-copy integration with Dataverse and Microsoft Fabric, eliminating the need to manage complex data export processes. With Fabric Link, your data stays securely within the your Dataverse environment, while authorized users in Microsoft Fabric can access the data, making it easier for your team to leverage data for insights without the hassle of managing separate storage and integration solutions. This streamlined approach can lead to cost savings and more efficient data utilization, especially if you’re already using Power BI. [See this document](/powerapps-docs/maker/data-platform/azure-synapse-link-transition-from-FnO.md#Simplification with Fabric link) for a comparison of Total Cost of Ownership (TCO) between Link to Fabric and Link to Azure Synapse. 

Using Fabric Link transition tool provided by [Dynamics 365 Fast track team](https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets/tree/master/Analytics/DataverseLink/FabricLink_SQLAnalyticsEndpoint), you can create a Fabric Data warehouse with the same data shapes as Export to Data lake feature and minimize the effort to transition your existing reports and data pipelines. 

### What option should I consider if I want to keep the data export solution? 
Upgrading from Export to Data Lake to Azure Synapse Link enables you to preserve your investments with minimal changes.  While Azure Synapse Link simplifies data integration by continuously exporting data in a more efficient Delta Parquet format, it provides similar outputs as Export to Data lake service thereby reducing the effort to switch. You can use Power BI, Microsoft Fabric as well as many third party tools that support Delta parquet format to work with your Dynamics 365 data. You can also secure your storage account with firewalls and enable restricted access via managed identities, ensuring secure data access and compliance. [See this document](/powerapps-docs/maker/data-platform/azure-synapse-link-transition-from-FnO.md#Upgrading to Azure Synapse Link) for a comparison of Total Cost of Ownership (TCO) between Link to Fabric and Link to Azure Synapse

Using Synapse Link transition tool provided by [Dynamics 365 Fast track team](https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets/tree/master/Analytics/DataverseLink/VirtualDatawarehouse) you can create a Synapse workspace with similar data shapes as Export to data lake feature and reduce the effort to transition your existing reports and data pipelines. 

### We don’t use Power BI or Fabric with Dynamics 365 data, can I extract change data? 
If you use Power BI or Microsoft Fabric to gain insights from your Dynamics 365 or Power Apps data, Fabric Link provides most benefits while simplifying data integration efforts. However, if you are using third party tools and/or use Export to Data lake change feeds to incrementally export data to your downstream data warehouse, you can use Synapse Link incremental data exports instead. [See this document for more details](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/azure-synapse-link-transition-from-fno#understanding-benefits--more-real-time-reporting)

Using Data integration tools provided by [Dynamics 365 Fast track team](https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets/tree/master/Analytics/DataverseLink/DataIntegration) you can create a pipeline to incrementally copy change data into a Azure SQL database, Synapse dedicated pool or an on-premise database. 

### Are there differences in columns/schema between Export to Data Lake and Fabric Link or Synapse Link?
Fabric Link and Synapse Link represent a unification of legacy services built into Dynamics 365. We rearchitected the same capabilities of these disparate services into simpler, unified experiences built into Power Apps (make.powerapps.com). In the process, to avoid conflicts, we had to make minor changes to schema. The underlying data engine behind Fabric Link and Synapse Link is the same these changes apply both to Fabric Link and Synapse Link options. 
-	Renaming SQL reserved words such as Level_, Resource_  
-	Id field in Export to Data lake tables become FnO_Id 
-	Deleted rows are included, ie. Synapse Link and Fabric Link perform what is referred to as a “soft delete”. You can use the isDelete flag to identify deleted rows and remove them.
-	TimeZoneID (TZID) fields are removed (these are legacy fields no longer used in Finance and Operations)
-	Fields that contain Binary data are removed 
-	nVarChar(max) fields are included but data is truncated at 2000 characters.

For more information, see [working data and metadata](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/azure-synapse-link-select-fno-data#working-with-data-and-metadata) 

Using [Fabric Link transition tool provided by Dynamics 365 Fast track team](https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets/tree/master/Analytics/DataverseLink/FabricLink_SQLAnalyticsEndpoint), you can create a Fabric Data warehouse with the same data shapes as Export to Data lake feature and minimize the effort to transition your existing reports and data pipelines. 

Using [Synapse Link transition tool provided by Dynamics 365 Fast track team](https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets/tree/master/Analytics/DataverseLink/VirtualDatawarehouse) you can create a Synapse workspace with similar data shapes as Export to data lake feature and reduce the effort to transition your existing reports and data pipelines. 

Using [Data integration tools provided by Dynamics 365 Fast track team](https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets/tree/master/Analytics/DataverseLink/DataIntegration) you can create a pipeline to incrementally copy change data into a Azure SQL database, Synapse dedicated pool or an on-premise database. 

### Why are all Dataverse tables auto selected with Fabric Link, why can’t I select only the Dataverse tables I need?
By selecting Link to Microsoft Fabric, the system adds all non-System Dataverse tables that have the "Track changes" property enabled. You can’t remove these tables as some of these tables may be used by Dynamics 365 as well as partner applications and removing them may cause the applications to fail.

Enabling Link to Fabric feature (or a Dynamics 365 application that contains insights features) may result in an increase in Dataverse database storage consumption. You can view additional storage consumption as additional files in the environment storage capacity details view in Power Platform admin center. For an example, you notice an additional file "Account-Amalytics" if you selected the "Account" table for Fabric link. Also note that the chart only displays tables consuming hightest storage. You can get a list of tables using the menu on top right of the chart.


### Export to data lake service is working well for us. Why did you retire these services?

As part of the Dynamics 365 platform unification project, we have consolidated several services that “exported data” in Dynamics 365 applications to a single service under the brand name Synapse Link for Dataverse. Using our learnings, we addressed many shortcomings of existing services in Synapse Link while maintaining same data formats – so that you can upgrade your investments with minimal disruptions. Fabric link service is a new, no-copy, no-ETL solution, which enables you to leverage innovations in Fabric without having to invest in data pipelines. It’s a “read-replica” of your data for authorized users in Fabric.


### Why can't I find some Tables and Entities from Finance and Operations in tables in Link to Fabric or Link to Azure Synapse  

Azure Synapse Link or Fabric link enables tables where the "change tracking" property is enabled. Currently, change tracking can't be enabled for all finance and operations entities. The **Track changes** option is unavailable for entities created in finance and operations in the past for data migration. In some entities, enabling change tracking might fail with the error message **chosen entity doesn't pass the validation rules** or the **Track changes** checkbox is disabled for some entities. 

For more information about entity validation rules and how you can fix them, go to [Enable row version change tracking for data entities](/dynamics365/fin-ops-core/dev-itpro/data-entities/rowversion-change-track#enable-row-version-change-tracking-for-data-entities). You might need developer assistance to complete the steps. If the chosen entity is unavailable because of the change tracking limitation, choose the tables that comprise the data from that entity. <br> You can use [EntityUtil](https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets/tree/master/Analytics/DataverseLink/DataIntegration/EntityUtil) solution provided by the FastTrack team to create entity shapes using tables.


### Is BYOD service retired? Is there a retirement date? 

As part of the Dynamics 365 platform unification project, we have consolidated several services that “exported data” in Dynamics 365 applications. [BYOD](/dynamics365/fin-ops-core/dev-itpro/analytics/export-entities-to-your-own-database) is a service that exports entity data into customers own Azure SQL database. While we haven't yet announced a retirement date for BYOD service, our guidance is to transition to Synapse Link or Fabric link services. Fabric link service is a new, no-copy, no-ETL solution, which enables you to query your data with SQL similar to a “read-replica” of your data in Fabric.

### Will you retire Synapse Link in the future?

As part of the platform unification project, we have consolidated several services that “exported data” in Dynamics 365 applications to a service under the brand name Synapse Link for Dataverse. We have also introduced Fabric link, a no-copy, no-ETL solution, which enables you to leverage innovations in Fabric without having to invest in data pipelines. It’s a “read-replica” of your data for authorized users in Fabric. 

While many customers are excited to adopt Fabric, we also understand some customers want to continue to export data and build their own integration pipelines. We do want to enable them to export data well into the future.

### Will export to data lake service stop since it's deprecated after November 1, 2024?

Export to data lake service is deprecated as of November 1, 2025 and our support will be limited. You can reduce the risk by beginning the transition process now. We plan to decommission export to data lake service beginning March 25, 2025 as customers transition to Synapse Link and Fabric link services. We plan to start the decommissioning process with customers who have completed the transition as well as customers who are not actively using the service. You will be notified before the decommission process begins and you will have the option to ask for a past due extension via the link [aka.ms/SynapseLinkPastDue](https://aka.ms/SynapseLinkPastDue).

### My transition might run beyond deprecation date, is there a process to get an extension?

Export to data lake service is deprecated as of November 1, 2024, but will continue to operate under limited support until March 25, 2025. If you haven't done so already, you should begin the transition process now.

To help customers who might need more time to complete their transition, we have introduced an in-product “past due extend” option. You can apply for a one-time “past due extension” by taking the survey the Azure Synapse Link area in Power Apps (make.powerapps.com) or the link [aka.ms/SynapseLinkPastDue](https://aka.ms/SynapseLinkPastDue). This option is available only to customers who are currently validating either Synapse Link or Fabric Link services.

If a past due extension is approved, you will receive a confirmation e-mail and the extended date will be shown within the product. You can join the community and stay in touch via the forum or weekly office hours at aka.ms/SynapseLinkforDynamics

### I have completed the transition, how can I uninstall "export to data lake" feature? 

If you aren't using this feature in your environment, ask your finance and operations apps administrator to uninstall this feature. To uninstall, visit the environment page in life cycle services (LCS), navigate to the **Environment Add-ins** section, and then select the **Uninstall** option in the **Export to Data lake** environment add-in.

