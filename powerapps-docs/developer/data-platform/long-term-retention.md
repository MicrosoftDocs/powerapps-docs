---
title: "Long-term data retention (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Dataverse long-term data retention enables customers to transfer data from their transactional database to the Dataverse managed data lake." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: 
ms.date: 05/18/2023
ms.reviewer: "pehecke"
ms.topic: "article"
author: "kagoswami" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "kagoswami" # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
---

# Long-term data retention

*Long-term retention* (LTR) is a Dataverse capability that enables customers to transfer their data from a transactional database to the Dataverse managed data lake. To perform the LTR operations, you are required to set up retention policies by defining the criteria for a given table. To set up the retention policy, you should have your environment (organization) and tables both enabled for retention.
  
## Configure retention policy using code

You can set up the retention policy by creating an entry in the retention configuration table. As part of retention policy set up, the platform will validate the policy against a Validate Retention Config table row.

More information: [validateretentionconfig EntityType](webapi/reference/validateretentionconfig.md)

The following code example demonstrates the retention APIs.

### [Web API](#tab/webapi)

The following is an example of a Web API request to retain all the closed opportunities, and will be run on a yearly basis. This example uses the [retentionconfigs EntitType](webapi/reference/retentionconfig.md).

**Request**

```http
POST [Organization Uri]/api/data/v9.1/retentionconfigs
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
  "statecode": 0,
   "name": "Retain all closed opportunities",
   "uniquename": "ui_RetainAllClosedOpportunities",
   "statuscode": 10,
   "criteria": "<fetch version=\"1.0\" output-format=\"xml-platform\" mapping=\"logical\" distinct=\"false\"><entity name=\"opportunity\"><attribute name=\"name\" /><attribute name=\"statecode\" /><attribute name=\"actualvalue\" /><attribute name=\"actualclosedate\" /><attribute name=\"customerid\" /><attribute name=\"opportunityid\" /><order attribute=\"actualclosedate\" descending=\"true\" /><filter type=\"and\"><filter type=\"or\"><condition attribute=\"statecode\" operator=\"eq\" value=\"1\" /><condition attribute=\"statecode\" operator=\"eq\" value=\"2\" /></filter></filter></entity></fetch>",
   "starttime": "2023-05-01T00:00:00",
   "recurrence": "FREQ=YEARLY;INTERVAL=1",
   "retentionconfigid": "35cc1317-20b7-4f4f-829d-5d9d5d77f712",
   "entitylogicalname": "incident"
}
```

> [!NOTE]
> If you want to run retention only once, set the recurrence value as empty.

---

## Configure retention policy using solution import

The retention policy can be configured during solution import. More information about solutions: [Solutions overview](../../maker/data-platform/solutions-overview.md).

Below is sample solution customization.xml code to create a retention policy.

```xml
<retentionconfig retentionconfigid="8fd449d1-f389-4f63-84c6-023c77275359">
  <criteria><fetch version="1.0" output-format="xml-platform" mapping="logical" distinct="true">
    <entity name="incident">
        <attribute name="title"/>
        <attribute name="incidentid"/>
        <attribute name="prioritycode"/>
        <filter type="and">
            <condition attribute="prioritycode" operator="eq" value="3"/>
        </filter>
    </entity>
</fetch></criteria>
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

## Add custom validation to the retention policy

Table and app owners can add their own custom validations whenever a retention policy is created or updated. This validation can be done by registering a custon [plug-in](apply-business-logic-with-code.md) against the `ValidateRetentionConfig` action.

`ValidateRetentionConfig` is a bound action, which gets bound to the table whenever retention is enabled.

More information: [validateretentionconfig Action](webapi/reference/validateretentionconfig.md)

The following code example demonstrates retention policy validation.

### [Web API](#tab/webapi)

The following example validates all closed opportunities, and will be run on a yearly basis.

**Request**

```http
POST [Organization Uri]/api/data/v9.1/ValidateRetentionConfig
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
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

**Response**

```http
HTTP/1.1 200 OK
{
    "@odata.context": "[Organization Uri]/api/data/v9.1/$metadata#Microsoft.Dynamics.CRM.ValidateRetentionConfigResponse",
    "IsValidationSuccessful": true,
    "ErrorMessage": null
}
```

---

## Add pre and post processing during retain and purge

### [Web API](#tab/webapi)

A message named *Retain* executes whenever a table row is marked for retention. You can optionally register a custom plug-in to be executed when the row is being marked for retention.

More information: [retain Action](webapi/reference/retain.md)

The following example executes retention on the an email record.

**Request**

```http
POST [Organization Uri]/api/data/v9.1/Retain
OData-MaxVersion: 4.0
OData-Version: 4.0
If-None-Match: null
Accept: application/json

{
"OperationId":"fd2639b2-f300-408c-b605-75febff98d4f" ,
"Target":{
"@odata.type": "Microsoft.Dynamics.CRM.email",
"activityid": "8b9cc8c0-8c08-46cf-a5c3-00057edc8e4e"}
}

```

**Response**

```http
HTTP/1.1 200 OK
{
    "@odata.context": "[Organization Uri]/api/data/v9.1/$metadata#Microsoft.Dynamics.CRM.RetainResponse",
    "EntityCountCollection": {
        "Count": 3,
        "IsReadOnly": false,
        "Keys": [
            "activityparty",
            "activitypointer",
            "email"
        ],
        "Values": [
            2,
            1,
            1
        ]
    }
}
```

---

### See also

[Use the Microsoft Dataverse Web API](webapi/overview.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
