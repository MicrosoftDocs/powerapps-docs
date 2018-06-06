---
title: "Import data (all record types) for Dynamics 365 Customer Engagement | MicrosoftDocs"
ms.custom: ""
ms.date: 10/30/2017
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
author: "jimholtz"
ms.assetid: 4483edc9-999d-4761-a9d1-d18fc130b615
caps.latest.revision: 19
ms.author: "rdubois"
manager: "brycho"
---
# Import data (all record types) from multiple sources

[!INCLUDE[cc-applies-to-update-9-0-0](../includes/cc_applies_to_update_9_0_0.md)]<br/>[!INCLUDE[cc-applies-to-update-8-2-0](../includes/cc_applies_to_update_8_2_0.md)]

Importing data is often the first important task that you need to perform after you have installed [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] Customer Engagement. You can import data from various [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] systems and data sources into standard and customized fields of most business and custom entities in [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)]. You can include related data, such as notes and attachments. To assure data integrity, you can enable duplicate detection that prevents importing duplicate records. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Detect duplicate data](https://docs.microsoft.com/dynamics365/customer-engagement/admin/detect-duplicate-data). For more complex data import scenarios, you can write code using the data import web service. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Import data using web services](https://docs.microsoft.com/dynamics365/customer-engagement/developer/import-data).
  
 Preliminary steps before you import the data into [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] Customer Engagement include:  
  
1.  Preparing source data files in one of the following formats: comma-separated values (.csv), XML Spreadsheet 2003 (.xml), Compressed (.zip) or text files. You can import data from one source file or several source files. A source file can contain data for one entity type or multiple entity types.  
  
2.  Preparing data maps for mapping data contained in the source file to the [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] record fields. You must map every column in the source file to an appropriate field. Unmapped data isn’t imported. [!INCLUDE[proc_more_information](../includes/proc-more-information.md)] [Select a data map](https://docs.microsoft.com/dynamics365/customer-engagement/basics/select-data-map)  
  
There are several ways to import data into [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)]:  
  
1.  To import large volumes of data, we recommend a programmatic way, as most efficient. When you import data programmatically, you gain additional capabilities that are not available when you use other methods of importing data. These advanced capabilities include viewing stored source data, accessing error logs and creating data maps that include complex transformation mapping, such as concatenation, split, and replace. 
  
2.  For smaller import jobs, you can use the Import Data Wizard tool included in the [!INCLUDE[pn_crm_shortest](../includes/pn-crm-shortest.md)] web application. For information about the Import Data Wizard or how to import specific record types, see [Import accounts, leads, or other data](https://docs.microsoft.com/dynamics365/customer-engagement/basics/import-accounts-leads-other-data).  
  
    > [!NOTE]
    >  For the Import Data Wizard, the maximum file size for .zip files is 32 MB; for the other file formats, it’s 8 MB.  
    >   
    >  With the Import Data Wizard, you can specify the “Map Automatically” option. The wizard automatically maps all the files and the column headings with [!INCLUDE[pn_dynamics_crm](../includes/pn-dynamics-crm.md)] record types and fields if:  
    >   
    >  -   The file names exactly match the display name of the record type.  
    > -   The column headings of the file you are importing exactly match the display names of the fields in the record.  
  
3.  To add data for an individual record, the quickest way is to use **Quick Create** from the nav bar or **New** from the entity form.  
  
### See also  
 [Detect duplicate data](https://docs.microsoft.com/dynamics365/customer-engagement/admin/detect-duplicate-data)
