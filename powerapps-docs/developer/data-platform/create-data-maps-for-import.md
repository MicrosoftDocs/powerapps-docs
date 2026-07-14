---
title: "Create data maps for import (Microsoft Dataverse) | Microsoft Docs"
description: "Data maps are required to import data, and contain mappings between the data contained in the source file and the respective table columns." 
ms.date: 08/03/2022
ms.reviewer: pehecke
ms.topic: article
author: mayadumesh # GitHub ID
ms.subservice: dataverse-developer
ms.author: mayadu # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
---
# Create data maps for import

To import data into Microsoft Dataverse, you must provide the appropriate data maps.  
  
 You can download examples of data maps from [Microsoft Downloads: DataImportMaps.zip](https://download.microsoft.com/download/D/5/F/D5F73E15-439B-4EBC-BFFB-C6837B146C76/DataImportMaps.zip).
  
 You use data maps to map the data contained in the source file to the Dataverse table columns. You must map every column in the source file to an appropriate column. The data in the unmapped columns is not imported during the data import operation.  
  
 The data map is represented by the [Data Map (ImportMap)](reference/entities/importmap.md) table. You can create a new map by creating new records of this table. The map has a unique name that is contained in the `ImportMap.Name` column. You can specify the name of the import source for which this data map is created by using the `ImportMap.Source` column.  
  
<a name="BKMK_Column"></a>   

## Column, list value, and lookup mappings

To map a column, a list value, or lookup value in the source file to a Dataverse column, use the following mappings:  
  
 **Column Mapping**  
  
Maps a column in a source file to a Dataverse column. For column mapping, use the [ColumnMapping](reference/entities/columnmapping.md) table. You can use 1:1 (one-to-one) or 1:N (one-to-many) relationships between source and target columns. For example, you can map account address information to the billing and shipping addresses in an order.  
  
 **List Value Mapping**  
  
Maps a list value in a source file to a Dataverse column of the <xref:Microsoft.Xrm.Sdk.OptionSetValue> type. For list value mapping, use the [List Value Mapping (PickListMapping)](reference/entities/picklistmapping.md) table.  
  
 If a value specified in the source file column is a list value, such as an OptionSetValue, Status, State, and Boolean, you must provide a list value mapping additionally to a column mapping. For example, map the "bill" and "ship" list values in the source file to the bill and ship values of the <xref:Microsoft.Xrm.Sdk.OptionSetValue> type.  
  
 **Lookup Mapping**
  
 Maps a lookup value in a source file to a Dataverse column of the <xref:Microsoft.Xrm.Sdk.EntityReference> type. For lookup mapping, use the [LookUpMapping](reference/entities/lookupmapping.md) table.  
  
 If the value specified in the source file references a table, you must provide a lookup mapping for this value. Use the `LookupMapping.LookupSourceCode` column to specify whether to search for the referenced table inside the source file or inside Dataverse. If you are using early bound types, you can use the `LookupSourceType` enumeration to set the lookup values. To search inside the source file, use the `LookupSourceType.Source` value. To search inside Dataverse, use the `LookupSourceType.System` value. For a list of the LookupSourceCode values, see the choice values for this table. To view the metadata for your organization, install the Metadata Browser solution described in [Browse table definitions in your environment](browse-your-metadata.md). You can also browse the reference documentation for tables in the [Table Reference](reference/about-entity-reference.md). You can provide multiple lookup mappings. The asynchronous transformation job processes all available mappings. It finds the referenced records and updates the parse table with the record unique identifiers. For more information, see [Run Data Import](run-data-import.md).  
  
<a name="BKMK_Owner"></a>

## Owner mapping

 Use owner mapping to map a user specified in the source file to a user in Dataverse. For logging information, use the Dataverse user logon name. For owner mapping, use the [OwnerMapping](reference/entities/ownermapping.md) table.  
  
<a name="BKMK_Notes"></a>

## Notes and attachments

 Mapping for notes and attachments is handled differently from other tables. Notes and attachments are used to append additional information to a record in Dataverse. Notes are stored as text and attachments are stored as files in the Dataverse database.  
  
 To create a note in Dataverse, set the `Annotation.IsDocument` column in the annotation (note) table to `false`. To create an attachment, set `IsDocument` to `true`.  
  
 Use the following settings for mapping notes and attachments:  
  
- Set the `ColumnMapping.SourceAttributeName` column to "`true`" or "`false`". The "`true`" value indicates an attachment. The "`false`" value indicates a note.  
  
- Set the `ColumnMapping.TargetAttributeName` column to `IsDocument`.  
  
- Set the `ColumnMapping.ProcessCode` column to the `ImportProcessCode.Internal` value of the `ImportProcessCode` enumeration, if you are using early bound types. For a list of the ProcessCode values, see the choice values for this table.  
  
  If the source data represents a note, map the text of the note to the `Annotation.NoteText` column. If you are working with Salesforce files, they are usually stored on the disk under unique identification numbers. To import an attachment, you must map a file identification number that is contained in the source file to the `Annotation.DocumentBody` column. The `DocumentBody` column stores the contents of the attachment.  
  
  The import asynchronous job checks for mappings that have the source column name set to "`true`" and "`false`" to discover notes and attachments. If it finds an attachment mapping, it looks for the specified files on the disk and uploads the file contents as attachments into Dataverse. If a file is not found, an error is returned.  
  
  If you do not provide mapping for an annotation (note) table, the import job generates a default mapping for the note.  
  
> [!NOTE]
> The maximum size of files that can be uploaded is determined by the **Organization.MaxUploadFileSize** property. This property is set in the **Email** tab of the **System Settings** in the Dataverse application. This setting limits the size of files that can be attached to email messages, notes, and web resources. The default setting is 5 MB. However, an attachment size cannot exceed the maximum HTTP request size (the default is 16MB).
  
<a name="BKMK_ImportExport"></a>

## Import and export data maps

 You can export an existing data map to an XML file and import XML data mappings into Dataverse. To export a data map from Dataverse, use the `ExportMappingsImportMap` message using <xref:Microsoft.Crm.Sdk.Messages.ExportMappingsImportMapRequest?text=ExportMappingsImportMapRequest Class> or the <xref:Microsoft.Dynamics.CRM.ExportMappingsImportMap?text=ExportMappingsImportMap Action> . To import XML data mappings and create a data map in Dataverse, use the `ImportMappingsImportMap` message using the <xref:Microsoft.Crm.Sdk.Messages.ImportMappingsImportMapRequest?text=ImportMappingsImportMapRequest Class> or <xref:Microsoft.Dynamics.CRM.ImportMappingsImportMap?text=ImportMappingsImportMap Action>.  
  
### See Also

[Import data](import-data.md)<br />
[Prepare source files for import](prepare-source-files-import.md)<br />
[Add transformation mappings for import](add-transformation-mappings-import.md)<br />
[Configure data import](configure-data-import.md)<br />
[Run data import](run-data-import.md)<br />
[Data import tables](data-import-entities.md)<br />
[Sample: Export and import a data map](org-service/samples/export-import-data-map.md)<br />
[Sample: Import data using complex data map](org-service/samples/import-data-complex-data-map.md)<br />


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
