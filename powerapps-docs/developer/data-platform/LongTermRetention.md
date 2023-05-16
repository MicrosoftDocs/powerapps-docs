---
title: "Long Term Retention (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Long term retention is a dataverse capability which allows customer to transfer the data from their transactional database to the dataverse managed data lake." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 05/16/2023
ms.reviewer: "pehecke"

ms.topic: "article"
author: "kagoswami" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "kagoswami" # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
---

# Long Term Retention

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

*Long term retention* is a dataverse capability which allows customer to transfer the data from their transactional database to the dataverse managed data lake.To perform the LTR operations, customer is required to setup retention policies by defining the criteria for a given table. To setup the retention policy, you should have org and table both enabled for retention.
  
## Setup retention API

You can setup the retention policy by creating an entry in retention config table. As part of retention policy setup, platform will validate the policy against the SDK Message Validate Retention Config.

https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/validateretentionconfig?view=dataverse-latest 
  
### Sample Configuration

#### [OData Web API](#tab/webapi)

RetentionConfig Table: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/retentionconfig?view=dataverse-latest

The following is an example of JSON body to retain all the closed opportunities and will run on a yearly basis.

**Request**

```http
POST [Organization Uri]/api/data/v9.1/retentionconfigs
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**JSON body**

```json
{
            "statecode": 0,
            "name": "Retain all closed opportunities",
            "uniquename": "ui_RetainAllClosedOpportunities",
            "statuscode": 10,
            "criteria": "<fetch version=\"1.0\" output-format=\"xml-platform\" mapping=\"logical\" distinct=\"false\"><entity name=\"opportunity\"><attribute name=\"name\" /><attribute name=\"statecode\" /><attribute name=\"actualvalue\" /><attribute name=\"actualclosedate\" /><attribute name=\"customerid\" /><attribute name=\"opportunityid\" /><order attribute=\"actualclosedate\" descending=\"true\" /><filter type=\"and\"><filter type=\"or\"><condition attribute=\"statecode\" operator=\"eq\" value=\"1\" /><condition attribute=\"statecode\" operator=\"eq\" value=\"2\" /></filter></filter></entity></fetch>",
            "starttime": "2023-05-01T00:00:00",
            "recurrence": "FREQ=YEARLY;INTERVAL=1" 
            "retentionconfigid": "35cc1317-20b7-4f4f-829d-5d9d5d77f712",
            "entitylogicalname": "incident"
}
```

> [!NOTE]
> If you want to run retention only once, keep recurrence value as empty.

#### [SDK for .NET](#tab/sdk)

The following is example code which can be used in a console app or any application using the Dataverse SDK to create retention config. 
See Dataverse SDK documentation for more information: https://docs.microsoft.com/en-us/power-apps/developer/data-platform/org-service/quick-start-org-service-console-app 

#### [Solution Tmport](#tab/solutionimport)

Retention policy can be configured as a solution import. See more information about solution: https://learn.microsoft.com/en-us/power-apps/maker/data-platform/solutions-overview.

Sample customization.xml to create retention policy.

```xml
<retentionconfig retentionconfigid="8fd449d1-f389-4f63-84c6-023c77275359">
  <criteria>&lt;fetch version="1.0" output-format="xml-platform" mapping="logical" distinct="true"&gt;
    &lt;entity name="incident"&gt;
        &lt;attribute name="title"/&gt;
        &lt;attribute name="incidentid"/&gt;
        &lt;attribute name="prioritycode"/&gt;
        &lt;filter type="and"&gt;
            &lt;condition attribute="prioritycode" operator="eq" value="3"/&gt;
        &lt;/filter&gt;
    &lt;/entity&gt;
&lt;/fetch&gt;</criteria>
  <entitylogicalname>incident</entitylogicalname>
  <iscustomizable>1</iscustomizable>
  <name>Resolved Cases in EastR1</name>
  <recurrence>FREQ=MONTHLY;INTERVAL=1</recurrence>
  <referenceconfigid>360ec029-5688-42e0-bc56-34833c8233d5</referenceconfigid>
  <starttime>5/5/2023 6:32:50 PM</starttime>
  <statecode>0</statecode>
  <statuscode>10</statuscode>
  <timezoneruleversionnumber>0</timezoneruleversionnumber>
  <uniquename>ui_360ec029-5688-42e0-bc56-34833c8233d5</uniquename>
</retentionconfig>
```
---

## Add Custom Validation to Retention Policy

Table and App owner can add their own custom validations whenever retention policy is create/updated.Those can be done by registering the plugin against the ValidateRetentionConfig Action.
It is an entity bound action, which gets bound to entity whenever it is enabled retention.
More information: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/validateretentionconfig?view=dataverse-latest 

### Sample Configuration

#### [OData Web API](#tab/webapi)

The following is an example of JSON body to validate all the closed opportunities and will run on a yearly basis.

**Request**

```http
POST [Organization Uri]/api/data/v9.1/ValidateRetentionConfig
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**JSON body**

```json
{
"PageSize":1000,
"FetchXml": "<fetch version='1.0' output-format='xml-platform' mapping='logical' distinct='false'>
<entity name='account'>
<attribute name='accountid' />
<order attribute='name' descending='false' />
<filter type='and'>
<condition attribute='name' operator='like' value='Name%' />
</filter>
</entity>
</fetch>",
"EntityName" : "account"
}
```

#### [SDK for .NET](#tab/sdk)

The following is example code which can be used in a console app or any application using the Dataverse SDK to create retention config. 
See Dataverse SDK documentation for more information: https://docs.microsoft.com/en-us/power-apps/developer/data-platform/org-service/quick-start-org-service-console-app

---

## Add Pre and Post processing during retain and purge

#### [OData Web API](#tab/webapi)

There is an SDK Message *Retain* which gets called whenever record is marked for retention.
If customer want to add any custom logic during the record being marked for retention, plugin can be added to this.
More information: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/retain?view=dataverse-latest 

**Request**

```http
POST [Organization Uri]/api/data/v9.1/Retain
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json
```

**JSON body**

The following is an example of JSON body to call all the retention on the opportunity record.

```json
{
"OperationId":"fd2639b2-f300-408c-b605-75febff98d4f" ,
"Target":{
"@odata.type": "Microsoft.Dynamics.CRM.opportunity",
"opportunityid": "8b9cc8c0-8c08-46cf-a5c3-00057edc8e4e"}
}
```
---

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
