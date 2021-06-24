---
title: "Annotation (note) table (Microsoft Dataverse) | Microsoft Docs"
description: "Learn about annotation table to append additional information to any row in the database. The annotation table represents an annotation and contains the annotation text, who created and modified the annotation, and whether a file is attached to the annotation."
ms.custom: ""
ms.date: 03/28/2021
ms.reviewer: "pehecke"
ms.service: powerapps
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
# Annotation (note) table

The *annotations (notes)* provide easy ways to append additional information to any record in the 
Microsoft Dataverse database. An annotation (note) is a text entry that can be associated with any table in 
Dataverse. However, you can associate annotations with only those custom tables that are created with 
the <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest.HasNotes> property set to `true` in the <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest> class. You can update a 
custom table, which is not enabled for notes, to have notes by setting the <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest>.<xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest.HasNotes> property to `true`. 

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

Using the Web API, set the `HasNotes` property of the <xref:Microsoft.Dynamics.CRM.EntityMetadata> EntityType.
  
 The `Annotation` table represents an annotation (note), and contains the following information:  
  
-   Annotation (note) text  
  
-   Who created and modified the annotation (note)  
  
-   Whether a file is attached to the annotation (note)  
  
 An attached file can be any standard computer file format that includes Office Word documents, Office Excel spreadsheets, CAD files, and PDF files. An attachment can be associated with any object, other than an annotation (note), in Dataverse.  
  
 To upload or remove an attachment, use the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*> method or <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> message, setting the `Annotation.Filename` and `Annotation.MimeType` columns. This uploads an attachment that has been decoded into a base64 string format. The [System.Convert.ToBase64String](/dotnet/api/system.convert.tobase64string) method can be used to convert the contents of a data file into a base64-formatted string. The maximum size of files that can be uploaded is determined by the **Organization.MaxUploadFileSize** property. This property is set in the **Email** tab of the **System Settings**. This setting limits the size of files that can be attached to email messages, notes, and web resources. The default setting is 5 MB.  
  
## See also  
 [Sample: Upload, Retrieve, and Download an Attachment](org-service/samples/upload-retrieve-download-attachment.md)<br/>  
 [Annotation table reference](reference/entities/annotation.md)   



[!INCLUDE[footer-include](../../includes/footer-banner.md)]
