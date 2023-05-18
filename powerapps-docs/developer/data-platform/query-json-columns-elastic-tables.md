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

## Create a column with Json format

This example creates a string column `contoso_SensorValue` with Json format in our `contoso_SensorData` elastic table. For cases where large json need to be stored, instead of using `StringAttributeMetadata` type, we can use `MemoAttributeMetadata` type with JSON format.

#### [SDK for .NET](#tab/sdk)

This function creates a new <xref:Microsoft.Xrm.Sdk.Metadata.StringAttributeMetadata> column using the <xref:Microsoft.Xrm.Sdk.Messages.CreateAttributeRequest> class.

```csharp
public static Guid CreateJsonAttribute(IOrganizationService service)
{
   var request = new CreateAttributeRequest
   {
         EntityName = "contoso_sensordata",
         Attribute = new StringAttributeMetadata
         {
            SchemaName = "contoso_SensorValue",
            RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
            MaxLength = 1000,
            FormatName = StringFormatName.Json,
            DisplayName = new Label("Sensor Value", 1033),
            Description = new Label("Stores unstructured sensor data as reported by device", 1033)
         }
   };

   var response = (CreateAttributeResponse)service.Execute(request);

   return response.AttributeId;
}
```

More information: [Add a String column to a table](org-service/create-custom-entity.md#add-a-string-column-to-the-custom-table)


#### [Web API](#tab/webapi)

This request creates a new <xref:Microsoft.Dynamics.CRM.StringAttributeMetadata> column by posting to the Web API `EntityDefinitions` resource referring to the `contoso_sensordata` table.

**Request**

```http
POST [Organization URI]/api/data/v9.2/EntityDefinitions(LogicalName='contoso_sensordata')/Attributes
MSCRM.SolutionUniqueName: examplesolution
Accept: application/json  
Content-Type: application/json; charset=utf-8  
OData-MaxVersion: 4.0  
OData-Version: 4.0  

{
   "AttributeType":"String",
   "AttributeTypeName":{
      "Value":"StringType"
   },
   "Description":{
      "@odata.type":"Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels":[
         {
            "@odata.type":"Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label":"Contains sensor data reported by IOT devices as JSON values",
            "LanguageCode":1033
         }
      ]
   },
   "DisplayName":{
      "@odata.type":"Microsoft.Dynamics.CRM.Label",
      "LocalizedLabels":[
         {
            "@odata.type":"Microsoft.Dynamics.CRM.LocalizedLabel",
            "Label":"sensorvalue",
            "LanguageCode":1033
         }
      ]
   },
   "RequiredLevel":{
      "Value":"None",
      "CanBeChanged":true,
      "ManagedPropertyLogicalName":"canmodifyrequirementlevelsettings"
   },
   "SchemaName":"sensorvalue",
   "@odata.type":"Microsoft.Dynamics.CRM.StringAttributeMetadata",
   "FormatName":{
      "Value":"Json"
   },
   "MaxLength":3500
}
```

**Response**

```http
HTTP/1.1 204 No Content  
OData-Version: 4.0  
OData-EntityId: [Organization URI]/api/data/v9.2/EntityDefinitions(402fa40f-287c-e511-80d2-00155d2a68d2)/Attributes(f01bef16-287c-e511-80d2-00155d2a68d2)  
```

More information: [Create columns](webapi/create-update-entity-definitions-using-web-api.md#create-columns)

---

## Set Json column data

This example creates a row in `contoso_SensorData` elastic table with JSON values in the `contoso_Value` column.

#### [SDK for .NET](#tab/sdk)

```csharp
public static Guid CreateWithJsonData(IOrganizationService service, string deviceId, ref string sessionToken)
{
   var entity = new Entity("contoso_sensordata")
   {
         Attributes =
         {
            { "contoso_sensorvalue", "{\"type\":\"Humidity\",\"value\": \"40\",\"timestamp\":\"2023-05-01Z05:00:00\"}" },
            { "contoso_deviceid", deviceId },
            { "partitionid", deviceId }
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

{
   "contoso_sensorvalue": "{\"type\":\"Humidity\",\"value\": \"40\",\"timestamp\":\"2023-05-01Z05:00:00\"}",
   "contoso_deviceid" : "device-001",
   "partitionid" : "device-001"
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

This example runs a query on `contoso_SensorData` elastic table with filter on sensorvalue.type json element to be equal to "Humidity".

All table columns can be queried with a `c.props` prefix to the schema name of the columns where `"c"` is an alias or a shorthand notation for the elastic table being queried. For example, `contoso_deviceid` column in `contoso_sensordata` table can be referenced in the Cosmos SQL query using `c.props.contoso_deviceid`.

#### [SDK for .NET](#tab/sdk)

The SDK for .NET doesn't yet have request and response classes for the  `ExecuteCosmosSqlQuery` message. You can use <xref:Microsoft.Xrm.Sdk.OrganizationRequest> and <xref:Microsoft.Xrm.Sdk.OrganizationResponse> classes. 

<!-- TODO This sample didn't work for me -->

```csharp
public static List<SensorValue> QueryJsonAttribute(IOrganizationService service)
{
    var request = new OrganizationRequest("ExecuteCosmosSqlQuery");
    
    request.Parameters["EntityLogicalName"] = "cr03e_hyperdocument";
    request.Parameters["QueryText"] = "select c.sensorvalue.type, c.sensorvalue.value, c.deviceid * from c where c.props.sensorvalue.type='Humidity'";

    OrganizationResponse response = service.Execute(request);

    // Deserialized query result into a class with expected schema.
    Entity result = (Entity)response.Results["Result"];    
    return JsonConvert.Deserialize<List<SensorValue>>(result["Result"].ToString());
}

public class SensorValue
{
   [JsonProperty("type")]
   public string Type {get;set;}
   [JsonProperty("value")]
   public string Value {get;set;}
   [JsonProperty("deviceid")]
   public string DeviceId {get;set;}
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
   @p1='select c.contoso_sensorvalue.type, c.contoso_sensorvalue.value, c.contoso_deviceid * from c where c.props.sensorvalue.type=@sensortype'
   &@p2='contoso_sensordata'
   &@p3={'Keys':['@sensortype'],'Values':[{'Type':'System.String','Value':'Humidity'}]}
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
            "type" : "Humidity",
            "value": "60",
            "deviceid" : "device-001"
        },
        {
            "type" : "Humidity",
            "value": "80",
            "deviceid" : "device-002"
        },
        {
            "type" : "Humidity",
            "value": "15",
            "deviceid" : "device-003"
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