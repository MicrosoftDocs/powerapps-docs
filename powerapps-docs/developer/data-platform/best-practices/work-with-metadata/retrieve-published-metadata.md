---
title: "Retrieve published metadata | MicrosoftDocs"
description: "Retrieving unpublished metadata not only will add overhead to processing the request itself, performing more slowly, it could also return metadata that the requestor does not expect."
services: ''
suite: powerapps
documentationcenter: na
author: jowells
manager: austinj
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 1/15/2019
ms.subservice: dataverse-developer
ms.author: jowells
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Retrieve published metadata

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

**Category**: Performance, Usage

**Impact potential**: High

<a name='symptoms'></a>

## Symptoms

Retrieving unpublished metadata could result in:

- Slower performance
- User confusion

<a name='guidance'></a>

## Guidance

It is not common to retrieve unpublished customizations and rarely would you have the need to retrieve those customizations.

An example of when you would need to retrieve unpublished customizations is if you want to create an application to edit customizable metadata.  For instance, if you were to create a custom metadata editor, you must retrieve any unpublished definitions of those items. If a developer defines some changes but does not publish them, your application must be able to retrieve them to ensure the developer is retrieving the latest developed customizations. Failure to do so could result in the loss of unpublished customizations.

However, if you are not creating an editor or do not have an explicit need for retrieving unpublished definitions, then only retrieve those that are published. The following examples show how to retrieve published customizations:

### Default behavior

By default, retrieving metadata will get only published customizations

```csharp
public RetrieveAllEntitiesAttributesResponse GetAllEntitiesImplicit(IOrganizationService service)
{
    var request = new RetrieveAllEntitiesRequest();
    request.EntityFilters = EntityFilters.Attributes;

    return service.Execute(request) as RetrieveAllEntitiesAttributesResponse;
}
```

### Explicitly controlling the behavior

Explicitly setting the `RetrieveAsIfPublished` property to retrieve only published customizations

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

The following operations allow for retrieving unpublished metadata through the `RetrieveAsIfPublished` parameter:

- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllEntitiesRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAllOptionSetsRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveAttributeRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveOptionSetRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveRelationshipRequest>
- <xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityKeyRequest>

Examples of retrieving unpublished customizations are documented below:

> [!WARNING]
> These scenarios should be avoided.

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

This guidance applies to the following Web API functions as well:

- <xref href="Microsoft.Dynamics.CRM.RetrieveAllEntities?text=RetrieveAllEntities Function" />
- <xref href="Microsoft.Dynamics.CRM.RetrieveEntity?text=RetrieveEntity Function" />

<a name='additional'></a>

## Additional information

The Dynamics 365 service allows for retrieval of certain metadata that is published or unpublished. Ever since Dynamics CRM 2011, published metadata is returned, by default, from the application's in-memory metadata cache unless the developer explicitly assigns the `RetrieveAsIfPublished` property value to `true`.

Retrieving unpublished metadata not only will add overhead to processing the request itself, performing more slowly, it could also return metadata that the requestor does not expect. For example, retrieving unpublished optionset metadata could return a label value that is not visible in the user interface, causing confusion to the end-user.

<a name='seealso'></a>

### See also

<xref:Microsoft.Xrm.Sdk.Messages.RetrieveEntityRequest>.<xref href="Microsoft.Xrm.Sdk.Messages.RetrieveEntityRequest.RetrieveAsIfPublished?text=RetrieveAsIfPublished Property" /><br />
[Work with metadata using the Organization service](../../org-service/work-with-metadata.md)<br />
[Use the Web API with metadata](../../webapi/use-web-api-metadata.md)<br />
[Publish customizations](../../../model-driven-apps/publish-customizations.md#retrieving-unpublished-metadata)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]