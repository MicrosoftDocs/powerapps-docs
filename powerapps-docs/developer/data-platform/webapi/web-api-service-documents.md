---
title: Web API Service Documents
description: Describes OData service documents you can use to understand the Dataverse Web API capabilities available in your environment.
ms.date: 01/10/2024
author: MsSQLGirl
ms.author: sriknair
ms.reviewer: jdaly
ms.service: powerapps
applies_to: 
  - "Dynamics 365 (online)" 
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Web API Service Documents

OData endpoints provide service documents that describe the capabilities of the service. Understanding these service documents help you use the resources that are available in the environment you're working with.

## Service document

Perform a `GET` request on Web API endpoint to see the service document for your environment. 

Your Web API endpoint looks something like this: `https://yourorg.api.crm.dynamics.com/api/data/v9.2/`. This part: `yourorg.api.crm`, depends on your environment. See [View developer resources](../view-download-developer-resources.md) to learn how to find it.

### [Using Insomnia](#tab/insomnia)

If you are using [Insomnia with the recommended environment settings](insomnia.md), just use the `_.webapiurl` environment variable.

### [Using PowerShell with Visual Studio Code](#tab/ps)

If you have installed the [Prerequisites](quick-start-ps.md#prerequisites) for [Quick Start Web API with PowerShell and Visual Studio Code](quick-start-ps.md), you can view the service document in Visual Studio Code using this PowerShell script after editing the `$environmentUrl` variable.

```powershell
$environmentUrl = 'https://yourorg.crm.dynamics.com/' # change this
## Login if not already logged in
if ($null -eq (Get-AzTenant -ErrorAction SilentlyContinue)) {
   Connect-AzAccount | Out-Null
}

# Get an access token
$secureToken = (Get-AzAccessToken `
   -ResourceUrl $environmentUrl `
   -AsSecureString).Token

# Convert the secure token to a string
$token = ConvertFrom-SecureString `
   -SecureString $secureToken `
   -AsPlainText


# Common headers
$baseHeaders = @{
   'Authorization'    = 'Bearer ' + $token
   'Accept'           = 'application/json'
   'OData-MaxVersion' = '4.0'
   'OData-Version'    = '4.0'
}
# View service document
Invoke-RestMethod -Uri ($environmentUrl + 'api/data/v9.2/') -Method 'Get' -Headers $baseHeaders
| ConvertTo-Json | Out-File -FilePath "service-document.json"
code "service-document.json"
```

If this doesn't work, see the [Troubleshooting](quick-start-ps.md#troubleshooting) steps in [Quick Start Web API with PowerShell and Visual Studio Code](quick-start-ps.md)

### [Using your browser](#tab/browser)

You can sent `GET` requests using your browser. Type the Web API endpoint URL in your browser address bar.

> [!TIP]
> Install a browser extension to format the JSON returned and make it easier to read, then  If you are using Microsoft Edge, search for extensions using [JSON formatter](https://microsoftedge.microsoft.com/addons/search/JSON%20formatter).

---

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

The service document provides a list of all the *EntitySets* available in your environment. An EntitySet is the name of a resource that refers to a table in Dataverse. You'll use the entity set name in the URL to perform operations on the data in a specific table.

> [!TIP]
> Use <kbd>Ctrl+F</kbd> on the results of this document to find the correct entity set name.

## Entity set name

Always use the entity set name rather than the logical collection name. By default, the entity set name matches the table [EntityMetadata.LogicalCollectionName](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.LogicalCollectionName) property value, but you shouldn't depend on this.


## Changing the entity set name

If you have a custom table that you want to address using a different entity set name, you can update the table [EntityMetadata.EntitySetName](xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.EntitySetName) property value to use a different name. [Learn about table properties you can change](../customize-entity-metadata.md#editable-table-properties)

> [!IMPORTANT]
> You should only change the `EntitySetName` of a table when you create it and before any code is written using the table. It will break any code that used the old name.

<a name="bkmk_csdl"></a>

## CSDL $metadata document

Append `$metadata` to the Web API endpoint to retrieve the Common Schema Definition Language (CSDL) $metadata document.

For example: `https://yourorg.api.crm.dynamics.com/api/data/v9.2/$metadata`

This XML document describes all the tables and operations that you can use in your environment.

You can download the CSDL $metadata document using Visual Studio Code and Powershell using [these instructions](use-ps-and-vscode-web-api.md#download-the-dataverse-web-api-csdl-metadata-document).

> [!IMPORTANT]
> This document is the source of truth for everything related to Web API. You will want to reference it frequently. Use `Ctrl+F` on this document to locate the specific `EntityType`, `Action`, `Function`, `ComplexType`, or `EnumType` that you will use. The names are case sensitive.

### Metadata annotations

To get even more information from the $metadata, append `?annotations=true` to the URL.

For example: `https://yourorg.api.crm.dynamics.com/api/data/v9.2/$metadata?annotations=true`

Setting this parameter includes many different kinds of annotations that can be useful. Most annotations aren't included by default because they increase the total size of the document.

These annotations can also be returned by adding the `Prefer: odata.include-annotations="*"` request header. This request header also works for other types of requests. The `annotations=true` query parameter only works for the $metadata document.

## Service namespace

Near the top of the $metadata you'll find this XML element:

```xml
    <edmx:DataServices>
        <Schema Namespace="Microsoft.Dynamics.CRM" Alias="mscrm" xmlns="http://docs.oasis-open.org/odata/ns/edm">
```

This element informs you that all the items in the service are within the `Microsoft.Dynamics.CRM` namespace and that `mscrm` is the alias for the namespace. In some situations, you'll need to use the fully qualified name of an object, so this requires using the namespace value.


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
