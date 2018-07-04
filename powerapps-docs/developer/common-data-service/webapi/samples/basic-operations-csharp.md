---
title: "Web API Basic Operations Sample (C#) (Common Data Service for Apps)| Microsoft Docs"
description: "This sample demonstrates how to perform basic CRUD (Create, Retrieve, Update, and Delete) and association and dissociation operations on Common Data Service for Apps entity instances, using the Common Data Service for Apps Web API"
ms.custom: ""
ms.date: 06/15/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 45cdefe5-0776-496a-9b06-b5cad768e543
caps.latest.revision: 20
author: "JimDaly"
ms.author: "jdaly"
---
# Web API Basic Operations Sample (C#)

This sample demonstrates how to perform basic CRUD (Create, Retrieve, Update, and Delete) and association and dissociation operations on Common Data Service for Apps entity instances, using the Common Data Service for Apps Web API.  
  
> [!NOTE]
>  This sample implements the Common Data Service for Apps operations and console output detailed in [Web API Basic Operations Sample](web-api-basic-operations-sample.md) and uses the common C# constructs described in [Web API Samples (C#)](web-api-samples-csharp.md).  
  
<a name="bkmk_prerequisites"></a>
   
## Prerequisites

Prerequisites for all Common Data Service for Apps Web API C# samples are detailed in the [Prerequisites](web-api-samples-csharp.md#bkmk_prerequisites) section of the parent topic [Web API Samples (C#)](web-api-samples-csharp.md).  
  
<a name="bkmk_runSample"></a>
  
## Run this sample

