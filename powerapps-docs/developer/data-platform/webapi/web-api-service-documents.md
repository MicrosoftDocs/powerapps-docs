---
title: Dataverse Web API Service Documents
description: Learn how to use OData service documents to discover and understand Dataverse Web API capabilities in your environment.
ms.date: 03/27/2026
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
ms.service: powerapps
applies_to: 
  - "Dynamics 365 (online)" 
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Web API service documents

OData endpoints provide service documents that describe the capabilities of the service. Understanding these service documents helps you use the resources that are available in the environment you're working with.

## Service document

Perform a `GET` request on the Web API endpoint to see the service document for your environment. 

Your Web API endpoint looks something like this: `https://yourorg.api.crm.dynamics.com/api/data/v9.2/`. This part: `yourorg.api.crm`, depends on your environment. See [View developer resources](../view-download-developer-resources.md) to learn how to find it.

### [Using Insomnia](#tab/insomnia)

If you're using [Insomnia with the recommended environment settings](insomnia.md), just use the `_.webapiurl` environment variable.

See the instructions to [View the CSDL $metadata document](insomnia.md#view-the-csdl-metadata-document). With Insomnia, you can use [XPath queries to filter the results of the large XML document](insomnia.md#find-definitions-of-types).

### [Using PowerShell with Visual Studio Code](#tab/ps)

If you installed the [Prerequisites](quick-start-ps.md#prerequisites) for [Quick Start Web API with PowerShell and Visual Studio Code](quick-start-ps.md), you can view the service document in Visual Studio Code.

To download the CSDL $metadata document, see [these instructions](use-ps-and-vscode-web-api.md#download-the-dataverse-web-api-csdl-metadata-document).

### [Using your browser](#tab/browser)

You can send `GET` requests by using your browser. Type the Web API endpoint URL in your browser address bar.

> [!TIP]
> To format the JSON returned and make it easier to read, install a browser extension. If you're using Microsoft Edge, search for extensions by using [JSON formatter](https://microsoftedge.microsoft.com/addons/search/JSON%20formatter).

---

You see results like this:

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

The service document provides a list of all the *EntitySets* available in your environment. An EntitySet is the name of a resource that refers to a table in Dataverse. Use the entity set name in the URL to perform operations on the data in a specific table.

> [!TIP]
> Use <kbd>Ctrl+F</kbd> on the results of this document to find the correct entity set name.

## Entity set name

Always use the [EntityMetadata.EntitySetName property](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.EntitySetName) value rather than the logical collection name value. By default, the entity set name matches the table [EntityMetadata.LogicalCollectionName property](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.LogicalCollectionName) value, but don't depend on this value.


## Changing the entity set name

If you have a custom table that you want to address by using a different entity set name, update the table [EntityMetadata.EntitySetName property](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.EntitySetName) value to use a different name. [Learn about table properties you can change](../customize-entity-metadata.md#editable-table-properties).

> [!IMPORTANT]
> Change the `EntitySetName` of a table only when you create the table and before you write any code that uses the table. Changing the name breaks any code that uses the old name.

<a name="bkmk_csdl"></a>

## CSDL $metadata document

To retrieve the Common Schema Definition Language (CSDL) $metadata document, append `$metadata` to the Web API endpoint.

For example: `https://yourorg.api.crm.dynamics.com/api/data/v9.2/$metadata`

This XML document describes all the tables and operations that you can use in your environment.

> [!IMPORTANT]
> This document is the source of truth for everything related to Web API. Reference it frequently. Use <kbd>Ctrl</kbd>+<kbd>F</kbd> on this document to locate the specific `EntityType`, `Action`, `Function`, `ComplexType`, or `EnumType` that you use. The names are case sensitive.



### Metadata annotations

To get more information from the $metadata, add `?annotations=true` to the URL.

For example: `https://yourorg.api.crm.dynamics.com/api/data/v9.2/$metadata?annotations=true`

Set this parameter to include many different kinds of annotations that can be useful. Most annotations aren't included by default because they increase the total size of the document.

You can also get these annotations by adding the `Prefer: odata.include-annotations="*"` request header. This request header works for other types of requests. The `annotations=true` query parameter only works for the $metadata document.

## Service namespace

Near the top of the $metadata, you find this XML element:

```xml
    <edmx:DataServices>
        <Schema Namespace="Microsoft.Dynamics.CRM" Alias="mscrm" xmlns="http://docs.oasis-open.org/odata/ns/edm">
```

This element informs you that all the items in the service are within the `Microsoft.Dynamics.CRM` namespace and that `mscrm` is the alias for the namespace. In some situations, you need to use the fully qualified name of an object, so you use the namespace value.


## Next steps

Learn about entity types.

> [!div class="nextstepaction"]
> [Entity Types](web-api-entitytypes.md)

### See also  

[Web API types and operations](web-api-types-operations.md)   
[Web API Entity Types](web-api-entitytypes.md)   
[Web API properties](web-api-properties.md)   
[Web API navigation properties](web-api-navigation-properties.md)   
[Web API actions](web-api-actions.md)   
[Web API functions](web-api-functions.md)   
[Web API complex and enumeration types](web-api-complex-enum-types.md)   
[Use the Dataverse Web API](overview.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
