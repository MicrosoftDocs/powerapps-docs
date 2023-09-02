---
title: Select columns using FetchXml
description: Learn how to use FetchXml to select columns when you retrieve data from Microsoft Dataverse.
ms.date: 08/31/2023
ms.reviewer: jdaly
ms.topic: how-to
author: pnghub
ms.subservice: dataverse-developer
ms.author: gned
search.audienceType: 
  - developer
---
# Select columns using FetchXml

As described in [Query data using FetchXml](overview.md), start your query by selecting a table using the [entity element](reference/entity.md).

Use the [attribute element](reference/attribute.md) to select the columns to return with your query. For example:

```xml
<fetch>
  <entity name='account'>
    <attribute name='accountclassificationcode' />
    <attribute name='createdby' />
    <attribute name='createdon' />
    <attribute name='name' />
  </entity>
</fetch>
```

This query returns the [AccountClassificationCode](../reference/entities/account.md#BKMK_AccountClassificationCode), [CreatedBy](../reference/entities/account.md#BKMK_CreatedBy), [CreatedOn](../reference/entities/account.md#BKMK_CreatedOn), and [Name](../reference/entities/account.md#BKMK_Name) columns of the first 5,000 rows from the [Account table](../reference/entities/account.md). If you need more rows than this, or you want to iterate through smaller sets of data, [learn how to page results using FetchXml](page-results.md)

For each attribute you want returned, add an [attribute element](reference/attribute.md) and set the `name` attribute value to the `LogicalName` of the column.

Use the [attribute element](reference/attribute.md) to select the columns for the [entity](reference/entity.md) of your query and any tables joined using the [link-entity element](reference/link-entity.md). [Learn how to join tables using FetchXml](join-tables.md).


> [!IMPORTANT]
> We strongly discourage returning all columns in a table. Returning all columns will make your applications run slower and may cause timeout errors. You should specify the minimum number of columns to retrieve with your data. If you do not specify columns, or you use the [all-attributes element](reference/all-attributes.md), data for all columns is returned.


## Formatted values

The typed data returned may not be suitable to display in your application. Formatted values are string values returned with the request that you can display in your application.

For example, the results of the example query above look something like this:

### [SDK for .NET](#tab/sdk)

This `SimpleOutput` method only accesses values in the [Entity.Attributes collection](xref:Microsoft.Xrm.Sdk.Entity.Attributes).

```csharp
/// <summary>
/// Output the entity attribute values
/// </summary>
/// <param name="service">The authenticated IOrganizaitonService instance</param>
static void SimpleOutput(IOrganizationService service) {

    string fetchXml = @"<fetch>
            <entity name='account'>
                <attribute name='accountclassificationcode' />
                <attribute name='createdby' />
                <attribute name='createdon' />
                <attribute name='name' />
            </entity>
            </fetch>";

    FetchExpression fetchExpression = new(fetchXml);

    //Retrieve the data
    EntityCollection entityCollection = service.RetrieveMultiple(query: fetchExpression);

    var table = new ConsoleTables.ConsoleTable("classificationcode", "createdby", "createdon", "name");

    foreach (var entity in entityCollection.Entities ) {

        var accountclassificationcode = entity.GetAttributeValue<OptionSetValue>("accountclassificationcode").Value;
        var createdby = entity.GetAttributeValue<EntityReference>("createdby").Name;
        var createdon = entity.GetAttributeValue<DateTime>("createdon");
        var name = entity.GetAttributeValue<string>("name");

        table.AddRow(accountclassificationcode, createdby, createdon, name);

    }
    table.Write();
}
```

**Output**:

```text
 ----------------------------------------------------------------------------------------------
 | classificationcode | createdby           | createdon             | name                    |
 ----------------------------------------------------------------------------------------------
 | 1                  | FirstName LastName  | 8/13/2023 10:30:08 PM | Fourth Coffee (sample)  |
 ----------------------------------------------------------------------------------------------
 | 1                  | FirstName LastName  | 8/13/2023 10:30:10 PM | Litware, Inc. (sample)  |
 ----------------------------------------------------------------------------------------------
 | 1                  | FirstName LastName  | 8/13/2023 10:30:10 PM | Adventure Works (sample)|
 ----------------------------------------------------------------------------------------------

```

### [Web API](#tab/webapi)

This request doesn't include the `Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"` header to return formatted values:

**Request**

```http
GET [Organization Uri]/api/data/v9.2/accounts?fetchXml=%3Cfetch%3E%3Centity%20name%3D%22account%22%3E%3Cattribute%20name%3D%22accountclassificationcode%22%20%2F%3E%3Cattribute%20name%3D%22createdby%22%20%2F%3E%3Cattribute%20name%3D%22createdon%22%20%2F%3E%3Cattribute%20name%3D%22name%22%20%2F%3E%3C%2Fentity%3E&$count=true
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#accounts(accountid,accountclassificationcode,createdon,_createdby_value,name,createdby,createdby())",
  "@odata.count": 3,
  "value": [
    {
      "@odata.etag": "W/\"1702706\"",
      "accountid": "41aa67df-283a-ee11-bdf4-000d3a11bec2",
      "accountclassificationcode": 1,
      "createdon": "2023-08-13T22:30:08Z",
      "_createdby_value": "ed8a38c1-4a28-ee11-bdf4-000d3a4f18ae",
      "name": "Fourth Coffee (sample)"
    },
    {
      "@odata.etag": "W/\"1702707\"",
      "accountid": "43aa67df-283a-ee11-bdf4-000d3a11bec2",
      "accountclassificationcode": 1,
      "createdon": "2023-08-13T22:30:10Z",
      "_createdby_value": "ed8a38c1-4a28-ee11-bdf4-000d3a4f18ae",
      "name": "Litware, Inc. (sample)"
    },
    {
      "@odata.etag": "W/\"1702708\"",
      "accountid": "45aa67df-283a-ee11-bdf4-000d3a11bec2",
      "accountclassificationcode": 1,
      "createdon": "2023-08-13T22:30:10Z",
      "_createdby_value": "ed8a38c1-4a28-ee11-bdf4-000d3a4f18ae",
      "name": "Adventure Works (sample)"
    }
  ]
}
```

---

These values may not be the user-friendly values you need to display in an application.

- The `accountclassificationcode` choice column returns the integer value.
- The SDK reference to `createdby` must use the [EntityReference.Name property](xref:Microsoft.Xrm.Sdk.EntityReference.Name)
- The Web API returns the `_createdby_value` [Lookup property](../webapi/query-data-web-api.md#lookup-property-data) that has the GUID value for the `createdby` lookup column.

To get the user-friendly values you want, you need to access *formatted values* that can be returned by Dataverse.

How you get these values depends on whether you use the SDK for .NET or Web API.


### [SDK for .NET](#tab/sdk)

The `OutputFetchRequest` sample method described in [Sample code](overview.md#sample-code) uses formatted values, so the results of the query look like this:

```text
 --------------------------------------------------------------------------------------------------
 | accountclassificationcode | createdby           | createdon          | name                    |
 --------------------------------------------------------------------------------------------------
 | Default Value             | FirstName LastName  | 8/13/2023 10:30 PM | Fourth Coffee (sample)  |
 --------------------------------------------------------------------------------------------------
 | Default Value             | FirstName LastName  | 8/13/2023 10:30 PM | Litware, Inc. (sample)  |
 --------------------------------------------------------------------------------------------------
 | Default Value             | FirstName LastName  | 8/13/2023 10:30 PM | Adventure Works (sample)|
 --------------------------------------------------------------------------------------------------

```

### [Web API](#tab/webapi)

This request includes the `Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"` header so that formatted values are returned with the `@OData.Community.Display.V1.FormattedValue` annotation.

**Request**

```http
GET [Organization Uri]/api/data/v9.2/accounts?fetchXml=%3Cfetch%3E%3Centity%20name%3D%22account%22%3E%3Cattribute%20name%3D%22accountclassificationcode%22%20%2F%3E%3Cattribute%20name%3D%22createdby%22%20%2F%3E%3Cattribute%20name%3D%22createdon%22%20%2F%3E%3Cattribute%20name%3D%22name%22%20%2F%3E%3C%2Fentity%3E&$count=true
Prefer: odata.include-annotations="OData.Community.Display.V1.FormattedValue"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#accounts(accountid,accountclassificationcode,createdon,_createdby_value,name,createdby,createdby())",
  "@odata.count": 3,
  "value": [
    {
      "@odata.etag": "W/\"1702706\"",
      "accountid": "41aa67df-283a-ee11-bdf4-000d3a11bec2",
      "accountclassificationcode@OData.Community.Display.V1.FormattedValue": "Default Value",
      "accountclassificationcode": 1,
      "createdon@OData.Community.Display.V1.FormattedValue": "8/13/2023 10:30 PM",
      "createdon": "2023-08-13T22:30:08Z",
      "_createdby_value@OData.Community.Display.V1.FormattedValue": "FirstName LastName",
      "_createdby_value": "ed8a38c1-4a28-ee11-bdf4-000d3a4f18ae",
      "name": "Fourth Coffee (sample)"
    },
    {
      "@odata.etag": "W/\"1702707\"",
      "accountid": "43aa67df-283a-ee11-bdf4-000d3a11bec2",
      "accountclassificationcode@OData.Community.Display.V1.FormattedValue": "Default Value",
      "accountclassificationcode": 1,
      "createdon@OData.Community.Display.V1.FormattedValue": "8/13/2023 10:30 PM",
      "createdon": "2023-08-13T22:30:10Z",
      "_createdby_value@OData.Community.Display.V1.FormattedValue": "FirstName LastName",
      "_createdby_value": "ed8a38c1-4a28-ee11-bdf4-000d3a4f18ae",
      "name": "Litware, Inc. (sample)"
    },
    {
      "@odata.etag": "W/\"1702708\"",
      "accountid": "45aa67df-283a-ee11-bdf4-000d3a11bec2",
      "accountclassificationcode@OData.Community.Display.V1.FormattedValue": "Default Value",
      "accountclassificationcode": 1,
      "createdon@OData.Community.Display.V1.FormattedValue": "8/13/2023 10:30 PM",
      "createdon": "2023-08-13T22:30:10Z",
      "_createdby_value@OData.Community.Display.V1.FormattedValue": "FirstName LastName",
      "_createdby_value": "ed8a38c1-4a28-ee11-bdf4-000d3a4f18ae",
      "name": "Adventure Works (sample)"
    }
  ]
}
```

---

Learn more about formatted values:

- [SDK for .NET Query data: Access formatted values](../org-service/entity-operations-query-data.md#access-formatted-values)
- [Web API Query data: Formatted values](../webapi/query-data-web-api.md#formatted-values)


## Column aliases

Column aliases are typically used for [aggregate operations](aggregate-data.md), but they also work for simple select operations, so we can introduce them here.

You can use the [attribute](reference/attribute.md) `alias` attribute to specify any unique column name you want for the results returned.

Each column returned must have a unique name. By default, the column names returned for the entity of your query are the column `LogicalName` values. All column logical names are unique for each table, so there can't be any duplicate names within that set.

When you use a [link-entity element](reference/link-entity.md) to [join tables](join-tables.md), the default column names follow this naming convention: `{Linked table LogicalName}.{Column LogicalName}`.  This prevents any duplicate column names. You can override this by using a unique alias. You can also set an `alias` value for the `link-entity` representing the joined table.

The behavior you see when using column aliases depends on whether you are using the SDK for .NET or Web API.

### [SDK for .NET](#tab/sdk)

This `SimpleAliasOutput` method uses aliases rather than the logical names of the columns. Because of this, the results are returned as <xref:Microsoft.Xrm.Sdk.AliasedValue>. To access the value of complex types like [OptionSetValue](xref:Microsoft.Xrm.Sdk.OptionSetValue) or [EntityReference](xref:Microsoft.Xrm.Sdk.EntityReference), you have to cast the value.



```csharp
/// <summary>
/// Output the entity attribute values with aliases
/// </summary>
/// <param name="service">The authenticated IOrganizaitonService instance</param>
static void SimpleAliasOutput(IOrganizationService service)
{
    string fetchXml = @"<fetch top='3'>
            <entity name='account'>
              <attribute name='accountclassificationcode' alias='code' />
              <attribute name='createdby' alias='whocreated' />
              <attribute name='createdon' alias='whencreated' />
              <attribute name='name' alias='companyname' />
            </entity>
          </fetch>";

    FetchExpression fetchExpression = new(fetchXml);

    //Retrieve the data
    EntityCollection entityCollection = service.RetrieveMultiple(query: fetchExpression);

    var table = new ConsoleTables.ConsoleTable("code", "whocreated", "whencreated", "companyname");

    foreach (var entity in entityCollection.Entities)
    {

        var code = ((OptionSetValue)entity.GetAttributeValue<AliasedValue>("code").Value).Value;
        var whocreated = ((EntityReference)entity.GetAttributeValue<AliasedValue>("whocreated").Value).Name;
        var whencreated = entity.GetAttributeValue<AliasedValue>("whencreated").Value;
        var companyname = entity.GetAttributeValue<AliasedValue>("companyname").Value;

        table.AddRow(code, whocreated, createdon, companyname);

    }
    table.Write();
}
```

Output:

```text
 ----------------------------------------------------------------------------------
 | code | whocreated           | whencreated           | companyname              |
 ----------------------------------------------------------------------------------
 | 1    | FirstName LastName   | 8/13/2023 10:30:08 PM | Fourth Coffee (sample)   |
 ----------------------------------------------------------------------------------
 | 1    | FirstName LastName   | 8/13/2023 10:30:10 PM | Litware, Inc. (sample)   |
 ----------------------------------------------------------------------------------
 | 1    | FirstName LastName   | 8/13/2023 10:30:10 PM | Adventure Works (sample) |
 ----------------------------------------------------------------------------------
```

> [!NOTE]
> The [AliasedValue class](xref:Microsoft.Xrm.Sdk.AliasedValue) has two properties that tell you the original [EntityLogicalName](xref:Microsoft.Xrm.Sdk.AliasedValue.EntityLogicalName) and [AttributeLogicalName](xref:Microsoft.Xrm.Sdk.AliasedValue.AttributeLogicalName) if you need them.

### [Web API](#tab/webapi)

The following request uses this fetchXml query specifying `alias` attribute values for these columns:

```xml
<fetch>
   <entity name='account'>
      <attribute name='accountclassificationcode' alias='code' />
      <attribute name='createdby' alias='whocreated' />
      <attribute name='createdon' alias='whencreated' />
      <attribute name='name' alias='companyname' />
   </entity>
</fetch>
```


**Request**

```http
GET [Organization Uri]/api/data/v9.2/accounts?fetchXml=%3Cfetch%3E%0D%0A++%3Centity+name%3D%22account%22%3E%0D%0A++++%3Cattribute+name%3D%22accountclassificationcode%22+alias%3D%22code%22+%2F%3E%0D%0A++++%3Cattribute+name%3D%22createdby%22+alias%3D%22whocreated%22+%2F%3E%0D%0A++++%3Cattribute+name%3D%22createdon%22+alias%3D%22whencreated%22+%2F%3E%0D%0A++++%3Cattribute+name%3D%22name%22+alias%3D%22companyname%22+%2F%3E%0D%0A++%3C%2Fentity%3E%0D%0A%3C%2Ffetch%3E&$count=true
Prefer: odata.include-annotations="*"
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

Because the request was sent with the `Prefer: odata.include-annotations="*"` header, the aliased columns also have an `@OData.Community.Display.V1.AttributeName` annotation that includes the original column name, in addition to the `@OData.Community.Display.V1.FormattedValue` annotation containing the formatted values.

**Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Preference-Applied: odata.include-annotations="*"

{
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#accounts(accountid,accountclassificationcode,createdby,createdon,name,createdby())",
  "@odata.count": 10,
  "@Microsoft.Dynamics.CRM.totalrecordcount": 10,
  "@Microsoft.Dynamics.CRM.totalrecordcountlimitexceeded": false,
  "@Microsoft.Dynamics.CRM.globalmetadataversion": "1700565",
  "value": [
    {
      "@odata.etag": "W/\"1702706\"",
      "accountid": "41aa67df-283a-ee11-bdf4-000d3a11bec2",
      "whencreated@OData.Community.Display.V1.AttributeName": "createdon",
      "whencreated@OData.Community.Display.V1.FormattedValue": "8/13/2023 10:30 PM",
      "whencreated": "2023-08-13T22:30:08Z",
      "code@OData.Community.Display.V1.AttributeName": "accountclassificationcode",
      "code@OData.Community.Display.V1.FormattedValue": "Default Value",
      "code": 1,
      "companyname@OData.Community.Display.V1.AttributeName": "name",
      "companyname": "Fourth Coffee (sample)",
      "whocreated@OData.Community.Display.V1.AttributeName": "createdby",
      "whocreated@OData.Community.Display.V1.FormattedValue": "FirstName LastName",
      "whocreated@Microsoft.Dynamics.CRM.lookuplogicalname": "systemuser",
      "whocreated": "ed8a38c1-4a28-ee11-bdf4-000d3a4f18ae"
    },
    {
      "@odata.etag": "W/\"1702707\"",
      "accountid": "43aa67df-283a-ee11-bdf4-000d3a11bec2",
      "whencreated@OData.Community.Display.V1.AttributeName": "createdon",
      "whencreated@OData.Community.Display.V1.FormattedValue": "8/13/2023 10:30 PM",
      "whencreated": "2023-08-13T22:30:10Z",
      "code@OData.Community.Display.V1.AttributeName": "accountclassificationcode",
      "code@OData.Community.Display.V1.FormattedValue": "Default Value",
      "code": 1,
      "companyname@OData.Community.Display.V1.AttributeName": "name",
      "companyname": "Litware, Inc. (sample)",
      "whocreated@OData.Community.Display.V1.AttributeName": "createdby",
      "whocreated@OData.Community.Display.V1.FormattedValue": "FirstName LastName",
      "whocreated@Microsoft.Dynamics.CRM.lookuplogicalname": "systemuser",
      "whocreated": "ed8a38c1-4a28-ee11-bdf4-000d3a4f18ae"
    },
    {
      "@odata.etag": "W/\"1702708\"",
      "accountid": "45aa67df-283a-ee11-bdf4-000d3a11bec2",
      "whencreated@OData.Community.Display.V1.AttributeName": "createdon",
      "whencreated@OData.Community.Display.V1.FormattedValue": "8/13/2023 10:30 PM",
      "whencreated": "2023-08-13T22:30:10Z",
      "code@OData.Community.Display.V1.AttributeName": "accountclassificationcode",
      "code@OData.Community.Display.V1.FormattedValue": "Default Value",
      "code": 1,
      "companyname@OData.Community.Display.V1.AttributeName": "name",
      "companyname": "Adventure Works (sample)",
      "whocreated@OData.Community.Display.V1.AttributeName": "createdby",
      "whocreated@OData.Community.Display.V1.FormattedValue": "FirstName LastName",
      "whocreated@Microsoft.Dynamics.CRM.lookuplogicalname": "systemuser",
      "whocreated": "ed8a38c1-4a28-ee11-bdf4-000d3a4f18ae"
    }
  ]
}
```
---

## Next steps

Learn how to join tables.

> [!div class="nextstepaction"]
> [Join tables](join-tables.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]