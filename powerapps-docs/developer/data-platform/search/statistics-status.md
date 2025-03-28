---
title: "Dataverse Search statistics and status (Microsoft Dataverse) | Microsoft Docs"
description: "Use Dataverse search statistics and status apis retrieve data about the data structures used to support search and to check the status of Dataverse search."
ms.date: 10/20/2023
ms.reviewer: jdaly
ms.topic: article
author: seanwat-msft
ms.author: seanwat
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
 - jeromeblouinms
---
# Dataverse Search statistics and status

Dataverse search provides two operations you can use to retrieve data about data structures used to support search and check whether search is enabled.

## Statistics

You might need to know the size of the data structure being returned to help you better optimize your query or query results and help you manage the size of your Database to manage cost.

Search statistics provides information about:

- Storage size in bytes
- Storage size in megabytes
- Number of documents


### Statistics examples

The following examples show how to use the `statistics` API.

#### [SDK for .NET](#tab/sdk)

This example is from the [SDK for .NET search operations sample](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp-NETCore/Search) on GitHub.

```csharp
/// <summary>
/// Demonstrate statistics API
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance to use.</param>
/// <returns></returns>
static void OutputSearchStatistics(IOrganizationService service)
{
   Console.WriteLine("OutputSearchStatistics START\n");

   var searchstatisticsResponse = (searchstatisticsResponse)service.Execute(new searchstatisticsRequest());

   JObject ResponseObj = (JObject)JsonConvert.DeserializeObject(value: searchstatisticsResponse.response);

   SearchStatisticsResult results = ResponseObj["value"].ToObject<SearchStatisticsResult>();

   Console.WriteLine($"\tStorageSizeInBytes: {results.StorageSizeInByte}");
   Console.WriteLine($"\tStorageSizeInMb: {results.StorageSizeInMb}");
   Console.WriteLine($"\tDocumentCount: {results.DocumentCount}");

   Console.WriteLine("\nOutputSearchStatistics END");
}
```

#### Output

When you invoke the `OutputSearchStatistics` method with an authenticated instance of the [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) class:

```csharp
OutputSearchStatistics(service: serviceClient);
```

The output looks something like the following:

```
OutputSearchStatistics START

        StorageSizeInBytes: 1341090
        StorageSizeInMb: 1
        DocumentCount: 1309

OutputSearchStatistics END
```

#### Supporting classes

The `OutputSearchStatistics` method depends on the following supporting classes to send the request and process the result:

##### searchstatisticsRequest and searchstatisticsResponse classes