First go to [Microsoft CRM Web API Basic Operations Sample (C#)](http://go.microsoft.com/fwlink/p/?LinkId=824042), download the sample archive file, Microsoft CRM Web API Basic Operations Sample (CS).zip, and extract its contents into a local folder. This folder should contain the following files:  
  
|File|Purpose/Description|  
|----------|--------------------------|  
|Program.cs|Contains the primary source code for this sample.|  
|App.config|The application configuration file, which contains placeholder Common Data Service for Apps server connection information.|  
|Authentication.cs<br />Configuration.cs<br />Exceptions.cs|Located in the folder **Web API Helper Code**, these files comprise the supplemental library detailed in [Use the Common Data Service for Apps Web API Helper Library (C#)](use-microsoft-dynamics-365-web-api-helper-library-csharp.md).|  
|BasicOperations.sln <br />BasicOperations.csproj <br />Packages.config <br />AssemblyInfo.cs|The standard Visual Studio 2015 solution, project, NuGet package configuration, and assembly information files for this sample.|  
  
 Next, use the following procedure to run this sample.  
  
1.  Locate and double-click on the solution file, BasicOperations.sln, to load the solution into Visual Studio. Build the **BasicOperations** solution.  This should automatically download and install all the required NuGet packages that are either missing or need to be updated.  
  
2.  Edit the application configuration file, App.config, to specify connection information for your Common Data Service for Apps server.  For more information, see [Helper code: Configuration classes](web-api-helper-code-configuration-classes.md).  
  
3.  Run the **BasicOperations** project from within Visual Studio.  All sample solutions are configured to run in debug mode by default.  
  
<a name="bkmk_codeListing"></a>
   
## Code listing
 
The most current source for this file  is found in sample download package.  
  
 `Program.cs`  
  
```csharp  
using Microsoft.Crm.Sdk.Samples.HelperCode;  
using Newtonsoft.Json;  
using Newtonsoft.Json.Linq;  
using System;  
using System.Text;  
using System.Collections.Generic;  
using System.Net.Http;  
using System.Net.Http.Headers;  
using System.Threading.Tasks;  
using System.Linq;  
using System.Net;  
  
namespace Microsoft.Crm.Sdk.Samples  
{  
 /// <summary>  
 /// This program performs basic create, retrieve, update, and delete (CRUD) and related  
 /// operations against a CRM Online 2016 or later organization using the Web API.  
 /// </summary>  
 /// <remarks>  
 /// Before building this application, you must first modify the following configuration   
 /// information in the app.config file:  
 ///   - All deployments: Provide connection string service URL's for your organization.  
 ///   - CRM Online: Replace the app settings with the correct values for your Azure   
 ///                 application registration.   
 /// See the provided app.config file for more information.   
 /// </remarks>  
 class BasicOperations  
 {  
  //Provides a persistent client-to-CRM server communication channel.  
  private HttpClient httpClient;  
  //Start with base version and update with actual version later.  
  private Version webAPIVersion = new Version(8, 0);   
  private string getVersionedWebAPIPath()  
  {  
   return string.Format("v{0}/", webAPIVersion.ToString(2));  
  }  
  
  public async Task getWebAPIVersion()  
  {  
  
   HttpRequestMessage RetrieveVersionRequest =  
     new HttpRequestMessage(HttpMethod.Get, getVersionedWebAPIPath() + "RetrieveVersion");  
  
   HttpResponseMessage RetrieveVersionResponse =  
       await httpClient.SendAsync(RetrieveVersionRequest);  
   if (RetrieveVersionResponse.StatusCode == HttpStatusCode.OK)  //200  
   {  
    JObject RetrievedVersion = JsonConvert.DeserializeObject<JObject>(  
        await RetrieveVersionResponse.Content.ReadAsStringAsync());  
    //Capture the actual version available in this organization  
    webAPIVersion = Version.Parse((string)RetrievedVersion.GetValue("Version"));  
   }  
   else  
   {  
    Console.WriteLine("Failed to retrieve the version for reason: {0}",  
        RetrieveVersionResponse.ReasonPhrase);  
    throw new CrmHttpResponseException(RetrieveVersionResponse.Content);  
   }  
  
  }  
  
  //Centralized collection of entity URIs used to manage lifetimes.  
  List<string> entityUris = new List<string>();  
  
  //A set of variables to hold the state of and URIs for primary entity instances.  
  private JObject contact1 = new JObject(), contact2 = new JObject(),  
      retrievedContact1, retrievedContact2;  
  private string contact1Uri;  
  private JObject account1 = new JObject(), account2 = new JObject(),  
      retrievedAccount1, retrievedAccount2;  
  private string account1Uri, account2Uri;  
  
  /// <summary>    
  /// Demonstrates basic create, update, and retrieval operations for entity instances and   
  ///  single properties.    
  /// </summary>  
  public async Task BasicCreateAndUpdatesAsync()  
  {  
   Console.WriteLine("--Section 1 started--");  
   string queryOptions;  //select, expand and filter clauses  
                         //First create a new contact instance,  then add additional property values and update   
                         // several properties.  
                         //Local representation of CRM Contact instance  
   contact1.Add("firstname", "Peter");  
   contact1.Add("lastname", "Cambel");  
  
   HttpRequestMessage createRequest1 =  
       new HttpRequestMessage(HttpMethod.Post, getVersionedWebAPIPath() + "contacts");  
   createRequest1.Content = new StringContent(contact1.ToString(),  
       Encoding.UTF8, "application/json");  
   HttpResponseMessage createResponse1 =  
       await httpClient.SendAsync(createRequest1);  
   if (createResponse1.StatusCode == HttpStatusCode.NoContent)  //204  
   {  
    Console.WriteLine("Contact '{0} {1}' created.",  
        contact1.GetValue("firstname"), contact1.GetValue("lastname"));  
    contact1Uri = createResponse1.Headers.  
        GetValues("OData-EntityId").FirstOrDefault();  
    entityUris.Add(contact1Uri);  
    Console.WriteLine("Contact URI: {0}", contact1Uri);  
   }  
   else  
   {  
    Console.WriteLine("Failed to create contact for reason: {0}",  
        createResponse1.ReasonPhrase);  
    throw new CrmHttpResponseException(createResponse1.Content);  
   }  
  
   //Add additional property values to the existing contact.  As a general   
   // rule, only transmit a minimum working set of properties.  
   JObject contact1Add = new JObject();  
   contact1Add.Add("annualincome", 80000);  
   contact1Add.Add("jobtitle", "Junior Developer");  
  
   HttpRequestMessage updateRequest1 = new HttpRequestMessage(  
       new HttpMethod("PATCH"), contact1Uri);  
   updateRequest1.Content = new StringContent(contact1Add.ToString(),  
       Encoding.UTF8, "application/json");  
   HttpResponseMessage updateResponse1 =  
       await httpClient.SendAsync(updateRequest1);  
   if (updateResponse1.StatusCode == HttpStatusCode.NoContent) //204  
   {  
    Console.WriteLine("Contact '{0} {1}' updated with job title" +  
        " and annual income.", contact1.GetValue("firstname"),  
        contact1.GetValue("lastname"));  
   }  
   else  
   {  
    Console.WriteLine("Failed to update contact for reason: {0}",  
        updateResponse1.ReasonPhrase);  
    throw new CrmHttpResponseException(updateResponse1.Content);  
   }  
  
   //Retrieve the contact with its explicitly initialized properties.  
   //fullname is a read-only calculated value.  
   queryOptions = "?$select=fullname,annualincome,jobtitle,description";  
   HttpResponseMessage retrieveResponse1 = await httpClient.GetAsync(  
       contact1Uri + queryOptions);  
   if (retrieveResponse1.StatusCode == HttpStatusCode.OK) //200  
   {  
    retrievedContact1 = JsonConvert.DeserializeObject<JObject>(  
        await retrieveResponse1.Content.ReadAsStringAsync());  
    Console.WriteLine("Contact '{0}' retrieved: \n\tAnnual income: {1}" +  
        "\n\tJob title: {2} \n\tDescription: {3}.",  
        // Can use either indexer or GetValue method (or a mix of two)  
        retrievedContact1.GetValue("fullname"),  
        retrievedContact1["annualincome"],  
        retrievedContact1["jobtitle"],  
        retrievedContact1["description"]);   //description is initialized empty.  
   }  
   else  
   {  
    Console.WriteLine("Failed to retrieve contact for reason: {0}",  
        retrieveResponse1.ReasonPhrase);  
    throw new CrmHttpResponseException(retrieveResponse1.Content);  
   }  
  
   //Modify specific properties and then update entity instance.  
   JObject contact1Update = new JObject();  
   contact1Update.Add("jobtitle", "Senior Developer");  
   contact1Update.Add("annualincome", 95000);  
   contact1Update.Add("description", "Assignment to-be-determined");  
   HttpRequestMessage updateRequest2 = new HttpRequestMessage(  
       new HttpMethod("PATCH"), contact1Uri);  
   updateRequest2.Content = new StringContent(contact1Update.ToString(),  
       Encoding.UTF8, "application/json");  
   HttpResponseMessage updateResponse2 =  
       await httpClient.SendAsync(updateRequest2);  
   if (updateResponse2.StatusCode == HttpStatusCode.NoContent)  
   {  
    Console.WriteLine("Contact '{0}' updated:", retrievedContact1["fullname"]);  
    Console.WriteLine("\tJob title: {0}", contact1Update["jobtitle"]);  
    Console.WriteLine("\tAnnual income: {0}", contact1Update["annualincome"]);  
    Console.WriteLine("\tDescription: {0}", contact1Update["description"]);  
   }  
   else  
   {  
    Console.WriteLine("Failed to update contact for reason: {0}",  
        updateResponse2.ReasonPhrase);  
    throw new CrmHttpResponseException(updateResponse2.Content);  
   }  
  
   // Change just one property   
   string phone1 = "555-0105";  
   // Create unique identifier by appending property name   
   string contactPhoneUri =  
           string.Format("{0}/{1}", contact1Uri, "telephone1");  
   JObject phoneValue = new JObject();  
   phoneValue.Add("value", phone1);   //Updates must use keyword "value".   
  
   HttpRequestMessage updateRequest3 =  
       new HttpRequestMessage(HttpMethod.Put, contactPhoneUri);  
   updateRequest3.Content = new StringContent(phoneValue.ToString(),  
       Encoding.UTF8, "application/json");  
   HttpResponseMessage updateResponse3 =  
       await httpClient.SendAsync(updateRequest3);  
   if (updateResponse3.StatusCode == HttpStatusCode.NoContent)  
   {  
    Console.WriteLine("Contact '{0}' phone number updated.",  
        retrievedContact1["fullname"]);  
   }  
   else  
   {  
    Console.WriteLine("Failed to update the contact phone number for reason: {0}.",  
        updateResponse3.ReasonPhrase);  
    throw new CrmHttpResponseException(updateResponse3.Content);  
   }  
  
   //Now retrieve just the single property.  
   JObject retrievedProperty1;  
   HttpResponseMessage retrieveResponse2 =  
       await httpClient.GetAsync(contactPhoneUri);  
   if (retrieveResponse2.StatusCode == HttpStatusCode.OK)  
   {  
    retrievedProperty1 = JsonConvert.DeserializeObject<JObject>(  
        await retrieveResponse2.Content.ReadAsStringAsync());  
    Console.WriteLine("Contact's telephone# is: {0}.",  
        retrievedProperty1["value"]);  
   }  
   else  
   {  
    Console.WriteLine("Failed to retrieve the contact phone number for reason: {0}.",  
        retrieveResponse2.ReasonPhrase);  
    throw new CrmHttpResponseException(retrieveResponse2.Content);  
   }  
  
   //The following capabilities require version 8.2 or higher  
   if (webAPIVersion >= Version.Parse("8.2"))  
   {  
  
    //Alternately, starting with December 2016 update (v8.2), a contact instance can be   
    //created and its properties returned in one operation by using a   
    //'Prefer: return=representation' header. Note that a 201 (Created) success status   
    // is returned, and not a 204 (No content).  
    string contactAltUri;  
    JObject contactAlt = new JObject();  
    contactAlt.Add("firstname", "Peter_Alt");  
    contactAlt.Add("lastname", "Cambel");  
    contactAlt.Add("jobtitle", "Junior Developer");  
    contactAlt.Add("annualincome", 80000);  
    contactAlt.Add("telephone1", "555-0110");  
  
    queryOptions = "?$select=fullname,annualincome,jobtitle,contactid";  
    HttpRequestMessage createRequestAlt =  
        new HttpRequestMessage(HttpMethod.Post, getVersionedWebAPIPath() + "contacts" + queryOptions);  
    createRequestAlt.Content = new StringContent(contactAlt.ToString(),  
        Encoding.UTF8, "application/json");  
    createRequestAlt.Headers.Add("Prefer", "return=representation");  
  
    HttpResponseMessage createResponseAlt = await httpClient.SendAsync(createRequestAlt);  
    if (createResponseAlt.StatusCode == HttpStatusCode.Created)  //201  
    {  
     //Body should contain the requested new-contact information.  
     JObject createdContactAlt = JsonConvert.DeserializeObject<JObject>(  
         await createResponseAlt.Content.ReadAsStringAsync());  
     //Because 'OData-EntityId' header not returned in a 201 response, you must instead   
     // construct the URI.  
     contactAltUri = httpClient.BaseAddress + getVersionedWebAPIPath() + "contacts(" + createdContactAlt["contactid"] + ")";  
     entityUris.Add(contactAltUri);  
     Console.WriteLine(  
         "Contact '{0}' created: \n\tAnnual income: {1}" + "\n\tJob title: {2}",  
         createdContactAlt["fullname"],  
         createdContactAlt["annualincome"],  
         createdContactAlt["jobtitle"]);  
     Console.WriteLine("Contact URI: {0}", contactAltUri);  
    }  
    else  
    {  
     Console.WriteLine("Failed to create contact for reason: {0}",  
         createResponseAlt.ReasonPhrase);  
     throw new CrmHttpResponseException(createResponseAlt.Content);  
    }  
  
    //Similarly, the December 2016 update (v8.2) also enables returning selected properties     
    //after an update operation (PATCH), with the 'Prefer: return=representation' header.  
    //Here a success is indicated by 200 (OK) instead of 204 (No content).  
  
    //Since we're reusing a local JObject, reinitialize it to remove extraneous properties.  
    contactAlt.RemoveAll();  
    contactAlt["annualincome"] = 95000;  
    contactAlt["jobtitle"] = "Senior Developer";  
    contactAlt["description"] = "MS Azure and Common Data Service for Apps Specialist";  
  
    queryOptions = "?$select=fullname,annualincome,jobtitle";  
    HttpRequestMessage updateRequestAlt = new HttpRequestMessage(  
        new HttpMethod("PATCH"), contactAltUri + queryOptions);  
    updateRequestAlt.Content = new StringContent(contactAlt.ToString(),  
        Encoding.UTF8, "application/json");  
    updateRequestAlt.Headers.Add("Prefer", "return=representation");  
  
    HttpResponseMessage updateResponseAlt = await httpClient.SendAsync(updateRequestAlt);  
    if (updateResponseAlt.StatusCode == HttpStatusCode.OK) //200  
    {  
     //Body should contain the requested updated-contact information.  
     JObject UpdatedContactAlt = JsonConvert.DeserializeObject<JObject>(  
         await updateResponseAlt.Content.ReadAsStringAsync());  
     Console.WriteLine(  
         "Contact '{0}' updated: \n\tAnnual income: {1}" + "\n\tJob title: {2}",  
         UpdatedContactAlt["fullname"],  
         UpdatedContactAlt["annualincome"],  
         UpdatedContactAlt["jobtitle"]);  
    }  
    else  
    {  
     Console.WriteLine("Failed to update contact for reason: {0}",  
         updateResponse1.ReasonPhrase);  
     throw new CrmHttpResponseException(updateResponse1.Content);  
    }  
   }  
  }  
  /// <summary>    
  /// Demonstrates creation of entity instance and simultaneous association to another,   
  ///  existing entity.   
  /// </summary>  
  public async Task CreateWithAssociationAsync()  
  {  
   Console.WriteLine("\n--Section 2 started--");  
   string queryOptions;  //select, expand and filter clauses  
                         //Create a new account and associate with existing contact in one operation.   
   account1.Add("name", "Contoso Ltd");  
   account1.Add("telephone1", "555-5555");  
   account1.Add("primarycontactid@odata.bind", contact1Uri);  
  
   HttpRequestMessage createRequest2 =  
       new HttpRequestMessage(HttpMethod.Post, getVersionedWebAPIPath() + "accounts");  
   createRequest2.Content = new StringContent(account1.ToString(),  
       Encoding.UTF8, "application/json");  
   HttpResponseMessage createResponse2 =  
       await httpClient.SendAsync(createRequest2);  
   if (createResponse2.StatusCode == HttpStatusCode.NoContent)  
   {  
    Console.WriteLine("Account '{0}' created.", account1.GetValue("name"));  
    account1Uri = createResponse2.Headers.GetValues("OData-EntityId").  
        FirstOrDefault();  
    entityUris.Add(account1Uri);  
   }  
   else  
   {  
    Console.WriteLine("Failed to create account for reason: {0}.",  
        createResponse2.ReasonPhrase);  
    throw new CrmHttpResponseException(createResponse2.Content);  
   }  
  
   //Retrieve account name and primary contact info  
   queryOptions =  
     "?$select=name,&$expand=primarycontactid($select=fullname,jobtitle,annualincome)";  
   HttpResponseMessage retrieveResponse3 =  
       await httpClient.GetAsync(account1Uri + queryOptions);  
   if (retrieveResponse3.StatusCode == HttpStatusCode.OK)  
   {  
    retrievedAccount1 = JsonConvert.DeserializeObject<JObject>(  
        await retrieveResponse3.Content.ReadAsStringAsync());  
    Console.WriteLine("Account '{0}' has primary contact '{1}':",  
        retrievedAccount1["name"],  
        retrievedAccount1.GetValue("primarycontactid")["fullname"]  
        );  
    Console.WriteLine("\tJob title: {0} \n\tAnnual income: {1}",  
        retrievedAccount1.GetValue("primarycontactid")["jobtitle"],  
        retrievedAccount1["primarycontactid"]["annualincome"]  
        );  
   }  
   else  
   {  
    Console.WriteLine("Failed to retrieve account for reason: {0}.",  
        retrieveResponse3.ReasonPhrase);  
    throw new CrmHttpResponseException(retrieveResponse3.Content);  
   }  
  }  
  
  /// <summary>    
  /// Demonstrates creation of entity instance and related entities in a single operation.    
  /// </summary>  
  public async Task CreateRelatedAsync()  
  {  
   Console.WriteLine("\n--Section 3 started--");  
   string queryOptions;  //select, expand and filter clauses  
                         //Create the following entries in one operation: an account, its   
                         // associated primary contact, and open tasks for that contact.  These   
                         // entity types have the following relationships:  
                         //    Accounts   
                         //       |---[Primary] Contact (N-to-1)  
                         //              |---Tasks (1-to-N)  
  
   //Build the Account object inside-out, starting with most nested type(s)  
   JArray tasks = new JArray();  
   JObject task1 = new JObject();  
   task1.Add("subject", "Sign invoice");  
   task1.Add("description", "Invoice #12321");  
   task1.Add("scheduledend", DateTimeOffset.Parse("4/19/2016"));  
   tasks.Add(task1);  
   JObject task2 = new JObject();  
   task2.Add("subject", "Setup new display");  
   task2.Add("description", "Theme is - Spring is in the air");  
   task2.Add("scheduledstart", DateTimeOffset.Parse("4/20/2016"));  
   tasks.Add(task2);  
   JObject task3 = new JObject();  
   task3.Add("subject", "Conduct training");  
   task3.Add("description", "Train team on making our new blended coffee");  
   task3.Add("scheduledstart", DateTimeOffset.Parse("6/1/2016"));  
   tasks.Add(task3);  
  
   contact2.Add("firstname", "Susie");  
   contact2.Add("lastname", "Curtis");  
   contact2.Add("jobtitle", "Coffee Master");  
   contact2.Add("annualincome", 48000);  
   //Add related tasks using corresponding navigation property  
   contact2.Add("Contact_Tasks", tasks);  
  
   account2.Add("name", "Fourth Coffee");  
   //Add related contacts using corresponding navigation property  
   account2.Add("primarycontactid", contact2);  
  
   HttpRequestMessage createRequest3 =  
       new HttpRequestMessage(HttpMethod.Post, getVersionedWebAPIPath() + "accounts");  
   createRequest3.Content = new StringContent(account2.ToString(),  
       Encoding.UTF8, "application/json");  
   HttpResponseMessage createResponse3 =  
       await httpClient.SendAsync(createRequest3);  
   if (createResponse3.StatusCode == HttpStatusCode.NoContent)  
   {  
    Console.WriteLine("Account '{0}' created.",  
        account2.GetValue("name"));  
    account2Uri = createResponse3.Headers.GetValues("OData-EntityId").  
        FirstOrDefault();  
    entityUris.Add(account2Uri);  
   }  
   else  
   {  
    Console.WriteLine("Failed to create account for reason: {0}.",  
        createResponse3.ReasonPhrase);  
    throw new CrmHttpResponseException(createResponse3.Content);  
   }  
  
   //Retrieve account, primary contact info, and assigned tasks for contact.  
   //CRM only supports querying-by-expansion one level deep, so first query   
   // account-primary contact.  
   queryOptions =  
     "?$select=name,&$expand=primarycontactid($select=fullname,jobtitle,annualincome)";  
   HttpResponseMessage retrieveResponse4 =  
       await httpClient.GetAsync(account2Uri + queryOptions);  
   if (retrieveResponse4.StatusCode == HttpStatusCode.OK)  
   {  
    retrievedAccount2 = JsonConvert.DeserializeObject<JObject>(  
        await retrieveResponse4.Content.ReadAsStringAsync());  
    Console.WriteLine("Account '{0}' has primary contact '{1}':",  
        retrievedAccount2.GetValue("name"),  
        retrievedAccount2.GetValue("primarycontactid")["fullname"]);  
    Console.WriteLine("\tJob title: {0} \n\tAnnual income: {1}",  
        retrievedAccount2["primarycontactid"]["jobtitle"],  
        retrievedAccount2["primarycontactid"]["annualincome"]);  
   }  
   else  
   {  
    Console.WriteLine("Failed to retrieve the account/contact info for " +  
        "reason: {0}.", retrieveResponse4.ReasonPhrase);  
    throw new CrmHttpResponseException(retrieveResponse4.Content);  
   }  
   //Next retrieve same contact and its assigned tasks.  
   //Don't have a saved URI for contact 'Susie Curtis', so create one   
   // from base address and entity ID.  
   string contact2Uri = string.Format("{0}contacts({1})",   
    httpClient.BaseAddress + getVersionedWebAPIPath(),   
    retrievedAccount2["primarycontactid"]["contactid"]);   
   entityUris.Add(contact2Uri);  
   queryOptions =  
   "?$select=fullname,&$expand=Contact_Tasks($select=subject,description,scheduledstart,scheduledend)";  
   HttpResponseMessage retrieveResponse5 =  
       await httpClient.GetAsync(contact2Uri + queryOptions);  
   if (retrieveResponse5.StatusCode == HttpStatusCode.OK)  
   {  
    retrievedContact2 = JsonConvert.DeserializeObject<JObject>(  
        await retrieveResponse5.Content.ReadAsStringAsync());  
    Console.WriteLine("Contact '{0}' has the following assigned tasks:",  
        retrievedContact2["fullname"]);  
    foreach (JToken tk in retrievedContact2["Contact_Tasks"])  
    {  
     Console.WriteLine(  
         "Subject: {0}, \n\tDescription: {1}\n\tStart: {2}\n\tEnd: {3}\n",  
         tk["subject"],  
         tk["description"],  
         tk["scheduledstart"].Value<DateTime>().ToString("d"),  
         tk["scheduledend"].Value<DateTime>().ToString("d")  
         );  
    }  
   }  
   else  
   {  
    Console.WriteLine("Failed to retrieve the contact info for reason: {0}.",  
        retrieveResponse5.ReasonPhrase);  
    throw new CrmHttpResponseException(retrieveResponse5.Content);  
   }  
  }  
  
  /// <summary>    
  /// Demonstrates associating and disassociating of existing entity instances.   
  /// </summary>  
  public async Task AssociateExistingAsync()  
  {  
   string queryOptions;  //select, expand and filter clauses  
   Console.WriteLine("\n--Section 4 started--");  
   //Add 'Peter Cambel' to the contact list of 'Fourth Coffee',   
   // a 1-to-N relationship.  
   JObject rel1 = new JObject();   //relationship object for msg content  
   rel1.Add("@odata.id", contact1Uri);  
   Uri navUri1 = new Uri(String.Format("{0}/{1}/$ref", account2Uri,  
       "contact_customer_accounts"));  
   HttpRequestMessage assocRequest1 =  
       new HttpRequestMessage(HttpMethod.Post, navUri1);  
   assocRequest1.Content = new StringContent(rel1.ToString(),  
       Encoding.UTF8, "application/json");  
   HttpResponseMessage assocResponse1 =  
       await httpClient.SendAsync(assocRequest1);  
   if (assocResponse1.StatusCode == HttpStatusCode.NoContent)  
   {  
    Console.WriteLine("Contact '{0}' associated to account '{1}'.",  
        retrievedContact1["fullname"], account2["name"]);  
   }  
   else  
   {  
    Console.WriteLine("Failed to associate account/contact entities " +  
        "for reason: {0}.", assocResponse1.ReasonPhrase);  
    throw new CrmHttpResponseException(assocResponse1.Content);  
   }  
   //Retrieve and output all contacts for account 'Fourth Coffee'.  
   JObject retrievedContactList1;  
   queryOptions = "?$select=fullname,jobtitle";  
   HttpResponseMessage retrieveResponse6 = await httpClient.GetAsync(  
       account2Uri + "/contact_customer_accounts" + queryOptions);  
   if (retrieveResponse6.StatusCode == HttpStatusCode.OK)  
   {  
    retrievedContactList1 = JsonConvert.DeserializeObject<JObject>(  
        await retrieveResponse6.Content.ReadAsStringAsync());  
    Console.WriteLine("Contact list for account '{0}':",  
        retrievedAccount2["name"]);  
    foreach (JToken ct in retrievedContactList1["value"])  
    {  
     Console.WriteLine("\tName: {0}, Job title: {1}",  
         ct["fullname"], ct["jobtitle"]);  
    }  
   }  
   else  
   {  
    Console.WriteLine("Failed to retrieve the account/contact info" +  
        " for reason: {0}.", retrieveResponse6.ReasonPhrase);  
    throw new CrmHttpResponseException(retrieveResponse6.Content);  
   }  
  
   //Dissociate the contact from the account.  For a collection-valued   
   // navigation property, must append URI of referenced entity.  
   string dis1Uri = navUri1 + "?$id=" + contact1Uri;  
   //Equivalently, could have dissociated from the other end of the   
   // relationship, using the single-valued navigation ref, located in   
   // the contact 'Peter Cambel'.  This dissociation URI has a simpler form:  
   // [Org URI]/api/data/v9.0/contacts([contactid#])/parentcustomerid_account/$ref   
  
   HttpResponseMessage disassocResponse1 =  
       await httpClient.DeleteAsync(dis1Uri);  
   if (disassocResponse1.StatusCode == HttpStatusCode.NoContent)  
   {  
    Console.WriteLine("Contact '{0}' dissociated from account '{1}'.",  
        retrievedContact1["fullname"], account2["name"]);  
   }  
   else  
   {  
    Console.WriteLine("Failed to disassociate entities for reason: {0}.",  
        disassocResponse1.ReasonPhrase);  
    throw new CrmHttpResponseException(disassocResponse1.Content);  
   }  
  
   //Associate an opportunity to a competitor, an N-to-N relationship.   
   //First, create the required entity instances.  
   string comp1Uri, oppor1Uri;  
   JObject comp1 = new JObject();  
   comp1.Add("name", "Adventure Works");  
   comp1.Add("strengths",  
       "Strong promoter of private tours for multi-day outdoor adventures");  
   JObject oppor1 = new JObject();  
   oppor1["name"] = "River rafting adventure";  
   oppor1["description"] = "Sales team on a river-rafting offsite and team building";  
  
   HttpRequestMessage createRequest4 =  
       new HttpRequestMessage(HttpMethod.Post, getVersionedWebAPIPath() + "competitors");  
   createRequest4.Content = new StringContent(comp1.ToString(),  
       Encoding.UTF8, "application/json");  
   HttpResponseMessage createResponse4 =  
       await httpClient.SendAsync(createRequest4);  
   if (createResponse4.StatusCode == HttpStatusCode.NoContent)  
   {  
    Console.WriteLine("Competitor '{0}' created.", comp1["name"]);  
    comp1Uri = createResponse4.Headers.GetValues("OData-EntityId").  
        FirstOrDefault();  
    entityUris.Add(comp1Uri);  
   }  
   else  
   {  
    Console.WriteLine("Failed to create competitor for reason: {0}",  
        createResponse4.ReasonPhrase);  
    throw new CrmHttpResponseException(createResponse4.Content);  
   }  
  
   HttpRequestMessage createRequest5 =  
       new HttpRequestMessage(HttpMethod.Post, getVersionedWebAPIPath() + "opportunities");  
   createRequest5.Content = new StringContent(oppor1.ToString(),  
       Encoding.UTF8, "application/json");  
   HttpResponseMessage createResponse5 =  
       await httpClient.SendAsync(createRequest5);  
   if (createResponse5.StatusCode == HttpStatusCode.NoContent)  
   {  
    Console.WriteLine("Opportunity '{0}' created.", oppor1["name"]);  
    oppor1Uri = createResponse5.Headers.GetValues("OData-EntityId").  
        FirstOrDefault();  
    entityUris.Add(oppor1Uri);  
   }  
   else  
   {  
    Console.WriteLine("Failed to create opportunity for reason: {0}",  
        createResponse5.ReasonPhrase);  
    throw new CrmHttpResponseException(createResponse5.Content);  
   }  
  
   //Associate opportunity to competitor via opportunitycompetitors_association.  
   // navigation property.  
   JObject rel2 = new JObject();  
   rel2.Add("@odata.id", comp1Uri);  
   Uri navUri2 = new Uri(String.Format("{0}/{1}/$ref", oppor1Uri,  
       "opportunitycompetitors_association"));  
   HttpRequestMessage assocRequest2 =  
       new HttpRequestMessage(HttpMethod.Post, navUri2);  
   assocRequest2.Content = new StringContent(rel2.ToString(),  
       Encoding.UTF8, "application/json");  
   HttpResponseMessage assocResponse2 =  
       await httpClient.SendAsync(assocRequest2);  
   if (assocResponse2.StatusCode == HttpStatusCode.NoContent)  
   {  
    Console.WriteLine(  
        "Opportunity '{0}' associated with competitor '{1}'.",  
        oppor1["name"], comp1["name"]);  
   }  
   else  
   {  
    Console.WriteLine("Failed to associate competitor/opportunity" +  
        "entities for reason: {0}.", assocResponse2.ReasonPhrase);  
    throw new CrmHttpResponseException(assocResponse2.Content);  
   }  
  
   //Retrieve all opportunities for competitor 'Adventure Works'.  
   JObject retrievedOpporList1;  
   //Select only 'name' to limit returned competitor properties.   
   queryOptions =  
       "?$select=name,&$expand=opportunitycompetitors_association($select=name,description)";  
   HttpResponseMessage retrieveResponse7 =  
       await httpClient.GetAsync(comp1Uri + queryOptions);  
   if (retrieveResponse7.StatusCode == HttpStatusCode.OK)  
   {  
    retrievedOpporList1 = JsonConvert.DeserializeObject<JObject>(  
        await retrieveResponse7.Content.ReadAsStringAsync());  
    Console.WriteLine("Competitor '{0}' has the following opportunities:",  
        retrievedOpporList1["name"]);  
    foreach (JToken op in  
        retrievedOpporList1["opportunitycompetitors_association"])  
    {  
     Console.WriteLine("\tName: {0}, \n\tDescription: {1}",  
         op["name"], op["description"]);  
    }  
   }  
   else  
   {  
    Console.WriteLine("Failed to retrieve the competitor/opportunity"  
        + " info for reason: {0}.",  
        retrieveResponse7.ReasonPhrase);  
    throw new CrmHttpResponseException(retrieveResponse7.Content);  
   }  
  
   //Dissociate opportunity from competitor.    
   string dis2Uri = navUri2 + "?$id=" + comp1Uri;  
   HttpResponseMessage disassocResponse2 =  
       await httpClient.DeleteAsync(dis2Uri);  
   if (disassocResponse2.StatusCode == HttpStatusCode.NoContent)  
   {  
    Console.WriteLine(  
        "Opportunity '{0}' disassociated from competitor '{1}'.",  
        oppor1["name"], comp1["name"]);  
   }  
   else  
   {  
    Console.WriteLine("Failed to disassociate entities for reason: {0}.",  
        disassocResponse1.ReasonPhrase);  
    throw new CrmHttpResponseException(disassocResponse1.Content);  
   }  
  }  
  
  /// <summary>   
  ///Provides the high-level logical flow of the program, as well as a section   
  /// containing cleanup code.  
  /// </summary>  
  public async Task RunAsync()  
  {  
   try  
   {  
    await getWebAPIVersion();  
    await BasicCreateAndUpdatesAsync();  
    await CreateWithAssociationAsync();  
    await CreateRelatedAsync();  
    await AssociateExistingAsync();  
   }  
   catch (Exception ex)  
   { DisplayException(ex); }  
   finally  
   {  
    #region Section 5: Delete sample entities   
    Console.WriteLine("\n--Section 5 started--");  
    //Delete all the created sample entities.  Note that explicit deletion is not required   
    // for contact tasks because these are automatically cascade-deleted with owner.   
    Console.Write("\nDo you want these entity records deleted? (y/n) [y]: ");  
    String answer = Console.ReadLine();  
    answer = answer.Trim();  
    if (!(answer.StartsWith("y") || answer.StartsWith("Y") || answer == String.Empty))  
    { entityUris.Clear(); }  
  
    HttpResponseMessage deleteResponse1;  
    int successCnt = 0, notFoundCnt = 0, failCnt = 0;  
    HttpContent lastBadResponseContent = null;  
    foreach (string ent in entityUris)  
    {  
     deleteResponse1 = await httpClient.DeleteAsync(ent);  
     if (deleteResponse1.IsSuccessStatusCode) //200-299  
     {  
      Console.WriteLine("Entity deleted: \n{0}.", ent);  
      successCnt++;  
     }  
     else if (deleteResponse1.StatusCode == HttpStatusCode.NotFound) //404  
     {  
      //May have been deleted by another user or via cascade operation  
      Console.WriteLine("Entity not found: {0}.", ent);  
      notFoundCnt++;  
     }  
     else  
     {  
      Console.WriteLine("Failed to delete: {0}.", ent);  
      failCnt++;  
      lastBadResponseContent = deleteResponse1.Content;  
     }  
    }  
    Console.WriteLine("Entities deleted: {0}, not found: {1}, delete " +  
        "failures: {2}. \n", successCnt, notFoundCnt, failCnt);  
    entityUris.Clear();  
    if (failCnt > 0)  
    {  
     //Throw last failure  
     throw new CrmHttpResponseException(lastBadResponseContent);  
    }  
    #endregion Section 5: Delete sample entities  
   }  
  }  
  
  static public void Main(string[] args)  
  {  
   BasicOperations app = new BasicOperations();  
   try  
   {  
    //Read configuration file and connect to specified CRM server.  
    app.ConnectToCRM(args);  
    Task.WaitAll(Task.Run(async () => await app.RunAsync()));  
   }  
   catch (System.Exception ex) { DisplayException(ex); }  
   finally  
   {  
    if (app.httpClient != null)  
    { app.httpClient.Dispose(); }  
    Console.WriteLine("Press <Enter> to exit the program.");  
    Console.ReadLine();  
   }  
  }  
  
  /// <summary>  
  /// Obtains the connection information from the application's configuration file, then   
  /// uses this info to connect to the specified CRM service.  
  /// </summary>  
  /// <param name="args"> Command line arguments. The first specifies the name of the   
  ///  connection string setting. </param>  
  private void ConnectToCRM(String[] cmdargs)  
  {  
   //Create a helper object to read app.config for service URL and application   
   // registration settings.  
   Configuration config = null;  
   if (cmdargs.Length > 0)  
   { config = new FileConfiguration(cmdargs[0]); }  
   else  
   { config = new FileConfiguration(null); }  
   //Create a helper object to authenticate the user with this connection info.  
   Authentication auth = new Authentication(config);  
   //Next use a HttpClient object to connect to specified CRM Web service.  
   httpClient = new HttpClient(auth.ClientHandler, true);  
   //Define the Web API base address, the max period of execute time, the   
   // default OData version, and the default response payload format.  
   httpClient.BaseAddress = new Uri(config.ServiceUrl + "api/data/");  
   httpClient.Timeout = new TimeSpan(0, 2, 0);  
   httpClient.DefaultRequestHeaders.Add("OData-MaxVersion", "4.0");  
   httpClient.DefaultRequestHeaders.Add("OData-Version", "4.0");  
   httpClient.DefaultRequestHeaders.Accept.Add(  
       new MediaTypeWithQualityHeaderValue("application/json"));  
  }  
  
  /// <summary> Helper method to display caught exceptions </summary>  
  private static void DisplayException(Exception ex)  
  {  
   Console.WriteLine("The application terminated with an error.");  
   Console.WriteLine(ex.Message);  
   while (ex.InnerException != null)  
   {  
    Console.WriteLine("\t* {0}", ex.InnerException.Message);  
    ex = ex.InnerException;  
   }  
  }  
 }  
}  
  
```  
  
### See also

[Use the Common Data Service for Apps Web API](overview.md)<br />
[Create an entity using the Web API](create-entity-web-api.md)<br />
[Update and delete entities using the Web API](update-delete-entities-using-web-api.md)<br />
[Retrieve an entity using the Web API](retrieve-entity-using-web-api.md)<br />
[Update and delete entities using the Web API](update-delete-entities-using-web-api.md)<br />
[Web API Samples](web-api-samples.md)<br />
[Web API Basic Operations Sample](web-api-basic-operations-sample.md)
[Web API Query Data Sample (C#)](samples/query-data-csharp.md)<br />
[Web API Conditional Operations Sample (C#)](samples/conditional-operations-csharp.md)<br />
[Web API Functions and Actions Sample (C#)](samples/functions-actions-csharp.md)
