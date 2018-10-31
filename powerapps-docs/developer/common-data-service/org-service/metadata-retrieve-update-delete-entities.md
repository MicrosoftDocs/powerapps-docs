---
title: "<Topic Title> (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Retrieve, update, and delete entities

This topic shows how to retrieve, update, and delete an entity by using the custom `Bank Account` entity created in [Create a Custom Entity](create-custom-entity.md).  
  
<a name="BKMK_RetrieveAndUpdateEntity"></a>  
 
## Retrieve and update an entity  

 The following sample retrieves an entity by using the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityRequest> message. It then updates the entity to disable mail merge by setting the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsMailMergeEnabled> property to `false`, and sets <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest.HasNotes> to `true` in the <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest> to specify that the entity should include a relationship to the `Annotation` entity so that the entity can display notes.  
  
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

## Delete a custom entity  

The following sample uses the <xref:Microsoft.Xrm.Sdk.Messages.DeleteEntityRequest> message to delete the entity with the logical name specified by the `_customEntityName` variable.  
  
```csharp

DeleteEntityRequest request = new DeleteEntityRequest()
{
 LogicalName = _customEntityName,
};
_serviceProxy.Execute(request);
```
  
### See also  
 [Use the IOrganizationService Sample and Helper Code](/dynamics365/customer-engagement/developer/use-sample-helper-code)   
 [Customize entity metadata](../customize-entity-metadata.md)   
 [Create and update an entity than can be emailed](/dynamics365/customer-engagement/developer/create-update-entity-emailed)   
 [Create a Custom Entity](create-custom-entity.md)