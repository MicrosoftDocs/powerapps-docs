---
title: "Data import entities (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Lists the data import entities used to create data maps, configure and run data imports, and log failure information." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Data import entities

The Common Data Service for Apps data import entities are used to create data maps, configure and run data imports, and log failure information.  

 The following table lists the entities that are used to configure, run, and log failures for import operations.  

|Entity name (display name)|Description|  
|----------------------------------|-----------------|  
|import (data import)|Status and ownership information for the import job.|  
|importfile (import source file)|Logical source file.|  
|importlog (import log)|Failure reason and other detailed information for a record that failed to import.|  

 The following table lists the entities that are used for creating data maps.  


|                    Entity name (display name)                     |                                                                                                                      Description                                                                                                                       |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                       importmap (data map)                        |                                                                                                           Data map that is used for import.                                                                                                            |
|                  columnmapping (column mapping)                   |                                                           Mapping between a column in the source file and a target attribute in CDS for Apps.                                                           |
|                  lookupmapping (lookup mapping)                   |       Mapping between a column in the source file, or an output of a complex transformation and a target attribute of type <xref:Microsoft.Xrm.Sdk.EntityReference>. Used in conjunction with column mapping or complex transformation mapping.        |
|                   ownermapping (owner mapping)                    |                                                             Mapping between a user specified in the source file and a user in CDS for Apps.                                                             |
|                picklistmapping (picklist mapping)                 | Mapping between a column in the source file and a target attribute of <xref:Microsoft.Xrm.Sdk.OptionSetValue>, Boolean, state, or status type in CDS for Apps. Used in conjunction with column mapping. |
|          transformationmapping (transformation mapping)           |                                                                                                            Complex transformation mapping.                                                                                                             |
| transformationparametermapping (transformation parameter mapping) |                                                                                           Parameter mapping that is used in complex transformation mapping.                                                                                            |

### See also  
 [Import Data in Dynamics 365](import-data.md)   
 [Import Entity](reference/entities/import.md)   
 [ImportFile Entity](reference/entities/importfile.md)   
 [ImportLog Entity](reference/entities/importlog.md)   
 [ImportMap Entity](reference/entities/importmap.md)   
 <!-- jdaly These links will have content when we re-gen docs after bug 689487 is checked in. START -->
 [ColumnMapping Entity](reference/entities/columnmapping.md)   
 [LookupMapping Entity](reference/entities/lookupmapping.md)   
 [OwnerMapping Entity](reference/entities/ownermapping.md)   
 [PicklistMapping Entity](reference/entities/picklistmapping.md)   
 [TransformationMapping Entity](reference/entities/transformationmapping.md)    
 [TransformationParameterMapping Entity](reference/entities/transformationparametermapping.md)   
 <!-- jdaly These links will have content  when we re-gen docs after bug 689487 is checked in. END -->
 [Sample: Export and Import a Data Map](/dynamics365/customer-engagement/developer/sample-export-import-data-map)   
 [Create data maps for import](create-data-maps-for-import.md)<br />
 [Add transformation mappings for import](add-transformation-mappings-import.md)<br />
 [Configure data import](configure-data-import.md)<br />
 [Run data import](run-data-import.md)<br />
 [Sample: Export and import a data map](/dynamics365/customer-engagement/developer/org-service/samples/export-import-data-map)<br />
 [Sample: Import data using complex data map](/dynamics365/customer-engagement/developer/org-service/samples/import-data-complex-data-map)<br />