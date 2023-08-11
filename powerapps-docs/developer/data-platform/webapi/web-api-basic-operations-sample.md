---
title: "Web API basic operations sample (Microsoft Dataverse)| Microsoft Docs"
description: "Code samples that demonstrate how to perform CRUD (Create, Retrieve, Update and Delete) operations using the Web API. The samples are coded using C# and client-side JavaScript."
ms.date: 08/29/2022
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType: 
  - developer
contributors: 
  - JimDaly
---

# Web API Basic Operations Sample

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

This collection of sample code snippets demonstrate how to perform basic CRUD (Create, Retrieve, Update, and Delete) and associative operations using the Microsoft Dataverse Web API.  
  
- [Web API Basic Operations Sample (C#)](samples/webapiservice-basic-operations.md) 
  
This topic describes a common set of operations implemented by each sample snippet in this group. This topic describes the HTTP requests and responses and text output that each sample will perform without the language specific details. See the language specific descriptions and the individual samples for details about how these operations are performed.  
  
<a name="bkmk_demonstrates"></a>  

## Demonstrates  

This sample is divided into the following sections, containing Dataverse Web API operations which are discussed in greater detail in the specified associated conceptual topics.  
  
|Code section|Associated conceptual topics|  
|------------------|----------------------------------|  
|[Section 1: Basic create and update operations](#bkmk_section1)|[Basic create](create-entity-web-api.md#bkmk_basicCreate)<br /> [Basic update](update-delete-entities-using-web-api.md#bkmk_update)|  
|[Section 2: Create with association](#bkmk_section2)|[Associate table rows on create](create-entity-web-api.md#associate-table-rows-on-create)|  
|[Section 3: Create related table rows (deep insert)](#bkmk_section3)|[Create related table rows in one operation](create-entity-web-api.md#bkmk_CreateRelated)|  
|[Section 4: Associate and disassociate existing table rows](#bkmk_section4)|[Associate and disassociate table rows using the Web API](associate-disassociate-entities-using-web-api.md)|  
|[Section 5: Delete table rows (sample cleanup)](#bkmk_section5)|[Basic delete](update-delete-entities-using-web-api.md#bkmk_delete)|  
  
> [!NOTE]
>  For brevity, less pertinent HTTP headers have been omitted. The URLs of the records will vary with the base organization address and the ID of the row assigned by your Dataverse server.  
  
<a name="bkmk_section1"></a>
   
## Section 1: Basic create and update operations

This section creates a single contact then performs a series of updates upon that instance. Note that the response header [OData-EntityId](https://docs.oasis-open.org/odata/odata/v4.0/os/part1-protocol/odata-v4.0-os-part1-protocol.html#_Toc372793637) contains the URL to this newly created row, which parenthetically includes the unique ID for this record.  
  
1. Create a new contact, named  Rafel Shillo.  
  
   **Request:**
   
   ```http
   POST [Organization Uri]/api/data/v9.2/contacts HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   
   {
    "firstname": "Rafel",
    "lastname": "Shillo"
   }
   ```
   
   **Response:**
   
   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/contacts(0928bcb4-bb27-ed11-9db1-002248274ada)
   ```
    
   **Console output:**
    
   ```
   Contact URI: [Organization Uri]/api/data/v9.2/contacts(0928bcb4-bb27-ed11-9db1-002248274ada)
   Contact relative Uri: contacts(0928bcb4-bb27-ed11-9db1-002248274ada)
   ```  
    
   The properties available for each type are defined within the metadata document and are also documented for each type in the <xref:Microsoft.Dynamics.CRM.EntityTypeIndex> section. For more general information, see [Web API types and operations](web-api-types-operations.md).  
  
1. Update the contact with values for annual income ($80,000)  and job title (Junior Developer).  
    
   **Request:**
   
   ```http
   PATCH [Organization Uri]/api/data/v9.2/contacts(0928bcb4-bb27-ed11-9db1-002248274ada) HTTP/1.1
   If-Match: *
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   
   {
    "annualincome": 80000,
    "jobtitle": "Junior Developer"
   }
   ```
   
   **Response:**
   
   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/contacts(0928bcb4-bb27-ed11-9db1-002248274ada)
   ```
    
   **Console output:**  
    
   ```  
   Contact 'Rafel Shillo' updated with jobtitle and annual income
   ```  
  
1. Retrieve the contact with its set of explicitly initialized properties.  The `fullname` is a read-only property that is calculated from the `firstname` and `lastname` properties, which were explicitly initialized when the instance was created. In contrast, the `description` property was not explicitly initialized, so it retains its default value, a `null` string.  
   
   Note that the response, in addition to the requested values and typical headers, also automatically returns the following types of additional information:  
   
   - The primary ID for the current table type, here `contactid`.  
   - An *ETag* value, denoted by the `@odata.etag` key, which identifies the specific version of the resource requested. For more information, see [Perform conditional operations using the Web API](perform-conditional-operations-using-web-api.md).  
   - The metadata context, denoted by the  `@odata.context` key, provides a way to compare query results to determine if they came from the same query.  
   - A `_transactioncurrencyid_value` that indicates the local currency of the monetary transaction.  
   
   **Request:**
   
   ```http
   GET [Organization Uri]/api/data/v9.2/contacts(0928bcb4-bb27-ed11-9db1-002248274ada)?$select=fullname,annualincome,jobtitle,description HTTP/1.1
   Prefer: odata.include-annotations="*"
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```
   
   **Response:**
   
   ```http
   HTTP/1.1 200 OK
   ETag: W/"72935648"
   OData-Version: 4.0
   Preference-Applied: odata.include-annotations="*"
   
   {
    "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#contacts(fullname,annualincome,jobtitle,description)/$entity",
    "@odata.etag": "W/\"72935648\"",
    "fullname": "Rafel Shillo",
    "annualincome@OData.Community.Display.V1.FormattedValue": "$80,000.00",
    "annualincome": 80000.0,
    "jobtitle": "Junior Developer",
    "description": null,
    "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
    "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
    "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
    "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
    "contactid": "0928bcb4-bb27-ed11-9db1-002248274ada"
   }
   ```
    
   **Console output:**  
    
   ```
   Contact 'Rafel Shillo' retrieved:
          Annual income: $80,000.00
          Job title: Junior Developer
          Description:
   ```  
    
   > [!IMPORTANT]
   >  You should always use selection and filtering in retrieval operations to optimize performance. For more information, see [Query Data using the Web API](query-data-web-api.md).  
  
1. Update the contact instance by supplying new values to these same properties.  
  
   **Request:**
   
   ```http
   PATCH [Organization Uri]/api/data/v9.2/contacts(0928bcb4-bb27-ed11-9db1-002248274ada) HTTP/1.1
   If-Match: *
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   
   {
    "jobtitle": "Senior Developer",
    "annualincome": 95000,
    "description": "Assignment to-be-determined"
   }
   ```

   **Response:**
   
   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/contacts(0928bcb4-bb27-ed11-9db1-002248274ada)
   ```
    
   **Console output:**  
    
   ```
   Contact 'Rafel Shillo' updated:
          Job title: Senior Developer
          Annual income: 95000
          Description: Assignment to-be-determined
   ```  
    
   > [!IMPORTANT]
   >  Only send changed properties in update requests. For more information, see [Basic update](update-delete-entities-using-web-api.md#bkmk_update).  
  
1. Explicitly set a single property, the primary phone number. Note this is a `PUT` request and that the JSON key named `value` is used when performing operations on individual properties.  
  
   **Request:**
   
   ```http
   PUT [Organization Uri]/api/data/v9.2/contacts(0928bcb4-bb27-ed11-9db1-002248274ada)/telephone1 HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   
   {
    "value": "555-0105"
   }
   ```
   
   **Response:**
   
   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   ```
    
   **Console output:**  
    
   ```  
   Contact 'Rafel Shillo' phone number updated.
   ```  
  
1. Retrieve that same single property, the primary phone number. Again note the use of the key named `value`.  
  
   **Request:**
   
   ```http
   GET [Organization Uri]/api/data/v9.2/contacts(0928bcb4-bb27-ed11-9db1-002248274ada)/telephone1 HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```
   
   **Response:**
   
   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0
   
   {
    "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#contacts(0928bcb4-bb27-ed11-9db1-002248274ada)/telephone1",
    "value": "555-0105"
   }
   ```
    
   **Console output:**  
    
   ```  
   Contact's telephone # is: 555-0105.  
   ``` 
   
   <a name="bkmk_section2"></a>  
    
## Section 2: Create with association

This section creates a new account record named `Contoso, Ltd.` and associates it to an existing contact, `Rafel Shillo`, which was created in [Section 1](#bkmk_section1).  This creation and association is performed in a single POST operation.  
  
1. Create the Contoso, Ltd. account and set its primary contact attribute to the existing contact Rafel Shillo.  The `@odata.bind` annotation indicates that an association is being created, here binding the `primarycontactid` single-valued navigation property to an existing contact, Rafel Shillo.  
     
   **Request:**
   
   ```http
   POST [Organization Uri]/api/data/v9.2/accounts HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   
   {
    "name": "Contoso Ltd",
    "telephone1": "555-5555",
    "primarycontactid@odata.bind": "contacts(0928bcb4-bb27-ed11-9db1-002248274ada)"
   }
   ```
   
   **Response:**
   
   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/accounts(2728bcb4-bb27-ed11-9db1-002248274ada)
   ```  
    
   **Console output:**  
    
   ```  
   Account 'Contoso Ltd' created.
   Account URI: accounts(2728bcb4-bb27-ed11-9db1-002248274ada)
   ```  
   
1. Retrieve the primary contact for the account Contoso, Ltd., again using `$expand`  with the  `primarycontactid` single-valued navigation property to access the associated <xref:Microsoft.Dynamics.CRM.contact?text=contact EntityType> record.  
  
   **Request:**
   
   ```http
   GET [Organization Uri]/api/data/v9.2/accounts(2728bcb4-bb27-ed11-9db1-002248274ada)?$select=name,&$expand=primarycontactid($select=fullname,jobtitle,annualincome) HTTP/1.1
   Prefer: odata.include-annotations="*"
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```
   
   **Response:**
   
   ```http
   HTTP/1.1 200 OK
   ETag: W/"72935670"
   OData-Version: 4.0
   Preference-Applied: odata.include-annotations="*"
   
   {
    "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#accounts(name,primarycontactid(fullname,jobtitle,annualincome))/$entity",
    "@odata.etag": "W/\"72935670\"",
    "name": "Contoso Ltd",
    "accountid": "2728bcb4-bb27-ed11-9db1-002248274ada",
    "primarycontactid": {
      "@odata.etag": "W/\"72935663\"",
      "fullname": "Rafel Shillo",
      "jobtitle": "Senior Developer",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$95,000.00",
      "annualincome": 95000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
      "contactid": "0928bcb4-bb27-ed11-9db1-002248274ada"
    }
   }
   ```
    
   **Console output:**  
    
   ```
   Account 'Contoso Ltd' has primary contact 'Rafel Shillo':
          Job title: Senior Developer
          Annual income: $95,000.00
   ```  
  
   <a name="bkmk_section3"></a>  
   
## Section 3: Create related table rows (deep insert)  

This section demonstrates how to create a table row and related row, in a single POST request. Using this method, all rows are newly created; there are no existing rows to associate with. This approach has two advantages. It is more efficient, replacing multiple simpler creation and association operations with one combined operation. Also, it is atomic, where either the entire operation succeeds and all the related objects are created, or the operation fails and none are created.  
  
This section creates an account, its primary contact, and a set of tasks for that contact in one request.  
  
1. Create the account `Fourth Coffee` and its primary contact `Susie Curtis` and their three related tasks in one operation.  Note the use of the single-valued `primarycontactid` navigation property and the collection-valued navigation property `Contact_Tasks` to define these relationships, respectively.  Single-valued navigational properties take an object value, whereas collection-valued navigation properties take an array value.  
  
   **Request:**
   
   ```http
   POST [Organization Uri]/api/data/v9.2/accounts HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   
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
          "scheduledstart": "2023-04-19T03:00:00+07:00",
          "scheduledend": "2023-04-19T04:00:00+07:00",
          "scheduleddurationminutes": 60
        },
        {
          "subject": "Setup new display",
          "description": "Theme is - Spring is in the air",
          "scheduledstart": "2023-04-20T03:00:00+07:00",
          "scheduledend": "2023-04-20T04:00:00+07:00",
          "scheduleddurationminutes": 60
        },
        {
          "subject": "Conduct training",
          "description": "Train team on making our new blended coffee",
          "scheduledstart": "2023-04-21T03:00:00+07:00",
          "scheduledend": "2023-04-21T04:00:00+07:00",
          "scheduleddurationminutes": 60
        }
      ]
    }
   }
   ```
   
   **Response:**
   
   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/accounts(2e28bcb4-bb27-ed11-9db1-002248274ada)
   ```
    
   **Console output:**  
    
   ```  
   Account 'Fourth Coffee  created.
   ```  
  
1. Selectively retrieve the newly created Fourth Coffee account and its primary contact.  An expansion is performed on the single-valued navigation property `primarycontactid`.  
  
   **Request:**
   
   ```http
   GET [Organization Uri]/api/data/v9.2/accounts(2e28bcb4-bb27-ed11-9db1-002248274ada)?$select=name&$expand=primarycontactid($select=fullname,jobtitle,annualincome) HTTP/1.1
   Prefer: odata.include-annotations="*"
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```
   
   **Response:**
   
   ```http
   HTTP/1.1 200 OK
   ETag: W/"72935710"
   OData-Version: 4.0
   Preference-Applied: odata.include-annotations="*"
   
   {
    "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#accounts(name,primarycontactid(fullname,jobtitle,annualincome))/$entity",
    "@odata.etag": "W/\"72935710\"",
    "name": "Fourth Coffee",
    "accountid": "2e28bcb4-bb27-ed11-9db1-002248274ada",
    "primarycontactid": {
      "@odata.etag": "W/\"72935689\"",
      "fullname": "Susie Curtis",
      "jobtitle": "Coffee Master",
      "annualincome@OData.Community.Display.V1.FormattedValue": "$48,000.00",
      "annualincome": 48000.0,
      "_transactioncurrencyid_value@OData.Community.Display.V1.FormattedValue": "US Dollar",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.associatednavigationproperty": "transactioncurrencyid",
      "_transactioncurrencyid_value@Microsoft.Dynamics.CRM.lookuplogicalname": "transactioncurrency",
      "_transactioncurrencyid_value": "228f42f8-e646-e111-8eb7-78e7d162ced1",
      "contactid": "2f28bcb4-bb27-ed11-9db1-002248274ada"
    }
   }
   ```
    
   **Console output:**  
    
   ```    
   Account 'Fourth Coffee' has primary contact 'Susie Curtis':
          Job title: Coffee Master
          Annual income: $48,000.00
   ```  
  
1. Selectively retrieve the tasks associated with the primary contact retrieved in the previous operation.  An expansion is performed on the collection-valued navigation property `Contact_Tasks`.  
  
   **Request:**
   
   ```http
   GET [Organization Uri]/api/data/v9.2/contacts(2f28bcb4-bb27-ed11-9db1-002248274ada)?$select=fullname&$expand=Contact_Tasks($select=subject,description,scheduledstart,scheduledend) HTTP/1.1
   Prefer: odata.include-annotations="*"
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```
   
   **Response:**
   
   ```http
   HTTP/1.1 200 OK
   ETag: W/"72935689"
   OData-Version: 4.0
   Preference-Applied: odata.include-annotations="*"
   
   {
    "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#contacts(fullname,Contact_Tasks(subject,description,scheduledstart,scheduledend))/$entity",
    "@odata.etag": "W/\"72935689\"",
    "fullname": "Susie Curtis",
    "contactid": "2f28bcb4-bb27-ed11-9db1-002248274ada",
    "Contact_Tasks": [
      {
        "@odata.etag": "W/\"72935719\"",
        "subject": "Sign invoice",
        "description": "Invoice #12321",
        "scheduledstart@OData.Community.Display.V1.FormattedValue": "4/18/2023 1:00 PM",
        "scheduledstart": "2023-04-18T20:00:00Z",
        "scheduledend@OData.Community.Display.V1.FormattedValue": "4/18/2023 2:00 PM",
        "scheduledend": "2023-04-18T21:00:00Z",
        "activityid": "3028bcb4-bb27-ed11-9db1-002248274ada"
      },
      {
        "@odata.etag": "W/\"72935723\"",
        "subject": "Setup new display",
        "description": "Theme is - Spring is in the air",
        "scheduledstart@OData.Community.Display.V1.FormattedValue": "4/19/2023 1:00 PM",
        "scheduledstart": "2023-04-19T20:00:00Z",
        "scheduledend@OData.Community.Display.V1.FormattedValue": "4/19/2023 2:00 PM",
        "scheduledend": "2023-04-19T21:00:00Z",
        "activityid": "3128bcb4-bb27-ed11-9db1-002248274ada"
      },
      {
        "@odata.etag": "W/\"72935727\"",
        "subject": "Conduct training",
        "description": "Train team on making our new blended coffee",
        "scheduledstart@OData.Community.Display.V1.FormattedValue": "4/20/2023 1:00 PM",
        "scheduledstart": "2023-04-20T20:00:00Z",
        "scheduledend@OData.Community.Display.V1.FormattedValue": "4/20/2023 2:00 PM",
        "scheduledend": "2023-04-20T21:00:00Z",
        "activityid": "3228bcb4-bb27-ed11-9db1-002248274ada"
      }
    ]
   }
   ```
    
   **Console output:**  
    
   ```    
   Contact 'Susie Curtis' has the following assigned tasks:
   Subject: Sign invoice,
          Description: Invoice #12321
          Start: 4/18/2023 1:00 PM
          End: 4/18/2023 2:00 PM
   
   Subject: Setup new display,
          Description: Theme is - Spring is in the air
          Start: 4/19/2023 1:00 PM
          End: 4/19/2023 2:00 PM
   
   Subject: Conduct training,
          Description: Train team on making our new blended coffee
          Start: 4/20/2023 1:00 PM
          End: 4/20/2023 2:00 PM 
   ```  
   
   <a name="bkmk_section4"></a>
      
## Section 4: Associate and disassociate existing entities  

This section demonstrates how to associate and disassociate existing table rows. Forming an association requires the use of a reference URI and relationship object, which are then sent in a POST request. Disassociating requires sending a DELETE request to the reference URI for that association.  First a one-to-many association is formed between a contact and an account.  Then a many-to-many association is formed between a competitor and one or more opportunities.  
  
1. Add Rafel Shillo as a contact to the account Fourth Coffee using the `contact_customer_accounts` collection-valued navigation property. Note the use of the special key `@odata.id` to specify the associated record.  
   
   **Request:**
   
   ```http
   POST [Organization Uri]/api/data/v9.2/accounts(2e28bcb4-bb27-ed11-9db1-002248274ada)/contact_customer_accounts/$ref HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   
   {
    "@odata.id": "[Organization Uri]/api/data/v9.2/contacts(0928bcb4-bb27-ed11-9db1-002248274ada)"
   }
   ```
   
   **Response:**
   
   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   ```
  
1. Confirm the previous operation by retrieving the collection of contacts for the account Fourth Coffee. The response contains the array with a single element, the recently assigned contact Rafel Shillo.  
   
   **Request:**
   
   ```http
   GET [Organization Uri]/api/data/v9.2/accounts(2e28bcb4-bb27-ed11-9db1-002248274ada)/contact_customer_accounts?$select=fullname,jobtitle HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```
   
   **Response:** 
   
   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0
   
   {
    "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#contacts(fullname,jobtitle)",
    "value": [
      {
        "@odata.etag": "W/\"72935741\"",
        "fullname": "Rafel Shillo",
        "jobtitle": "Senior Developer",
        "contactid": "0928bcb4-bb27-ed11-9db1-002248274ada"
      }
    ]
   }
   ```
    
   **Console output:**  
    
   ```    
   Contact list for account 'Fourth Coffee':
          Name: Rafel Shillo, Job title: Senior Developer  
   ```  
   
1. Remove the association that was just created between account Fourth Coffee and contact Rafel Shillo.  
   
   **Request:**
   
   ```http
   DELETE [Organization Uri]/api/data/v9.2/accounts(2e28bcb4-bb27-ed11-9db1-002248274ada)/contact_customer_accounts(0928bcb4-bb27-ed11-9db1-002248274ada)/$ref HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```
   
   **Response:**
   
   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   ```
   
1. Create a security role named `Example Security Role`.  
   
   **Request:**
   
   ```http
   POST [Organization Uri]/api/data/v9.2/roles HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   
   {
    "businessunitid@odata.bind": "businessunits(38e0dbe4-131b-e111-ba7e-78e7d1620f5e)",
    "name": "Example Security Role"
   }
   ```

   **Response:**
   
   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   OData-EntityId: [Organization Uri]/api/data/v9.2/roles(e359feba-bb27-ed11-9db1-002248274ada)
   ``` 
  
1. Associate the new security role to your systemuser record.
   
   **Request:**
   
   ```http
   POST [Organization Uri]/api/data/v9.2/systemusers(4026be43-6b69-e111-8f65-78e7d1620f5e)/systemuserroles_association/$ref HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   
   {
    "@odata.id": "[Organization Uri]/api/data/v9.2/roles(e359feba-bb27-ed11-9db1-002248274ada)"
   }
   ```
   
   **Response:**
   
   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   ``` 
    
   **Console output:**  
    
   ```  
   Security Role 'Example Security Role' associated with to your user account.
   ```  
  
1. Retrieve the Example Security Role using the `systemuserroles_association` many-to-many relationship: 
   
   **Request:**
   
   ```http
   GET [Organization Uri]/api/data/v9.2/systemusers(4026be43-6b69-e111-8f65-78e7d1620f5e)/systemuserroles_association?$select=name&$filter=roleid%20eq%20e359feba-bb27-ed11-9db1-002248274ada HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```
   
   **Response:**
   
   ```http
   HTTP/1.1 200 OK
   OData-Version: 4.0
   
   {
    "@odata.context": "[Organization Uri]/api/data/v9.2/$metadata#roles(name)",
    "value": [
      {
        "@odata.etag": "W/\"72935763\"",
        "name": "Example Security Role",
        "roleid": "e359feba-bb27-ed11-9db1-002248274ada"
      }
    ]
   }
   ``` 
    
   **Console output:**  
    
   ```  
   Retrieved role: Example Security Role
   ``` 
   
1. Dissociate the security role from the from your user record.  Note again, that this has the same general syntax used to remove a one-to-many association.  
   
   **Request:**
   
   ```http
   DELETE [Organization Uri]/api/data/v9.2/systemusers(4026be43-6b69-e111-8f65-78e7d1620f5e)/systemuserroles_association(e359feba-bb27-ed11-9db1-002248274ada)/$ref HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```
   
   **Response:**
   
   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   ```
  
   <a name="bkmk_section5"></a> 
  
## Section 5: Delete table rows
  
1. Each element of the collection of row URLs is deleted.  The first is a contact record for Rafel Shillo.  
   
   **Request:**
   
   ```http
   DELETE [Organization Uri]/api/data/v9.2/contacts(0928bcb4-bb27-ed11-9db1-002248274ada) HTTP/1.1
   OData-MaxVersion: 4.0
   OData-Version: 4.0
   If-None-Match: null
   Accept: application/json
   ```
   
   **Response:**
   
   ```http
   HTTP/1.1 204 NoContent
   OData-Version: 4.0
   ```
   
1. Subsequent iterations through the collection delete the remaining records.  
   
   **Request:** 
     
   ```http    
   DELETE [Organization Uri]/api/data/v9.2/accounts(2728bcb4-bb27-ed11-9db1-002248274ada) HTTP/1.1
   . . .  
    
   DELETE [Organization Uri]/api/data/v9.2/accounts(2e28bcb4-bb27-ed11-9db1-002248274ada) HTTP/1.1 
   . . .  
     
   DELETE [Organization Uri]/api/data/v9.2/contacts(2f28bcb4-bb27-ed11-9db1-002248274ada) HTTP/1.1
   . . .  
     
   DELETE [Organization Uri]/api/data/v9.2/roles(e359feba-bb27-ed11-9db1-002248274ada) HTTP/1.1  
   ```  
  
### See also  

[Use the Dataverse Web API](overview.md)<br />
[Create a table row using the Web API](create-entity-web-api.md)<br />
[Retrieve a table row using the Web API](retrieve-entity-using-web-api.md)<br />
[Update and delete table rows using the Web API](update-delete-entities-using-web-api.md)<br />
[Associate and disassociate table rows using the Web API](associate-disassociate-entities-using-web-api.md)<br />
[Web API Basic Operations Sample (C#)](samples/webapiservice-basic-operations.md)<br />

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
