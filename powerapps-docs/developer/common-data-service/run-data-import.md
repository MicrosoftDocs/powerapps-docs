---
title: "Run data import (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Data importation runs directly on the Dynamics 365 server, and requires three asynchronous jobs for parsing, map-guided transformation, and uploading." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Run data import

Data import runs directly on the Common Data Service for Apps server. To run data import, set up asynchronous jobs to run in the background that do the following, in this order:  
  
- Parse source data that is contained in the import file.  
  
- Transform parsed data by using the data map.  
  
- Upload transformed data into CDS for Apps.  
  
  All CDS for Apps users who have appropriate permissions can run data import.  
  
<a name="parse"></a>   
## Parse source data  
 Parsing source data includes parsing of all import files associated with a particular import (data import).  
  
 Parsed data is stored in the temporary parse tables that are created for every imported file. The name of the parse table is stored in the `ImportFile.ParsedTableName` attribute. The source file column headings are specified in the `ImportFile.HeaderRow` attribute. If the source file does not include a first row that contains the column headings, this attribute specifies the system-generated default column headings.  
  
 Save parsed data in the parse table by using the <xref:Microsoft.Crm.Sdk.Messages.ParseImportRequest> message. Retrieve data from the parse table by using the <xref:Microsoft.Crm.Sdk.Messages.GetDistinctValuesImportFileRequest> message and the <xref:Microsoft.Crm.Sdk.Messages.RetrieveParsedDataImportFileRequest> message.  
  
 The following table lists the messages that you can use to parse the import files and retrieve the parsed data from the parse tables.  
  
|Message|Description|  
|-------------|-----------------|  
|<xref:Microsoft.Crm.Sdk.Messages.ParseImportRequest>|Submits an asynchronous job that parses all import files associated with the specified import (data import). Pass the ID of the associated import (data import) in the <xref:Microsoft.Crm.Sdk.Messages.ParseImportRequest.ImportId> property of this request. The ID of the asynchronous job that runs in the background and performs parsing of data is returned in the <xref:Microsoft.Crm.Sdk.Messages.ParseImportResponse.AsyncOperationId> property of the message response.|  
|<xref:Microsoft.Crm.Sdk.Messages.GetDistinctValuesImportFileRequest>|Returns distinct values for a column in the source file that contains list values. Pass the ID of the associated import file in the <xref:Microsoft.Crm.Sdk.Messages.GetHeaderColumnsImportFileRequest.ImportFileId> property of this request. The distinct values are returned in an array of strings, in the <xref:Microsoft.Crm.Sdk.Messages.GetDistinctValuesImportFileResponse.Values> property of the message response. Use this message only after you have created a parse table by using the <xref:Microsoft.Crm.Sdk.Messages.ParseImportRequest> message. **Important:**  Do not use this message after you use the <xref:Microsoft.Crm.Sdk.Messages.ImportRecordsImportRequest> message. You cannot access the parse table after the import job submitted by the <xref:Microsoft.Crm.Sdk.Messages.ImportRecordsImportRequest> message has finished running.|  
|<xref:Microsoft.Crm.Sdk.Messages.RetrieveParsedDataImportFileRequest>|Retrieves the data from the parse table. Pass the ID of the associated import file in the <xref:Microsoft.Crm.Sdk.Messages.RetrieveParsedDataImportFileRequest.ImportFileId> property of this request. The parsed data is returned in a two-dimensional array of strings in the <xref:Microsoft.Crm.Sdk.Messages.RetrieveParsedDataImportFileResponse.Values> property of the message response. The data is returned with the same column order as the column order in the source file. Use this message only after you have created a parse table by using the <xref:Microsoft.Crm.Sdk.Messages.ParseImportRequest> message. **Important:**  Do not use this message after you use the <xref:Microsoft.Crm.Sdk.Messages.ImportRecordsImportRequest> message. You cannot access the parse table after the import job submitted by the `ImportRecordsMessage` message has finished running.|  
  
