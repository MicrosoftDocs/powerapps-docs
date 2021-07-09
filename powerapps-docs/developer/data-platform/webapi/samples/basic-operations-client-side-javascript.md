---
title: "Web API Basic Operations Sample (Client-side JavaScript) (Microsoft Dataverse)| Microsoft Docs"
description: "This sample demonstrates how to perform basic CRUD (create, retrieve, update, and delete) and association and dissociation operations on entity instances using client-side JavaScript and the Microsoft Dataverse Web API"
ms.custom: ""
ms.date: 10/31/2018
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 11847c67-2807-4cb5-998b-90f45d3d98a7
caps.latest.revision: 27
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
# Web API Basic Operations Sample (Client-side JavaScript)

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample demonstrates how to perform basic CRUD (create, retrieve, update, and delete) and association and dissociation operations on entity instances using client-side JavaScript.  
  
> [!NOTE]
>  This sample implements the operations detailed in the [Web API Basic Operations Sample](../web-api-basic-operations-sample.md) and uses the common JavaScript constructs described in [Web API Samples (Client-side JavaScript)](../web-api-samples-client-side-javascript.md)
  
<a name="bkmk_prerequisites"></a>

## Prerequisites

 To run this sample, the following is required:  
  
- Access to Microsoft Dataverse environment.  
  
- A user account with privileges to import solutions and perform CRUD operations, typically a system administrator or system customizer security role.  
  
<a name="bkmk_runsample"></a>

## Run this sample

