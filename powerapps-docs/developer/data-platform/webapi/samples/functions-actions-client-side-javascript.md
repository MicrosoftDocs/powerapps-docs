---
title: "Web API Functions and Actions Sample (Client-side JavaScript) (Microsoft Dataverse)| Microsoft Docs"
description: "This sample demonstrates how to perform bound and unbound functions and actions, including custom actions, using the Microsoft Dataverse Web API and client-side JavaScript"
ms.custom: ""
ms.date: 10/31/2018
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 337f5d15-66be-46db-a96a-309951a37a2a
caps.latest.revision: 20
author: "JimDaly" # GitHub ID
ms.author: "jdaly"
ms.reviewer: "pehecke"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Web API Functions and Actions Sample (Client-side JavaScript)

[!INCLUDE[cc-data-platform-banner](../../../../includes/cc-data-platform-banner.md)]

This sample demonstrates how to perform bound and unbound functions and actions, including custom actions, using the Microsoft Dataverse Web API using client-side JavaScript.  
  
> [!NOTE]
>  This sample implements the operations detailed in the [Web API Functions and Actions Sample](../web-api-functions-actions-sample.md) and uses the common client-side JavaScript constructs described in [Web API Samples (Client-side JavaScript)](../web-api-samples-client-side-javascript.md)  
  
## In this section  
  
