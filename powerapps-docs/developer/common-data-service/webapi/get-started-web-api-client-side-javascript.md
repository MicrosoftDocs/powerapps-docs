---
title: "Get started with the Common Data Service for Apps Web API (client-side JavaScript) | MicrosoftDocs"
description: "JavaScript can be used in HTML web resources, form scripts or ribbon commands to perform operations on Common Data Service for Appsdata using Web API"
ms.custom: ""
ms.date: 06/15/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "get-started-article"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: get-started-dynamics-365-web-api-client-side-JavaScript
caps.latest.revision: 51
author: "JimDaly"
ms.author: "jdaly"
manager: "amyla"
---
# Get started with the Common Data Service for Apps Web API (client-side JavaScript)

<!-- TODO: 
> [!NOTE]
> ![This page is under construction. Check back soon!](../../media/under_construction.png "Coming soon") [!INCLUDE[cc-under-construction](../../includes/cc-under-construction.md)] -->

In HTML web resources, form scripts, or ribbon commands you can use JavaScript to perform operations on Common Data Service for Apps data using the Web API introduced with CDS for Apps.

<!-- TODO:
If you are using the [!INCLUDE[pn_crm_9_0_0_online](../../includes/pn-crm-9-0-0-online.md)], use the new [Xrm.WebApi](../clientapi/reference/xrm-webapi.md) client API methods to use Web API with JavaScript and web resources.  -->

