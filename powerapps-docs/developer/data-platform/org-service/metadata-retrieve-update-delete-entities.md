---
title: "Retrieve, update, and delete tables using the Dataverse SDK for .NET"
description: "Learn how to retrieve, update, and delete Dataverse tables using the Dataverse SDK for .NET."
ms.date: 03/04/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
ms.topic: article
search.audienceType: 
  - developer
---

# Retrieve, update, and delete tables using the Dataverse SDK for .NET

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Learn how to retrieve, update, and delete a table definition. This article uses the custom `Bank Account` table that you created in [Create a custom table](create-custom-entity.md).  
  
<a name="BKMK_RetrieveAndUpdateEntity"></a>  

## Retrieve and update a table  

The following static `DemonstrateRetrieveUpdateTable` sample method retrieves a table definition by using the <xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityRequest> class. It then updates the table to disable mail merge by setting the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsMailMergeEnabled> property to `false`, and sets <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest.HasNotes> to `true` in the <xref:Microsoft.Xrm.Sdk.Messages.UpdateEntityRequest> to specify that the table should include a relationship to the `Annotation` table for the purpose of displaying notes.  
  
```csharp
static void DemonstrateRetrieveUpdateTable(IOrganizationService service, string LogicalName)
{
    RetrieveEntityRequest request = new RetrieveEntityRequest
    {
        EntityFilters = EntityFilters.Entity,
        LogicalName = LogicalName
    };
    RetrieveEntityResponse response = (RetrieveEntityResponse)service.Execute(request);
    EntityMetadata table = response.EntityMetadata;

    // Disable Mail merge
    table.IsMailMergeEnabled = new BooleanManagedProperty(false);
    // Enable Notes
    UpdateEntityRequest updateBankAccountRequest = new UpdateEntityRequest
    {
        Entity = table,
        HasNotes = true
    };

    service.Execute(updateBankAccountRequest);
}
```

> [!NOTE]
> [Learn about available options](../query-schema-definitions.md#evaluate-other-options-to-retrieve-schema-definitions) to retrieve table schema information.
  
<a name="BKMK_DeleteCustomEntity"></a>

## Delete a custom table

The following static `DeleteTable` sample method uses the <xref:Microsoft.Xrm.Sdk.Messages.DeleteEntityRequest> class to delete the table definition with the logical name specified by the `_customEntityName` variable.  
  
```csharp
static void DeleteTable(IOrganizationService service, string LogicalName)
{
    DeleteEntityRequest request = new DeleteEntityRequest()
    {
        LogicalName = LogicalName,
    };
    service.Execute(request);
}
```
  
### See also

[Customize table definitions](../customize-entity-metadata.md)   
[Create and update a table to send email activities to rows](create-update-entity-emailed.md)   
[Create a custom table](create-custom-entity.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
