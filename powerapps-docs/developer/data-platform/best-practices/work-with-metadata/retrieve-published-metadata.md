---
title: "Retrieve published metadata | MicrosoftDocs"
description: "Retrieving unpublished metadata not only adds overhead to processing the request itself, performing more slowly, it could also return metadata that the requestor doesn't expect."
suite: powerapps
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
ms.topic: how-to
ms.date: 03/02/2026
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
---
# Retrieve published metadata

**Category**: Performance, Usage

**Impact potential**: High

<a name='symptoms'></a>

## Symptoms

Retrieving unpublished metadata can cause:

- Slower performance
- User confusion

<a name='guidance'></a>

## Guidance

It's uncommon to retrieve unpublished customizations and you rarely need to retrieve those customizations.

You might need to retrieve unpublished customizations if you want to create an application to edit customizable metadata. For example, if you create a custom metadata editor, you must retrieve any unpublished definitions of those items. If a developer defines some changes but doesn't publish them, your application must be able to retrieve them to ensure the developer is retrieving the latest developed customizations. Failure to do so could result in the loss of unpublished customizations.

However, if you're not creating an editor or don't have an explicit need for retrieving unpublished definitions, then only retrieve definitions that are published. The following examples show how to retrieve published customizations:

### Default behavior

By default, retrieving metadata gets only published customizations.

```csharp
public RetrieveAllEntitiesAttributesResponse GetAllEntitiesImplicit(IOrganizationService service)
{
    var request = new RetrieveAllEntitiesRequest();
    request.EntityFilters = EntityFilters.Attributes;

    return service.Execute(request) as RetrieveAllEntitiesAttributesResponse;
}
```

### Explicitly controlling the behavior

Explicitly set the `RetrieveAsIfPublished` property to retrieve only published customizations.

```csharp
public RetrieveAllEntitiesAttributesResponse GetAllEntitiesExplicit(IOrganizationService service)
{
    var request = new RetrieveAllEntitiesRequest()
    {
        RetrieveAsIfPublished = false
        EntityFilters = EntityFilters.Attributes
    };

    return service.Execute(request) as RetrieveAllEntitiesAttributesResponse;
}
```

<a name='problem'></a>

## Problematic patterns

The following operations can retrieve unpublished metadata through the `RetrieveAsIfPublished` parameter:

- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllEntitiesRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllOptionSetsRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAttributeRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveOptionSetRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRelationshipRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityKeyRequest>

The following examples show how to retrieve unpublished customizations:

> [!WARNING]
> Avoid these scenarios.

```csharp
public RetrieveEntityKeyResponse GetEntityKey(IOrganizationService service, string entityName, string keyName)
{
    var request = new RetrieveEntityKeyRequest()
    {
        EntityLogicalName = entityName,
        LogicalName = keyName,
        RetrieveAsIfPublished = true
    };

    return service.Execute(request) as RetrieveEntityKeyResponse;
}

public RetrieveRelationshipResponse GetRelationship(IOrganizationService service, Guid id)
{
    var request = new RetrieveRelationshipRequest()
    {
        MetadataId = id,
        RetrieveAsIfPublished = true
    };

    return service.Execute(request) as RetrieveRelationshipResponse;
}

public RetrieveEntityAttributesResponse GetEntity(IOrganizationService service, Guid id)
{
    var request = new RetrieveEntityRequest()
    {
        MetadataId = id,
        RetrieveAsIfPublished = true,
        EntityFilters = EntityFilters.Attributes
    };

    return service.Execute(request) as RetrieveEntityAttributesResponse;
}
```

## Web API functions

This guidance also applies to the following Web API functions:

- <xref href="Microsoft.Dynamics.CRM.RetrieveAllEntities?text=RetrieveAllEntities Function" />
- <xref href="Microsoft.Dynamics.CRM.RetrieveEntity?text=RetrieveEntity Function" />

<a name='additional'></a>

## Additional information

The Dynamics 365 service allows retrieval of certain metadata that is published or unpublished. Since Dynamics CRM 2011, the application's in-memory metadata cache returns published metadata by default, unless you explicitly set the `RetrieveAsIfPublished` property to `true`.

Retrieving unpublished metadata adds overhead to processing the request, so it performs more slowly. It can also return metadata that the requestor doesn't expect. For example, retrieving unpublished optionset metadata can return a label value that isn't visible in the user interface, causing confusion for the end-user.

<a name='seealso'></a>

### See also

[RetrieveEntityRequest.RetrieveAsIfPublished Property](xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityRequest.RetrieveAsIfPublished)   
[Work with metadata using the SDK for .NET](../../org-service/work-with-metadata.md)   
[Use the Web API with metadata](../../webapi/use-web-api-metadata.md)   
[Publish customizations](../../../model-driven-apps/publish-customizations.md#retrieving-unpublished-metadata)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
