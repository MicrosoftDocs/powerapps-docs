---
title: "Sample: ExportDataUsingFetchXmlToAnnotation Custom API plug-in (Microsoft Dataverse) | Microsoft Docs"
description: "Learn how to write write a plug-in for a custom api that will export data to a CSV file you can download."
ms.date: 04/27/2023
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - sopat20
  - cwithfourplus
---

# Sample: ExportDataUsingFetchXmlToAnnotation Custom API

This sample shows how to write a plug-in that supports a Custom API 
named `sample_ExportDataUsingFetchXmlToAnnotation`.
You can download the sample from 
[here](https://github.com/Microsoft/PowerApps-Samples/tree/master/dataverse/orgsvc/C%23/ExportDataUsingFetchXmlToAnnotation).

The plug-in provides logic for the main operation of the Custom API. 
The `sample_ExportDataUsingFetchXmlToAnnotation` custom api retrieves data using 
the provided `FetchXML` input parameter and creates a CSV file. It then creates
an annotation record and returns the `annotationid` as the `AnnotationId` response property..

**NOTE :**
The size of data in CSV file should be under the attachment size limit 
specified in the system settings; otherwise the creation of attachment will fail.

## How to run this sample

To run the code found in this sample, you must first create a Custom API in your organization.

There are two ways to create the custom api:

1. [Import the managed solution file](#import-the-managed-solution-file)
1. [Create the custom API](#create-the-custom-api)

### Import the managed solution file

The `ExportDataUsingFetchXmlToAnnotation_1_0_0_0_managed.zip` in this folder contains the `sample_ExportDataUsingFetchXmlToAnnotation` Custom API that uses this code, and a cleanup API `sample_CleanupExportedDataAnnotations`. You can simply import this solution file to create the Custom API in your organization.  See [Import solutions](../../../../maker/data-platform/import-update-export-solutions.md) for instructions.

After you are finished testing, invoke the `sample_CleanupExportedDataAnnotations` Custom API and delete the managed solution to remove the Custom API.

`sample_ExportDataUsingFetchXmlToAnnotation` is an unbound Custom API . It takes one input parameter `FetchXml` which is used to fetch the data and returns `AnnotationId` the record Id of the created annotation record which will have the CSV attached.

The `sample_CleanupExportedDataAnnotations` API has no input/output parameters.

### Create the custom API

You can also build the plug-in assembly in this project, create the custom API and associate the plug-in step manually.

1. Build the solution included above, and using the Plugin Registration Tool, register the assembly `ExportDataUsingFetchXmlToAnnotation.dll`, and include both the plugins
`PowerApps.Samples.ExportDataUsingFetchXmlToAnnotationPlugin` and `PowerApps.Samples.CleanUpExportedDataAnnotationsPlugin` and note the plugintypeids generated for these.

1. Using the following JSON data create these Custom APIs:

```json
{
    "uniquename": "sample_ExportDataUsingFetchXmlToAnnotation",
    "allowedcustomprocessingsteptype": 0,
    "bindingtype": 0,
    "boundentitylogicalname": null,
    "description": "Exports data using the input Fetch Xml to CSV attaches to an annotation record.",
    "name" : "Export Data Using Fetch XML to Annotation",
    "displayname": "Export Data Using Fetch XML to Annotation",
    "isfunction": false,
    "isprivate": false,
    "workflowsdkstepenabled": false,
    "customapiid": "bd8ffcee-5a38-4d0a-b296-6848c94dd22e",
    "iscustomizable": {
        "Value": true,
    },
    "CustomAPIRequestParameters": [
        {            
            "uniquename": "FetchXml",
            "name": "Fetch Xml",
            "description": "Fetch XML which is used to fetch all data and export to CSV",
            "displayname": "Fetch Xml",
            "type": 10,
            "isoptional": false
        }
    ],
    "CustomAPIResponseProperties": [
        {
            "uniquename": "AnnotationId",
            "name": "Annotation Id",
            "description": "Id of the created annotation entity record.",
            "displayname": "Annotation Id",
            "type": 12,
        }
    ],
    "PluginTypeId@odata.bind": "plugintypes(<Plugin type id for ExportDataUsingFetchXmlToAnnotationPlugin>)"
}
```

```json
{
    "uniquename": "sample_CleanupExportedDataAnnotations",
    "allowedcustomprocessingsteptype": 0,
    "bindingtype": 0,
    "boundentitylogicalname": null,
    "description": "Clean Up Exported Data Annotations",
    "name" : "Clean Up Exported Data Annotations",
    "displayname": "Clean Up Exported Data Annotations",
    "isfunction": false,
    "isprivate": false,
    "workflowsdkstepenabled": false,
    "customapiid": "e54824e5-6a98-435a-93ea-f50eb453a1f1",
    "iscustomizable": {
        "Value": true,
    },
    "PluginTypeId@odata.bind": "plugintypes(<Plugin type id for CleanupExportedDataAnnotationsPlugin>)"
}
```

The above created Custom APIs will be created as part of unmanaged customization in your enviornment. To remove it you must delete the Custom API and the plugin assembly.

More information: [Create a Custom API with code](../../create-custom-api-with-code.md)


## How this sample works

You can use either the Web API or the Organization Service using the Dataverse .NET Framework SDK assemblies to invoke the Custom API.

### [SDK for .NET](#tab/sdk)


1. You can use the Organization Service Quick Start sample instructions to create a .NET Framework Console application with C#. See [Quickstart: Execute an Organization service request (C#)](../quick-start-org-service-console-app.md)
1. Add the following static method to the program class to create a re-usable method for exporting data using FetchXML to Annotation.

   ```csharp
   static Guid ExportDataUsingFetchXmlToAnnotation(IOrganizationService service)
   {
       var req = new OrganizationRequest("sample_ExportDataUsingFetchXmlToAnnotation")
       {
           ["FetchXml"] = @"<fetch version='1.0' output-format='xml-platform' mapping='logical'>
                           <entity name='account'>
                               <attribute name='accountid'/>
                               <attribute name='name'/>  
                           </entity>
                       </fetch>"
       };
   
       var resp = service.Execute(req);
   
       var annotationId = (Guid)resp["AnnotationId"];
   
       return annotationId;
   }
   ```

1. Replace the code that is calling `WhoAmIRequest` with the following:

   ```csharp
    var annotationId = ExportDataUsingFetchXmlToAnnotation(svc)
   ```

### [Web API](#tab/webapi)

To use the Custom API with the Web API, send a `POST` request to the API endpoint.

 **Request**

```http
POST [Organization URI]/api/data/v9.2/sample_ExportDataUsingFetchXmlToAnnotation
Content-Type: application/json
OData-MaxVersion: 4.0
OData-Version: 4.0
Accept: application/json

{
    "FetchXml": "<fetch version='1.0' output-format='xml-platform' mapping='logical'>
                    <entity name='account'>
                        <attribute name='accountid'/>
                        <attribute name='name'/>  
                    </entity>
                </fetch>"
}
```

 **Response**

```http
HTTP/1.1 200 OK
OData-Version: 4.0
Content-Type: application/json; odata.metadata=minimal

{
    "@odata.context": "[Organization URI]/api/data/v9.2/$metadata#Microsoft.Dynamics.CRM.sample_ExportDataUsingFetchXmlToAnnotation",
    "AnnotationId": "c9fdfe63-41e3-ed11-8845-0022480b2800"
}
```

The `AnnotationId` value indicates the record in annotation table.

---

### Demonstrates

1. How to recursively fetch data from fetch xml.
1. How to create a csv attachment to annotation entity.
1. How to write a plug-in to support a Custom API
1. How to invoke a Custom API using the Web API
1. How to invoke a Custom API using the Organization service

## Clean Up

To clean up all the created data, invoke the `sample_CleanupExportedDataAnnotations` Custom API action to delete the created annotation records, and then uninstall the managed solution.

If the Custom APIs were created using WebApi then you will have delete the Custom APIs and the registered aassemblies manually.

`sample_CleanupExportedDataAnnotations` deletes all annotation records that meet the following criteria:


|Column|Value|
|---------|---------|
|`subject`|`Export Data Using FetchXml To Csv`|
|`filename`|`exportdatausingfetchxml.csv`|


## See also

[Create and use Custom APIs](../../custom-api.md)<br />
[Write a plug-in](../../write-plug-in.md)<br />
[Register a plug-in](../../register-plug-in.md)