---
title: "Sample: File Operations using Dataverse Web API (Microsoft Dataverse) | Microsoft Learn" 
description: "This sample demonstrates how to perform operations with file columns using the Dataverse Web API." 
ms.date: 10/28/2022
author: MsSQLGirl
ms.author: jukoesma
ms.reviewer: jdaly
search.audienceType:
  - developer
contributors:
  - JimDaly
  - phecke
---
# Sample: File Operations using Dataverse Web API

This .NET 6.0 sample demonstrates how to perform operations with file columns using the Dataverse Web API.

This sample uses the common helper code in the [WebAPIService class library (C#)](webapiservice.md).

> [!div class="nextstepaction"]
> [View this sample on Github](https://github.com/microsoft/PowerApps-Samples/tree/master/dataverse/webapi/CSharp-NETx/FileOperations)

## Prerequisites

- Microsoft Visual Studio 2022
- Access to Dataverse with system administrator or system customizer privileges.

## How to run the sample

1. Clone or download the [PowerApps-Samples](https://github.com/microsoft/PowerApps-Samples) repository.
1. Open the `PowerApps-Samples\dataverse\webapi\C#-NETx\FileOperations\FileOperations.sln` file using Visual Studio 2022.
1. Edit the `appsettings.json` file to set the following property values:

   |Property|Instructions  |
   |---------|---------|
   |`Url`|The Url for your environment. Replace the placeholder `https://yourorg.api.crm.dynamics.com` value with the value for your environment. See [View developer resources](../../view-download-developer-resources.md) to find this. |
   |`UserPrincipalName`|Replace the placeholder `you@yourorg.onmicrosoft.com` value with the UPN value you use to access the environment.|
   |`Password`|Replace the placeholder `yourPassword` value with the password you use.|

1. Save the `appsettings.json` file
1. Select which of the projects you want to run in solution explorer. Right click the project and choose **Set as Startup Project**.
1. Press F5 to run the sample.

## Sample Output

The output of the sample should look something like this:

```
Creating file column named 'sample_FileColumn' on the account table ...
Created file column named 'sample_FileColumn' in the account table.
Created account record with accountid:5fb4f993-7c55-ed11-bba3-000d3a9933c9
Uploading file Files\25mb.pdf ...
Uploaded file Files\25mb.pdf
Downloading file from accounts(5fb4f993-7c55-ed11-bba3-000d3a9933c9)/sample_filecolumn ...
Downloaded the file to E:\GitHub\PowerApps-Samples\dataverse\webapi\C#-NETx\FileOperations\FileOperationsWithActions\bin\Debug\net6.0//downloaded-25mb.pdf.
Deleted the file using FileId.
Deleted the account record.
Deleting the file column named 'sample_filecolumn' on the account table ...
Deleted the file column named 'sample_filecolumn' in the account table.
```

## Demonstrates

This sample is a solution  with three projects. Each project performs the same operations in a different manner. See the respective README files for details on each project.

- [Web API File Operations with actions sample README](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/CSharp-NETx/FileOperations/FileOperationsWithActions/README.md)
- [Web API File Operations with chunks sample README](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/CSharp-NETx/FileOperations/FileOperationsWithChunks/README.md)
- [Web API File Operations with stream sample README](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/CSharp-NETx/FileOperations/FileOperationsWithStream/README.md)

The code for each project is in the respective `Program.cs` file.

- [Web API File Operations with actions sample Program.cs](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/CSharp-NETx/FileOperations/FileOperationsWithActions/Program.cs)
- [Web API File Operations with chunks sample Program.cs](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/CSharp-NETx/FileOperations/FileOperationsWithChunks/Program.cs)
- [Web API File Operations with stream sample Program.cs](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/CSharp-NETx/FileOperations/FileOperationsWithStream/Program.cs)

Each project uses a shared `Utility` class to perform common operations. This class is in the [Utility.cs](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/webapi/CSharp-NETx/FileOperations/Utility.cs) file.

At a high level, each project performs these operations:

### Create a file column

The `Utility.CreateFileColumn` function creates a file column named `sample_FileColumn` in the account table with a `MaxSizeInKb` value of 10 MB.

### Update a file column

The `Utility.UpdateFileColumnMaxSizeInKB` function updates the `MaxSizeInKb` value of the `sample_FileColumn` file column to 100 MB.

> **Tip**: If you want to create some error scenarios because the file column size is too small, comment out this line.

### Retrieve the file column MaxSizeInKb value

The `Utility.GetFileColumnMaxSizeInKb` retrieves the `MaxSizeInKb` value of the `sample_FileColumn` file column and stores it in a variable named `fileColumnMaxSizeInKb`.

### Create an account record

Before a file can be uploaded to the file column, a record must exist.

### Upload a file

The function to upload the file accepts a parameter named `fileColumnMaxSizeInKb` and uses that value to test the size of the file. If the file is larger than the configured limit of the file column, it will throw an error.

### Download the file

If the file upload succeeded, the function to download the file will save it to the current directory. You can try opening the file to confirm it was uploaded and downloaded correctly.

### Delete the file

If the file upload succeeded, the file is deleted.

### Clean up

To leave the system in the state before the sample ran, it does the following:

- Delete the account record
- Delete the file column

### See Also

[Use file column data](../../file-column-data.md)<br />
[Sample: File Operations using Dataverse SDK for .NET](../../org-service/samples/file-operations.md)<br />
[Use image column data](../../image-column-data.md)<br />
[Sample: Image Operations using Dataverse Web API](image-operations.md)

[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
