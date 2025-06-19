---
title: Use DeleteMultiple (preview)
description: Learn how to use Delete to delete multiple rows of data in a Microsoft Dataverse elastic table. 
ms.date: 09/03/2024
author: pnghub
ms.author: gned
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - sumantb-msft
ms.custom: bap-template
---

# Use DeleteMultiple (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

> [!IMPORTANT]
> This is a preview feature.
>
> [!INCLUDE [cc-preview-features-definition](../../includes/cc-preview-features-definition.md)]

### DeleteMultiple

Delete multiple rows of data in elastic tables with a single request.

##### [SDK for .NET](#tab/sdk)

You must use the [OrganizationRequest class](xref:Microsoft.Xrm.Sdk.OrganizationRequest) because the [SDK for .NET](org-service/overview.md) doesn't have a `DeleteMultipleRequest` class. Learn how to [use messages with the SDK for .NET](org-service/use-messages.md).

The following `DeleteMultipleExample` static method uses the `DeleteMultiple` message with the [OrganizationRequest class](xref:Microsoft.Xrm.Sdk.OrganizationRequest) to delete multiple rows from the `contoso_SensorData` elastic table using the alternate key to include the `partitionid` to uniquely identify the rows.

```csharp
public static void DeleteMultipleExample(IOrganizationService service)
{
    string tableLogicalName = "contoso_sensordata";

    List<EntityReference> entityReferences = new() {
        {
            new EntityReference(logicalName: tableLogicalName,
               keyAttributeCollection: new KeyAttributeCollection
               {
                  { "contoso_sensordataid", "3f56361a-b210-4a74-8708-3c664038fa41" },
                  { "partitionid", "deviceid-001" }
               })
        },
        { new EntityReference(logicalName: tableLogicalName,
               keyAttributeCollection: new KeyAttributeCollection
               {
                  { "contoso_sensordataid", "e682715b-1bba-415e-b2bc-de9327308423" },
                  { "partitionid", "deviceid-002" }
               })
        }
    };

    OrganizationRequest request = new(requestName:"DeleteMultiple")
    {
        Parameters = {
            {"Targets", new EntityReferenceCollection(entityReferences)}
        }
    };

    service.Execute(request);
}
```

##### [Web API](#tab/webapi)

The following example shows how to use the [DeleteMultiple action](xref:Microsoft.Dynamics.CRM.DeleteMultiple) to delete multiple rows from the `contoso_SensorData` elastic table including the `partitionid` to uniquely identify the rows.

**Request:**

```http
POST [Organization Uri]/api/data/v9.2/contoso_sensordatas/Microsoft.Dynamics.CRM.DeleteMultiple
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
Content-Type: application/json; charset=utf-8
Content-Length: 603

{
    "Targets": [
        {
            "@odata.type": "Microsoft.Dynamics.CRM.contoso_sensordata",
            "contoso_sensordataid": "6114ca58-0928-ee11-9965-6045bd5cd155",
            "partitionid": "Device-ABC-1234"
        },
        {
            "@odata.type": "Microsoft.Dynamics.CRM.contoso_sensordata",
            "contoso_sensordataid": "6214ca58-0928-ee11-9965-6045bd5cd155",
            "partitionid": "Device-ABC-1234"
        },
        {
            "@odata.type": "Microsoft.Dynamics.CRM.contoso_sensordata",
            "contoso_sensordataid": "6314ca58-0928-ee11-9965-6045bd5cd155",
            "partitionid": "Device-ABC-1234"
        }
    ]
}
```

**Response:**

```http
HTTP/1.1 204 NoContent
OData-Version: 4.0
```

---

## Availability

`DeleteMultiple` is supported only for elastic tables. Elastic tables don't support [table relationship cascading behavior](configure-entity-relationship-cascading-behavior.md), which can result in unpredictable execution times for delete operations. If you use `DeleteMultiple` on a standard table, you get the error: `DeleteMultiple has not yet been implemented.`


## Examples

You can find sample code on GitHub in [github.com/microsoft/PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples):

- [Elastic table sample code](elastic-table-samples.md)
- Within [Sample: SDK for .NET Use bulk operations](org-service/samples/create-update-multiple.md) or [Sample: Web API Use bulk operations](webapi/samples/create-update-multiple.md), change the `Settings.cs` config file and choose the `UseElastic` option.

### See also

[Use bulk operation messages](bulk-operations.md)   
[Elastic tables](elastic-tables.md)  
[Elastic table sample code](elastic-table-samples.md)   
[Sample: SDK for .NET Use bulk operations](org-service/samples/create-update-multiple.md)   
[Sample: Web API Use bulk operations](webapi/samples/create-update-multiple.md)   