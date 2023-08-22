---
title: Query JSON columns in elastic tables (preview)
description: Learn how to query data stored in JSON columns with Dataverse elastic tables with code.
ms.topic: article
ms.date: 06/10/2023
author: pnghub
ms.author: gned
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors:
 - sumantb-msft
 - JimDaly
---
# Query JSON columns in elastic tables (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Elastic tables support the JavaScript Object Notation (JSON) format for text columns. These columns can be used to store schema-less arbitrary JSON according to application needs. You can use the `ExecuteCosmosSQLQuery` message to run any Cosmos SQL query directly against your elastic table and filter rows based on properties inside JSON.

For an example that shows how to create a JSON column, see [Create a column with JSON format](create-elastic-tables.md#create-a-column-with-json-format).

## Set JSON column data

This example creates a row in the `contoso_SensorData` elastic table that has JSON data in the `contoso_EnergyConsumption` column.

#### [SDK for .NET](#tab/sdk)

```csharp
public static Guid CreateWithJsonData(
    IOrganizationService service, 
    string deviceId, 
    ref string sessionToken)
{
    var entity = new Entity("contoso_sensordata")
    {
        Attributes =
        {
            { "contoso_deviceid", deviceId },
            { "contoso_sensortype", "Humidity" },
            { "contoso_value", 40 },
            { "contoso_energyconsumption", "{ \"power\": 0.55, \"powerUnit\":\"kWh\", \"voltage\": 2, \"voltageUnit\": \"kV\" }",
            { "contoso_timestamp", DateTime.UtcNow},
            { "partitionid", deviceId },
            { "ttlinseconds", 86400  }  // 86400  seconds in a day
        }
    };

    var request = new CreateRequest
    {
        Target = entity
    };

    var response = (CreateResponse)service.Execute(request);

    // Capture the session token
    sessionToken = response.Results["x-ms-session-token"].ToString();

    return response.id;
}
```

#### [Web API](#tab/webapi)

**Request:**

```http
POST [Organization URI]/api/data/v9.2/contoso_sensordatas
Content-Type: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0

{
    "contoso_deviceid" : "device-001",
    "contoso_sensortype", "Humidity",
    "contoso_value", 40,
    "contoso_energyconsumption": "{ \"power\": 0.55, \"powerUnit\":\"kWh\", \"voltage\": 2, \"voltageUnit\": \"kV\" }",
    "contoso_timestamp", DateTime.UtcNow},
    "partitionid", device-001
    "ttlinseconds", 86400,  // 86400  seconds in a day
}
```

**Response:**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
x-ms-session-token: hj23ad#1543
OData-EntityId: [Organization URI]/api/data/v9.2/sensordata(7eb682f1-ca75-e511-80d4-00155d2a68d1)
```

---

## Query JSON column data

This example runs a query on the `contoso_SensorData` elastic table to filter for all rows where the `energyconsumption.power` value is more than 5.

All table columns can be queried by using a `c.props` prefix on the schema name of the columns. In this prefix, `c` is an alias or shorthand notation for the elastic table that is being queried. For example, the `contoso_deviceid` column in the `contoso_sensordata` table can be referenced in the Cosmos SQL query by using `c.props.contoso_deviceid`.

[Learn about queries in Azure Cosmos DB for NoSQL](/azure/cosmos-db/nosql/query/getting-started).

#### [SDK for .NET](#tab/sdk)

The SDK for .NET doesn't yet have request and response classes for the `ExecuteCosmosSqlQuery` message. You can use the [OrganizationRequest class](xref:Microsoft.Xrm.Sdk.OrganizationRequest) and the [OrganizationResponse class](xref:Microsoft.Xrm.Sdk.OrganizationResponse).

The `ExecuteCosmosSqlQuery` message has the following input parameters.

| Name | Type | Description |
|------|------|-------------|
| `QueryText` | String | (Required) The Cosmos SQL query. |
| `EntityLogicalName`| String | (Required) The logical name of the table. |
| `QueryParameters` | [ParameterCollection](xref:Microsoft.Xrm.Sdk.ParameterCollection) | (Optional) Values for any parameters that are specified in the `QueryText` parameter. |
| `PageSize`| Long | (Optional) The number of records to return on a single page. |
| `PagingCookie`| String | (Optional) The paging cookie to use. |
| `PartitionId` | String | (Optional) The `Partitionid` value to set the scope of the query. |

`ExecuteCosmosSqlQuery` returns an [Entity](xref:Microsoft.Xrm.Sdk.Entity) that is an open type. This entity has the following attributes.

| Name | Type | Description |
|------|------|-------------|
| `PagingCookie` | String | A value to set for subsequent requests when there are more results. |
| `HasMore` | Bool | A value that indicates whether there are more records in the results. |
| `Result` | String | JSON with values for the results.|

```csharp
public static List<QueryResult> QueryJsonAttribute(IOrganizationService service)
{
    StringBuilder query = new();
    query.Append("select c.props.contoso_deviceid as deviceId, ");
    query.Append("c.props.contoso_timestamp as timestamp, ");
    query.Append("c.props.contoso_energyconsumption.power as power ");
    query.Append("from c where c.props.contoso_sensortype='Humidity' ");
    query.Append("and c.props.contoso_energyconsumption.power > 5");

    var request = new OrganizationRequest("ExecuteCosmosSqlQuery")
    {
        Parameters = {
            { "EntityLogicalName","contoso_sensordata" },
            { "QueryText", query.ToString() }
        }
    };

    OrganizationResponse response = service.Execute(request);

    // Deserialized query result into a class with expected schema.
    Entity result = (Entity)response.Results["Result"];
    return JsonConvert.DeserializeObject<List<QueryResult>>(result["Result"].ToString());
}

public class QueryResult
{
    [JsonProperty("deviceId")]
    public string DeviceId {get;set;}
    [JsonProperty("timestamp")]
    public DateTime Timestamp {get;set;}
    [JsonProperty("power")]
    public int Power {get;set;}
}

```

- [Learn about open types in Dataverse](use-open-types.md)
- [Learn to use messages with the Organization service](org-service/use-messages.md)

#### [Web API](#tab/webapi)

This request uses the [ExecuteCosmosSqlQuery function](xref:Microsoft.Dynamics.CRM.ExecuteCosmosSqlQuery).

**Request:**

```http
GET [Organization URI]/api/data/v9.2/ExecuteCosmosSqlQuery(
    QueryText=@p1,
    EntityLogicalName=@p2,
    QueryParameters=@p3)?
    @p1='select c.props.contoso_deviceid as deviceId, c.props.contoso_timestamp as timestamp, c.props.contoso_energyconsumption.power as power from c where c.props.contoso_sensortype=@sensortype and c.props.contoso_energyconsumption.power > @power'
    &@p2='contoso_sensordata'
    &@p3={'Keys':['@sensortype', '@power'],'Values':[{'Type':'System.String','Value':'Humidity'}, {'Type':'System.Int32','Value': '5'}]}
```

**Response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; odata.metadata=minimal
OData-Version: 4.0

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#executecosmossqlquery",
    "Result": [
        {
            "deviceid" : "device-001"
            "timestamp" : "2023-05-05T16:30:00Z",
            "power": "12"
        },
        {
            "deviceid" : "device-001"
            "timestamp" : "2023-05-05T07:00:00Z",
            "power": "7"
        },
        {
            "deviceid" : "device-002"
            "timestamp" : "2023-05-01T05:00:00Z",
            "power": "16"
        }
    ]
}
```

---

## Next steps

> [!div class="nextstepaction"]
> [Elastic table sample code (preview)](elastic-table-samples.md)<br/>

### See also

[Elastic tables for developers (preview)](elastic-tables.md)   
[Create elastic tables using code (preview)](create-elastic-tables.md)   
[Use elastic tables using code (preview)](use-elastic-tables.md)   
[Bulk operation messages (preview)](bulk-operations.md)   
[Elastic table sample code (preview)](elastic-table-samples.md)