<a name="transform"></a>   
## Transform parsed data  
 During transformation, you change parsed data by applying all available data mappings and transformations that are associated with a particular import (data import) to the data.  
  
 Use the <xref:Microsoft.Crm.Sdk.Messages.TransformImportRequest> message to submit an asynchronous job to transform the parsed data. Pass a unique identifier of the associated import (data import) in the `Import.ImportId` attribute of the request. A unique identifier of the asynchronous job that runs in the background and performs the transformation is returned in the <xref:Microsoft.Crm.Sdk.Messages.TransformImportResponse.AsyncOperationId> property of the message response.  
  
<a name="upload"></a>   
## Upload transformed data to the target server  
 After you successfully complete the transformation, the data is ready to be uploaded into the CDS for Apps server.  
  
 Use the <xref:Microsoft.Crm.Sdk.Messages.ImportRecordsImportRequest> message to submit an asynchronous job to upload the transformed data into CDS for Apps. The unique identifier of the associated import (data import) must be specified in the <xref:Microsoft.Crm.Sdk.Messages.ImportRecordsImportRequest.ImportId> property of the request. A unique identifier of the asynchronous job that runs in the background and uploads the data into CDS for Apps is returned in the <xref:Microsoft.Crm.Sdk.Messages.ImportRecordsImportResponse.AsyncOperationId> property of the message response. All import files that are associated with the specified import (data import) are imported.  
  
 Each import job has a unique sequence number that it stores in the `ImportSequenceNumber` attribute of records it creates. The `Organization.CurrentImportSequenceNumber` attribute contains a unique sequence number of the last import job that ran in the system. You can use these unique sequence numbers to track records that belong to one import job.  
  
<a name="log"></a>   
## Log failures  
 A failure to import a record can occur during parsing, transformation, or uploading of data. The failure reasons and other detailed information about the records that failed to import are captured in the import log (ImportLog) entity.  
  
 To find out how many records failed to import, retrieve the `ImportFile.FailureCount` attribute of the record. To verify how many records had partial failures during import, retrieve the `ImportData.HasError` attribute. If the `HasError` attribute is `true`, a partial failure occurred, if it is `false`, the record imported successfully.  
  
<a name="import_audit"></a>   
## Import auditing data  
 The CDS for Apps entities have four default attributes that are used to track the date and time when a record was created and last modified, and the person who created and modified it.  
  
 The `createdon` attribute specifies the date and time that the record was created. To import data in the `createdon` attribute, map the source column that contains this data to the `overriddencreatedon` attribute. During import, the record’s `createdon` attribute is updated with the value that was mapped to the `overriddencreatedon` attribute and the `overriddencreatedon` attribute is set to the date and time that the data was imported. If no source value is mapped to the `overriddencreatedon` attribute, the `createdon` attribute is set to the date and time that the data was imported and the `overriddencreatedon` attribute is not set to any value.  
  
> [!NOTE]
>  To override the value in the `createdon` attribute during import, you need the `prvOverrideCreatedOnCreatedBy` privilege. Note that the privilege name implies that you can also override the `createdby` attribute during import. However, this capability is not currently supported.  
  
 You cannot import data into the `modifiedon`, `createdby`, and `modifiedby` attributes. If you have to store data related to who created and modified the data and when the data was modified, you can create custom attributes in CDS for Apps and map the source columns to the new custom attributes.  
  
### See Also

[Import data](import-data.md)<br />
[Prepare source files for import](prepare-source-files-import.md)<br />
[Create data maps for import](create-data-maps-for-import.md)<br />
[Add transformation mappings for import](add-transformation-mappings-import.md)<br />
[Configure data import](configure-data-import.md)<br />
[Data import entities](data-import-entities.md)<br />
[Sample: Export and import a data map](org-service/samples/export-import-data-map.md)<br />
[Sample: Import data using complex data map](org-service/samples/import-data-complex-data-map.md)<br />
[Blog Post: How to Import attachments programmatically](http://blogs.msdn.com/b/crm/archive/2012/08/06/how-to-import-attachments-programmatically.aspx) 