If you are using an earlier version of Common Data Service for Apps Customer Engagement, follow instruction available at [Get started with the Microsoft Common Data Service for Apps Web API (client-side JavaScript)](https://msdn.microsoft.com/library/gg334279.aspx)  
  
<!--

The Web API is especially easy to use with JavaScript and web resources because the JSON data that is sent and received with it is easily converted into JavaScript objects. Even so, most developers will want to create or use a helper JavaScript library to benefit from code re-use and keep their business logic code separate from their code to access data. This topic describes how to use the `XMLHttpRequest` object to perform operations with JavaScript as well as opportunities to create re-usable JavaScript libraries that provide functions to work with the Web API.  
  
<a name="bkmk_clientsideJS"></a>   
## Where you can use Client-side JavaScript  
 There are two areas where you can use client-side JavaScript to access Common Data Service for Apps using the Web API:  
  
 JavaScript web resources  
 JavaScript code included in a JavaScript web resource running in the context of an HTML web resource, form scripts or ribbon commands.  
  
 When you use JavaScript web resources in Common Data Service for Apps you do not need to authenticate because the web resources are part of the application the user is already authenticated. The rest of this topic will focus on this scenario. More information:[Web resources for CDS for Apps](../web-resources.md),[Script (JScript) web resources](../script-jscript-web-resources.md), [Use JavaScript with CDS for Apps](../use-javascript.md), & [Client scripting in Customer Engagement using JavaScript](../clientapi/client-scripting.md).  
  
 Single Page Applications  
 JavaScript code in a JavaScript library from another application running in a browser and authenticating to Common Data Service for Apps using Cross-Origin Resource Sharing (CORS). This pattern is typically used for single page applications.  
  
 When you use JavaScript in a single page application (SPA) you can use the adal.js library to allow the user to authenticate and access Common Data Service for Apps data in a page hosted on a different domain. Most of the information in this topic applies to this scenario but you must also integrate an authorization header into any request which contains a authentication token. For more information see [Use OAuth with Cross-Origin Resource Sharing  to connect a Single Page Application](../oauth-cross-origin-resource-sharing-connect-single-page-application.md)  
  
<a name="bkmk_understandingXHR"></a>   
## Understanding XMLHttpRequest  
 When you use the Web API  will use an [XMLHttpRequest](http://www.w3.org/TR/XMLHttpRequest/) object. `XMLHttpRequest (XHR)` is a native object found in all modern browsers, and it enables AJAX techniques to make webpages dynamic. Although the name of the object contains “XML,” all requests using the Web API will use JSON rather than XML.  
  
<a name="bkmk_XHRUsedByJavaScriptFrameworks"></a>   
### XMLHttpRequest used by JavaScript frameworks  
 JavaScript frameworks such as jQuery often wrap the underlying `XMLHttpRequest` object in a function (such as `$.ajax`) because previously not all browsers provided a native `XMLHttpRequest` in a standard way and also to simplify use. Now that modern browsers have a standard `XMLHttpRequest` implementation, you don’t need a separate library to mitigate these differences. Yet many developers continue to depend on JavaScript frameworks to request server resources. While it is fine to use jQuery and other JavaScript frameworks in HTML web resources or SPAs, we recommend avoiding them in form scripts or ribbon commands. With various solutions that may be installed for an organization, each potentially including different versions of a JavaScript framework, particularly jQuery, it can lead to unexpected results unless everyone performs steps to avoid conflicts. If you will perform Web API requests in form scripts or ribbon commands, we recommend that you use the `XMLHttpRequest` directly and not take a dependency on jQuery. More information:[Use of jQuery](../use-javascript.md#BKMK_UsingjQuery)  
  
 This topic describes how to use native `XMLHttpRequest` directly, but the same concepts will apply when using jQuery or other JavaScript frameworks that run in a browser since they all use `XMLHttpRequest`. You can use a library that uses XHR directly in a browser with any JavaScript framework.  
  
<a name="bkmk_usingXHR"></a>   
## Using XMLHttpRequest  
 The following is a very simple example showing how to create an account entity using the Web API and the `XMLHttpRequest` object. In this example, only the `clientURL` variable is not defined.  
  
```javascript  
var req = new XMLHttpRequest()  
req.open("POST",encodeURI(clientURL + "/api/data/v8.1/accounts"), true);  
req.setRequestHeader("Accept", "application/json");  
req.setRequestHeader("Content-Type", "application/json; charset=utf-8");  
req.setRequestHeader("OData-MaxVersion", "4.0");  
req.setRequestHeader("OData-Version", "4.0");  
req.onreadystatechange = function () {  
 if (this.readyState == 4 /* complete */) {  
  req.onreadystatechange = null;  
  if (this.status == 204) {  
   var accountUri = this.getResponseHeader("OData-EntityId");  
   console.log("Created account with URI: "+ accountUri)  
  }  
  else {  
   var error = JSON.parse(this.response).error;  
   console.log(error.message);  
  }  
 }  
};  
req.send(JSON.stringify({ name: "Sample account" }));  
```  
  
 The following sections describe what this code does.  
  
<a name="bkmk_openXHR"></a>   
### Open the XMLHttpRequest  
 After you initialize the `XMLHttpRequest` object, you have to open it before you can set properties or send it. The `open` method parameters are an HTTP request method, a URL, and a `boolean` parameter to indicate whether the operation should be performed asynchronously. You should always choose to perform operations asynchronously. More information:[Use asynchronous data access methods](../use-javascript.md#bkmk_useasynchronous)  
  
 In this example, because we’re creating an account entity, we need to set the URL to match the entity set path for the <xref href="Microsoft.Dynamics.CRM.account?text=account EntityType" />. The full URL in this example is `clientURL + "/api/data/v8.1/accounts` and the `clientURL` variable must be set to root URL of the Common Data Service for Apps application.  For web resources that have access to the context object, the [getClientUrl](../clientapi/reference/Xrm-Utility/getGlobalContext/getClientUrl.md) method that can be accessed through the client-side context object available using the [getGlobalContext method](../clientapi/reference/Xrm-Utility/getGlobalContext.md). You should use the [encodeURI](https://msdn.microsoft.com/library/xh9be5xc.aspx) function on any URL you send to the service to ensure it doesn’t include unsafe characters.  
  
 Because this function creates an entity, the HTTP request method is POST as described in [Create an entity using the Web API](create-entity-web-api.md).  
  
 The `XMLHttpRequest``open` method also provides for specifying a user name and password. You don’t need to specify a value for these parameters with web resources because the user is already authenticated. For SPAs, the authentication is managed through a token rather than these parameters.  
  
<a name="bkmk_setXHRHeaders"></a>   
### Set the headers and event handler  
 After you open the `XMLHttpRequest` you can apply a number of request headers using the `setRequestHeader` method. You should generally use the headers shown here with some variations for special kinds of operations. More information:[Http headers](compose-http-requests-handle-errors.md#bkmk_headers).  
  
 Before you send the request, you need to include an event handler that detects when the operation is complete. After you send the request, it progresses through several states before the response is returned. To capture the moment that the `XMLHttpRequest` completes, you must set an event handler to the `onreadystatechange` property to detect when the `readystate` property equals 4, which indicates complete. At that time you can examine the `status` property.  
  
> [!NOTE]
>  After the `XMLHttpRequest` is complete, it is a best practice to set the `onreadystatechange` property to `null` to avoid potential memory leak issues.  
  
 Within the anonymous function that is your event handler, after you have verified completion, you can examine the `status` property to determine whether the operation was successful. In this case, the expected status value is 204 No Content because nothing is expected in the body of the response from a create operation. The URI for the account created is in the `OData-EntityId` header and can be accessed using the `getResponseHeader` method.  
  
 If this was a different operation that was expected to return data in the response, it would have a 200 OK`status` value and the function would use `JSON.parse` on the `XMLHttpRequest` response to convert the JSON response into a JavaScript object that your code could access. More information:[Parsing JSON returned](get-started-web-api-client-side-javascript.md#bkmk_parsingJSON)  
  
 If the status isn’t the expected value, it’s an error and an error object is returned with the properties described in [Parse errors from the response](compose-http-requests-handle-errors.md#bkmk_parseErrors). This example uses `JSON.parse` to convert the `XMLHttpRequest``response` property into a JavaScript object so that the `message` property can be accessed.  
  
<a name="bkmk_sendXHR"></a>   
### Send the XMLHttpRequest  
 Finally, use the `XMLHttpRequest``send` method to send the request, including any JSON data required. Use `JSON.stringify` to convert JavaScript objects to JSON strings that can be included in the body of the request when you send it.  
  
<a name="bkmk_composingJSON"></a>   
## Composing JSON data to send  
 In the preceding example, the account entity is created using just a single property set. To determine which properties are available for an entity you need to look at the [CSDL metadata document](web-api-types-operations.md#bkmk_csdl), documentation generated from that document, or code generated using that document. For system  business entities included in all Common Data Service for Apps organizations you can refer to the <xref:Microsoft.Dynamics.CRM.EntityTypeIndex>. Property names are lower case and accept simple data types that correspond to the following JavaScript types: `Boolean`, `Number`, `String`, `Array`, `Object`, and `Date`.  
  
> [!NOTE]
>  The only exception to using simple data types is the <xref href="Microsoft.Dynamics.CRM.BooleanManagedProperty?text=BooleanManagedProperty ComplexType" /> which is used for entities which store solution-aware data such as web resources, templates, reports, roles, savedqueries, and in metadata entities. This property is never used for entities that store business data. Metadata entities use  many complex types and follow different rules. For more information see [Use the Web API with Common Data Service for Apps metadata](use-web-api-metadata.md).  
  
 Composing data to send in a request is usually a simple matter of creating an ordinary JavaScript object and setting appropriate properties. The following code shows two valid methods for defining a JavaScript object with properties and values. This example uses selected properties from the contact entity defined in <xref href="Microsoft.Dynamics.CRM.contact?text=contact EntityType" />.  
  
```javascript  
var contact = new Object();  
contact.firstname = "John";  
contact.lastname = "Smith";  
contact.accountrolecode = 2; //Employee  
contact.creditonhold = false; //Number value works here too. 0 is false and 1 is true  
contact.birthdate = new Date(1980, 11, 2);  
contact["parentcustomerid_account@odata.bind"] = "/accounts(f3a11f36-cd9b-47c1-8c44-e65b961257ed)"  
  
var contact = {  
 firstname: "John",  
 lastname: "Smith",  
 accountrolecode: 2,//Employee  
 creditonhold: false,  
 birthdate: new Date(1980, 11, 2),  
 "parentcustomerid_account@odata.bind": "/accounts(f3a11f36-cd9b-47c1-8c44-e65b961257ed)"  
};  
```  
  
 Regardless of how these objects are defined, after you use `JSON.stringify` they will both be converted into the same JSON string.  
  
```json  
{  
 "firstname": "John",  
 "lastname": "Smith",  
 "accountrolecode": 2,  
 "creditonhold": false,  
 "birthdate": "1980-12-02T08:00:00.000Z",  
 "parentcustomerid_account@odata.bind": "/accounts(f3a11f36-cd9b-47c1-8c44-e65b961257ed)"  
}  
```  
  
 There are times when you must define a property that doesn’t follow ordinary property naming guidelines for JavaScript. For example, when you set the value of a single-valued navigation property when creating an entity you need to append `@odata.bind` to the name of the property and set the value to a URL corresponding to the related entity. In this case, you must define the property in an bracket notation style as shown in the preceding example.  
  
 Except when working with metadata entities, you won’t set entity properties to an object. With metadata entities you frequently need to set properties that are complex type or enumeration values. But this is not common with ordinary business entities.  
  
 When you create related entities you may set the value of a collection-valued navigation property using an `Array`, but this is a rather specialized operation. More information:[Create related entities in one operation](create-entity-web-api.md#bkmk_CreateRelated)  
  
### Entity type properties  
 When you post an entity to an action where the parameter type represents a base type for the entity, such as <xref href="Microsoft.Dynamics.CRM.crmbaseentity?text=crmbaseentity EntityType" /> or <xref href="Microsoft.Dynamics.CRM.activitypointer?text=activitypointer EntityType" />, you may need to include the `@odata.type` property with the full name of the entity type as the value. For example, since <xref href="Microsoft.Dynamics.CRM.letter?text=letter EntityType" /> inherits from activitypointer, you may need to explicitly state the type of entity using the following property and value:`"@odata.type": "Microsoft.Dynamics.CRM.letter"`.  
  
<a name="bkmk_sendingUpdateData"></a>   
### Sending data for update operations  
 When you update entities, it’s important to only set property values for those properties you intend to update. You should not retrieve an entity, update properties of the retrieved instance and then use that instance in an update operation. Instead, you should create a new object and set new properties only for those properties you intend to update.  
  
 If you simply copy over all the properties of a retrieved entity and update it using PATCH, each of the properties you send will be considered an update, even if the value is the same as the current value. If you have auditing enabled for the entity and the attribute it will indicate that the data is changed when there was no actual change in the value. More information:[Basic update](update-delete-entities-using-web-api.md#bkmk_update)  
  
<a name="bkmk_parsingJSON"></a>   
## Parsing JSON returned  
 Although the create operation used in the preceding example doesn’t return JSON data, most operations using GET will return JSON. For most types of data returned, converting the JSON into JavaScript can be achieved using the following line of code.  
  
```javascript  
var data = JSON.parse(this.response)  
```  
  
 However, data that includes dates are a problem because dates are passed as a string, for example `2015-10-25T17:23:55Z`. To convert this into a JavaScript`Date` object you must use the `reviver` parameter for the [JSON.parse](https://msdn.microsoft.com/library/cc836466.aspx) function. The following is an example of a function that can be used to parse dates.  
  
```javascript  
function dateReviver(key, value) {  
  var a;  
  if (typeof value === 'string') {  
   a = /^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2}(?:\.\d*)?)Z$/.exec(value);  
   if (a) {  
    return new Date(Date.UTC(+a[1], +a[2] - 1, +a[3], +a[4], +a[5], +a[6]));  
   }  
  }  
  return value;  
 };  
```  
  
 To apply this function just include it as a parameter, as shown here.  
  
```javascript  
var data = JSON.parse(this.response,dateReviver)  
```  
  
<a name="bkmk_createCallbackFunction"></a>   
## Create a re-usable function using callbacks  
 When you have the code to perform a specific operation you’ll want to re-use it rather than write the same code again and again. The next step is to create a JavaScript library that contains a function to perform the operation with any available options. In this case there are only two variables for the create operation: the entity set name and the JSON definition of the entity to create. Rather than writing all the code shown previously, the same operation can be contained in a function that just takes a few lines of code to use.  
  
 Asynchronous operations with JavaScript have traditionally employed callback functions as a way to capture any return values from the asynchronous operation and continue the logic in your program. Using the code for the create operation described previously, the goal here is to allow for the same operation to be performed using just the following code.  
  
```javascript  
MyNameSpace.WebAPI.create("accounts",  
{ name: "Sample account" },  
function (accountUri) { console.log("Created account with URI: " + accountUri) },  
function (error) { console.log(error.message); });  
```  
  
 In this example, `MyNameSpace.WebAPI` represents the best practice of providing a unique name for any functions you use. More information:[Define unique names for your JavaScript functions](../use-javascript.md#bkmk_DefineUniqueNames)  
  
 For this library we plan to include functions for additional operations so there is an opportunity to have re-usable private functions to support operations. The following code shows a library which demonstrates this and includes a `MyNameSpace.WebAPI.create` function using callbacks.  
  
```javascript  
"use strict";  
var MyNameSpace = window.MyNameSpace || {};  
MyNameSpace.WebAPI = MyNameSpace.WebAPI || {};  
(function () {  
 this.create = function (entitySetName, entity, successCallback, errorCallback) {  
  var req = new XMLHttpRequest();  
  req.open("POST", encodeURI(getWebAPIPath() + entitySetName), true);  
  req.setRequestHeader("Accept", "application/json");  
  req.setRequestHeader("Content-Type", "application/json; charset=utf-8");  
  req.setRequestHeader("OData-MaxVersion", "4.0");  
  req.setRequestHeader("OData-Version", "4.0");  
  req.onreadystatechange = function () {  
   if (this.readyState == 4 /* complete */) {  
    req.onreadystatechange = null;  
    if (this.status == 204) {  
     if (successCallback)  
      successCallback(this.getResponseHeader("OData-EntityId"));  
    }  
    else {  
     if (errorCallback)  
      errorCallback(MyNameSpace.WebAPI.errorHandler(this.response));  
    }  
   }  
  };  
  req.send(JSON.stringify(entity));  
 };  
  
 //Internal supporting functions  
 function getClientUrl() {  
  //Get the organization URL  
  if (typeof GetGlobalContext == "function" &&  
      typeof GetGlobalContext().getClientUrl == "function") {  
   return GetGlobalContext().getClientUrl();  
  }  
  else {  
   //If GetGlobalContext is not defined check for Xrm.Page.context;  
   if (typeof Xrm != "undefined" &&  
       typeof Xrm.Page != "undefined" &&  
       typeof Xrm.Page.context != "undefined" &&  
       typeof Xrm.Page.context.getClientUrl == "function") {  
    try {  
     return Xrm.Page.context.getClientUrl();  
    } catch (e) {  
     throw new Error("Xrm.Page.context.getClientUrl is not available.");  
    }  
   }  
   else { throw new Error("Context is not available."); }  
  }  
 }  
 function getWebAPIPath() {  
  return getClientUrl() + "/api/data/v8.1/";  
 }  
  
 // This function is called when an error callback parses the JSON response  
 // It is a public function because the error callback occurs within the onreadystatechange   
 // event handler and an internal function would not be in scope.  
 this.errorHandler = function (resp) {  
  try {  
   return JSON.parse(resp).error;  
  } catch (e) {  
   return new Error("Unexpected Error")  
  }  
 }  
  
}).call(MyNameSpace.WebAPI);  
```  
  
 This library demonstrates the best practice of defining a function within a self-executing anonymous function (also known as a self-invoked anonymous function or immediately-invoked anonymous function) and attaching the function to the `MyNameSpace.WebAPI` namespace. This allows you to define internal functions that are not accessible by other code. Any function that is defined as a part of `this` will be public and any functions within the anonymous function can be used by public functions but not code external to the anonymous function. The code within the function cannot be modified by other code in the page.  
  
 The namespace is defined so that it will not overwrite any other code that uses the same namespace but it will overwrite any functions with the same name that are part of that namespace. You can create separate libraries which add additional public functions to the namespace as long as they do not have the same name.  
  
 The `MyNameSpace.WebAPI.create` function provides the following parameters:  
  
|Name|Description|  
|----------|-----------------|  
|`entitySetName`|The name of the entity set for the type of entity you want to create.|  
|`entity`|An object with the properties for the entity you want to create.|  
|`successCallback`|The function to call when the entity is created. The Uri of the created entity is passed to this function.|  
|`errorCallback`|The function to call when there is an error. The error will be passed to this function.|  
  
 The code that configures the `XMLHttpRequest` object has been modified to use these parameter values and also an additional internal helper function `getWebAPIPath` which will find the base organization URI and append the URL to match the root URI for the Web API so you don’t need to include it. The URI for the created entity is passed to the `successCallback` if it is defined. Similarly the public `errorHandler` function is used to parse any error that is returned. The `errorHandler` function must be public because it is called within the event handler for the `onreadystatechange` event and this is not within the scope of the namespace. It must be called using the full name: `MyNameSpace.WebAPI.errorHandler`.  
  
<a name="bkmk_createPromiseFunction"></a>   
## Create a re-usable function using promises  
 While callbacks have been traditionally used for asynchronous operations, many developers feel they are somewhat unwieldy, and difficult to read and debug because a series of asynchronous operations will build upon each other to create code that forms a “*pyramid of doom*” as indentation causes the code, using anonymous functions, to move further and further to the right of the page. Although this issue can be addressed by using named functions rather than anonymous functions, many developers appreciate the benefits offered by *promises*. A `Promise` object represents an operation that is not completed yet, but is expected to complete in the future.  
  
 There are many third party libraries and JavaScript frameworks which offer different implementations of promises. JQuery has offered a behavior based on the [CommonJS Promises/A](http://wiki.commonjs.org/wiki/Promises/A) design via [Deferred object](https://api.jquery.com/category/deferred-object/) and others insist on compliance with the [Promises/A+](https://github.com/promises-aplus/promises-spec) specification. An explanation of the differences between these implementations is beyond the scope of this topic. The objective of this section is simply to call out how a helper function for the Common Data Service for Apps Web API using a native `XMLHttpRequest` object can be written to use the native [Promise object](https://msdn.microsoft.com/library/dn802826.aspx) that is implemented in most modern browsers supported by Common Data Service for Apps. The following browsers have a native implementation of promises: [!INCLUDE[tn_Google_Chrome](../../includes/tn-google-chrome.md)] 32, Opera 19, [!INCLUDE[tn_Mozilla_Firefox](../../includes/tn-mozilla-firefox.md)] 29, [!INCLUDE[tn_Apple_Safari](../../includes/tn-apple-safari.md)] 8 and [!INCLUDE[pn_microsoft_edge](../../includes/pn-microsoft-edge.md)].  
  
> [!NOTE]
> [!INCLUDE[pn_ie_11](../../includes/pn-ie-11.md)] doesn’t implement native promises. For browsers that do not implement native promises, you must include a separate library to provide a *polyfill*. A polyfill is code that provides capabilities not provided natively by a browser. There are several polyfills or libraries which will allow [!INCLUDE[pn_ie_11](../../includes/pn-ie-11.md)] to have promises: [es6-promise](https://github.com/jakearchibald/es6-promise), [q.js](https://github.com/kriskowal/q), and [bluebird](http://bluebirdjs.com/docs/getting-started.html).  
  
 The benefit of using promises can be best demonstrated by an example. The following code uses the callback version of `MyNameSpace.WebAPI.create` to create an account and then three tasks associated with it.  
  
```javascript  
MyNameSpace.WebAPI.create("accounts",  
 { name: "Sample account" },  
 function (accountUri) {  
  console.log("Created account with URI: " + accountUri);  
  MyNameSpace.WebAPI.create("tasks",  
   { subject: "Task 1", "regardingobjectid_account_task@odata.bind": accountUri },  
   function () {  
    MyNameSpace.WebAPI.create("tasks",  
     { subject: "Task 2", "regardingobjectid_account_task@odata.bind": accountUri },  
     function () {  
      MyNameSpace.WebAPI.create("tasks",  
       { subject: "Task 3", "regardingobjectid_account_task@odata.bind": accountUri },  
       function () {  
        //Finished creating three tasks  
        console.log("Three tasks created");  
       },  
      function (error) { console.log(error.message); });  
     },  
     function (error) { console.log(error.message); });  
   },  
  function (error) { console.log(error.message); });  
 },  
function (error) { console.log(error.message); });  
```  
  
 For the purpose of this example, ignore the fact that all these records could be created in a single operation using deep insert. More information:[Create related entities in one operation](create-entity-web-api.md#bkmk_CreateRelated)  
  
 The callback code is challenging because it ends in the middle of the code block. Meanwhile, using promises you can create the same records with the following code.  
  
```javascript  
var accountUri;  
MyNameSpace.WebAPI.create("accounts", { name: "Sample account" })  
.then(function (aUri) {  
 accountUri = aUri;  
 console.log("Created account with URI: " + accountUri);  
})  
.then(function () {  
 return MyNameSpace.WebAPI.create("tasks", { subject: "Task 1", "regardingobjectid_account_task@odata.bind": accountUri });  
})  
.then(function () {  
 return MyNameSpace.WebAPI.create("tasks", { subject: "Task 2", "regardingobjectid_account_task@odata.bind": accountUri });  
})  
.then(function () {  
 return MyNameSpace.WebAPI.create("tasks", { subject: "Task 3", "regardingobjectid_account_task@odata.bind": accountUri });  
})  
.catch(function (error) { console.log(error.message); });  
```  
  
 Using promises preserves the flow of the code and allows for catching any error that occurs in a single catch function.  
  
 Converting the function with callbacks to use promises is a matter of removing the callback parameters and returning a slightly modified `XMLHttpRequest`, as shown in the following code example.  
  
```javascript  
return new Promise(function (resolve, reject) {  
 var req = new XMLHttpRequest();  
 req.open("POST", encodeURI(getWebAPIPath() + entitySetName), true);  
 req.setRequestHeader("Accept", "application/json");  
 req.setRequestHeader("Content-Type", "application/json; charset=utf-8");  
 req.setRequestHeader("OData-MaxVersion", "4.0");  
 req.setRequestHeader("OData-Version", "4.0");  
 req.onreadystatechange = function () {  
 if (this.readyState == 4 /* complete */) {  
  req.onreadystatechange = null;  
  if (this.status == 204) {  
  resolve(req.getResponseHeader("OData-EntityId"));  
  }  
  else {  
  reject(MyNameSpace.WebAPI.errorHandler(req.response));  
  }  
 }  
 };  
 req.send(JSON.stringify(entity));  
});  
```  
  
 Besides removing the callback parameters, the `XMLHttpRequest` is included in the `Promise` and rather than passing results or errors to the success or error callbacks, they’re passed to `resolve` or `reject` parameters. The following code represents the entire JavaScript library containing the `MyNameSpace.WebAPI.create` function. All that’s left to do is add more re-usable Web API operations using the same pattern.  
  
```javascript  
"use strict";  
var MyNameSpace = window.MyNameSpace || {};  
MyNameSpace.WebAPI = MyNameSpace.WebAPI || {};  
(function () {  
 /** @description Create a new entity  
  * @param {string} entitySetName The name of the entity set for the type of entity you want to create.  
  * @param {object} entity An object with the properties for the entity you want to create.  
  */  
 this.create = function (entitySetName, entity) {  
  /// <summary>Create a new entity</summary>  
  /// <param name="entitySetName" type="String">The name of the entity set for the entity you want to create.</param>  
  /// <param name="entity" type="Object">An object with the properties for the entity you want to create.</param>         
  if (!isString(entitySetName)) {  
   throw new Error("MyNameSpace.WebAPI.create entitySetName parameter must be a string.");  
  }  
  if (isNullOrUndefined(entity)) {  
   throw new Error("MyNameSpace.WebAPI.create entity parameter must not be null or undefined.");  
  }  
  
  return new Promise(function (resolve, reject) {  
   var req = new XMLHttpRequest();  
   req.open("POST", encodeURI(getWebAPIPath() + entitySetName), true);  
   req.setRequestHeader("Accept", "application/json");  
   req.setRequestHeader("Content-Type", "application/json; charset=utf-8");  
   req.setRequestHeader("OData-MaxVersion", "4.0");  
   req.setRequestHeader("OData-Version", "4.0");  
   req.onreadystatechange = function () {  
    if (this.readyState == 4 /* complete */) {  
     req.onreadystatechange = null;  
     if (this.status == 204) {  
      resolve(req.getResponseHeader("OData-EntityId"));  
     }  
     else {  
      reject(MyNameSpace.WebAPI.errorHandler(req.response));  
     }  
    }  
   };  
   req.send(JSON.stringify(entity));  
  });  
  
 };  
  
 //Internal supporting functions  
 function getClientUrl() {  
  //Get the organization URL  
  if (typeof GetGlobalContext == "function" &&  
      typeof GetGlobalContext().getClientUrl == "function") {  
   return GetGlobalContext().getClientUrl();  
  }  
  else {  
   //If GetGlobalContext is not defined check for Xrm.Page.context;  
   if (typeof Xrm != "undefined" &&  
       typeof Xrm.Page != "undefined" &&  
       typeof Xrm.Page.context != "undefined" &&  
       typeof Xrm.Page.context.getClientUrl == "function") {  
    try {  
     return Xrm.Page.context.getClientUrl();  
    } catch (e) {  
     throw new Error("Xrm.Page.context.getClientUrl is not available.");  
    }  
   }  
   else { throw new Error("Context is not available."); }  
  }  
 }  
 function getWebAPIPath() {  
  return getClientUrl() + "/api/data/v8.1/";  
 }  
  
 //Internal validation functions  
 function isString(obj) {  
  if (typeof obj === "string") {  
   return true;  
  }  
  return false;  
  
 }  
 function isNull(obj) {  
  if (obj === null)  
  { return true; }  
  return false;  
 }  
 function isUndefined(obj) {  
  if (typeof obj === "undefined") {  
   return true;  
  }  
  return false;  
 }  
 function isFunction(obj) {  
  if (typeof obj === "function") {  
   return true;  
  }  
  return false;  
 }  
 function isNullOrUndefined(obj) {  
  if (isNull(obj) || isUndefined(obj)) {  
   return true;  
  }  
  return false;  
 }  
 function isFunctionOrNull(obj) {  
  if (isNull(obj))  
  { return true; }  
  if (isFunction(obj))  
  { return true; }  
  return false;  
 }  
  
 // This function is called when an error callback parses the JSON response.  
 // It is a public function because the error callback occurs in the onreadystatechange   
 // event handler and an internal function wouldn’t be in scope.  
 this.errorHandler = function (resp) {  
  try {  
   return JSON.parse(resp).error;  
  } catch (e) {  
   return new Error("Unexpected Error")  
  }  
 }  
  
}).call(MyNameSpace.WebAPI);  
```
-->  
  
### See also  

[Use the Common Data Service for Apps Web API](overview.md)<br />
<!-- TODO:
[Work with Common Data Service for Apps data using web resources](../work-data-using-web-resources.md)<br /> -->
[Perform operations using the Web API](perform-operations-web-api.md)<br /> 
[Use OAuth with Cross-Origin Resource Sharing  to connect a Single Page Application](../oauth-cross-origin-resource-sharing-connect-single-page-application.md)