- [Prerequisites](#bkmk_prerequisites)  
- [Run this sample](#bkmk_runsample)  
- [Code sample](#bkmk_codeSample)  
  
<a name="bkmk_prerequisites"></a>
  
## Prerequisites

 To run this sample, the following is required:  
  
- Access to Dataverse online or on-premises version 8.0 or higher.  
- A user account with privileges to import solutions and perform CRUD operations, typically a system administrator or system customizer security role.  
  
<a name="bkmk_runsample"></a>
 
## Run this sample

To run this sample, go to  [Microsoft CRM Web API Functions and Actions Sample (Client-side JavaScript)](/samples/browse/) and download the Microsoft CRM Web API Functions and Actions Sample (Client-side JavaScript).zip sample file. Extract the contents and locate the  WebAPIFunctionsandActions_1_0_0_0_managed.zip managed solution file. Import the managed solution into your Dataverse organization and view the configuration page of the solution to run the sample. For instructions on how to import the sample solution, see [Web API Samples (Client-side JavaScript)](../web-api-samples-client-side-javascript.md).  
  
<a name="bkmk_codeSample"></a>

## Code sample

 This sample includes two web resources:  
  
- [WebAPIFunctionsAndActions.html](#bkmk_WebAPIFunctionsAndActions)  
- [WebAPIFunctionsAndActions.js](#bkmk_WebAPIFunctionsAndActionsJS)  
  
<a name="bkmk_WebAPIFunctionsAndActions"></a>
   
### WebAPIFunctionsAndActions.html

The WebAPIFunctionsAndActions.html web resource provides the context in which the JavaScript code will run.  
  
```html  
<!DOCTYPE html>  
<html>  
<head>  
 <title>Microsoft CRM Web API Functions and Actions Example</title>  
 <meta charset="utf-8" />  
 <meta http-equiv="X-UA-Compatible" content="IE=Edge" />  
 <script src="../ClientGlobalContext.js.aspx" type="text/javascript"></script>  
 <script src="scripts/es6promise.js"></script>  
 <script src="scripts/WebAPIFunctionsAndActions.js"></script>  
  
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
 <h1>Microsoft CRM Web API Functions and Actions Example</h1>  
 <p>This page demonstrates the CRM Web API's Functions and Actions using JavaScript.</p>  
  
 <h2>Instructions</h2>  
 <p>  
  Choose your preferences and run the JavaScript code.  
  Use your browser's developer tools to view the output written to the console (e.g.: in IE11 or Microsoft Edge,   
  press F12 to load the Developer Tools).  
 </p>  
 <form id="preferences">  
  <p>  
   Remove sample data (Choose whether you want to delete sample data created for this sample):<br />  
   <input name="removesampledata" type="radio" value="yes" checked /> Yes  
   <input name="removesampledata" type="radio" value="no" /> No  
  </p>  
  <input type="button" name="start_samples" value="Start Samples" onclick="Sdk.startSample()" />  
 </form>  
  
</body>  
</html>  
  
```  
  
<a name="bkmk_WebAPIFunctionsAndActionsJS"></a>

### WebAPIFunctionsAndActions.js

The WebAPIFunctionsAndActions.js web resource is the JavaScript library that defines the operations this sample performs.  
  
```javascript  
"use strict";  
var Sdk = window.Sdk || {};  
  
/**  
 * @function getClientUrl   
 * @description Get the client URL.  
 * @return {string} The client URL.  
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
  
// Global variables  
var entitiesToDelete = [];              // Entity URIs to be deleted later   
                                        // (if user chooses to delete sample data).  
var deleteData = true;                  // Controls whether sample data are deleted at the end of this sample run.  
var clientUrl = Sdk.getClientUrl();     // ie.: https://org.crm.dynamics.com  
var webAPIPath = "/api/data/v8.1";      // Path to the web API.  
var incidentUri;                        // Incident created with three closed tasks.  
var opportunityUri;                     // Closed opportunity to re-open before deleting.  
var letterUri;                          // Letter to add to contact's queue.  
var myQueueUri;                         // The contact's queue uri.  
var contactUri;                         // Add a note to this contact.  
var CUSTOMERACCOUNTNAME = "Account Customer Created in WebAPIFunctionsAndActions sample"; // For custom action.  
  
/**  
 * @function getWebAPIPath   
 * @description Get the full path to the Web API.  
 * @return {string} The full URL of the Web API.  
 */  
Sdk.getWebAPIPath = function () {  
 return Sdk.getClientUrl() + webAPIPath;  
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
  uri = clientUrl + webAPIPath + uri;  
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
     case 200: // Success with content returned in response body.  
     case 204: // Success with no content returned in response body.  
     case 304: // Success with Not Modified  
      resolve(this);  
      break;  
     default: // All other statuses are error cases.  
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
 * @function Sdk.startSample  
 * @description Initiates a chain of promises to show use of Functions and Actions with the Web API.  
 * Functions and actions represent re-usable operations you can perform using the Web API.  
 * For more info, see https://msdn.microsoft.com/library/mt607990.aspx#bkmk_actions  
 * The following standard CRM Web API functions and actions are invoked:  
 *  - WhoAmI, a basic unbound function  
 *  - GetTimeZoneCodeByLocalizedName, an unbound function that requires parameters  
 *  - CalculateTotalTimeIncident, a bound function  
 *  - WinOpportunity, an unbound action that takes parameters  
 *  - AddToQueue, a bound action that takes parameters  
 *  - In addition, a custom bound and an unbound action contained within the solution are invoked.   
 */  
Sdk.startSample = function () {  
 // Initializing.  
 deleteData = document.getElementsByName("removesampledata")[0].checked;  
 entitiesToDelete = []; // Reset the array.  
  
 console.log("-- Sample started --");  
  
 // Create the CRM entry intances used by this sample program.  
 Sdk.createRequiredRecords()  
 .then(function () {  
  console.log("-- Working with functions --");  
  // Bound and Unbound functions  
  // See https://msdn.microsoft.com/library/gg309638.aspx#bkmk_boundAndUnboundFunctions  
  
  console.log("Using functions to look up your full name.");  
  // Calling a basic unbound function without parameters.  
  // Retrieves the user's full name using a series of function requests.  
  //  - Call WhoAmI via the Sdk.getUsersFullName function.  
  // For more info on the WhoAmI function, see https://msdn.microsoft.com/library/mt607925.aspx  
  return Sdk.getUsersFullName();  
 })  
 .then(function (fullName) {  
  console.log("\tYour full name is: %s\n", fullName);  
  
  console.log("Unbound function: GetTimeZoneCodeByLocalizedName");  
  // Calling a basic unbound function with no parameters.  
  // Retrieves the time zone code for the specified time zone.  
  //  - Pass parameters to an unbound function by calling  the GetTimeZoneCodeByLocalizedName Function.  
  // For more info, see https://msdn.microsoft.com/library/mt607644.aspx  
  var localizedStandardName = 'Pacific Standard Time';  
  var localeId = 1033;  
  // Demonstrates best practice of passing parameters.  
  var uri = ["/GetTimeZoneCodeByLocalizedName",  
   "(LocalizedStandardName=@p1,LocaleId=@p2)",  
   "?@p1='" + localizedStandardName + "'&@p2=" + localeId];  
  
  /* This would also work:  
    var uri = ["/GetTimeZoneCodeByLocalizedName",  
    "(LocalizedStandardName='" + localizedStandardName + "',LocaleId=" + localeId + ")"];  
  */  
  
  return Sdk.request("GET", uri.join("")) // Send request.  
 })  
 .then(function (request) {  
  // Returns GetTimeZoneCodeByLocalizedNameResponse ComplexType.   
  // For more info, see https://msdn.microsoft.com/library/mt607889.aspx  
  var localizedStandardName = 'Pacific Standard Time';  
  var timeZoneCode = JSON.parse(request.response).TimeZoneCode;  
  console.log("\tFunction returned time zone %s, with code '%s'.", localizedStandardName, timeZoneCode);  
  
  console.log("Bound function: CalculateTotalTimeIncident");  
  // Calling a basic bound function that requires parameters.  
  // Retrieve the total time, in minutes, spent on all tasks associated with this incident.  
  //  - Use CalculateTotalTimeIncident to get the total duration of all closed activities.  
  // For more info, see https://msdn.microsoft.com/library/mt593054.aspx  
  // Note that in a bound function the full function name includes the    
  // namespace Microsoft.Dynamics.CRM. Functions that aren’t bound must not use the full name.  
  return Sdk.request("GET", incidentUri + "/Microsoft.Dynamics.CRM.CalculateTotalTimeIncident()")  
 })  
 .then(function (request) {  
  // Returns CalculateTotalTimeIncidentResponse ComplexType.  
  // For more info, see https://msdn.microsoft.com/library/mt607924.aspx  
  var totalTime = JSON.parse(request.response).TotalTime; //returns 90  
  console.log("\tFunction returned %s minutes - total duration of tasks associated with the incident.\n",  
   totalTime);  
  
  console.log("-- Working with Actions --");  
  // For more info about Action, see https://msdn.microsoft.com/library/mt607600.aspx  
  
  console.log("Unbound Action: WinOpportunity");  
  // Calling an unbound action that requires parameters.  
  // Closes an opportunity and markt it as won.  
  //  - Update the WinOpportunity (created by Sdk.createRequiredRecords()) by closing it as won.  
  // Use WinOpportunity Action (https://msdn.microsoft.com/library/mt607971.aspx)  
  // This action does not return a value  
  var parameters = {  
   "Status": 3,  
   "OpportunityClose": {  
    "subject": "Won Opportunity",  
    "opportunityid@odata.bind": opportunityUri  
   }  
  }  
  
  return Sdk.request("POST", "/WinOpportunity", parameters)  
 })  
 .then(function () {  
  console.log("\tOpportunity won.");  
  
  console.log("Bound Action: AddToQueue");  
  // Calling a bound action that requires parameters.  
  // Adds a new letter tracking activity to the current user's queue.  
  // The letter was created as part of the Sdk.createRequiredRecords().  
  //  - Get a reference to the current user.  
  //  - Get a reference to the letter activity.  
  //  - Add letter to current user's queue via the bound action AddToQueue.  
  // For more info on AddToQueue, see https://msdn.microsoft.com/library/mt607880.aspx  
  
  return Sdk.request("GET", "/WhoAmI");  
 })  
 .then(function (request) {  
  var whoAmIResponse = JSON.parse(request.response);  
  var myId = whoAmIResponse.UserId;  
  
  // Get a reference to the current user.  
  return Sdk.request("GET", Sdk.getWebAPIPath() + "/systemusers(" + myId + ")/queueid/$ref")  
 })  
 .then(function (request) {  
  myQueueUri = JSON.parse(request.response)["@odata.id"];  
  
  // Get a reference to the letter activity.  
  return Sdk.request("GET", letterUri + "?$select=activityid")  
 })  
 .then(function (request) {  
  
  var letterActivityId = JSON.parse(request.response).activityid  
  
  var parameters = {  
   Target: {  
    activityid: letterActivityId,  
    "@odata.type": "Microsoft.Dynamics.CRM.letter"  
   }  
  }  
  //Adding the letter to the user's default queue.  
  return Sdk.request("POST", myQueueUri + "/Microsoft.Dynamics.CRM.AddToQueue", parameters);  
 })  
 .then(function (request) {  
  var queueItemId = JSON.parse(request.response).QueueItemId;  
  console.log("\tQueueItemId returned from AddToQueue Action: %s\n", queueItemId);  
  
  console.log("-- Working with custom actions --");  
  console.log("Custom action: sample_AddNoteToContact");  
  // Add a note to an existing contact.  
  // This operation calls a custom action named sample_AddNoteToContact.   
  // This custom action is installed when you install this sample's solution to your CRM server.  
  //  - Add a note to an existing contact (e.g.: contactUri)  
  //  - Get the note info and the contact's full name.  
  // For more info, see https://msdn.microsoft.com/library/mt607600.aspx#bkmk_customActions  
  //sample_AddNoteToContact custom action parameters  
  var parameters = {  
   NoteTitle: "The Title of the Note",  
   NoteText: "The text content of the note."  
  }  
  return Sdk.request("POST", contactUri + "/Microsoft.Dynamics.CRM.sample_AddNoteToContact", parameters)  
 })  
 .then(function (request) {  
  var annotationid = JSON.parse(request.response).annotationid;  
  var annotationUri = Sdk.getWebAPIPath() + "/annotations(" + annotationid + ")";  
  // The annotation will be deleted with the contact when it is deleted.  
  
  return Sdk.request("GET", annotationUri + "?$select=subject,notetext&$expand=objectid_contact($select=fullname)")  
 })  
 .then(function (request) {  
  var annotation = JSON.parse(request.response);  
  console.log("\tA note with the title '%s' and the content '%s' was created and associated with the contact %s.\n",  
   annotation.subject, annotation.notetext, annotation.objectid_contact.fullname);  
  
  console.log("Custom action: sample_CreateCustomer");  
  // Create a customer of a specified type using the custom action sample_CreateCustomer.  
  //  - Shows how create a valid customer of type "account".  
  //  - Shows how to handle exception from a custom action.  
  
  var parameters = {  
   CustomerType: "account",  
   AccountName: CUSTOMERACCOUNTNAME  
  }  
  
  // Create the account. This is a valid request  
  return Sdk.request("POST", "/sample_CreateCustomer", parameters)  
 })  
 .then(function (request) {  
  // Retrieve the account we just created  
  return Sdk.request("GET", "/accounts?$select=name&$filter=name eq '" + CUSTOMERACCOUNTNAME + "'");  
 })  
 .then(function (request) {  
  var customerAccount = JSON.parse(request.response).value[0];  
  var customerAccountId = customerAccount.accountid;  
  var customerAccountIdUri = Sdk.getWebAPIPath() + "/accounts(" + customerAccountId + ")";  
  entitiesToDelete.push(customerAccountIdUri);  
  console.log("\tAccount customer created with the name '%s'", customerAccount.name);  
  
  // Create a contact but uses invalid parameters  
  //  - Throws an error intentionally  
  return new Promise(function (resolve, reject) {  
   var parameters = {  
    CustomerType: "contact",  
    AccountName: CUSTOMERACCOUNTNAME //not valid for contact  
    // e.g.: ContactFirstName and ContactLastName are required when CustomerType is "contact".  
   }  
   Sdk.request("POST", "/sample_CreateCustomer", parameters) // This request is expected to fail.  
   .then(function () {  
    console.log("Not expected.")  
    reject(new Error("Call to sample_CreateCustomer not expected to succeed."))  
   })  
   .catch(function (err) {  
    //Expected error  
    console.log("\tExpected custom error: " + err.message); // Custom action can return custom error messages.  
    resolve(); // Show the error but resolve the thread so sample can continue.  
   });  
  });  
 })  
 .then(function () {  
  // House cleaning.  
  console.log("\n-- Deleting sample data --");  
  if (deleteData) {  
   return Sdk.deleteEntities();  
  }  
  else {  
   console.log("Sample data not deleted.");  
  }  
 })  
 .catch(function (err) {  
  console.log("ERROR: " + err.message);  
 });  
}  
  
/**  
 * @function Sdk.deleteEntities  
 * @description Deletes the entities created by this sample  
 */  
Sdk.deleteEntities = function () {  
 return new Promise(function (resolve, reject) {  
  
  entitiesToDelete.unshift(opportunityUri) // Adding to the beginning so it will get deleted before the parent account.  
  // Re-open the created opportunity so it can be deleted.  
  Sdk.request("PATCH", opportunityUri, { statecode: 0, statuscode: 2 })  
  .then(function () {  
   // Get the opportunityclose URI so it can be deleted  
   return Sdk.request("GET", opportunityUri + "/Opportunity_OpportunityClose/$ref")  
  })  
  .then(function (request) {  
   var opportunityCloseUri = JSON.parse(request.response).value[0]["@odata.id"];  
  
   // Adding to the opportunityclose URI it will get deleted before the opportunity.  
   entitiesToDelete.unshift(opportunityCloseUri)  
  
   /*  
  These deletions have to be done consecutively in a specific order to avoid a Generic SQL error  
  which can occur because of relationship behavior actions for the delete event.  
  */  
  
   return Sdk.request("DELETE", entitiesToDelete[0]) //opportunityclose  
  })  
  .then(function () {  
   console.log(entitiesToDelete[0] + " Deleted");  
   return Sdk.request("DELETE", entitiesToDelete[1]) //opportunity  
  })  
  .then(function () {  
   console.log(entitiesToDelete[1] + " Deleted");  
   return Sdk.request("DELETE", entitiesToDelete[2])//account  
  })  
  .then(function () {  
   console.log(entitiesToDelete[2] + " Deleted");  
   return Sdk.request("DELETE", entitiesToDelete[3]) //Fourth Coffee account  
  })  
  .then(function () {  
   console.log(entitiesToDelete[3] + " Deleted");  
   return Sdk.request("DELETE", entitiesToDelete[4]) //Letter  
  })  
  .then(function () {  
   console.log(entitiesToDelete[4] + " Deleted");  
   return Sdk.request("DELETE", entitiesToDelete[5]) //Contact  
  })  
  .then(function () {  
   console.log(entitiesToDelete[5] + " Deleted");  
   return Sdk.request("DELETE", entitiesToDelete[6]) //AccountCustomer  
  })  
  .then(function () {  
   console.log(entitiesToDelete[6] + " Deleted");  
   resolve();  
  })  
  .catch(function (err) {  
   reject(new Error("Error from Sdk.deleteEntities: " + err.message));  
  });  
 });  
};  
  
/**  
 * @function Sdk.getUsersFullName  
 * @description Retrieves the current user's full name.  
 * @returns {Promise} - A Promise that returns the full name of the user  
 */  
Sdk.getUsersFullName = function () {  
 return new Promise(function (resolve, reject) {  
  //Use WhoAmI Function (https://msdn.microsoft.com/library/mt607925.aspx)  
  Sdk.request("GET", "/WhoAmI")  
  .then(function (request) {  
   //Returns WhoAmIResponse ComplexType (https://msdn.microsoft.com/library/mt607982.aspx)  
   var myId = JSON.parse(request.response).UserId;  
   //Retrieve the systemuser Entity fullname property (https://msdn.microsoft.com/library/mt608065.aspx)  
   return Sdk.request("GET", "/systemusers(" + myId + ")?$select=fullname")  
  })  
  .then(function (request) {  
   //Return the users full name  
   resolve(JSON.parse(request.response).fullname);  
  })  
  .catch(function (err) {  
   reject("Error in Sdk.getUsersFullName function: " + err.message);  
  });  
 });  
};  
  
/**  
 * @function Sdk.createRequiredRecords  
 * @description Creates data required by this sample program.  
 *  - Create an account with three 30 minute tasks.  
 *  - Create another account associated with an opportunity.  
 *  - Create a letter.  
 *  - Create a contact.  
 * @returns {Promise} - resolve the promise if all goes well; reject otherwise.  
 */  
Sdk.createRequiredRecords = function () {  
 console.log("-- Creating sample data --");  
 // Create a parent account, an associated incident with three   
 // associated tasks(required for CalculateTotalTimeIncident).  
 return new Promise(function (resolve, reject) {  
  Sdk.createAccountWithIncidentAndThree30MinuteClosedTasks()  
  .then(function (iUri) {  
   incidentUri = iUri;  
  
   //Create another account and associated opportunity (required for CloseOpportunityAsWon).  
   return Sdk.createAccountWithOpportunityToWin();  
  })  
  .then(function (oUri) {  
   opportunityUri = oUri;  
  
   // Create a letter to use with AddToQueue action.  
   var letter = {  
    description: "Example letter"  
   }  
   return Sdk.request("POST", "/letters", letter)  
  })  
  .then(function (request) {  
   letterUri = request.getResponseHeader("OData-EntityId");  
   entitiesToDelete.push(letterUri);  
  
   // Create a contact to use with custom action sample_AddNoteToContact   
   var contact = {  
    firstname: "Jon",  
    lastname: "Fogg"  
   }  
   return Sdk.request("POST", "/contacts", contact)  
  })  
  .then(function (request) {  
   contactUri = request.getResponseHeader("OData-EntityId");  
   entitiesToDelete.push(contactUri);  
  
   resolve()  
  })  
  .catch(function (err) {  
   reject("Error in Sdk.createRequiredRecords function: " + err.message);  
  });  
 });  
}  
  
/**  
 * @function Sdk.createAccountwithIncidentAndThree30MinuteClosedTasks  
 * @description Create an account and associate three 30 minute tasks. Close the tasks.  
 * @returns {Promise} - A Promise that returns the uri of an incident created.  
 */  
Sdk.createAccountWithIncidentAndThree30MinuteClosedTasks = function () {  
 return new Promise(function (resolve, reject) {  
  var iUri; // incidentUri  
  // Create a parent account for the incident.  
  Sdk.request("POST", "/accounts", { name: "Fourth Coffee" })  
  .then(function (request) {  
   // Capture the URI of the created account so it can be deleted later.  
   var accountUri = request.getResponseHeader("OData-EntityId");  
   entitiesToDelete.push(accountUri);  
   // Define an incident associated with the account with three related tasks.  
   // Each task has a 30 minute duration.  
   var incident = {  
    title: "Sample Case",  
    "customerid_account@odata.bind": accountUri,  
    Incident_Tasks: [  
     {  
      subject: "Task 1",  
      actualdurationminutes: 30  
     },  
     {  
      subject: "Task 2",  
      actualdurationminutes: 30  
     },  
     {  
      subject: "Task 3",  
      actualdurationminutes: 30  
     }  
    ]  
   };  
   // Create the incident and related tasks.  
   return Sdk.request("POST", "/incidents", incident)  
  })  
  .then(function (request) {  
   iUri = request.getResponseHeader("OData-EntityId");  
  
   // Retrieve references to the tasks created.  
   return Sdk.request("GET", iUri + "/Incident_Tasks/$ref")  
  })  
  .then(function (request) {  
   // Capture the URL for the three tasks in this array.  
   var taskReferences = [];  
   JSON.parse(request.response).value.forEach(function (tr) {  
    taskReferences.push(tr["@odata.id"]);  
   });  
   // An array to hold a set of promises.  
   var promises = [];  
   // The data to use to update the tasks so that they are closed.  
   var update = {  
    statecode: 1, //Completed  
    statuscode: 5 //Completed  
   }  
   // Fill the array with promises  
   taskReferences.forEach(function (tr) {  
    promises.push(Sdk.request("PATCH", tr, update))  
   })  
   // When all the promises resolve, return a promise.  
   return Promise.all(promises);  
  })  
  .then(function () {  
   // Return the incident URI to the calling code.  
   resolve(iUri);  
  })  
  .catch(function (err) {  
   // Differentiate the message for any error returned by this function.  
   reject(new Error("ERROR in Sdk.createAccountwithIncidentAndThree30MinuteClosedTasks function: " + err.message))  
  });  
 });  
}  
  
/**  
 * @function Sdk.createAccountwithOpportunityToWin  
 * @description Create an account and an associated opportunity.  
 * @returns {Promise} - A Promise that returns the uri of an opportunity.  
 */  
Sdk.createAccountWithOpportunityToWin = function () {  
 return new Promise(function (resolve, reject) {  
  var accountUri;  
  var account = {  
   name: "Sample Account for WebAPIFunctionsAndActions sample",  
   opportunity_customer_accounts: [{  
    name: "Opportunity to win"  
   }]  
  };  
  Sdk.request("POST", "/accounts", account) // Create the account.  
  .then(function (request) {  
   accountUri = request.getResponseHeader("OData-EntityId");  
   entitiesToDelete.push(accountUri);  
  
   // Retrieve the opportunity's reference.  
   return Sdk.request("GET", accountUri + "/opportunity_customer_accounts/$ref")  
  })  
  .then(function (request) {  
   var oUri = JSON.parse(request.response).value[0]["@odata.id"];  
   resolve(oUri); // Return the opportunity's uri.  
  })  
  .catch(function (err) {  
   reject(new Error("Error in Sdk.createAccountwithOpportunityToWin: " + err.message));  
  });  
 });  
};  
```  
  
### See also

[Use the Dataverse Web API](../overview.md)<br />
[Use Web API functions](../use-web-api-functions.md)<br />
[Use Web API actions](../use-web-api-actions.md)<br />
[Web API Samples](../web-api-samples.md)<br />
[Web API Functions and Actions Sample](../web-api-functions-actions-sample.md)<br />
[Web API Functions and Actions Sample (C#)](functions-actions-csharp.md)<br />
[Web API Samples (Client-side JavaScript)](../web-api-samples-client-side-javascript.md)<br />
[Web API Basic Operations Sample (Client-side JavaScript)](basic-operations-client-side-javascript.md)<br />
[Web API Query Data Sample (Client-side JavaScript)](query-data-client-side-javascript.md)<br />
[Web API Conditional Operations Sample (Client-side JavaScript)](conditional-operations-client-side-javascript.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]