---
title: "Sample: Attachment and Annotation file operations using Dataverse Web API (Microsoft Dataverse) | Microsoft Learn"
description: "This sample demonstrates how to perform operations with file data using the Attachment (ActivityMimeAttachment) and Note (Annotation) tables using the Dataverse Web API." 
ms.date: 02/04/2023
author: JimDaly
ms.author: jdaly
ms.reviewer: jdaly
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---
# Sample: Attachment and Annotation file operations using Dataverse Web API

This .NET 6.0 sample demonstrates how to perform operations using file data with <xref:Microsoft.Dynamics.CRM.activitymimeattachment> and <xref:Microsoft.Dynamics.CRM.annotation> entity types using the Dataverse Web API.

> [!div class="nextstepaction"]
> [View this sample on Github](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/CSharp-NETx/AttachmentAndAnnotationOperations)

This sample uses the common helper code in the [WebAPIService class library (C#)](webapiservice.md) sample project.

## Prerequisites

- Microsoft Visual Studio 2022
- Access to Dataverse with system administrator or system customizer privileges.

## How to run the sample

1. Clone or download the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repository.
1. Open the `PowerApps-Samples\dataverse\webapi\C#-NETx\AttachmentAndAnnotationOperations\AttachmentAndAnnotationOperations.sln` file using Visual Studio 2022.

   This solution contains two projects that include samples:

   - **ActivityMimeAttachmentOperations**: Demonstrates using Attachments.
   - **AnnotationOperations**: Demonstrates using Annotations.
   
   **Note**: The **WebAPIService** project is included so that each of the other projects can depend on the common helper code provided by the service. The samples use several classes in the `WebAPIService/Messages` folder.
   
   In **Solution Explorer**, right-click the project you want to run and choose **Set as Startup Project**.

1. In either project, edit the `appsettings.json` file to set the following property values:

   |Property|Instructions  |
   |---------|---------|
   |`Url`|The Url for your environment. Replace the placeholder `https://yourorg.api.crm.dynamics.com` value with the value for your environment. See [View developer resources](../../view-download-developer-resources.md) to find this. |
   |`UserPrincipalName`|Replace the placeholder `you@yourorg.onmicrosoft.com` value with the UPN value you use to access the environment.|
   |`Password`|Replace the placeholder `yourPassword` value with the password you use.|

1. Save the `appsettings.json` file.

   **Note**: Both projects refer to the same `appsettings.json` file, so you only need to do this one time to run either project.

1. Press **F5** to run the sample.

## Demonstrates

This sample is a solution  with two projects. See the respective README files for details on each project.

- [Web API Attachment (ActivityMimeAttachment) Operations sample README](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/CSharp-NETx/AttachmentAndAnnotationOperations/ActivityMimeAttachmentOperations/README.md)
- [Web API Annotation (Note) Operations sample README](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/CSharp-NETx/AttachmentAndAnnotationOperations/AnnotationOperations/README.md)

## Utility class

Both projects use a shared `Utility` class to perform common operations. This class contains three static methods:

### GetMimeType

Based on a [FileInfo](xref:System.IO.FileInfo) parameter, this function uses [Microsoft.AspNetCore.StaticFiles.FileExtensionContentTypeProvider](xref:Microsoft.AspNetCore.StaticFiles.FileExtensionContentTypeProvider) to try to get the mimetype of the file. If this cannot be determined, it returns `application/octet-stream`

### GetMaxUploadFileSize

Using the **WebAPIService** `Service` `service` parameter, this function returns the integer `maxuploadfilesize` value from the `organization` table.

### SetMaxUploadFileSize

Using the **WebAPIService** `Service`  `service` parameter, this function sets the integer `maxuploadfilesize` value from the `organization` table to the value of the integer `maxUploadFileSizeInBytes` parameter.

### See also

[Use file data with Attachment and Note records](../../attachment-annotation-files.md)<br />
[Sample: File operations with Attachments and Notes using the Dataverse SDK for .NET](../../org-service/samples/attachment-annotation-files.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
