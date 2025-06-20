---
title: "Data import tables (Microsoft Dataverse) | Microsoft Docs" 
description: "Lists the data import tables used to create data maps, configure and run data imports, and log failure information." 
ms.date: 08/03/2022
ms.reviewer: pehecke
ms.topic: article
author: mayadumesh 
ms.subservice: dataverse-developer
ms.author: mayadu
search.audienceType: 
  - developer
---
# Data import tables

The Microsoft Dataverse data import tables are used to create data maps, configure and run data imports, and log failure information.  

The following table lists the tables that are used to configure, run, and log failures for import operations.  

|Table|Description|  
|----------------------------------|-----------------|  
|[Data Import (Import)](reference/entities/import.md)|Status and ownership information for the import job.|  
|[Import Source File (ImportFile)](reference/entities/importfile.md)|Logical source file.|  
|[ImportLog](reference/entities/importlog.md)|Failure reason and other detailed information for a record that failed to import.|  

 The following table lists the tables that are used for creating data maps.  

|Table|Description|
|-----|-----|
|[Data Map (ImportMap)](reference/entities/importmap.md)|Data map that is used for import.|
|[ColumnMapping](reference/entities/columnmapping.md)|Mapping between a column in the source file and a target column in Dataverse.|
|[LookUpMapping](reference/entities/lookupmapping.md)|Mapping between a column in the source file, or an output of a complex transformation and a target column of type <xref:Microsoft.Xrm.Sdk.EntityReference>. Used in conjunction with column mapping or complex transformation mapping.|
|[OwnerMapping](reference/entities/ownermapping.md)|Mapping between a user specified in the source file and a user in Dataverse.                                                             |
|[List Value Mapping (PickListMapping)](reference/entities/picklistmapping.md)|Mapping between a column in the source file and a target column of <xref:Microsoft.Xrm.Sdk.OptionSetValue>, Boolean, state, or status type in Dataverse. Used in conjunction with column mapping. |
|[TransformationMapping](reference/entities/transformationmapping.md)|Complex transformation mapping.|
|[TransformationParameterMapping](reference/entities/transformationparametermapping.md)| Parameter mapping that is used in complex transformation mapping.|

### See also

[Import data](import-data.md)<br />
[Create data maps for import](create-data-maps-for-import.md)<br />
[Add transformation mappings for import](add-transformation-mappings-import.md)<br />
[Configure data import](configure-data-import.md)<br />
[Run data import](run-data-import.md)<br />
[Sample: Export and import a data map](org-service/samples/export-import-data-map.md)<br />
[Sample: Import data using complex data map](org-service/samples/import-data-complex-data-map.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
