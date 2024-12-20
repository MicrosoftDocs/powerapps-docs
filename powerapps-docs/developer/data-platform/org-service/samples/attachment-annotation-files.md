---
title: "Sample: File operations with Attachments and Notes using the Dataverse SDK for .NET | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "This sample showcases how to work with file data within attachment and note tables." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 12/04/2024
author: JimDaly
ms.author: jdaly
ms.reviewer: jdaly
ms.topic: sample
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---
# Sample: File operations with Attachments and Notes using the Dataverse SDK for .NET

This .NET 6.0 sample demonstrates how to perform operations using file data with [Attachment (ActivityMimeAttachment)](../../reference/entities/activitymimeattachment.md) and [Note (Annotation)](../../reference/entities/annotation.md) tables using the Dataverse SDK for .NET.

This sample uses the [Microsoft.PowerPlatform.Dataverse.Client.ServiceClient Class](xref:Microsoft.PowerPlatform.Dataverse.Client.ServiceClient).

## Prerequisites

- Microsoft Visual Studio 2022
- Access to Dataverse with system administrator or system customizer privileges.

## How to run the sample

1. Clone or download the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repository.
1. Open the `PowerApps-Samples\dataverse\orgsvc\C#-NETCore\AttachmentAndAnnotationOperations\AttachmentAndAnnotationOperations.sln` file using Visual Studio 2022.

   This solution contains two projects that include samples:

   - **ActivityMimeAttachmentOperations**: Demonstrates using Attachments.
   - **AnnotationOperations**: Demonstrates using Annotations.

   In **Solution Explorer**, right-click the project you want to run and choose **Set as Startup Project**.

1. In either project, edit the *appsettings.json* file. Set the connection string `Url` and `Username` parameters as appropriate for your test environment.

   The environment Url can be found in the Power Platform admin center. It has the form `https://<environment-name>.crm.dynamics.com`.

1. Build the solution, and then run the desired project.

When the sample runs, you will be prompted in the default browser to select an environment user account and enter a password. To avoid having to do this every time you run a sample, insert a password parameter into the connection string in the `appsettings.json` file. For example:

```json
{
"ConnectionStrings": {
    "default": "AuthType=OAuth;Url=https://myorg.crm.dynamics.com;Username=someone@myorg.onmicrosoft.com;Password=mypassword;RedirectUri=http://localhost;AppId=51f81489-12ee-4a9e-aaae-a2591f45987d;LoginPrompt=Auto"
  }
}
```

Read the following important information about using a connection string in application code.
[!INCLUDE [cc-connection-string](../../includes/cc-connection-string.md)]

> [!TIP]
> You can set a user environment variable named `DATAVERSE_APPSETTINGS` to the file path of the appsettings.json file stored anywhere on your computer. The samples will use that appsettings file if the environment variable exists and is not null. Be sure to log out and back in again after you define the variable for it to take affect. To set an environment variable, go to **Settings > System > About**, select **Advanced system settings**, and then choose **Environment variables**.

## Demonstrates

This sample is a solution with two projects. See the respective README files for details on each project.

- [SDK for .NET Attachment (ActivityMimeAttachment) Operations sample README](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/orgsvc/CSharp-NETCore/AttachmentAndAnnotationOperations/ActivityMimeAttachmentOperations/README.md)
- [SDK for .NET Annotation (Note) Operations sample README](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/orgsvc/CSharp-NETCore/AttachmentAndAnnotationOperations/AnnotationOperations/README.md)

## Utility class

Both projects use a shared `Utility` class to perform common operations. This class contains three static methods:

### GetMimeType

Based on a [FileInfo](xref:System.IO.FileInfo) parameter, this function uses [Microsoft.AspNetCore.StaticFiles.FileExtensionContentTypeProvider](xref:Microsoft.AspNetCore.StaticFiles.FileExtensionContentTypeProvider) to try to get the mimetype of the file. If this cannot be determined, it returns `application/octet-stream`

### GetMaxUploadFileSize

Using the [IOrganizationService](xref:Microsoft.Xrm.Sdk.IOrganizationService) `service` parameter, this function returns the integer `maxuploadfilesize` value from the `organization` table.

### SetMaxUploadFileSize

Using the [IOrganizationService](xref:Microsoft.Xrm.Sdk.IOrganizationService) `service` parameter, this function sets the integer `maxuploadfilesize` value from the `organization` table to the value of the integer `maxUploadFileSizeInBytes` parameter.

### See also

[Use file data with Attachment and Note records](../../attachment-annotation-files.md)<br />
[Sample: Attachment and Annotation file operations using Dataverse Web API](../../webapi/samples/attachment-annotation-file-operations.md)

[!INCLUDE [footer-banner](../../../../includes/footer-banner.md)]