These classes are generated using Power Platform CLI [pac modelbuilder build](/power-platform/developer/cli/reference/modelbuilder#pac-modelbuilder-build) command as described in [Generate early-bound classes for the SDK for .NET](../org-service/generate-early-bound-classes.md).

##### SearchStatisticsResult class

Used to deserialize the `searchstatisticsResponse.response.value` property.

```csharp
class SearchStatisticsResult
{

   /// <summary>
   /// The storage size in Bytes
   /// </summary>
   [JsonProperty(PropertyName = "storagesizeinbytes")]
   public long StorageSizeInByte { get; set; }


   /// <summary>
   /// The storage size in Megabytes
   /// </summary>
   [JsonProperty(PropertyName = "storagesizeinmb")]
   public long StorageSizeInMb { get; set; }

   /// <summary>
   /// The document count
   /// </summary>
   [JsonProperty(PropertyName = "documentcount")]
   public long DocumentCount { get; set; }
}
```

#### [Web API](#tab/webapi)

Use the [searchstatistics function](xref:Microsoft.Dynamics.CRM.searchstatistics) to receive a [searchstatisticsResponse complex type](xref:Microsoft.Dynamics.CRM.searchstatisticsResponse).

**Request**

```http
GET [Organization Uri]/api/data/v9.2/searchstatistics
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
  "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.searchstatisticsResponse",
  "response": "{\"value\":{\"storagesizeinbytes\":4539149,\"storagesizeinmb\":3,\"documentcount\":5515}}"
}
```

The unescaped `response` JSON looks like this:

```json
{
  "value": {
    "storagesizeinbytes": 4539149,
    "storagesizeinmb": 3,
    "documentcount": 5515
  }
}
```

#### [Search 2.0 endpoint](#tab/search)

The response from the `search/v2.0/statistics` endpoint is the same as the Web API. Only the URL is different.

**Request URL**

```http
GET [Organization URI]/api/search/v2.0/statistics
```

---

## Status

Use search status to know:

- Whether search is enabled.
- Which tables and columns are enabled for search.

### Status response types

The status operation returns data using the following types:

#### searchstatusResponse.response.value

The [searchstatusResponse](xref:Microsoft.Dynamics.CRM.searchstatusResponse)`.response` property has a `value` property with the following properties:

|Name|Type|Description|
|---------|---------|---------|
|`entitystatusresults`|[EntityStatusInfo](#entitystatusinfo)[]|[!INCLUDE [entitystatusinfo.description](includes/entitystatusinfo.description.md)]|
|`manytomanyrelationshipsyncstatus`|[ManyToManyRelationshipSyncStatus](#manytomanyrelationshipsyncstatus)[]|[!INCLUDE [manytomanyrelationshipsyncstatus.description](includes/manytomanyrelationshipsyncstatus.description.md)]|
|`status`|[Status](#status)|[!INCLUDE [status.description](includes/status.description.md)]|
|`lockboxstatus`|[LockBoxStatus](#lockboxstatus)|[!INCLUDE [lockboxstatus.description](includes/lockboxstatus.description.md)]|
|`cmkstatus`|[CMKStatus](#cmkstatus)|[!INCLUDE [cmkstatus.description](includes/cmkstatus.description.md)]|

#### EntityStatusInfo

[!INCLUDE [entitystatusinfo.description](includes/entitystatusinfo.description.md)]

|Name|Type|Description|
|---------|---------|---------|
|`entitylogicalname`|string|The logical name of the table|
|`objecttypecode`|string|The object type code of the table.|
|`primarynamefield`|string|The primary column of the table.|
|`lastdatasynctimestamp`|string|The last data sync time.|
|`lastprincipalobjectaccesssynctimestamp`|string|The last principal object access sync time.|
|`entitystatus`|string|The entity level status.|
|`searchableindexedfieldinfomap`|Dictionary<string,[FieldStatusInfo](#fieldstatusinfo)>|The dictionary of indexed column names and details.|

#### FieldStatusInfo

Details for the indexed fields of a table.

|Name|Type|Description|
|---------|---------|---------|
|`indexfieldname`|string|The index field name.|

#### Status

[!INCLUDE [status.description](includes/status.description.md)]

|Name|Value|Description|
|---------|---------|---------|
|`notprovisioned`|0|Organization isn't provisioned for search.|
|`provisioninginprogress`|1|Organization provisioning in progress|
|`provisioned`|2|Organization provisioned for search.|

#### CMKStatus

[!INCLUDE [cmkstatus.description](includes/cmkstatus.description.md)]

More information: [Manage the encryption key](/power-platform/admin/manage-encryption-key)

|Name|Value|Description|
|---------|---------|---------|
|`Unknown`|0|Dataverse search isn't provisioned.|
|`Disabled`|1|Customer managed key is disabled.|
|`Enabled`|2|Customer managed key is enabled.|
|`DisablingInProgress`|3|Customer managed key is in the process of being disabled.|
|`EnablingInProgress`|4|Customer managed key is in the process of being enabled.|

#### LockBoxStatus

[!INCLUDE [lockboxstatus.description](includes/lockboxstatus.description.md)]

More information: [Securely access customer data using Customer Lockbox in Power Platform (preview)](/power-platform/admin/about-lockbox)

|Name|Value|Description|
|---------|---------|---------|
|`Unknown`|0|Dataverse search isn't provisioned.|
|`Disabled`|1|Lockbox is disabled.|
|`Enabled`|2|Lockbox is enabled.|
|`DisablingInProgress`|3|Lockbox is in the process of being disabled.|
|`EnablingInProgress`|4|Lockbox is in the process of being enabled.|

#### ManyToManyRelationshipSyncStatus

[!INCLUDE [manytomanyrelationshipsyncstatus.description](includes/manytomanyrelationshipsyncstatus.description.md)]

|Name|Type|Description|
|---------|---------|---------|
|`relationshipName`|string|The name of the relationship.|
|`relationshipMetadataId`|unique identifier|The ID of the relationship.|
|`searchEntity`|string|The name of the search table.|
|`relatedEntity`|string|The name of the related table.|
|`searchEntityIdAttribute`|string|The name of the primary key of the search table.|
|`relatedEntityIdAttribute`|string|The name of the primary key of the related table.|
|`intersectEntity`|string|The name of the intersect table that supports the many-to-many relationship.|
|`searchEntityObjectTypeCode`|int|The search table object type code.|
|`lastSyncedVersion`|string|The last synchronized version.|

### Status examples

The following samples show the output of the status API.

#### [SDK for .NET](#tab/sdk)

This example is from the [SDK for .NET search operations sample](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/CSharp-NETCore/Search) on GitHub.

```csharp
/// <summary>
/// Demonstrate status API
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance to use.</param>
/// <returns></returns>
static void OutputSearchStatus(IOrganizationService service)
{
    Console.WriteLine("OutputSearchStatus START\n");

    var searchStatusResponse = (searchstatusResponse)service.Execute(new searchstatusRequest());

    JObject ResponseObj = (JObject)JsonConvert.DeserializeObject(searchStatusResponse.response);

    SearchStatusResult results = ResponseObj["value"].ToObject<SearchStatusResult>();

    Console.WriteLine($"\tStatus: {results.Status}");
    Console.WriteLine($"\tLockboxStatus: {results.LockboxStatus}");
    Console.WriteLine($"\tCMKStatus: {results.CMKStatus}");

    if (results.Status == SearchStatus.Provisioned)
    {
        // There will be no results if status is notprovisioned
        if (results.EntityStatusInfo?.Count > 0)
        {
            Console.WriteLine("\tEntity Status Results:\n");
            results.EntityStatusInfo.ForEach(result =>
            {
                Console.WriteLine($"\t\tentitylogicalname: {result.EntityLogicalName}");
                Console.WriteLine($"\t\tobjecttypecode: {result.ObjectTypeCode}");
                Console.WriteLine($"\t\tprimarynamefield: {result.PrimaryNameField}");
                Console.WriteLine($"\t\tlastdatasynctimestamp: {result.LastDataSyncTimeStamp}");
                Console.WriteLine($"\t\tlastprincipalobjectaccesssynctimestamp: {result.LastPrincipalObjectAccessSyncTimeStamp}");
                Console.WriteLine($"\t\tentitystatus: {result.EntityStatus}");

                Console.WriteLine($"\t\tsearchableindexedfieldinfomap:");
                result.SearchableIndexedFieldInfoMap.ToList().ForEach(searchableindexedfield =>
                {
                    Console.WriteLine($"\t\t\t{searchableindexedfield.Key}\t indexfieldname:{searchableindexedfield.Value.IndexFieldName}");
                });
                Console.WriteLine("\n");
            });
        }
    }

    Console.WriteLine("OutputSearchStatus END\n");
}
```

#### Output

When you invoke the `OutputSearchStatus` method with an authenticated instance of the [ServiceClient](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient) class:

```csharp
OutputSearchStatus(service: serviceClient);
```

The output looks something like the following:

```
OutputSearchStatus START

        Status: Provisioned
        LockboxStatus: Disabled
        CMKStatus: Disabled
        Entity Status Results:

                entitylogicalname: account
                objecttypecode: 1
                primarynamefield: name
                lastdatasynctimestamp: 1555508!10/16/2023 02:21:59
                lastprincipalobjectaccesssynctimestamp: 0!10/16/2023 02:22:00
                entitystatus: EntitySyncComplete
                searchableindexedfieldinfomap:
                        accountid        indexfieldname:a_0
                        accountnumber    indexfieldname:a0w
                        address1_city    indexfieldname:a0x
                        createdon        indexfieldname:i_0
                        emailaddress1    indexfieldname:a0y
                        entityimage_url  indexfieldname:h_0
                        modifiedon       indexfieldname:j_0
                        name     indexfieldname:d_0
                        ownerid  indexfieldname:b_0
                        owningbusinessunit       indexfieldname:c_0
                        primarycontactid         indexfieldname:a0z
                        statecode        indexfieldname:f_0
                        statuscode       indexfieldname:g_0
                        telephone1       indexfieldname:a12
                        telephone2       indexfieldname:a13
                        versionnumber    indexfieldname:e_0


                <Additional tables removed for brevity>


OutputSearchStatus END
```


#### Supporting classes

The `OutputSearchStatus` method depends on the following supporting classes to send the request and process the result:

##### searchstatusRequest and searchstatusResponse classes

These classes are generated using Power Platform CLI [pac modelbuilder build](/power-platform/developer/cli/reference/modelbuilder#pac-modelbuilder-build) command as described in [Generate early-bound classes for the SDK for .NET](../org-service/generate-early-bound-classes.md).

##### SearchStatusResult class

Used to deserialize the [searchstatusResponse.response.value](#searchstatusresponseresponsevalue) data.

```csharp
class SearchStatusResult
{
   /// <summary>
   /// The current search status
   /// </summary>
   [JsonProperty("status")]
   public SearchStatus Status { get; set; }

   /// <summary>
   /// The current lockbox status
   /// </summary>
   [JsonProperty("lockboxstatus")]
   public LockboxStatus LockboxStatus { get; set; }

   /// <summary>
   /// The current customer managed key status
   /// </summary>
   [JsonProperty("cmkstatus")]
   public CMKStatus CMKStatus { get; set; }

   /// <summary>
   /// Information on enabled tables
   /// </summary>
   [JsonProperty("entitystatusresults")]
   public List<EntityStatusInfo>? EntityStatusInfo { get; set; }

   /// <summary>
   /// Information about th status of synchronized many-to-many relationships
   /// </summary>
   [JsonProperty("manytomanyrelationshipsyncstatus")]
   public List<ManyToManyRelationshipSyncStatus>? ManyToManyRelationshipSyncStatus { get; set; }
}
```

##### SearchStatus enum

Used to deserialize the [Status](#status) data.

```csharp
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.Runtime.Serialization;

[DataContract]
[JsonConverter(typeof(StringEnumConverter))]
public enum SearchStatus
{
    /// <summary>
    /// Organization is not provisioned for search.
    /// </summary>
    [EnumMember(Value = "notprovisioned")]
    NotProvisioned = 0,

    /// <summary>
    /// Organization provisioning in progress.
    /// </summary>
    [EnumMember(Value = "provisioninginprogress")]
    ProvisioningInProgress = 1,

    /// <summary>
    /// Organization provisioned for search.
    /// </summary>
    [EnumMember(Value = "provisioned")]
    Provisioned = 2,
}
```

##### LockboxStatus enum

Used to deserialize the [LockBoxStatus](#lockboxstatus) data.

```csharp
using Newtonsoft.Json.Converters;
using System.Runtime.Serialization;
using Newtonsoft.Json;

/// <summary>
/// Indicates the status of the lockbox.
/// </summary>
[DataContract]
[JsonConverter(typeof(StringEnumConverter))]
public enum LockboxStatus
{
    /// <summary>
    /// Indicates dataverse search is not provisioned.
    /// </summary>
    [EnumMember]
    Unknown = 0,

    /// <summary>
    /// Indicates lockbox is disabled.
    /// </summary>
    [EnumMember]
    Disabled = 1,

    /// <summary>
    /// Indicates lockbox is enabled.
    /// </summary>
    [EnumMember]
    Enabled = 2,

    /// <summary>
    /// Indicates lockbox is disabling in progress.
    /// </summary>
    [EnumMember]
    DisablingInProgress = 3,

    /// <summary>
    /// Indicates lockbox is enabling in progress.
    /// </summary>
    [EnumMember]
    EnablingInProgress = 4,
}
```

##### CMKStatus enum

Used to deserialize the [CMKStatus](#cmkstatus) data.

```csharp
using Newtonsoft.Json.Converters;
using System.Runtime.Serialization;
using Newtonsoft.Json;

/// <summary>
/// Indicates the status of the customer managed key.
/// </summary>
[DataContract]
[JsonConverter(typeof(StringEnumConverter))]
public enum CMKStatus
{
    /// <summary>
    /// Indicates dataverse search is not provisioned.
    /// </summary>
    [EnumMember]
    Unknown = 0,

    /// <summary>
    /// Indicates customer managed key is disabled.
    /// </summary>
    [EnumMember]
    Disabled = 1,

    /// <summary>
    /// Indicates customer managed key is enabled.
    /// </summary>
    [EnumMember]
    Enabled = 2,

    /// <summary>
    /// Indicates customer managed key is disabling in progress.
    /// </summary>
    [EnumMember]
    DisablingInProgress = 3,

    /// <summary>
    /// Indicates customer managed key is enabling in progress.
    /// </summary>
    [EnumMember]
    EnablingInProgress = 4,
}
```

##### EntityStatusInfo class

Used to deserialize the [EntityStatusInfo](#entitystatusinfo) data.

```csharp
using Newtonsoft.Json;

public sealed class EntityStatusInfo
{
    /// <summary>
    /// Gets or sets the entity logical name.
    /// </summary>
    [JsonProperty(PropertyName = "entitylogicalname")]
    public string EntityLogicalName { get; set; }

    /// <summary>
    /// Gets or sets the object type code.
    /// </summary>
    [JsonProperty(PropertyName = "objecttypecode")]
    public int ObjectTypeCode { get; set; }

    /// <summary>
    /// Gets or sets the primary field name.
    /// </summary>
    [JsonProperty(PropertyName = "primarynamefield")]
    public string PrimaryNameField { get; set; }

    /// <summary>
    /// Gets or sets the last data sync time.
    /// </summary>
    [JsonProperty(PropertyName = "lastdatasynctimestamp")]
    public string LastDataSyncTimeStamp { get; set; }

    /// <summary>
    /// Gets or sets the last principal object access sync time.
    /// </summary>
    [JsonProperty(PropertyName = "lastprincipalobjectaccesssynctimestamp")]
    public string LastPrincipalObjectAccessSyncTimeStamp { get; set; }

    /// <summary>
    /// Gets or sets entity level status.
    /// </summary>
    [JsonProperty(PropertyName = "entitystatus")]
    public string EntityStatus { get; set; }

    /// <summary>
    /// Gets or sets the dictionary of attribute name and details.
    /// </summary>
    [JsonProperty(PropertyName = "searchableindexedfieldinfomap")]
    public IDictionary<string, FieldStatusInfo> SearchableIndexedFieldInfoMap { get; set; }
}
```

##### FieldStatusInfo class

Used to deserialize the [FieldStatusInfo](#fieldstatusinfo) data.

```csharp
using Newtonsoft.Json;
using System.Diagnostics.CodeAnalysis;

namespace PowerApps.Samples.Search.Types;

[ExcludeFromCodeCoverage]
public sealed class FieldStatusInfo
{
    /// <summary>
    /// Gets or sets index field name.
    /// </summary>
    [JsonProperty(PropertyName = "indexfieldname")]
    public string IndexFieldName { get; set; }
}
```

##### ManyToManyRelationshipSyncStatus class

Used to deserialize the [ManyToManyRelationshipSyncStatus](#manytomanyrelationshipsyncstatus) data.

```csharp
using Newtonsoft.Json;

public sealed class ManyToManyRelationshipSyncStatus
{   
    /// <summary>
    /// Gets the relationship name.
    /// </summary>
    [JsonProperty("relationshipName")]
    public string? RelationshipName { get; }

    /// <summary>
    /// Gets the relationship metadata id.
    /// </summary>
    [JsonProperty("relationshipMetadataId")]
    public Guid RelationshipMetadataId { get; }

    /// <summary>
    /// Gets the search entity name.
    /// </summary>
    [JsonProperty("searchEntity")]
    public string? SearchEntity { get; }

    /// <summary>
    /// Gets the second entity name.
    /// </summary>
    [JsonProperty("relatedEntity")]
    public string? RelatedEntity { get; }

    /// <summary>
    /// Gets the search entity Id attribute.
    /// </summary>
    [JsonProperty("searchEntityIdAttribute")]
    public string? SearchEntityIdAttribute { get; }

    /// <summary>
    /// Gets the related entity Id attribute.
    /// </summary>
    [JsonProperty("relatedEntityIdAttribute")]
    public string? RelatedEntityIdAttribute { get; }

    /// <summary>
    /// Gets the intersect entity name.
    /// </summary>
    [JsonProperty("intersectEntity")]
    public string? IntersectEntity { get; }

    /// <summary>
    /// Gets the search entity object type code.
    /// </summary>
    [JsonProperty("searchEntityObjectTypeCode")]
    public int SearchEntityObjectTypeCode { get; }

    /// <summary>
    /// Gets the synced version.
    /// </summary>
    [JsonProperty("lastSyncedVersion")]
    public string? LastSyncedDataVersion { get; }
}
```

#### [Web API](#tab/webapi)

Use the [searchstatus function](xref:Microsoft.Dynamics.CRM.searchstatus) to receive a [searchstatusResponse complex type](xref:Microsoft.Dynamics.CRM.searchstatusResponse).

**Request**

```http
GET [Organization URI]/api/data/v9.2/searchstatus HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

```

When not provisioned, you should get a response like this:

**Response**

```http
HTTP/1.1 200 OK

{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.searchstatusResponse",
  "response": "{\"value\":{\"status\":\"notprovisioned\",\"lockboxstatus\":\"Unknown\"}}"
}
```

When search is enabled, there's more data that describes the search status for the org. See [Status response types](#status-response-types) for details.

**Response**

```http
HTTP/1.1 200 OK

{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.searchstatusResponse",
  "response": "{\"value\":{\"entitystatusresults\":[{\"entitylogicalname\":\"account\",\"objecttypecode\":1,\"primarynamefield\":\"name\",\"lastdatasynctimestamp\":\"73630169!09/12/2022 14:26:14\",\"lastprincipalobjectaccesssynctimestamp\":\"72969347!09/12/2022 14:26:14\",\"entitystatus\":\"EntitySyncComplete\",\"searchableindexedfieldinfomap\":{\"emailaddress1\":{\"indexfieldname\":\"a3x\"},\"address1_city\":{\"indexfieldname\":\"a3y\"},\"modifiedon\":{\"indexfieldname\":\"j_0\"},\"telephone1\":{\"indexfieldname\":\"a3z\"},\"statecode\":{\"indexfieldname\":\"f_0\"},\"primarycontactid\":{\"indexfieldname\":\"a40\"},\"statuscode\":{\"indexfieldname\":\"g_0\"},\"createdon\":{\"indexfieldname\":\"i_0\"},\"entityimage_url\":{\"indexfieldname\":\"h_0\"},\"industrycode\":{\"indexfieldname\":\"a43\"},\"name\":{\"indexfieldname\":\"d_0\"},\"owningbusinessunit\":{\"indexfieldname\":\"c_0\"},\"crdcb_testrollupfield\":{\"indexfieldname\":\"a45\"},\"ownerid\":{\"indexfieldname\":\"b_0\"},\"accountnumber\":{\"indexfieldname\":\"a46\"},\"telephone2\":{\"indexfieldname\":\"a47\"},\"versionnumber\":{\"indexfieldname\":\"e_0\"},\"accountid\":{\"indexfieldname\":\"a_0\"},\"crdcb_throwawaydate\":{\"indexfieldname\":\"a48\"},\"crdcb_budget\":{\"indexfieldname\":\"a8f\"}}}, 
  
  <Information on other tables removed for brevity> 
  
  ],\"status\":\"provisioned\",\"lockboxstatus\":\"Disabled\",\"cmkstatus\":\"Disabled\"}}"
}
```

When unescaped, the JSON of the `response.value` property looks like this:

```json
{
  "value": {
    "entitystatusresults": [
      {
        "entitylogicalname": "account",
        "objecttypecode": 1,
        "primarynamefield": "name",
        "lastdatasynctimestamp": "73630169!09/12/2022 14:26:14",
        "lastprincipalobjectaccesssynctimestamp": "72969347!09/12/2022 14:26:14",
        "entitystatus": "EntitySyncComplete",
        "searchableindexedfieldinfomap": {
          "emailaddress1": { "indexfieldname": "a3x" },
          "address1_city": { "indexfieldname": "a3y" },
          "modifiedon": { "indexfieldname": "j_0" },
          "telephone1": { "indexfieldname": "a3z" },
          "statecode": { "indexfieldname": "f_0" },
          "primarycontactid": { "indexfieldname": "a40" },
          "statuscode": { "indexfieldname": "g_0" },
          "createdon": { "indexfieldname": "i_0" },
          "entityimage_url": { "indexfieldname": "h_0" },
          "industrycode": { "indexfieldname": "a43" },
          "name": { "indexfieldname": "d_0" },
          "owningbusinessunit": { "indexfieldname": "c_0" },
          "ownerid": { "indexfieldname": "b_0" },
          "accountnumber": { "indexfieldname": "a46" },
          "telephone2": { "indexfieldname": "a47" },
          "versionnumber": { "indexfieldname": "e_0" },
          "accountid": { "indexfieldname": "a_0" }
        }
      },

      <Information on other tables removed for brevity> 

    ],
    "status": "provisioned",
    "lockboxstatus": "Disabled",
    "cmkstatus": "Disabled"
  }
}
```

#### [Search 2.0 endpoint](#tab/search)

The response from the `search/v2.0/status` endpoint is the same as the Web API. Only the URL is different.

**Request URL**

```http
GET [Organization URI]/api/search/v2.0/status
```

---

### See also

[Search for Dataverse records](overview.md)   
[Dataverse Search query](query.md)   
[Dataverse Search suggest](suggest.md)   
[Dataverse Search autocomplete](autocomplete.md)   
[Dataverse legacy search](legacy.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]



