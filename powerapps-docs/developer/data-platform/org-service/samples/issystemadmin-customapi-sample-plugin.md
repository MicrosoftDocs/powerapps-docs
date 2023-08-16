---
title: "Sample: IsSystemAdmin custom API plug-in (Microsoft Dataverse) | Microsoft Docs"
description: "Learn how to write a plug-in to support a custom API"
ms.date: 09/27/2022
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---

# Sample: IsSystemAdmin custom API

[!INCLUDE[cc-terminology](../../includes/cc-terminology.md)]

This sample shows how to write a plug-in that supports a custom API named `sample_IsSystemAdmin`.

> [!div class="nextstepaction"]
> [SDK for .NET: IsSystemAdmin custom API sample code](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/IsSystemAdminCustomAPI)

This sample creates a plug-in for the main operation of the `sample_IsSystemAdmin` custom API. This custom API will detect whether a user has the System Administrator security role.

Detecting whether a user has the System Administrator security role may require two separate queries depending on whether the user has been assigned the security role directly or whether they have it because of team that they belong to. This custom API encapsulates these queries into a single API call which will return a boolean value. This makes it easier to use by delegating the operation to the Dataverse server.

## How to run this sample

To run the code found in this sample, you must first create a custom API in your organization. There are two ways to do this.

### Import the managed solution file

The `IsSystemAdminFunction_1_0_0_0_managed.zip` in this folder contains the `sample_IsSystemAdmin` custom API that uses this code. You can simply import this solution file to create the custom API in your organization. See [Import solutions](../../../../maker/data-platform/import-update-export-solutions.md) for instructions.

After you are finished testing, delete the managed solution to remove the custom API.

### Create the custom API

You can create the custom API yourself and set the plug-in assembly created by this code.
There are several ways to create custom API, and they are documented here: [Create and use custom APIs](../../custom-api.md)

This custom API is defined with the following data:

```
{
  "uniquename": "sample_IsSystemAdmin",
  "allowedcustomprocessingsteptype": 0,
  "bindingtype": 1,
  "boundentitylogicalname": "systemuser",
  "description": "Returns whether the user has the System Administrator security role",
  "name": "Is System Administrator",
  "displayname": "Is System Administrator",
  "executeprivilegename": null,
  "isfunction": true,
  "isprivate": false,
  "workflowsdkstepenabled": false,
  "iscustomizable": {
    "Value": false
  },
  "CustomAPIResponseProperties": [
    {
      "uniquename": "HasRole",
      "name": "Has Role",
      "description": "Whether the user has the System Administrator security role",
      "displayname": "Has Role",
      "type": 0,
      "logicalentityname": null,
      "iscustomizable": {
        "Value": false
      }
    }
  ]
}
```

You can use this data to create the custom API using Postman and the Web API by following the example here: [Create a custom API with code](../../create-custom-api-with-code.md).

For information about the values passed see these topics: [CustomAPI tables](../../custom-api-tables.md)

This custom API is a function bound to the [User (SystemUser) table](../../reference/entities/systemuser.md). It has a single boolean response property `HasRole` which will return `true` when the user has the System Administrator security role.

After you create the custom API as defined above, build this .NET Class Library project to generate a plug-in assembly named `IsSystemAdminCustomAPI.dll`. This assembly will have a single plug-in type named `PowerApps.Samples.IsSystemAdmin`.

You must register the plug-in assembly created by using the Plug-in registration tool as described here: [Register plug-in](../../tutorial-write-plug-in.md#register-plug-in)

After the plug-in is registered, you will be able to set it as the plug-in type for the custom API.

The `sample_IsSystemAdmin` custom API you create will be part of the unmanaged customizations in your environment. To remove it you must delete the custom API and the Plugin Assembly.

## What this sample does

This `sample_IsSystemAdmin` custom API uses this code to query the system to detect whether the user has the System Administrator security role.

## How this sample works

To use the `sample_IsSystemAdmin` custom API, you can use either the Web API or the Organization Service using the Dataverse .NET Framework SDK assemblies.

### Using Web API

The Web API is easiest to try because you don't need to write any code. You can test it using your browser.

1. Get the Web API Url from the Developer Resources page. See [View developer resources](../../view-download-developer-resources.md). The value will look something like this: `https://yourorgname.api.crm.dynamics.com/api/data/v9.2`.
1. Copy the Web API URL and paste it into a browser address bar. You may be prompted to authenticate if you have not previously run a model-driven application before.
1. Edit the Web API URL to return information about system users. Append the following to the Web API Url: `/systemusers?$select=fullname`. Your you should be able to see JSON data in your browser.
1. Select a one of the `systemuserid` values for a user and open a different browser tab.
1. In this browser tab, compose the following URL using your Web API Url and the `systemuserid` value: <br />
   `https://<your org url>/api/data/v9.2/systemusers(<The systemuserid value>)/Microsoft.Dynamics.CRM.sample_IsSystemAdmin`<br />
   You must include the `Microsoft.Dynamics.CRM` namespace because this is a bound function. More information: [Bound functions](../../webapi/use-web-api-functions.md#bound-functions)
1. You should see results like the following when you send the request:<br />

```
{
  "@odata.context": "https://yourorgname.api.crm.dynamics.com/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.sample_IsSystemAdminResponse",
  "HasRole": false
}
```

The `HasRole` value indicates if the user has the System Administrator security role.

### Using Organization Service

1. You can use the Organization Service Quick Start sample instructions to create a .NET Framework Console application with C#. [Quickstart: Organization service sample (C#)](../quick-start-org-service-console-app.md)
1. Add the following static method to the program class. This creates a re-usable method.

   ```csharp
   static bool IsSystemAdmin(IOrganizationService svc, Guid systemuserid)
   {

       var req = new OrganizationRequest("sample_IsSystemAdmin")
       {
           ["Target"] = new EntityReference("systemuser", systemuserid)
       };

       var resp = svc.Execute(req);

       var hasRole = (bool)resp["HasRole"];

       return hasRole;
   }
   ```

1. Replace the code that is calling `WhoAmIRequest` with the following:

   ```csharp
    //Compose a query to retrieve top 10 users
   QueryExpression query = new QueryExpression("systemuser");
   query.ColumnSet = new ColumnSet("fullname");
   query.TopCount = 10;

    //Execute the query to retrieve the data
   EntityCollection users = svc.RetrieveMultiple(query);

   foreach (Entity user in users.Entities)
   {
        //Test each record returned using  the custom API
       bool isAdmin = IsSystemAdmin(svc, user.Id);

        //Show the results in the console
       Console.WriteLine($"{user["fullname"]} is{(isAdmin? string.Empty: " not")} an administrator");
   }
   ```

   This code will retrieve 10 users and loop through each one, testing whether they are a system administrator or not, writing the results to the console.

### Demonstrate

1. How to query to detect if the user is a system administrator
1. How to write a plug-in to support a custom API
1. How to invoke a custom API function using the Web API
1. How to invoke a custom API using the Organization service

### See also

[Create and use custom APIs](../../custom-api.md)<br />
[Write a plug-in](../../write-plug-in.md)<br />
[Register a plug-in](../../register-plug-in.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