To run this sample, download the solution package from [here](https://github.com/microsoft/PowerApps-Samples/tree/master/cds/webapi/JS/WebAPIBasicOperations) and extract the contents. Locate the `WebAPIBasicOperations_1_0_0_1_managed.zip` solution and import it into your Dataverse environment and run the sample. For instructions on how to import the sample solution, see [Web API Samples (Client-side JavaScript)](../web-api-samples-client-side-javascript.md).  
  
<a name="bkmk_codesample"></a>

## Code sample

 This sample includes two web resources:  
  
- [WebAPIBasicOperations.html](#bkmk_WebAPIBasicOperations)  
  
- [WebAPIBasicOperations.js](#bkmk_WebAPIBasicOperationsJS)  
  
<a name="bkmk_WebAPIBasicOperations"></a>

### WebAPIBasicOperations.html

 The WebAPIBasicOperations.html web resource provides the context in which the JavaScript code will run.  
  
```html  
<html>  
<head>  
    <title>Microsoft CRM Web API Basic Operations Example</title>  
    <meta charset="utf-8" />  
    <meta http-equiv="X-UA-Compatible" content="IE=Edge" />  
    <script src="../ClientGlobalContext.js.aspx" type="text/javascript"></script>  
    <script src="scripts/es6promise.js" type="text/javascript"></script>  
    <script src="scripts/WebAPIBasicOperations.js" type="text/javascript"></script>  
  
    <style type="text/css">  
        body {  
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;  
        }  
  
        #preferences {  
            border: inset;  
            padding: 10px 10px;  
        }  
  
        #output_area {  
            border: inset;  
            background-color: gainsboro;  
            padding: 10px 10px;  
        }  
    </style>  
</head>  
<body>  
    <h1>Microsoft CRM Web API Basic Operations Example</h1>  
    <p>This page demonstrates the CRM Web API's basic operations using JavaScript.</p>  
  
    <h2>Instructions</h2>  
    <p>  
        Choose your preferences and run the JavaScript code.   
    Use your browser's developer tools to view the output written to the console (e.g.: in IE 11 or Microsoft Edge,   
    press F12 to load the Developer Tools).  
    </p>  
    <p>  
        Remove sample data (Choose whether you want to delete sample data created during this execution):  
            <br />  
        <input name="removesampledata" type="radio" value="yes" checked />  
        Yes  
            <input name="removesampledata" type="radio" value="no" />  
        No  
    </p>  
    <input type="button" name="start_sample" value="Start Sample" onclick="Sdk.startSample()" />  
  
</body>  
</html>  
  
```  
  
<a name="bkmk_WebAPIBasicOperationsJS"></a>

### WebAPIBasicOperations.js

 The WebAPIBasicOperations.js web resource is the JavaScript library that defines the operations this sample performs.  
  
```javascript
  
"use strict";  
var Sdk = window.Sdk || {};  
  
/**  
 * @function getClientUrl  
 * @description Get the client URL.  
 * @returns {string} The client URL.  
 */  
Sdk.getClientUrl = function () {  
 var context;  
 // GetGlobalContext defined by including reference to   
 // ClientGlobalContext.js.aspx in the HTML page.  
 if (typeof GetGlobalContext != "undefined") {  
  context = GetGlobalContext();  
 } else {  
  if (typeof Xrm != "undefined") {  
   // Xrm.Page.context defined within the Xrm.Page object model for form scripts.  
   context = Xrm.Page.context;  
  } else {  
   throw new Error("Context is not available.");  
  }  
 }  
 return context.getClientUrl();  
  
};  
  
/**  
 * An object instantiated to manage detecting the  
 * Web API version in conjunction with the   
 * Sdk.retrieveVersion function  
 */  
Sdk.versionManager = new function () {  
 //Start with base version  
 var _webAPIMajorVersion = 8;  
 var _webAPIMinorVersion = 0;  
 //Use properties to increment version and provide WebAPIPath string used by Sdk.request;  
 Object.defineProperties(this, {  
  "WebAPIMajorVersion": {  
   get: function () {  
    return _webAPIMajorVersion;  
   },  
   set: function (value) {  
    if (typeof value != "number") {  
     throw new Error("Sdk.versionManager.WebAPIMajorVersion property must be a number.")  
    }  
    _webAPIMajorVersion = parseInt(value, 10);  
   }  
  },  
  "WebAPIMinorVersion": {  
   get: function () {  
    return _webAPIMinorVersion;  
   },  
   set: function (value) {  
    if (isNaN(value)) {  
     throw new Error("Sdk.versionManager._webAPIMinorVersion property must be a number.")  
    }  
    _webAPIMinorVersion = parseInt(value, 10);  
   }  
  },  
  "WebAPIPath": {  
   get: function () {  
    return "/api/data/v" + _webAPIMajorVersion + "." + _webAPIMinorVersion;  
   }  
  }  
 })  
  
}  
  
//Setting variables specific to this sample within a container so they won't be   
// overwritten by another scripts code  
Sdk.SampleVariables = {  
 entitiesToDelete: [],   // Entity URIs to be deleted later (if user so chooses)  
 deleteData: true,       // Controls whether sample data are deleted at the end of sample run  
 contact1Uri: null,      // e.g.: Peter Cambel  
 contactAltUri: null,    // e.g.: Peter_Alt Cambel  
 account1Uri: null,      // e.g.: Contoso, Ltd  
 account2Uri: null,      // e.g.: Fourth Coffee  
 contact2Uri: null,      // e.g.: Susie Curtis  
 opportunity1Uri: null,  // e.g.: Adventure Works  
 competitor1Uri: null  
  
}  
  
/**  
 * @function request  
 * @description Generic helper function to handle basic XMLHttpRequest calls.  
 * @param {string} action - The request action. String is case-sensitive.  
 * @param {string} uri - An absolute or relative URI. Relative URI starts with a "/".  
 * @param {object} data - An object representing an entity. Required for create and update actions.  
 * @param {object} addHeader - An object with header and value properties to add to the request  
 * @returns {Promise} - A Promise that returns either the request object or an error object.  
 */  
Sdk.request = function (action, uri, data, addHeader) {  
 if (!RegExp(action, "g").test("POST PATCH PUT GET DELETE")) { // Expected action verbs.  
  throw new Error("Sdk.request: action parameter must be one of the following: " +  
      "POST, PATCH, PUT, GET, or DELETE.");  
 }  
 if (!typeof uri === "string") {  
  throw new Error("Sdk.request: uri parameter must be a string.");  
 }  
 if ((RegExp(action, "g").test("POST PATCH PUT")) && (!data)) {  
  throw new Error("Sdk.request: data parameter must not be null for operations that create or modify data.");  
 }  
 if (addHeader) {  
  if (typeof addHeader.header != "string" || typeof addHeader.value != "string") {  
   throw new Error("Sdk.request: addHeader parameter must have header and value properties that are strings.");  
  }  
 }  
  
 // Construct a fully qualified URI if a relative URI is passed in.  
 if (uri.charAt(0) === "/") {  
  //This sample will try to use the latest version of the web API as detected by the   
  // Sdk.retrieveVersion function.  
  uri = Sdk.getClientUrl() + Sdk.versionManager.WebAPIPath + uri;  
 }  
  
 return new Promise(function (resolve, reject) {  
  var request = new XMLHttpRequest();  
  request.open(action, encodeURI(uri), true);  
  request.setRequestHeader("OData-MaxVersion", "4.0");  
  request.setRequestHeader("OData-Version", "4.0");  
  request.setRequestHeader("Accept", "application/json");  
  request.setRequestHeader("Content-Type", "application/json; charset=utf-8");  
  if (addHeader) {  
   request.setRequestHeader(addHeader.header, addHeader.value);  
  }  
  request.onreadystatechange = function () {  
   if (this.readyState === 4) {  
    request.onreadystatechange = null;  
    switch (this.status) {  
     case 200: // Operation success with content returned in response body.  
     case 201: // Create success.   
     case 204: // Operation success with no content returned in response body.  
      resolve(this);  
      break;  
     default: // All other statuses are unexpected so are treated like errors.  
      var error;  
      try {  
       error = JSON.parse(request.response).error;  
      } catch (e) {  
       error = new Error("Unexpected Error");  
      }  
      reject(error);  
      break;  
    }  
   }  
  };  
  request.send(JSON.stringify(data));  
 });  
};  
  
/**  
 * @function startSample  
 * @description Runs the sample.   
 * This sample demonstrates basic CRUD+ operations.   
 * Results are sent to the debugger's console window.  
 */  
Sdk.startSample = function () {  
 // Initializing.  
 Sdk.SampleVariables.deleteData = document.getElementsByName("removesampledata")[0].checked;  
 Sdk.SampleVariables.entitiesToDelete = []; // Reset the array.  
 Sdk.SampleVariables.contact1Uri = "";  
 Sdk.SampleVariables.account1Uri = "";  
 Sdk.SampleVariables.account2Uri = "";  
 Sdk.SampleVariables.contact2Uri = "";  
 Sdk.SampleVariables.opportunity1Uri = "";  
 Sdk.SampleVariables.competitor1Uri = "";  
  
 /**  
  * Behavior of this sample varies by version  
  * So starting by retrieving the version;  
  */  
  
 Sdk.retrieveVersion()  
 .then(function () {  
  return Sdk.basicCreateAndUpdatesAsync()  
 })  
.then(function () {  
 return Sdk.createWithAssociationAsync()  
})  
.then(function () {  
 return Sdk.createRelatedAsync()  
})  
.then(function () {  
 return Sdk.associateExistingAsync()  
})  
.then(function () {  
 return Sdk.deleteSampleData()  
})  
.catch(function (err) {  
 console.log("ERROR: " + err.message);  
});  
  
}  
  
Sdk.retrieveVersion = function () {  
 return new Promise(function (resolve, reject) {  
  Sdk.request("GET", "/RetrieveVersion")  
  .then(function (request) {  
   try {  
    var RetrieveVersionResponse = JSON.parse(request.response);  
    var fullVersion = RetrieveVersionResponse.Version;  
    var versionData = fullVersion.split(".");  
    Sdk.versionManager.WebAPIMajorVersion = parseInt(versionData[0], 10);  
    Sdk.versionManager.WebAPIMinorVersion = parseInt(versionData[1], 10);  
    resolve();  
   } catch (err) {  
    reject(new Error("Error processing version: " + err.message))  
   }  
  })  
  .catch(function (err) {  
   reject(new Error("Error retrieving version: " + err.message))  
  })  
 });  
};  
  
Sdk.basicCreateAndUpdatesAsync = function () {  
 return new Promise(function (resolve, reject) {  
  
  // Section 1.  
  //  
  // Create the contact using POST request.   
  // A new entry will be added regardless if a contact with this info already exists in the system or not.  
  console.log("--Section 1 started--");  
  var contact = {};  
  contact.firstname = "Peter";  
  contact.lastname = "Cambel";  
  
  var entitySetName = "/contacts";  
  
  Sdk.request("POST", entitySetName, contact)  
 .then(function (request) {  
  // Process response from previous request.  
  Sdk.SampleVariables.contact1Uri = request.getResponseHeader("OData-EntityId");  
  Sdk.SampleVariables.entitiesToDelete.push(Sdk.SampleVariables.contact1Uri); // To delete later  
  console.log("Contact 'Peter Cambel' created with URI: %s", Sdk.SampleVariables.contact1Uri);  
  
  // Setup for next request.  
  //  
  // Update contact.  
  // Add property values to a specific contact using PATCH request.  
  var contact = {};  
  contact.annualincome = 80000.00;  
  contact.jobtitle = "Junior Developer";  
  return Sdk.request("PATCH", Sdk.SampleVariables.contact1Uri, contact)  
 })  
 .then(function () {  
  // Process response from previous request.  
  console.log("Contact 'Peter Cambel' updated with job title and annual income.");  
  
  // Setup for next request.  
  //  
  // Retrieve selected properties of a Contact entity using GET request.   
  // NOTE: It is performance best practice to select only the properties you need.  
  
  // Retrieved contact properties.  
  var properties = [  
   "fullname",  
   "annualincome",  
   "jobtitle",  
   "description"].join();  
  
  // NOTE: For performance best practices, use $select to limit the properties you want to return  
  // See also: https://msdn.microsoft.com/library/gg334767.aspx#bkmk_requestProperties  
  var query = "?$select=" + properties;  
  return Sdk.request("GET", Sdk.SampleVariables.contact1Uri + query, null);  
 })  
 .then(function (request) {  
  // Process response from previous request.  
  var contact1 = JSON.parse(request.response);  
  var successMsg = "Contact '%s' retrieved:\n"  
      + "\tAnnual income: %s \n"  
      + "\tJob title: %s \n"  
      + "\tDescription: %s";  
  console.log(successMsg,  
      contact1.fullname,      // This property is read-only. Calculated from firstname and lastname.  
      contact1.annualincome,  
      contact1.jobtitle,  
      contact1.description); // Description will be "null" because it has not been set yet.  
  
  // Setup for next request.  
  //  
  // Update properties.  
  // Set new values for some of the properties and apply the values to the server via PATCH request.  
  // Notice that we are updating the jobtitle and annualincome properties and adding value to the   
  // description property in the same request.  
  var contact = {};  
  contact.jobtitle = "Senior Developer";  
  contact.annualincome = 95000.00;  
  contact.description = "Assignment to-be-determined. ";  
  return Sdk.request("PATCH", Sdk.SampleVariables.contact1Uri, contact);  
 })  
 .then(function () {  
  // Process response from previous request.  
  console.log("Contact 'Peter Cambel' updated:\n"  
                      + "\tJob title: Senior Developer, \n"  
                      + "\tAnnual income: 95000, \n"  
                      + "\tDescription: Assignment to-be-determined.");  
  
  // Setup for next request.  
  //  
  // Set value for a single property using PUT request.  
  // In this case, we are setting the telephone1 property to "555-0105".  
  var value = { value: "555-0105" };  
  return Sdk.request("PUT", Sdk.SampleVariables.contact1Uri + "/telephone1", value);  
 })  
 .then(function () {  
  // Process response from previous request.  
  console.log("Contact 'Peter Cambel' phone number updated.");  
  
  // Setup for next request.  
  //  
  // Retrieve single value property.  
  // Get a value of a single property using GET request.  
  // In this case, telephone1 is retrieved. We should get back "555-0105".  
  return Sdk.request("GET", Sdk.SampleVariables.contact1Uri + "/telephone1", null);  
 })  
 .then(function (request) {  
  // Process response from previous request.  
  var phoneNumber = JSON.parse(request.response);  
  console.log("Contact's phone number is: %s", phoneNumber.value);  
 })  
 .then(function () {  
  // Setup for next request.  
  //The following operations require version 8.2 or higher  
  if (Sdk.versionManager.WebAPIMajorVersion > 8 ||  
   (Sdk.versionManager.WebAPIMajorVersion == 8 && Sdk.versionManager.WebAPIMinorVersion >= 2)  
   ) {  
   // Starting with December 2016 update (v8.2), a contact instance can be   
   // created and its properties returned in one operation by using a   
   //'Prefer: return=representation' header.  
   var contactAlt = {};  
   contactAlt.firstname = "Peter_Alt";  
   contactAlt.lastname = "Cambel";  
   contactAlt.jobtitle = "Junior Developer";  
   contactAlt.annualincome = 80000;  
   contactAlt.telephone1 = "555-0110";  
   var properties = [  
    "fullname",  
    "annualincome",  
    "jobtitle"].join();  
   var query = "?$select=" + properties;  
   // Create contact and return its state (in the body).  
   var retRepHeader = { header: "Prefer", value: "return=representation" };  
   Sdk.request("POST", entitySetName + query, contactAlt, retRepHeader)  
  .then(function (request) {  
   var contactA = JSON.parse(request.response);  
   //Because 'OData-EntityId' header not returned in a 201 response, you must instead   
   // construct the URI.  
   Sdk.SampleVariables.contactAltUri = Sdk.getClientUrl() +  
    Sdk.versionManager.WebAPIPath +  
    "/contacts(" +  
    contactA.contactid +  
    ")";  
   Sdk.SampleVariables.entitiesToDelete.push(Sdk.SampleVariables.contactAltUri);  
   var successMsg = "Contact '%s' created:\n"  
       + "\tAnnual income: %s \n"  
       + "\tJob title: %s \n";  
   console.log(successMsg,  
       contactA.fullname,  
       contactA.annualincome,  
       contactA.jobtitle);  
   console.log("Contact URI: %s", Sdk.SampleVariables.contactAltUri);  
  })  
  .then(function () {  
   // Setup for next request.  
   //Similarly, the December 2016 update (v8.2) also enables returning selected properties     
   //after an update operation (PATCH), with the 'Prefer: return=representation' header.  
   var contactAlt = {};  
   contactAlt.jobtitle = "Senior Developer";  
   contactAlt.annualincome = 95000;  
   contactAlt.description = "MS Azure and Dataverse Specialist";  
   var properties = [  
      "fullname",  
      "annualincome",  
      "jobtitle",  
      "description"].join();  
   var query = "?$select=" + properties;  
   // Update contact and return its state (in the body).  
   var retRepHeader = { header: "Prefer", value: "return=representation" };  
   return Sdk.request("PATCH", Sdk.SampleVariables.contactAltUri + query, contactAlt, retRepHeader);  
  })  
  .then(function (request) {  
   // Process response from previous request.  
   var contactA = JSON.parse(request.response);  
   var successMsg = "Contact '%s' updated:\n"  
       + "\tAnnual income: %s \n"  
       + "\tJob title: %s \n";  
   console.log(successMsg,  
       contactA.fullname,  
       contactA.annualincome,  
       contactA.jobtitle);  
   //End this series of operations:  
   resolve();  
  })  
  .catch(function (err) {  
   reject(err);  
  });  
  }  
  else {  
   resolve();  
  }  
 })  
 .catch(function (err) {  
  reject(err);  
 });  
 });  
};  
  
Sdk.createWithAssociationAsync = function () {  
 return new Promise(function (resolve, reject) {  
  // Section 2.  
  //  
  // Create a new account entity and associate it with an existing contact using POST request.  
  console.log("\n--Section 2 started--");  
  var account = {};  
  account.name = "Contoso, Ltd.";  
  account.telephone1 = "555-5555";  
  account["primarycontactid@odata.bind"] = Sdk.SampleVariables.contact1Uri; //relative URI ok. E.g.: "/contacts(###)".  
  
  var entitySetName = "/accounts";  
  
  Sdk.request("POST", entitySetName, account)  
 .then(function (request) {  
  // Process response from previous request.  
  Sdk.SampleVariables.account1Uri = request.getResponseHeader("OData-EntityId");  
  Sdk.SampleVariables.entitiesToDelete.push(Sdk.SampleVariables.account1Uri);  
  console.log("Account 'Contoso, Ltd.' created.");  
  
  // Setup for next request.  
  //  
  // Retrieve account's primary contact with selected properties using GET request and 'expand' query.  
  var contactProperties = [  
      "fullname",  
      "jobtitle",  
      "annualincome"  
  ].join();  
  var query = "?$select=name,telephone1&$expand=primarycontactid($select=" + contactProperties + ")";  
  return Sdk.request("GET", Sdk.SampleVariables.account1Uri + query, null);  
 })  
 .then(function (request) {  
  // Process response from previous request.  
  var account1 = JSON.parse(request.response);  
  var successMsg = "Account '%s' has primary contact '%s':  \n"  
                  + "\tJob title:  %s \n"  
                  + "\tAnnual income:  %s ";  
  console.log(successMsg,  
      account1.name,  
      account1.primarycontactid.fullname,  
      account1.primarycontactid.jobtitle,  
      account1.primarycontactid.annualincome);  
  //End this series of operations:  
  resolve();  
 })  
 .catch(function (err) {  
  reject(err);  
 });  
 });  
};  
  
Sdk.createRelatedAsync = function () {  
 return new Promise(function (resolve, reject) {  
  
  // Section 3.  
  //  
  // Create related entities (deep insert).  
  // Create the following entities in one operation using deep insert technique:  
  //   account  
  //   |--- contact  
  //        |--- tasks  
  // Then retrieve properties of these entities  
  //  
  // Constructing the entity relationship.  
  console.log("\n--Section 3 started--");  
  var account = {};  
  account.name = "Fourth Coffee";  
  account.primarycontactid = {  
   firstname: "Susie",  
   lastname: "Curtis",  
   jobtitle: "Coffee Master",  
   annualincome: 48000.00,  
   Contact_Tasks: [  
       {  
        subject: "Sign invoice",  
        description: "Invoice #12321",  
        scheduledend: new Date("April 19th, 2016")  
       },  
       {  
        subject: "Setup new display",  
        description: "Theme is - Spring is in the air",  
        scheduledstart: new Date("4/20/2016")  
       },  
       {  
        subject: "Conduct training",  
        description: "Train team on making our new blended coffee",  
        scheduledstart: new Date("6/1/2016")  
       }  
   ]  
  };  
  
  var entitySetName = "/accounts";  
  Sdk.request("POST", entitySetName, account)  
 .then(function (request) {  
  // Process response from previous request.  
  Sdk.SampleVariables.account2Uri = request.getResponseHeader("OData-EntityId");  
  Sdk.SampleVariables.entitiesToDelete.push(Sdk.SampleVariables.account2Uri);  
  console.log("Account 'Fourth Coffee' created.");  
  
  // Setup for next request.  
  //  
  // Retrieve account entity info using GET request and 'expand' query.  
  var contactProperties = [  
   "fullname",  
   "jobtitle",  
   "annualincome"].join();  
  
  // Expand on primarycontactid to select some of contact's properties.  
  // NOTE: With $expand, the CRM server will return values for the selected properties.   
  // The CRM Web API only supports expansions one level deep.  
  // See also: https://msdn.microsoft.com/library/mt607871.aspx#bkmk_expandRelated  
  var query = "?$select=name&$expand=primarycontactid($select=" + contactProperties + ")";  
  return Sdk.request("GET", Sdk.SampleVariables.account2Uri + query, null);  
 })  
 .then(function (request) {  
  // Process response from previous request.  
  var account2 = JSON.parse(request.response);  
  var successMsg = "Account '%s' has primary contact '%s':\n"  
      + "\tJob title:  %s \n"  
      + "\tAnnual income:  %s";  
  console.log(successMsg,  
      account2.name,  
      account2.primarycontactid.fullname,  
      account2.primarycontactid.jobtitle,  
      account2.primarycontactid.annualincome);  
  
  // Setup for next request.  
  //  
  // Retrieve contact entity and expanding on its tasks using GET request.  
  Sdk.SampleVariables.contact2Uri = Sdk.getClientUrl() + Sdk.versionManager.WebAPIPath + "/contacts(" + account2.primarycontactid.contactid + ")"; //Full URI.  
  Sdk.SampleVariables.entitiesToDelete.push(Sdk.SampleVariables.contact2Uri); // For Susie Curtis  
  var contactProperties = ["fullname", "jobtitle"].join();  
  var contactTaskProperties = ["subject", "description", "scheduledstart", "scheduledend"].join();  
  
  // Expand on contact_tasks to select some of its properties for each task.  
  var query = "?$select=" + contactProperties +  
      "&$expand=Contact_Tasks($select=" + contactTaskProperties + ")";  
  return Sdk.request("GET", Sdk.SampleVariables.contact2Uri + query, null);  
 })  
 .then(function (request) {  
  // Process response from previous request.  
  var contact2 = JSON.parse(request.response);  
  console.log("Contact '%s' has the following assigned tasks:", contact2.fullname);  
  
  // construct the output string.  
  var successMsg = "Subject: %s \n"  
  + "\tDescription: %s \n"  
  + "\tStart: %s \n"  
  + "\tEnd: %s \n";  
  
  for (var i = 0; i < contact2.Contact_Tasks.length; i++) {  
   console.log(successMsg,  
       contact2.Contact_Tasks[i].subject,  
       contact2.Contact_Tasks[i].description,  
       contact2.Contact_Tasks[i].scheduledstart,  
       contact2.Contact_Tasks[i].scheduledend  
   );  
  }  
  
  //End this series of operations:  
  resolve();  
 })  
 .catch(function (err) {  
  reject(err);  
 });  
 });  
};  
  
Sdk.associateExistingAsync = function () {  
 return new Promise(function (resolve, reject) {  
  
  // Section 4  
  //  
  // Entity associations:  
  // Associate to existing entities via the different relationship types:  
  // 1) 1:N relationship - Associate an existing contact to an existing account   
  //      (e.g.: contact - Peter Cambel to account - Fourth Coffee).  
  // 2) N:N relationship - Associate an competitor to opportunity.  
  
  console.log("\n--Section 4 started--");  
  var contact = {};  
  contact["@odata.id"] = Sdk.SampleVariables.contact1Uri;  
  
  Sdk.request("POST", Sdk.SampleVariables.account2Uri + "/contact_customer_accounts/$ref", contact)  
 .then(function () {  
  // Process response from previous request.  
  console.log("Contact 'Peter Cambel' associated to account 'Fourth Coffee'.");  
  
  // Setup for next request.  
  //  
  // Verify that the reference was made as expected.  
  var contactProperties = ["fullname", "jobtitle"].join();  
  
  // This returns a collection of all associated contacts...in a "value" array.  
  var query = "/contact_customer_accounts?$select=" + contactProperties;  
  return Sdk.request("GET", Sdk.SampleVariables.account2Uri + query, null);  
 })  
 .then(function (request) {  
  // Process response from previous request.  
  var relatedContacts = JSON.parse(request.response).value; //collection is in the "value" array.  
  var successMsg = "\tName: %s, "  
                  + "Job title: %s ";  
  
  console.log("Contact list for account 'Fourth Coffee': ");  
  
  for (var i = 0; i < relatedContacts.length; i++) {  
   console.log(successMsg,  
       relatedContacts[i].fullname,  
       relatedContacts[i].jobtitle  
   );  
  }  
  
  // Setup for next request.  
  //  
  // Disassociate a contact from an account.  
  return Sdk.request("DELETE", Sdk.SampleVariables.account2Uri + "/contact_customer_accounts/$ref?$id=" + Sdk.SampleVariables.contact1Uri, null);  
 })  
 .then(function () {  
  // Process response from previous request.  
  console.log("Contact 'Peter Cambel' disassociated from account 'Fourth Coffee'.");  
  
  // Setup for next request.  
  //  
  // N:N relationship:  
  // Associate a competitor to an opportunity.  
  var competitor = {};  
  competitor.name = "Adventure Works";  
  competitor.strengths = "Strong promoter of private tours for multi-day outdoor adventures.";  
  
  var entitySetName = "/competitors";  
  return Sdk.request("POST", entitySetName, competitor);  
 })  
 .then(function (request) {  
  // Process response from previous request.  
  Sdk.SampleVariables.competitor1Uri = request.getResponseHeader("OData-EntityId");  
  Sdk.SampleVariables.entitiesToDelete.push(Sdk.SampleVariables.competitor1Uri);  
  console.log("Competitor 'Adventure Works' created.");  
  
  // Setup for next request.  
  //   
  // Create a new opportunity...  
  var opportunity = {};  
  opportunity.name = "River rafting adventure";  
  opportunity.description = "Sales team on a river-rafting offsite and team building.";  
  var entitySetName = "/opportunities";  
  return Sdk.request("POST", entitySetName, opportunity);  
 })  
 .then(function (request) {  
  // Process response from previous request.  
  Sdk.SampleVariables.opportunity1Uri = request.getResponseHeader("OData-EntityId");  
  Sdk.SampleVariables.entitiesToDelete.push(Sdk.SampleVariables.opportunity1Uri);  
  console.log("Opportunity 'River rafting adventure' created.");  
  
  // Setup for next request.  
  //  
  // Associate competitor to opportunity.  
  var competitor = {};  
  competitor["@odata.id"] = Sdk.SampleVariables.competitor1Uri;  
  return Sdk.request("POST", Sdk.SampleVariables.opportunity1Uri + "/opportunitycompetitors_association/$ref", competitor);  
 })  
 .then(function () {  
  // Process response from previous request.  
  console.log("Opportunity 'River rafting adventure' associated with competitor 'Adventure Works'.");  
  
  // Setup for next request.  
  //  
  // Retrieve competitor entity and expanding on its opportunitycompetitors_association  
  // for all opportunities, using GET request.  
  var opportunityProperties = ["name", "description"].join();  
  var competitorProperties = ["name"].join();  
  var query = "?$select=" + competitorProperties +  
      "&$expand=opportunitycompetitors_association($select=" + opportunityProperties + ")";  
  return Sdk.request("GET", Sdk.SampleVariables.competitor1Uri + query, null);  
 })  
 .then(function (request) {  
  // Process response from previous request.  
  var competitor1 = JSON.parse(request.response);  
  console.log("Competitor '%s' has the following opportunities:", competitor1.name);  
  var successMsg = "\tName: %s, \n"  
                 + "\tDescription: %s";  
  for (var i = 0; i < competitor1.opportunitycompetitors_association.length; i++) {  
   console.log(successMsg,  
       competitor1.opportunitycompetitors_association[i].name,  
       competitor1.opportunitycompetitors_association[i].description  
   );  
  }  
  
  // Setup for next request.  
  //  
  // Disassociate competitor from opportunity.  
  return Sdk.request("DELETE", Sdk.SampleVariables.opportunity1Uri +  
          "/opportunitycompetitors_association/$ref?$id=" + Sdk.SampleVariables.competitor1Uri, null);  
 })  
 .then(function () {  
  // Process response from previous request.  
  console.log("Opportunity 'River rafting adventure' disassociated with competitor 'Adventure Works'");  
  //End this series of operations:  
  resolve();  
 })  
 .catch(function (err) {  
  reject(err);  
 });  
 });  
};  
  
Sdk.deleteSampleData = function () {  
 return new Promise(function (resolve, reject) {  
  
  // House cleaning - deleting sample data  
  // NOTE: If instances have a parent-child relationship, then deleting the parent will,   
  // by default, automatically cascade delete child instances. In this program,   
  // tasks related using the Contact_Tasks relationship have contact as their parent.   
  // Other relationships may behave differently.  
  // See also: https://msdn.microsoft.com/library/gg309412.aspx#BKMK_CascadingBehavior  
  console.log("\n--Section 5 started--");  
  if (Sdk.SampleVariables.deleteData) {  
   for (var i = 0; i < Sdk.SampleVariables.entitiesToDelete.length; i++) {  
    console.log("Deleting entity: " + Sdk.SampleVariables.entitiesToDelete[i]);  
    Sdk.request("DELETE", Sdk.SampleVariables.entitiesToDelete[i], null)  
    .catch(function (err) {  
     reject(new Error("ERROR: Delete failed --Reason: \n\t" + err.message))  
    });  
   }  
   resolve();  
  } else {  
   console.log("Sample data not deleted.");  
   resolve();  
  }  
  
 });  
};  
  
```  
  
### See also

[Use the Dataverse Web API](../overview.md)<br />
[Create a table using the Web API](../create-entity-web-api.md)<br />
[Retrieve a table using the Web API](../retrieve-entity-using-web-api.md)<br />
[Update and delete tables using the Web API](../update-delete-entities-using-web-api.md)<br />
[Web API Samples](../web-api-samples.md)<br />
[Web API Basic Operations Sample](../web-api-basic-operations-sample.md)<br />
[Web API Basic Operations Sample (C#)](cdswebapiservice-basic-operations.md)<br />
[Web API Samples (Client-side JavaScript)](../web-api-samples-client-side-javascript.md)<br />
[Web API Query Data Sample (Client-side JavaScript)](query-data-client-side-javascript.md)<br />
[Web API Conditional Operations Sample (Client-side JavaScript)](conditional-operations-client-side-javascript.md)<br />
[Web API Functions and Actions Sample (Client-side JavaScript)](functions-actions-client-side-javascript.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]