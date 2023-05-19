---
title: "Query JSON columns in elastic tables (Preview) (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to query data stored in JSON columns with elastic tables with code" # 115-145 characters including spaces. This abstract displays in the search result.
ms.topic: article
ms.date: 05/18/2022
author: pnghub
ms.author: gned
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors:
 - sumantb-msft
 - JimDaly
---
# Query JSON columns in elastic tables (Preview)

Elastic table supports a new JSON format for text columns. This column can be used to store schema-less arbitrary json as per application needs. You can use the `ExecuteCosmosSQLQuery` message to run any Cosmos SQL query directly against your elastic table and filter rows based on properties inside JSON.

For an example showing how to create a JSON column, see [Create a column with Json format](create-elastic-tables.md#create-a-column-with-json-format)

## Set Json column data

This example creates a row in `contoso_SensorData` elastic table with JSON data in the `contoso_energyconsumption` column.

#### [SDK for .NET](#tab/sdk)

```csharp
public static Guid CreateWithJsonData(IOrganizationService service, string deviceId, ref string sessionToken)
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

**Request**

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

**Response**

```http
HTTP/1.1 204 No Content
OData-Version: 4.0
x-ms-session-token: hj23ad#1543
OData-EntityId: [Organization URI]/api/data/v9.2/sensordata(7eb682f1-ca75-e511-80d4-00155d2a68d1)
```

---


## Query Json column data

This example runs a query on `contoso_SensorData` elastic table with filters all rows which has `energyconsumption.power` greater than 5

All table columns can be queried with a `c.props` prefix to the schema name of the columns where `"c"` is an alias or a shorthand notation for the elastic table being queried. For example, `contoso_deviceid` column in `contoso_sensordata` table can be referenced in the Cosmos SQL query using `c.props.contoso_deviceid`.

#### [SDK for .NET](#tab/sdk)

The SDK for .NET doesn't yet have request and response classes for the  `ExecuteCosmosSqlQuery` message. You can use <xref:Microsoft.Xrm.Sdk.OrganizationRequest> and <xref:Microsoft.Xrm.Sdk.OrganizationResponse> classes. 

<!-- TODO This sample didn't work for me -->

```csharp
public static List<QueryResult> QueryJsonAttribute(IOrganizationService service)
{
    var request = new OrganizationRequest("ExecuteCosmosSqlQuery");
    
    request.Parameters["EntityLogicalName"] = "contoso_sensordata";
    request.Parameters["QueryText"] = "select c.props.contoso_deviceid as deviceId, c.props.contoso_timestamp as timestamp, c.props.contoso_energyconsumption.power as power from c where c.props.contoso_sensortype='Humidity' and c.props.contoso_energyconsumption.power > 5";

    OrganizationResponse response = service.Execute(request);

    // Deserialized query result into a class with expected schema.
    Entity result = (Entity)response.Results["Result"];    
    return JsonConvert.Deserialize<List<QueryResult>>(result["Result"].ToString());
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

More information: [Use messages with the Organization service](org-service/use-messages.md)

#### [Web API](#tab/webapi)

This request uses the [ExecuteCosmosSqlQuery Function](xref:Microsoft.Dynamics.CRM.ExecuteCosmosSqlQuery).

**Request**

```http
GET [Organization URI]/api/data/v9.2/ExecuteCosmosSqlQuery(
   QueryText=@p1,
   EntityLogicalName=@p2,
   QueryParameters=@p3)?
   @p1='select c.props.contoso_deviceid as deviceId, c.props.contoso_timestamp as timestamp, c.props.contoso_energyconsumption.power as power from c where c.props.contoso_sensortype=@sensortype and c.props.contoso_energyconsumption.power > @power'
   &@p2='contoso_sensordata'
   &@p3={'Keys':['@sensortype', '@power'],'Values':[{'Type':'System.String','Value':'Humidity'}, {'Type':'System.Int32','Value': 5}]}
```

**Response**

```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#executecosmossqlquery",
    "Result": [
        {
            "deviceid" : "device-001"
            "timestamp" : "2023-05-02T16:30:00Z",
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

Learn how to perform bulk operations on elastic tables with code.

> [!div class="nextstepaction"]
> [Bulk operations with elastic tables](bulk-operations-elastic-tables.md)<br/>

### See also

[Use elastic tables (Preview)](elastic-tables.md)<br />
[Create elastic tables (Preview)](create-elastic-tables.md)<br />
[Use elastic tables (Preview)](use-elastic-tables.md)<br />
[Bulk operations with elastic tables (Preview)](bulk-operations-elastic-tables.md)<br />