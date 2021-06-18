---
title: "Web API basic operations sample (Microsoft Dataverse)| Microsoft Docs"
description: "Code samples that demonstrate how to perform CRUD (Create, Retrieve, Update and Delete) operations using the Web API. The samples are coded using client-side JavaScript and also C#."
ms.custom: ""
ms.date: 06/15/2021
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: f006f88c-74cb-4fde-90e5-e1faf2051673
caps.latest.revision: 25
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

# Web API Basic Operations Sample

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

This collection of sample code snippets demonstrate how to perform basic CRUD (Create, Retrieve, Update, and Delete) and associative operations using the Microsoft Dataverse Web API.  
  
-   [Web API Basic Operations Sample (C#)](samples/cdswebapiservice-basic-operations.md)  
  
 This topic describes a common set of operations implemented by each sample snippet in this group. This topic describes the HTTP requests and responses and text output that each sample will perform without the language specific details. See the language specific descriptions and the individual samples for details about how these operations are performed.  
  
<a name="bkmk_demonstrates"></a>  

## Demonstrates  

This sample is divided into the following sections, containing Dataverse Web API operations which are discussed in greater detail in the specified associated conceptual topics.  
  
|Code section|Associated conceptual topics|  
|------------------|----------------------------------|  
|[Section 1: Basic create and update operations](#bkmk_section1)|[Basic create](create-entity-web-api.md#bkmk_basicCreate) <br /> [Create with data returned](create-entity-web-api.md#bkmk_createWithDataReturned) <br /> [Basic update](update-delete-entities-using-web-api.md#bkmk_update) <br /> [Update with data returned](update-delete-entities-using-web-api.md#bkmk_updateWithDataReturned)|  
|[Section 2: Create with association](#bkmk_section2)|[Associate table rows on create](associate-disassociate-entities-using-web-api.md#bkmk_Associaterowsoncreate)|  
|[Section 3: Create related table rows (deep insert)](#bkmk_section3)|[Create related table rows in one operation](create-entity-web-api.md#bkmk_CreateRelated)|  
|[Section 4: Associate and disassociate existing table rows](#bkmk_section4)|[Associate and disassociate table rows using the Web API](associate-disassociate-entities-using-web-api.md)|  
|[Section 5: Delete table rows (sample cleanup)](#bkmk_section5)|[Basic delete](update-delete-entities-using-web-api.md#bkmk_delete)|  
  
> [!NOTE]
>  For brevity, less pertinent HTTP headers have been omitted. The URLs of the records will vary with the base organization address and the ID of the row assigned by your Dataverse server.  
  
<a name="bkmk_section1"></a>
   
## Section 1: Basic create and update operations

This section creates a single contact then performs a series of updates upon that instance. Note that the response header [OData-EntityId](https://docs.oasis-open.org/odata/odata/v4.0/os/part1-protocol/odata-v4.0-os-part1-protocol.html#_Toc372793637) contains the URL to this newly created row, which parenthetically includes the unique ID for this record.  
  
1.  Create a new contact, named  Peter Cambel.  
  
 **Request** 
  
```http
POST https://[Organization URI]/api/data/v9.0/contacts HTTP/1.1  
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
{  
  "firstname": "Peter",  
  "lastname": "Cambel"  
}  
```  
  
**Response**  
  
```http  
HTTP/1.1 204 No Content  
OData-Version: 4.0  
OData-EntityId: https://[Organization URI]/api/data/v9.0/contacts(60f77a42-5f0e-e611-80e0-00155da84c03)  
```  
  
**Console output**
  
```
Contact 'Peter Cambel' created.  
```  
  
The properties available for each type are defined within the metadata document and are also documented for each type in the <xref:Microsoft.Dynamics.CRM.EntityTypeIndex> section. For more general information, see [Web API types and operations](web-api-types-operations.md).  
  
2.  Update the contact with values for annual income ($80,000)  and job title (Junior Developer).  
  
 **Request** 
  
```http  
PATCH https://[Organization URI]/api/data/v9.0/contacts(60f77a42-5f0e-e611-80e0-00155da84c03) HTTP/1.1  
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
{  
  "annualincome": 80000,  
  "jobtitle": "Junior Developer"  
}  
```  
  
**Response**  
  
```http  
HTTP/1.1 204 No Content  
```  
  
**Console output**  
  
```  
Contact 'Peter Cambel' updated with job title and annual income.  
```  
  
3.  Retrieve the contact with its set of explicitly initialized properties.  The `fullname` is a read-only property that is calculated from the `firstname` and `lastname` properties, which were explicitly initialized when the instance was created. In contrast, the `description` property was not explicitly initialized, so it retains its default value, a `null` string.  
  
     Note that the response, in addition to the requested values and typical headers, also automatically returns the following types of additional information:  
  
    -   The primary ID for the current table type, here `contactid`.  
  
    -   An *ETag* value, denoted by the `@odata.etag` key, which identifies the specific version of the resource requested. For more information, see [Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md).  
  
    -   The metadata context, denoted by the  `@odata.context` key, provides a way to compare query results to determine if they came from the same query.  
  
    -   A `_transactioncurrencyid_value` that indicates the local currency of the monetary transaction.  
  
 **Request** 
  
```http  
GET https://[Organization URI]/api/data/v9.0/contacts(60f77a42-5f0e-e611-80e0-00155da84c03)?$select=fullname,annualincome,jobtitle,description HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
 **Response**  
  
```http
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
{   
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#contacts(fullname,annualincome,jobtitle,description)/$entity",  
   "@odata.etag":"W/\"628883\"",  
   "fullname":"Peter Cambel",  
   "annualincome":80000.0000,  
   "jobtitle":"Junior Developer",  
   "description":null,  
   "_transactioncurrencyid_value":"0d4ed62e-95f7-e511-80d1-00155da84c03",  
   "contactid":"60f77a42-5f0e-e611-80e0-00155da84c03"  
}  
```  
  
**Console output**  
  
```http    
Contact 'Peter Cambel' retrieved:  
       Income: 80000  
       Job title: Junior Developer  
       Description: .    
```  
  
> [!IMPORTANT]
>  You should always use selection and filtering in retrieval operations to optimize performance. For more information, see [Query Data using the Web API](query-data-web-api.md).  
  
4.  Update the contact instance by supplying new values to these same properties.  
  
**Request** 
  
```http
PATCH https://[Organization URI]/api/data/v9.0/contacts(60f77a42-5f0e-e611-80e0-00155da84c03) HTTP/1.1  
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
{  
   "jobtitle": "Senior Developer",  
   "annualincome": 95000,  
   "description": "Assignment to-be-determined"  
}    
```  
  
**Response**  
  
```http    
HTTP/1.1 204 No Content    
```  
  
**Console output**  
  
```http    
Contact 'Peter Cambel' updated:  
       Job title: Senior Developer  
       Annual income: 95000  
       Description: Assignment to-be-determined    
```  
  
> [!IMPORTANT]
>  Only send changed properties in update requests. For more information, see [Basic update](update-delete-entities-using-web-api.md#bkmk_update).  
  
5.  Explicitly set a single property, the primary phone number. Note this is a `PUT` request and that the JSON key named `value` is used when performing operations on individual properties.  
  
**Request** 
  
```http  
PUT https://[Organization URI]/api/data/v9.0/contacts(60f77a42-5f0e-e611-80e0-00155da84c03)/telephone1 HTTP/1.1  
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
{  
  "value": "555-0105"  
}  
```  
  
**Response**  
  
```http  
HTTP/1.1 204 No Content  
```  
  
**Console output**  
  
```  
Contact 'Peter Cambel' phone number updated.  
```  
  
6.  Retrieve that same single property, the primary phone number. Again note the use of the key named `value`.  
  
**Request** 
  
```http  
GET https://[Organization URI]/api/data/v9.0/contacts(60f77a42-5f0e-e611-80e0-00155da84c03)/telephone1 HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
```  
  
**Response**  
  
```http    
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
{   
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#contacts(60f77a42-5f0e-e611-80e0-00155da84c03)/telephone1",  
   "value":"555-0105"  
}    
```  
  
**Console output**  
  
```  
Contact's telephone# is: 555-0105.  
```  
  
7.  Create a similar contact but also return instance information in the same operation. This latter capability is enabled by the `Prefer: return=representation` header.  
  
**Request** 
  
```http    
POST https://[Organization URI]/api/data/v9.0/contacts?$select=fullname,annualincome,jobtitle,contactid HTTP/1.1  
OData-Version: 4.0  
Content-Type: application/json; charset=utf-8  
Prefer: return=representation  
{  
  "firstname": "Peter_Alt",  
  "lastname": "Cambel",  
  "jobtitle": "Junior Developer",  
  "annualincome": 80000,  
  "telephone1": "555-0110"  
 }    
 ```  
  
 **Response**  
  
 ```http    
 HTTP/1.1 201 Created  
 Content-Type: application/json; odata.metadata=minimal  
 Preference-Applied: return=representation  
 OData-Version: 4.0  
 {  
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#contacts/$entity","@odata.etag":"W/\"758870\"","_transactioncurrencyid_value":"0d4ed62e-95f7-e511-80d1-00155da84c03","annualincome":80000.0000,"contactid":"199250b7-6cbe-e611-80f7-00155da84c08","jobtitle":"Junior Developer","fullname":"Peter_Alt Cambel"  
 }    
 ```  
  
 **Console output**  
  
 ```    
 Contact 'Peter_Alt Cambel' created:  
        Annual income: 80000  
        Job title: Junior Developer  
 Contact URI: https://[Organization URI]/api/data/v9.0/contacts(199250b7-6cbe-e611-80f7-00155da84c08)  
 ```  
  
8.  Update this similar contact and also return instance information in the same operation. Again, this capability is enabled by the `Prefer: return=representation` header.
  
 **Request** 
  
 ```http    
 POST https://[Organization URI]/api/data/v9.0/contacts?$select=fullname,annualincome,jobtitle,contactid HTTP/1.1  
 OData-Version: 4.0  
 Content-Type: application/json; charset=utf-8  
 Prefer: return=representation  
 {  
   "firstname": "Peter_Alt",  
   "lastname": "Cambel",  
   "jobtitle": "Junior Developer",  
   "annualincome": 80000,  
   "telephone1": "555-0110"  
 }    
 ```  
  
 **Response**  
  
 ```http    
 HTTP/1.1 201 Created  
 Content-Type: application/json; odata.metadata=minimal  
 Preference-Applied: return=representation  
 OData-Version: 4.0  
 {  
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#contacts/$entity","@odata.etag":"W/\"758870\"","_transactioncurrencyid_value":"0d4ed62e-95f7-e511-80d1-00155da84c03","annualincome":80000.0000,"contactid":"199250b7-6cbe-e611-80f7-00155da84c08","jobtitle":"Junior Developer","fullname":"Peter_Alt Cambel"  
 }    
 ```  
  
 **Console output**  
  
```    
Contact 'Peter_Alt Cambel' updated:  
        Annual income: 95000  
        Job title: Senior Developer   
```  
  
<a name="bkmk_section2"></a>  
 
## Section 2: Create with association 
 
This section creates a new account instance named `Contoso, Ltd.` and associates it to an existing contact, `Peter Cambel`, which was created in [Section 1](#bkmk_section1).  This creation and association is performed in a single POST operation.  
  
1.  Create the Contoso, Ltd. account and set its primary contact attribute to the existing contact Peter Cambel.  The `@odata.bind` annotation indicates that an association is being created, here binding the `primarycontactid` single-valued navigation property to an existing contact, Peter Cambel.  
  
**Request** 
  
```http  
POST https://[Organization URI]/api/data/v9.0/accounts HTTP/1.1  
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
{  
  "name": "Contoso Inc",  
  "telephone1": "555-5555",  
  "primarycontactid@odata.bind": "https://[Organization URI]/api/data/v9.0/contacts(60f77a42-5f0e-e611-80e0-00155da84c03)"  
}    
```  
  
**Response**  
  
```http    
HTTP/1.1 204 No Content  
OData-Version: 4.0  
OData-EntityId: https://[Organization URI]/api/data/v9.0/accounts(65f77a42-5f0e-e611-80e0-00155da84c03)    
```  
  
**Console output**  
  
```  
Account 'Contoso Inc' created.  
```  
  
2.  Retrieve the primary contact for the account Contoso, Ltd., again using `$expand`  with the  `primarycontactid` single-valued navigation property to access the associated <xref href="Microsoft.Dynamics.CRM.contact?text=contact EntityType" /> record.  
  
**Request** 
  
```http    
GET https://[Organization URI]/api/data/v9.0/accounts(65f77a42-5f0e-e611-80e0-00155da84c03)?$select=name,&$expand=primarycontactid($select=fullname,jobtitle,annualincome) HTTP/1.1  
OData-MaxVersion: 4.0  
OData-Version: 4.0   
```  
  
**Response**  
  
```http    
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0  
{   
       "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#accounts(name,primarycontactid,primarycontactid(fullname,jobtitle,annualincome))/$entity",  
       "@odata.etag":"W/\"628886\"",  
       "name":"Contoso Inc",  
       "accountid":"65f77a42-5f0e-e611-80e0-00155da84c03",  
       "primarycontactid":{   
          "@odata.etag":"W/\"628885\"",  
          "fullname":"Peter Cambel",  
          "jobtitle":"Senior Developer",  
          "annualincome":95000.0000,  
          "_transactioncurrencyid_value":"0d4ed62e-95f7-e511-80d1-00155da84c03",  
          "contactid":"60f77a42-5f0e-e611-80e0-00155da84c03"  
     }  
}    
```  
  
 **Console output**  
  
 ```
 Account 'Contoso Inc' has primary contact 'Peter Cambel':  
     Job title: Senior Developer  
     Income: 95000    
 ```  
  
<a name="bkmk_section3"></a>  
 
## Section 3: Create related table rows (deep insert)  

This section demonstrates how to create a table row and related row, in a single POST request. Using this method, all rows are newly created; there are no existing rows to associate with. This approach has two advantages. It is more efficient, replacing multiple simpler creation and association operations with one combined operation. Also, it is [atomic](https://msdn.microsoft.com/library/aa719484\(v=vs.71\).aspx), where either the entire operation succeeds and all the related objects are created, or the operation fails and none are created.  
  
This section creates an account, its primary contact, and a set of tasks for that contact in one request.  
  
1.  Create the account `Fourth Coffee` and its primary contact `Susie Curtis` and her three related tasks in one operation.  Note the use of the single-valued `primarycontactid` navigation property and the collection-valued navigation property `Contact_Tasks` to define these relationships, respectively.  Single-valued navigational properties take an object value, whereas collection-valued navigation properties take an array value.  
  
 **Request** 
  
 ```http    
 POST https://[Organization URI]/api/data/v9.0/accounts HTTP/1.1  
 Content-Type: application/json  
 OData-MaxVersion: 4.0  
 OData-Version: 4.0  
 {  
   "name": "Fourth Coffee",  
   "primarycontactid": {  
   "firstname": "Susie",  
   "lastname": "Curtis",  
   "jobtitle": "Coffee Master",  
   "annualincome": 48000,  
   "Contact_Tasks": [  
   {  
       "subject": "Sign invoice",  
       "description": "Invoice #12321",  
       "scheduledend": "2016-04-19T00:00:00-07:00"  
    },  
    {  
       "subject": "Setup new display",  
       "description": "Theme is - Spring is in the air",  
       "scheduledstart": "2016-04-20T00:00:00-07:00"  
    },  
    {  
       "subject": "Conduct training",  
       "description": "Train team on making our new blended coffee",  
       "scheduledstart": "2016-06-01T00:00:00-07:00"  
     }  
   ]  
  }  
}    
```  
  
**Response**  
  
```http    
HTTP/1.1 204 No Content  
OData-Version: 4.0  
OData-EntityId: https://[Organization URI]/api/data/v9.0/accounts(6af77a42-5f0e-e611-80e0-00155da84c03)    
```  
  
**Console output**  
  
```  
Account 'Fourth Coffee' created.  
```  
  
2.  Selectively retrieve the newly created Fourth Coffee account and its primary contact.  An expansion is performed on the single-valued navigation property `primarycontactid`.  
  
**Request** 
  
```http    
GET https://[Organization URI]/api/data/v9.0/accounts(6af77a42-5f0e-e611-80e0-00155da84c03)?$select=name,&$expand=primarycontactid($select=fullname,jobtitle,annualincome) HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0    
```  
  
**Response**  
  
```http    
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0   
{   
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#accounts(name,primarycontactid,primarycontactid(fullname,jobtitle,annualincome))/$entity",  
   "@odata.etag":"W/\"628902\"",  
   "name":"Fourth Coffee",  
   "accountid":"6af77a42-5f0e-e611-80e0-00155da84c03",  
   "primarycontactid":{   
     "@odata.etag":"W/\"628892\"",  
     "fullname":"Susie Curtis",  
     "jobtitle":"Coffee Master",  
     "annualincome":48000.0000,  
     "_transactioncurrencyid_value":"0d4ed62e-95f7-e511-80d1-00155da84c03",  
     "contactid":"6bf77a42-5f0e-e611-80e0-00155da84c03"  
  }  
}    
```  
  
**Console output**  
  
```    
Account 'Fourth Coffee' has primary contact 'Susie Curtis':  
       Job title: Coffee Master  
       Income: 48000    
```  
  
3.  Selectively retrieve the tasks associated with the primary contact retrieved in the previous operation.  An expansion is performed on the collection-valued navigation property `Contact_Tasks`.  
  
**Request** 
  
```http    
GET https://[Organization URI]/api/data/v9.0/contacts(6bf77a42-5f0e-e611-80e0-00155da84c03)?$select=fullname,&$expand=Contact_Tasks($select=subject,description,scheduledstart,scheduledend) HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0    
```  
  
**Response**  
  
```http    
HTTP/1.1 200 OK  
Content-Type: application/json; odata.metadata=minimal  
OData-Version: 4.0   
{   
    "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#contacts(fullname,Contact_Tasks,Contact_Tasks(subject,description,scheduledstart,scheduledend))/$entity",  
    "@odata.etag":"W/\"628892\"",  
    "fullname":"Susie Curtis",  
    "contactid":"6bf77a42-5f0e-e611-80e0-00155da84c03",  
    "Contact_Tasks":[   
      {   
         "@odata.etag":"W/\"628903\"",  
         "subject":"Sign invoice",  
         "description":"Invoice #12321",  
         "scheduledstart":"2016-04-19T00:00:00Z",  
         "scheduledend":"2016-04-19T00:00:00Z",  
         "activityid":"6cf77a42-5f0e-e611-80e0-00155da84c03"  
      },  
      {   
         "@odata.etag":"W/\"628905\"",  
         "subject":"Setup new display",  
         "description":"Theme is - Spring is in the air",  
         "scheduledstart":"2016-04-20T00:00:00Z",  
         "scheduledend":"2016-04-20T00:00:00Z",  
         "activityid":"6df77a42-5f0e-e611-80e0-00155da84c03"  
      },  
          {   
             "@odata.etag":"W/\"628907\"",  
             "subject":"Conduct training",  
             "description":"Train team on making our new blended coffee",  
             "scheduledstart":"2016-06-01T00:00:00Z",  
             "scheduledend":"2016-06-01T00:00:00Z",  
             "activityid":"6ef77a42-5f0e-e611-80e0-00155da84c03"  
          }  
       ]  
    }    
```  
  
**Console output**  
  
```    
Contact 'Susie Curtis' has the following assigned tasks:  
Subject: Sign invoice,  
        Description: Invoice #12321  
        Start: 4/19/2016  
        End: 4/19/2016  
  
Subject: Setup new display,  
        Description: Theme is - Spring is in the air  
        Start: 4/20/2016  
        End: 4/20/2016  
  
Subject: Conduct training  
        Description: Train team on making our new blended coffee,  
        Start: 6/1/2016  
        End: 6/1/2016    
```  
  
<a name="bkmk_section4"></a>
   
## Section 4: Associate and disassociate existing entities  

This section demonstrates how to associate and disassociate existing table rows. Forming an association requires the use of a reference URI and relationship object, which are then sent in a POST request. Disassociating requires sending a DELETE request to the reference URI for that association.  First a one-to-many association is formed between a contact and an account.  Then a many-to-many association is formed between a competitor and one or more opportunities.  
  
1.  Add Peter Cambel as a contact to the account Fourth Coffee using the `contact_customer_accounts` collection-valued navigation property. Note the use of the special key `@odata.id` to specify the associated record.  
  
**Request** 
  
```http    
POST https://[Organization URI]/api/data/v9.0/accounts(6af77a42-5f0e-e611-80e0-00155da84c03)/contact_customer_accounts/$ref HTTP/1.1  
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
{  
  "@odata.id": "https://[Organization URI]/api/data/v9.0/contacts(60f77a42-5f0e-e611-80e0-00155da84c03)"  
}    
```  
  
**Response**  
  
```http    
HTTP/1.1 204 No Content    
```  
  
**Console output**  
  
```  
Contact 'Peter Cambel' associated to account 'Fourth Coffee'.  
```  
  
2.  Confirm the previous operation by retrieving the collection of contacts for the account Fourth Coffee. The response contains the array with a single element, the recently assigned contact Peter Cambel.  
  
**Request** 
  
```http    
GET https://[Organization URI]/api/data/v9.0/accounts(6af77a42-5f0e-e611-80e0-00155da84c03)/contact_customer_accounts?$select=fullname,jobtitle HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0    
```  
  
**Response**  
  
```http    
    HTTP/1.1 200 OK  
    Content-Type: application/json; odata.metadata=minimal  
    OData-Version: 4.0   
    {  
      "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#contacts(fullname,jobtitle)","value":[  
        {  
          "@odata.etag":"W/\"632481\"","fullname":"Peter Cambel","jobtitle":"Senior Developer","contactid":"00b6e0e2-b010-e611-80e1-00155da84c03"  
        }  
      ]  
    }    
```  
  
**Console output**  
  
```    
    Contact list for account 'Fourth Coffee':  
    Name: Peter Cambel, Job title: Senior Developer    
```  
  
3.  Remove the association that was just created between account Fourth Coffee and contact Peter Cambel.  
  
 **Request** 
  
```http    
DELETE https://[Organization URI]/api/data/v9.0/accounts(6af77a42-5f0e-e611-80e0-00155da84c03)/contact_customer_accounts/$ref?$id=https://[Organization URI]/api/data/v9.0/contacts(60f77a42-5f0e-e611-80e0-00155da84c03) HTTP/1.1  
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0    
```  
  
**Response**  
  
```http    
HTTP/1.1 204 No Content    
```  
  
 **Console output**  
  
```  
Contact 'Peter Cambel' dissociated from account 'Fourth Coffee'.  
```  
  
4.  Create a competitor named `Adventure Works`.  
  
**Request** 
  
```http    
POST https://[Organization URI]/api/data/v9.0/competitors HTTP/1.1  
    Content-Type: application/json  
    OData-MaxVersion: 4.0  
    OData-Version: 4.0  
    {  
      "name": "Adventure Works",  
      "strengths": "Strong promoter of private tours for multi-day outdoor adventures"  
    }    
```  
  
**Response**  
  
```http    
HTTP/1.1 204 No Content  
OData-Version: 4.0  
OData-EntityId: https://[Organization URI]/api/data/v9.0/accounts(77f77a42-5f0e-e611-80e0-00155da84c03)    
```  
  
**Console output**  
  
```  
Competitor 'Adventure Works' created.  
```  
  
5.  Create an opportunity named `River rafting adventure`.  
  
**Request** 
  
```http    
POST https://[Organization URI]/api/data/v9.0/opportunities HTTP/1.1  
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
{  
  "name": "River rafting adventure",  
  "description": "Sales team on a river-rafting offsite and team building"  
}    
```  
  
**Response**  
  
```http    
HTTP/1.1 204 No Content  
OData-Version: 4.0  
OData-EntityId: https://[Organization URI]/api/data/v9.0/opportunities(7cf77a42-5f0e-e611-80e0-00155da84c03)    
```  
  
**Console output**  
  
```  
Opportunity 'River rafting adventure' created.  
```  
  
6.  Associate this new opportunity to this new competitor. Note that the same general syntax is used in this many-to-many association as was used in the previous one-to-many association.  
  
**Request** 
  
```http    
POST https://[Organization URI]/api/data/v9.0/opportunities(7cf77a42-5f0e-e611-80e0-00155da84c03)/opportunitycompetitors_association/$ref HTTP/1.1  
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0  
{  
  "@odata.id": "https://[Organization URI]/api/data/v9.0/competitors(77f77a42-5f0e-e611-80e0-00155da84c03)"  
}    
```  
  
**Response**  
  
```http    
HTTP/1.1 204 No Content    
```  
  
**Console output**  
  
```  
Opportunity 'River rafting adventure' associated with competitor 'Adventure Works'.  
```  
  
7.  Selectively retrieve all the opportunities associated with the competitor Adventure Works.  An array is returned containing a single opportunity.  
  
 **Request** 
  
```http    
GET https://[Organization URI]/api/data/v9.0/competitors(77f77a42-5f0e-e611-80e0-00155da84c03)?$select=name,&$expand=opportunitycompetitors_association($select=name,description) HTTP/1.1  
Accept: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0    
```  
  
 **Response**  
  
```http    
HTTP/1.1 200 OK  
{   
   "@odata.context":"https://[Organization URI]/api/data/v9.0/$metadata#competitors(name,opportunitycompetitors_association,opportunitycompetitors_association(name,description))/$entity",  
   "@odata.etag":"W/\"628913\"",  
   "name":"Adventure Works",  
   "competitorid":"77f77a42-5f0e-e611-80e0-00155da84c03",  
   "opportunitycompetitors_association":[   
      {   
        "@odata.etag":"W/\"628917\"",  
        "name":"River rafting adventure",  
        "description":"Sales team on a river-rafting offsite and team building",  
        "opportunityid":"7cf77a42-5f0e-e611-80e0-00155da84c03"  
      }  
   ]  
}    
```  
  
 **Console output**  
  
```    
Competitor 'Adventure Works' has the following opportunities:  
       Name: River rafting adventure,  
       Description: Sales team on a river-rafting offsite and team building    
```  
  
8.  Dissociate the opportunity from the competitor.  Note again, that this has the same general syntax used to remove a one-to-many association.  
  
**Request** 
  
```http    
DELETE https://[Organization URI]/api/data/v9.0/opportunities(7cf77a42-5f0e-e611-80e0-00155da84c03)/opportunitycompetitors_association/$ref?$id=https://[Token-CRM-Org-Name]/Contoso/api/data/v8.1/competitors(77f77a42-5f0e-e611-80e0-00155da84c03) HTTP/1.1  
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0    
```  
  
**Response**  
  
```http    
HTTP/1.1 204 No Content    
```  
  
**Console output**  
  
```  
Opportunity 'River rafting adventure' disassociated from competitor 'Adventure Works'.  
```  
  
<a name="bkmk_section5"></a> 
  
## Section 5: Delete table rows
 
<!-- TODO:
This section demonstrates how to delete entity instances. The corresponding message is a straightforward DELETE request that uses the URI of the entity instance to be deleted.  If the target entity has a parent-child relationship with other entities, then deleting the parent will, by default, automatically cascade delete child instances. For example, in this sample, tasks have contact as their parent. For more information, see [Entity relationship behavior](../entity-relationship-behavior.md).   -->
  
1.  Each element of the collection of row URLs is deleted.  The first is a contact record for Peter Cambel.  
  
**Request** 
  
```http
DELETE https://[Organization URI]/api/data/v9.0/contacts(60f77a42-5f0e-e611-80e0-00155da84c03) HTTP/1.1  
Content-Type: application/json  
OData-MaxVersion: 4.0  
OData-Version: 4.0    
```  
  
**Response**  
  
```http    
HTTP/1.1 204 No Content    
```  
  
2.  Subsequent iterations through the collection delete the remaining records.  
  
**Request** 
  
```http    
DELETE https://[Organization URI]/api/data/v9.0/accounts(65f77a42-5f0e-e611-80e0-00155da84c03) HTTP/1.1  
. . .  
  
DELETE https://[Organization URI]/api/data/v9.0/accounts(6af77a42-5f0e-e611-80e0-00155da84c03) HTTP/1.1  
. . .  
  
DELETE https://[Organization URI]/api/data/v9.0/contacts(6bf77a42-5f0e-e611-80e0-00155da84c03) HTTP/1.1  
. . .  
  
DELETE https://[Organization URI]/api/data/v9.0/competitors(77f77a42-5f0e-e611-80e0-00155da84c03) HTTP/1.1  
. . .  
  
DELETE https://[Organization URI]/api/data/v9.0/opportunities(7cf77a42-5f0e-e611-80e0-00155da84c03) HTTP/1.1  
. . .    
```  
  
### See also  

[Use the Dataverse Web API](overview.md)<br />
[Create a table row using the Web API](create-entity-web-api.md)<br />
[Retrieve a table row using the Web API](retrieve-entity-using-web-api.md)<br />
[Update and delete table rows using the Web API](update-delete-entities-using-web-api.md)<br />
[Associate and disassociate table rows using the Web API](associate-disassociate-table rows-using-web-api.md)<br />
[Web API Basic Operations Sample (C#)](samples/cdswebapiservice-basic-operations.md)<br />

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
