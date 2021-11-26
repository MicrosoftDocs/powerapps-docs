---
title: "Web API Service Documents (Microsoft Dataverse)| Microsoft Docs"
description: "Describes OData service documents you can use to understand the Dataverse Web API capabilities available in your environment."
ms.custom: ""
ms.date: 11/24/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)" 
author: "JimDaly" # GitHub ID
ms.author: pehecke
manager: "sunilg"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Web API Service Documents

OData endpoints provide service documents that describe the capabilities of the service. Understanding these service documents will help you understand how to use the resources that are available in the environment you are working with.

## Service document

Simply perform a `GET` request on Web API endpoint to see the service document for your environment. If you haven't set up a Postman environment, you can just paste the Web API endpoint into your browser.

Your Web API endpoint will look something like this: `https://yourorg.api.crm.dynamics.com/api/data/v9.2/`.

> [!NOTE]
> If you are using the recommended Postman environment, simply use the `{{webapiurl}}` environment variable. More information: [Set up a Postman environment](setup-postman-environment.md).
>
> If you are not using Postman, you can install a browser extension to format the JSON returned and make it easier to read. If you are using Microsoft Edge, search for extensions using [JSON formatter](https://microsoftedge.microsoft.com/addons/search/JSON%20formatter).

You should see results like this:

```json
{
    "@odata.context": "https://yourorg.api.crm.dynamics.com/api/data/v9.2/$metadata",
    "value": [
        {
            "name": "accountleadscollection",
            "kind": "EntitySet",
            "url": "accountleadscollection"
        },
        {
            "name": "accounts",
            "kind": "EntitySet",
            "url": "accounts"
        },
    ...
```

The service document provides a list of all the *EntitySets* available in your environment. An EntitySet is the name of a resource that refers to a table in Dataverse. You will use the entity set name in the URL to perform operations on the data in a specific table.

> [!TIP]
> Use `Ctrl+F` on the results of this to find the correct entity set name.

## Entity set name

Always use the entity set name rather than the logical collection name.

> [!NOTE]
> By default, the entity set name matches the table <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.LogicalCollectionName> property value, but you shouldn't depend on this.

If you have a custom table that you want to address using a different entity set name, you can update the table <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.EntitySetName> property value to use a different name. You should only change the `EntitySetName` of a table when you create it and before any code is written using the table.

<a name="bkmk_csdl"></a>

## CSDL $metadata document

Append `$metadata` to the Web API endpoint to retrieve the Common Schema Definition Language (CSDL) $metadata document.

For example: `https://yourorg.api.crm.dynamics.com/api/data/v9.2/$metadata`

This large XML document describes all the data and operations that you can use in your environment.

> [!IMPORTANT]
> This document is the source of truth for everything related to Web API. You will want to reference it frequently. Use `Ctrl+F` on this document to locate the specific `EntityType`, `Action`, `Function`, `ComplexType`, or `EnumType` that you will use. The names are case sensitive.

### Metadata annotations

To get even more information from the $metadata, append `?annotations=true` to the URL.

For example: `https://yourorg.api.crm.dynamics.com/api/data/v9.2/$metadata?annotations=true`

This will include many different kinds of annotations that can be useful. Most annotations are not included by default because they increase the total size of the document.

These annotations can also be returned by adding the `Prefer: odata.include-annotations="*"` request header. This request header also works for other types of requests. The `annotations=true` query parameter only works for the $metadata document.

## Service namespace

Near the top of the $metadata you will find this XML element:

```xml
    <edmx:DataServices>
        <Schema Namespace="Microsoft.Dynamics.CRM" Alias="mscrm" xmlns="http://docs.oasis-open.org/odata/ns/edm">
```

This informs you that all the items in the service are within the `Microsoft.Dynamics.CRM` namespace and that `mscrm` is the alias for the namespace. In some situations, you will need to use the fully qualified name of an object, so this will require using the namespace value.

### See also  

[Use the Dataverse Web API](overview.md)<br />
[Web API types and operations](web-api-types-operations.md)<br />


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]