---
title: "Annotation(note) entity (Common Data Service for Apps) | Microsoft Docs"
description: "Learn about annotation entity to append additional information to any record in the database. The annotation  entity represents an annotation and contains the annotation text, who created and modified the annotation, and whether a file is attached to the annotation."
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Annotation (note) entity

The *annotations (notes)* provide easy ways to append additional information to any record in the 
Common Data Service for Apps database. An annotation (note) is a text entry that can be associated with any entity in 
CDS for Apps. However, you can associate annotations with only those custom entities that are created with 
the <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest.HasNotes> property set to `true` in the <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest> class. You can update a 
custom entity, which is not enabled for notes, to have notes by setting the <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest>.<xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest.HasNotes> property to `true`.  

Using the Web API, set the `HasNotes` property of the <xref:Microsoft.Dynamics.CRM.EntityMetadata> EntityType controls this.
  
 The `Annotation` entity represents an annotation (note), and contains the following information:  
  
-   Annotation (note) text  
  
-   Who created and modified the annotation (note)  
  
-   Whether a file is attached to the annotation (note)  
  
 An attached file can be any standard computer file format that includes Office Word documents, Office Excel spreadsheets, CAD files, and PDF files. An attachment can be associated with any object, other than an annotation (note), in CDS for Apps.  
  
 To upload or remove an attachment, use the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Update*> method or <xref:Microsoft.Xrm.Sdk.Messages.UpdateRequest> message, setting the `Annotation.Filename` and `Annotation.MimeType` properties. This uploads an attachment that has been decoded into a base64 string format. The [System.Convert.ToBase64String](https://msdn.microsoft.com/library/system.convert.tobase64string.aspx) method can be used to convert the contents of a data file into a base64-formatted string. The maximum size of files that can be uploaded is determined by the **Organization.MaxUploadFileSize** property. This property is set in the **Email** tab of the **System Settings** in the Dynamics 365 application. This setting limits the size of files that can be attached to email messages, notes, and web resources. The default setting is 5 MB.  
  
## In This Section  
 [Sample: Upload, Retrieve, and Download an Attachment](sample-upload-retrieve-download-attachment.md)  
  
### See also 
 [Annotation Entity](reference/entities/annotation.md)   
 [Model Your Business Data](model-business-data.md)   
 [UserQuery (Saved View) Entity](userquery-saved-view-entity.md)