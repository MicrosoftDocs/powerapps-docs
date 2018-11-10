---
title: "Create data maps for import (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Data maps are required to import data, and contain mappings between the data contained in the source file and the respective entity attributes." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Create data maps for import

To import data into Common Data Service for Apps, you must provide the appropriate data maps.  
  
 You can download examples of data maps from [Microsoft Downloads: DataImportMaps.zip](http://download.microsoft.com/download/D/5/F/D5F73E15-439B-4EBC-BFFB-C6837B146C76/DataImportMaps.zip).
  
 You use data maps to map the data contained in the source file to the CDS for Apps entity attributes. You must map every column in the source file to an appropriate attribute. The data in the unmapped columns is not imported during the data import operation.  
  
 The data map is represented by the import map (data map) entity. You can create a new map by using the <xref:Microsoft.Xrm.Sdk.Messages.CreateRequest> message or update an existing map by using the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*> method. The map has a unique name that is contained in the `ImportMap.Name` attribute. You can specify the name of the import source for which this data map is created by using the `ImportMap.Source` attribute.  
  
<a name="BKMK_Column"></a>   
## Column, list value, and lookup mappings  
 To map a column, a list value, or lookup value in the source file to a CDS for Apps attribute, use the following mappings:  
  
 **Column Mapping**  
  
 Maps a column in a source file to a CDS for Apps entity attribute. For column mapping, use the column mapping (`ColumnMapping`) entity. You can use 1:1 (one-to-one) or 1:N (one-to-many) relationships between source and target attributes. For example, you can map account address information to the billing and shipping addresses in an order.  
  
 **List Value Mapping**  
  
 Maps a list value in a source file to a CDS for Apps attribute of the <xref:Microsoft.Xrm.Sdk.OptionSetValue> type. For list value mapping, use the picklist mapping (`PicklistMapping`) entity.  
  
 If a value specified in the source file column is a list value, such as an OptionSetValue, Status, State, and Boolean, you must provide a list value mapping additionally to a column mapping. For example, map the "bill" and "ship" list values in the source file to the bill and ship values of the <xref:Microsoft.Xrm.Sdk.OptionSetValue> type.  
  
 **Lookup Mapping**  
  
 Maps a lookup value in a source file to a CDS for Apps attribute of the <xref:Microsoft.Xrm.Sdk.EntityReference> type. For lookup mapping, use the lookup mapping (`LookupMapping`) entity.  
  
 If the value specified in the source file references an entity, you must provide a lookup mapping for this value. Use the `LookupMapping.LookupSourceCode` attribute to specify whether to search for the referenced entity inside the source file or inside CDS for Apps. If you are using early bound types, you can use the `LookupSourceType` enumeration to set the lookup values. To search inside the source file, use the `LookupSourceType.Source` value. To search inside CDS for Apps, use the `LookupSourceType.System` value. For a list of the LookupSourceCode values, see the picklist values for this entity. To view the entity metadata for your organization, install the Metadata Browser solution described in [Browse the metadata for your organization](/dynamics365/customer-engagement/developer/browse-your-metadata). You can also browse the reference documentation for entities in the [Entity Reference](reference/about-entity-reference.md). You can provide multiple lookup mappings. The asynchronous transformation job processes all available mappings. It finds the referenced records and updates the parse table with the record unique identifiers. For more information, see [Run Data Import](run-data-import.md).  
  
<a name="BKMK_Owner"></a>   
## Owner mapping  
 Use owner mapping to map a user specified in the source file to a user in CDS for Apps. For logging information, use the CDS for Apps user logon name. For owner mapping, use the owner mapping (`OwnerMapping`) entity.  
  
<a name="BKMK_Notes"></a>   
## Notes and attachments  
 Mapping for notes and attachments is handled differently from other entities. Notes and attachments are used to append additional information to a record in CDS for Apps. Notes are stored as text and attachments are stored as files in the CDS for Apps database.  
  
 To create a note in CDS for Apps, set the `Annotation.IsDocument` attribute in the annotation (note) entity to `false`. To create an attachment, set `IsDocument` to `true`.  
  
 Use the following settings for mapping notes and attachments:  
  
- Set the `ColumnMapping.SourceAttributeName` attribute to “`true`” or “`false`”. The “`true`” value indicates an attachment. The “`false`” value indicates a note.  
  
- Set the `ColumnMapping.TargetAttributeName` attribute to `IsDocument`.  
  
- Set the `ColumnMapping.ProcessCode` attribute to the `ImportProcessCode.Internal` value of the `ImportProcessCode` enumeration, if you are using early bound types. For a list of the ProcessCode values, see the picklist values for this entity.  
  
  If the source data represents a note, map the text of the note to the `Annotation.NoteText` attribute. If you are working with Salesforce files, they are usually stored on the disk under unique identification numbers. To import an attachment, you must map a file identification number that is contained in the source file to the `Annotation.DocumentBody` attribute. The `DocumentBody` attribute stores the contents of the attachment.  
  
  The import asynchronous job checks for mappings that have the source attribute name set to “`true`” and “`false`” to discover notes and attachments. If it finds an attachment mapping, it looks for the specified files on the disk and uploads the file contents as attachments into CDS for Apps. If a file is not found, an error is returned.  
  
  If you do not provide mapping for an annotation (note) entity, the import job generates a default mapping for the note.  
  
> [!NOTE]
> The maximum size of files that can be uploaded is determined by the **Organization.MaxUploadFileSize** property. This property is set in the **Email** tab of the **System Settings** in the CDS for Apps application. This setting limits the size of files that can be attached to email messages, notes, and web resources. The default setting is 5 MB. However, an attachment size cannot exceed the maximum HTTP request size (the default is 16MB). For the change to take effect, reset Internet Information Services. To do this, click **Start**, click **Run**, type `iisreset`, and then click **OK**.  
  
<a name="BKMK_ImportExport"></a>   
## Import and export data maps  
 You can export an existing data map to an XML file and import XML data mappings into CDS for Apps. To export a data map from CDS for Apps, use the <xref:Microsoft.Crm.Sdk.Messages.ExportMappingsImportMapRequest> message. To import XML data mappings and create a data map in CDS for Apps, use the <xref:Microsoft.Crm.Sdk.Messages.ImportMappingsImportMapRequest> message.  
  
### See Also

[Import data](import-data.md)<br />
[Prepare source files for import](prepare-source-files-import.md)<br />
[Add transformation mappings for import](add-transformation-mappings-import.md)<br />
[Configure data import](configure-data-import.md)<br />
[Run data import](run-data-import.md)<br />
[Data import entities](data-import-entities.md)<br />
[Sample: Export and import a data map](org-service/samples/export-import-data-map.md)<br />
[Sample: Import data using complex data map](org-service/samples/import-data-complex-data-map.md)<br />