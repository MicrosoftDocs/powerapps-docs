---
title: "Dataverse Search status (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use Dataverse search status to check the status of Dataverse search." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 09/12/2022
ms.reviewer: jdaly
ms.topic: article
author: mspilde # GitHub ID
ms.author: mspilde # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
---
# Dataverse Search status

Use search status to know:

- Whether search is enabled.
- Which tables and columns are enabled for search.

#### [SDK for .NET](#tab/sdk)

```csharp
static void CheckSearchStatus(IOrganizationService service) {
   try
   {     
      OrganizationResponse searchStatusResponse = (searchstatusResponse)service.Execute(new OrganizationRequest("searchstatus"));
  
      string responseString = searchStatusResponse.Results["response"];

      Console.WriteLine(responseString);
      //Expect that this value is an escaped string containing JSON that must be parsed
   }
   catch (FaultException<OrganizationServiceFault> osf)
   {
      Console.WriteLine($"OrganizationServiceFault:{osf.Message}");
      // Fails here, Due to plug-in in Custom API?

      /*
      ErrorCode: 0x80048D0A IsvAbortedInternalServerError
      Message: Object reference not set to an instance of an object.
      
      */
   }
   catch (Exception ex) {

      Console.WriteLine($"Exception:{ex.Message}");
   }      
}
```

**Output**

```
//TODO: Should be the same as the Web API.
```

#### [Web API](#tab/webapi)

**Request**

```http
GET [Organization URI]/api/data/v9.2/searchstatus HTTP/1.1
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

```

The `response` property returned by <xref:Microsoft.Dynamics.CRM.searchstatusResponse?text=searchstatusResponse ComplexType> is an escaped string containing JSON data. The `status` property value can be either: `notprovisioned`, `provisioninginprogress`, or `provisioned`.

When not provisioned, you should get a response like this:

**Response**

```http
HTTP/1.1 200 OK

{
  "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.searchstatusResponse",
  "response": "{\"value\":{\"status\":\"notprovisioned\",\"lockboxstatus\":\"Unknown\"}}"
}
```

When search is enabled, there is more data that describes the search status for the org.

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

When unescaped, the JSON of the `response` property looks like this:

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

The `entitystatusresults` contains information about each table configured for search. For each table, the `searchableindexedfieldinfomap` tells you which columns are included in search for that table. The `indexfieldname` property is for internal use only.

- `lockboxstatus` refers to the Power Platform Customer Lockbox. More information: [Securely access customer data using Customer Lockbox in Power Platform (preview)](/power-platform/admin/about-lockbox)
- `cmkstatus` refers to whether the environment has a customer managed key. More information: [Manage the encryption key](/power-platform/admin/manage-encryption-key)


#### [Search 2.0 endpoint](#tab/search)

**Request**

```http
GET [Organization URI]/api/search/v2.0/status HTTP/1.1
```

The response from the search endpoint is the same as the Web API.

---


### See also

[Search for Dataverse records](overview.md)<br />
[Dataverse Search query](query.md)<br />
[Dataverse Search suggest](suggest.md)<br />
[Dataverse Search autocomplete](autocomplete.md)<br />
[Dataverse Search statistics](statistics.md)<br />
[Dataverse legacy search](legacy.md)

[!INCLUDE [footer-banner](../../../includes/footer-banner.md)]