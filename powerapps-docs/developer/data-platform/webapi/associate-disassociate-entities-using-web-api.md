---
title: "Associate and disassociate table rows using the Web API (Microsoft Dataverse)| Microsoft Docs"
description: "Read how to add a reference to a collection-valued navigation property, remove a reference, and change an existing reference using the Web API"
ms.custom: ""
ms.date: 05/03/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: ad4e4eac-117a-4958-9df0-b7353305b0c7
caps.latest.revision: 13
author: "JimDaly" # GitHub ID
ms.author: "jdaly"
ms.reviewer: "pehecke"
manager: "annbe"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Associate and disassociate table rows using the Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

There are several methods you can use to associate and disassociate tables (entities). Which method you apply depends on whether you’re creating or updating the tables and whether you’re operating in the context of the referenced table or the referencing table.  

<a name="bkmk_Addareferencetoacollection"></a>

## Add a reference to a collection-valued navigation property

 The following example shows how to associate an existing opportunity with the `opportunityid` value of `00000000-0000-0000-0000-000000000001` to the collection-valued `opportunity_customer_accounts` navigation property for an account with the `accountid` value of `00000000-0000-0000-0000-000000000002`. This is a 1:N relationship but you can perform the same operation for an N:N relationship.  
  
**Request**  
```http  
POST [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000002)/opportunity_customer_accounts/$ref HTTP/1.1   
Content-Type: application/json   
Accept: application/json   
OData-MaxVersion: 4.0   
OData-Version: 4.0  
  
{  
"@odata.id":"[Organization URI]/api/data/v9.0/opportunities(00000000-0000-0000-0000-000000000001)"  
}  
```  
  
**Response**  
```http 
HTTP/1.1 204 No Content  
OData-Version: 4.0  
```  
  


<a name="bkmk_Changethereferenceinasingle"></a>
 
## Change the reference in a single-valued navigation property

 You can associate rows by setting the value of a single-valued navigation property using PUT request with the following pattern.  
  
 **Request**

```http 
PUT [Organization URI]/api/data/v9.0/opportunities(00000000-0000-0000-0000-000000000001)/customerid_account/$ref HTTP/1.1  
Content-Type: application/json  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
  
{  
 "@odata.id":"accounts(00000000-0000-0000-0000-000000000002)"  
}  
```  
  
 **Response**  

```http 
HTTP/1.1 204 No Content  
OData-Version: 4.0  
```  


<a name="bkmk_Removeareferencetoarow"></a>

## Remove a reference to a table row

 Use a DELETE request to remove a reference to a row. The way you do it is different depending on whether you’re referring to a collection-valued navigation property or a single-valued navigation property.  
  
 **Request**  
 For a collection-valued navigation property, use the following.  
  
```http  
DELETE [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000002)/opportunity_customer_accounts/$ref?$id=[Organization URI]/api/data/v9.0/opportunities(00000000-0000-0000-0000-000000000001) HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
 Or, use this.  
  
```http 
DELETE [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000002)/opportunity_customer_accounts(00000000-0000-0000-0000-000000000001)/$ref HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
 **Request**  
 For a single-valued navigation property, remove the `$id` query string parameter.  
  
```http 
DELETE [Organization URI]/api/data/v9.0/opportunities(00000000-0000-0000-0000-000000000001)/customerid_account/$ref HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
 **Response**  
 Either way, a successful response has status 204.  
  
```http 
HTTP/1.1 204 No Content  
OData-Version: 4.0  
```

<a name="bkmk_Associaterowsoncreate"></a>

## Associate table rows on create

As described in [Associate rows on create](create-entity-web-api.md#associate-table-rows-on-create), you can associate the new row to existing rows by setting the navigation properties using the `@odata.bind` annotation.

As described in [Create related tables in one operation](create-entity-web-api.md#bkmk_CreateRelated), new tables can be created with relationships using *deep insert*.  
  
## Associate and disassociate table rows on update

You can set the value of single-valued navigation properties using `PATCH` to associate or disassociate rows.

<a name="bkmk_Associaterowsonupdate"></a>

### Associate table rows on update

 You can associate rows on update using the same message described in [Basic update](update-delete-entities-using-web-api.md#bkmk_update) but you must use the `@odata.bind` annotation to set the value of a single-valued navigation property. The following example changes the account associated to an opportunity using the `customerid_account` single-valued navigation property.  
  
 **Request**

```http 
PATCH [Organization URI]/api/data/v9.0/opportunities(00000000-0000-0000-0000-000000000001) HTTP/1.1  
Content-Type: application/json  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
  
{  
 "customerid_account@odata.bind":"accounts(00000000-0000-0000-0000-000000000002)"  
}  
```  
  
 **Response**  

```http 
HTTP/1.1 204 No Content  
OData-Version: 4.0  
```  

### Disassociate table rows on update

You can remove a reference to a single-valued navigation property when updating by setting the value to `null`. This method allows you to disassociate multiple references in a single operation.
There are two ways to do this:

You can set the value to `null` using the `@odata.bind` annotation:

```http  
PATCH [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001) HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0

{
	"parentaccountid@odata.bind":  null,
	"primarycontactid@odata.bind": null
}


```  
  
 Or, just use the name of the single-valued navigation property. 
  
```http 
PATCH [Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000001) HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  

{
    "parentaccountid":  null,
    "primarycontactid": null
}

``` 

More information: [Basic update](update-delete-entities-using-web-api.md#basic-update)

<a name="bkmk_Associaterowsonupdate_multi"></a>

## Associate table rows on update using collection-valued navigation property

The following example shows how to associate multiple existing [ActivityParty](../reference/entities/activityparty.md) with an [Email](../reference/entities/email.md) using collection-valued navigation property `email_activity_parties`.

> [!NOTE]
> Associating multiple tables with a table on update is a special scenario that is possible only with <xref:Microsoft.Dynamics.CRM.activityparty?text=activityparty EntityType />.

**Request**

```HTTP
PUT [Organization URI]/api/data/v9.0/emails(2479d20d-3a39-e711-8145-e0071b6a2001)/email_activity_parties
Content-Type: application/json  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0

{
	"value": [
		{
			"partyid_contact@odata.bind":"contacts(a30d4045-fc46-e711-8115-e0071b66df51)",
			"participationtypemask":3
			
		},
		{
			"partyid_contact@odata.bind":"contacts(1dcdda07-3a39-e711-8145-e0071b6a2001)",
			"participationtypemask":2
			
		}
		]
}
```

**Response**

```HTTP
HTTP/1.1 204 No Content  
OData-Version: 4.0 
```

### See also

 [Web API Basic Operations Sample (C#)](samples/cdswebapiservice-basic-operations.md)   
 [Web API Basic Operations Sample (Client-side JavaScript)](samples/basic-operations-client-side-javascript.md)   
 [Perform operations using the Web API](perform-operations-web-api.md)   
 [Compose Http requests and handle errors](compose-http-requests-handle-errors.md)   
 [Query Data using the Web API](query-data-web-api.md)   
 [Create a table using the Web API](create-entity-web-api.md)   
 [Retrieve a table using the Web API](retrieve-entity-using-web-api.md)   
 [Update and delete tables using the Web API](update-delete-entities-using-web-api.md)   
 [Use Web API functions](use-web-api-functions.md)   
 [Use Web API actions](use-web-api-actions.md)   
 [Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)   
 [Impersonate another user using the Web API](impersonate-another-user-web-api.md)   
 [Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
