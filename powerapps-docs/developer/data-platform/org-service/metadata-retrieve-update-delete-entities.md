---
title: "Retrieve, update, and delete tables (Microsoft Dataverse) | Microsoft Docs"
description: "Learn how to retrieve, update, and delete tables."
ms.date: 04/03/2022
author: mkannapiran
ms.author: kamanick
ms.reviewer: jdaly
ms.topic: "article"
search.audienceType: 
  - developer
---

# Retrieve, update, and delete tables

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Learn how to retrieve, update, and delete a table definition. This article uses the custom `Bank Account` table that was created in [Create a custom table](create-custom-entity.md).  
  
<a name="BKMK_RetrieveAndUpdateEntity"></a>  

## Retrieve and update a table  

The following code sample retrieves a table definition by using the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityRequest> message. It then updates the table to disable mail merge by setting the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsMailMergeEnabled> property to `false`, and sets <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest.HasNotes> to `true` in the <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest> to specify that the table should include a relationship to the `Annotation` table for the purpose of displaying notes.  
  
```csharp

RetrieveEntityRequest retrieveBankAccountEntityRequest = new RetrieveEntityRequest
{
 EntityFilters = EntityFilters.Entity,
 LogicalName = _customEntityName
};
RetrieveEntityResponse retrieveBankAccountEntityResponse = (RetrieveEntityResponse)_serviceProxy.Execute(retrieveBankAccountEntityRequest);
EntityMetadata BankAccountEntity = retrieveBankAccountEntityResponse.EntityMetadata;

// Disable Mail merge
BankAccountEntity.IsMailMergeEnabled = new BooleanManagedProperty(false);
// Enable Notes
UpdateEntityRequest updateBankAccountRequest = new UpdateEntityRequest
{
 Entity = BankAccountEntity,
 HasNotes = true
};

_serviceProxy.Execute(updateBankAccountRequest);
```
  
<a name="BKMK_DeleteCustomEntity"></a>

## Delete a custom table

The following code sample uses the <xref:Microsoft.Xrm.Sdk.Messages.DeleteEntityRequest> message to delete the table definition with the logical name specified by the `_customEntityName` variable.  
  
```csharp

DeleteEntityRequest request = new DeleteEntityRequest()
{
 LogicalName = _customEntityName,
};
_serviceProxy.Execute(request);
```
  
### See also

[Customize table definitions](../customize-entity-metadata.md)<br />
[Create and update a table to send email activities to rows](create-update-entity-emailed.md)<br />
[Create a custom table](create-custom-entity.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
