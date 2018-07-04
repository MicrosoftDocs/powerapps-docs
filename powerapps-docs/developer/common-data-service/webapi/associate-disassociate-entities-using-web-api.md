---
title: "Associate and disassociate entities using the Web API (Common Data Service for Apps)| Microsoft Docs"
description: "Read how to add  reference to a collection-valued navigation property, remove a reference and change an existing reference using the Web API"
ms.custom: ""
ms.date: 06/15/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: ad4e4eac-117a-4958-9df0-b7353305b0c7
caps.latest.revision: 13
author: "JimDaly"
ms.author: "jdaly"
manager: "amyla"
---
# Associate and disassociate entities using the Web API

There are several methods you can use to associate and disassociate entities. Which method you apply depends on whether you’re creating or updating the entities and whether you’re operating in the context of the referenced entity or the referencing entity.  

<a name="bkmk_Addareferencetoacollection"></a>

## Add a reference to a collection-valued navigation property

 The following example shows how to associate an existing opportunity entity with the `opportunityid` value of `00000000-0000-0000-0000-000000000001` to the collection-valued `opportunity_customer_accounts` navigation property for an account entity with the `accountid` value of `00000000-0000-0000-0000-000000000002`. This is a 1:N relationship but you can perform the same operation for an N:N relationship.  
  
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
  
<a name="bkmk_Removeareferencetoanentity"></a>

## Remove a reference to an entity

 Use a DELETE request to remove a reference to an entity. The way you do it is different depending on whether you’re referring to a collection-valued navigation property or a single-valued navigation property.  
  
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
  
<a name="bkmk_Changethereferenceinasingle"></a>
 
## Change the reference in a single-valued navigation property

 You can associate entities by setting the value of a single-valued navigation property using PUT request with the following pattern.  
  
 **Request**

```http 
PUT [Organization URI]/api/data/v9.0/opportunities(00000000-0000-0000-0000-000000000001)/customerid_account/$ref HTTP/1.1  
Content-Type: application/json  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
  
{  
 "@odata.id":"[Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000002)"  
}  
```  
  
 **Response**  

```http 
HTTP/1.1 204 No Content  
OData-Version: 4.0  
```  
  
<a name="bkmk_Associateentitiesoncreate"></a>

## Associate entities on create

 As described in [Create related entities in one operation](create-entity-web-api.md#bkmk_CreateRelated), new entities can be created with relationships using *deep insert*.  
  
<a name="bkmk_Associateentitiesonupdate"></a>

## Associate entities on update using single-valued navigation property

 You can associate entities on update using the same message described in [Basic update](update-delete-entities-using-web-api.md#bkmk_update) but you must use the @odata.bind annotation to set the value of a single-valued navigation property. The following example changes the account associated to an opportunity using the `customerid_account` single-valued navigation property.  
  
 **Request**

```http 
PATCH [Organization URI]/api/data/v9.0/opportunities(00000000-0000-0000-0000-000000000001) HTTP/1.1  
Content-Type: application/json  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
  
{  
 "customerid_account@odata.bind":"[Organization URI]/api/data/v9.0/accounts(00000000-0000-0000-0000-000000000002)"  
}  
```  
  
 **Response**  

```http 
HTTP/1.1 204 No Content  
OData-Version: 4.0  
```  
<a name="bkmk_Associateentitiesonupdate_multi"></a>

## Associate entities on update using collection-valued navigation property

The following example shows how to associate multiple existing [ActivityParty](../reference/entities/activityparty.md) entities with an [Email](../reference/entities/email.md) entity using collection-valued navigation property `email_activity_parties`.

> [!NOTE]
> Associating multiple entities with an entity on update is a special scenario that is possible only with <xref href="Microsoft.Dynamics.CRM.activityparty?text=activityparty EntityType" />.

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

 [Web API Basic Operations Sample (C#)](sample-web-api-basic-operations-csharp.md)   
 [Web API Basic Operations Sample (Client-side JavaScript)](sample-web-api-basic-operations-client-side-javascript.md)   
 [Perform operations using the Web API](perform-operations-web-api.md)   
 [Compose Http requests and handle errors](compose-http-requests-handle-errors.md)   
 [Query Data using the Web API](query-data-web-api.md)   
 [Create an entity using the Web API](create-entity-web-api.md)   
 [Retrieve an entity using the Web API](retrieve-entity-using-web-api.md)   
 [Update and delete entities using the Web API](update-delete-entities-using-web-api.md)   
 [Use Web API functions](use-web-api-functions.md)   
 [Use Web API actions](use-web-api-actions.md)   
 [Execute batch operations using the Web API](execute-batch-operations-using-web-api.md)   
 [Impersonate another user using the Web API](impersonate-another-user-web-api.md)   
 [Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md)
