---
title: "Grant limited access to Dataverse files using shared access signatures" 
description: "Learn how to create a shared access signature URL that enables anyone to download the file or image from Dataverse" 
ms.date: 06/18/2024
ms.reviewer: jdaly
ms.topic: article
author: JimDaly
ms.subservice: dataverse-developer
ms.author: jdaly
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Grant limited access to Dataverse files using shared access signatures

For one hour, anyone can download a file stored in Dataverse when you provide a url generated using the `GetFileSasUrl` message. This url provides anonymous access for anyone during this hour, starting when the url is generated. The person calling `GetFileSasUrl` to generate the url must have access to the record containing the file.

Files can be attachments, notes, file columns, or image columns. [Some limitations apply](#limitations)

You can use the `GetFileSasUrl` message using either the SDK for .NET or Web API.

## [SDK for .NET](#tab/sdk)

Use the [GetFileSasUrlRequest class](/dotnet/api/microsoft.crm.sdk.messages.getfilesasurlrequest) to specify which file to generate a link for.

- The [Target property](/dotnet/api/microsoft.crm.sdk.messages.getfilesasurlrequest.target) is an [EntityReference](/dotnet/api/microsoft.xrm.sdk.entityreference) that identifies the table row that contains an attachment, note, image, or file column.
- The [FileAttributeName property](/dotnet/api/microsoft.crm.sdk.messages.getfilesasurlrequest.fileattributename) must specify the name of the file column unless the `Target` property refers an attachment or note record. In these cases, the parameter is still required, but should be an empty string.
- Set the [DataSource property](/dotnet/api/microsoft.crm.sdk.messages.getfilesasurlrequest.datasource) to `retained` if the record was flagged for [long-term data retention](long-term-retention.md).

The [GetFileSasUrlResponse class](/dotnet/api/microsoft.crm.sdk.messages.getfilesasurlresponse) instance returned contains a [Result property](/dotnet/api/microsoft.crm.sdk.messages.getfilesasurlresponse.result) that is an instance of the [FileSasUrlResponse class](/dotnet/api/microsoft.xrm.sdk.filesasurlresponse). This type contains properties with data you need to send the URL to someone so they can download the file: `Filename`, `FileSizeInBytes`, `MimeType`, and `SasUrl`.

## [Web API](#tab/webapi)

Use the [GetFileSasUrl function](/power-apps/developer/data-platform/webapi/reference/getfilesasurl) to specify which file to generate a link for. 

- The `Target` parameter is an identifies the table row that contains an attachment, note, image, or file column. [Pass record reference to a function](webapi/use-web-api-functions.md#pass-record-reference-to-a-function) describes how to do this using the `@odata.id` annotation.
- The `FileAttributeName` parameter must specify the name of the file column unless the `Target` property refers an attachment or note record. In these cases, the parameter is still required, but should be an empty string.
- Set the `DataSource` parameter to `retained` if the record was flagged for [long-term data retention](long-term-retention.md).

The [GetFileSasUrlResponse complex type](/power-apps/developer/data-platform/webapi/reference/getfilesasurlresponse) instance returned contains a `Result` property that is an instance of the [FileSasUrlResponse complex type](/power-apps/developer/data-platform/webapi/reference/filesasurlresponse). This type contains properties with data you need to send the URL to someone so they can download the file: `Filename`, `FileSizeInBytes`, `MimeType`, and `SasUrl`.

---


## Examples

These example functions show how to use the `GetFileSasUrl` with both the SDK for .NET and Web API.

### [SDK for .NET](#tab/sdk)

This static `GetFileSasUrl` method returns a [FileSasUrlResponse class](/dotnet/api/microsoft.xrm.sdk.filesasurlresponse) instance with information needed to anonymously download a file.

```csharp
/// <summary>
/// Generates a link for anonymous access to a file.
/// </summary>
/// <param name="service">The authenticated IOrganizationService instance.</param>
/// <param name="target">The record that has the file data.</param>
/// <param name="fileAttributeName">Optional name of the file or image column</param>
/// <param name="dataSource">Optional source of the data when retained or deleted.</param>
/// <returns>Information to download a file</returns>
static FileSasUrlResponse GetFileSasUrl(IOrganizationService service, 
    EntityReference target, 
    string? fileAttributeName = null, 
    string? dataSource = null) { 

    var request = new GetFileSasUrlRequest() { 
        Target = target
    };

    if (target.LogicalName != "annotation" &&
        target.LogicalName != "activitymimeattachment"){

        if (!string.IsNullOrEmpty(fileAttributeName))
        {
            request.FileAttributeName = fileAttributeName;
        }
        else
        {

            string message = "fileAttributeName is required ";
            message += "when the target isn't annotation ";
            message += "or activitymimeattachment";

            throw new Exception(message);
        }
    }
    else
    {
        //FileAttributeName is required
        request.FileAttributeName = string.Empty;
    }
    

    if (!string.IsNullOrEmpty(dataSource)) {
        //dataSource should be 'retained' or 'bin'
        request.DataSource = dataSource;
    }

   var response = (GetFileSasUrlResponse)service.Execute(request);

    return response.Result;
}
```

[Use the SDK for .NET](org-service/overview.md)

### [Web API](#tab/webapi)

This `Get-FileSasUrl` PowerShell function  returns a [FileSasUrlResponse complex type](/power-apps/developer/data-platform/webapi/reference/filesasurlresponse) instance with information needed to anonymously download a file. 

This function depends on the `$baseURI` and `$baseHeaders` global variables set by the [Connect function](webapi/use-ps-and-vscode-web-api.md#create-a-connect-function) described in [Use PowerShell and Visual Studio Code with the Dataverse Web API](webapi/use-ps-and-vscode-web-api.md)

```powershell
function Get-FileSasUrl {
   param (
      [Parameter(Mandatory)] 
      [string] 
      $setName,
      [Parameter(Mandatory)] 
      [guid] 
      $id,
      [string] 
      $columnName,
      [string] 
      $dataSource
   )

   $uri = $baseURI + "GetFileSasUrl(Target=@t,FileAttributeName=@f"

   $query = "?@t={'@odata.id':'$setName($id)'}&@f="

   if ($setName -ne 'annotations' -and $setName -ne 'activitymimeattachments') {

      if ($null -ne $columnName) {

         $query += "'$columnName'"
         
      }
      else {

         $message = "columnName is required "
         $message += "when the setName isn't annotations "
         $message += "or activitymimeattachments"

         throw $message
         
      }
   }
   else {
      $query += '''''' # empty string
   }

   if("" -ne $dataSource) {
      $uri += ",DataSource=@d"
      # $dataSource should be 'retained' or 'bin'
      $query += "&@d='$dataSource'"
   }

   $GetFileSasUrlRequest = @{
      Uri     = $uri + ')' + $query
      Method  = 'Get'
      Headers = $baseHeaders
   }
   Invoke-RestMethod @GetFileSasUrlRequest | Select-Object -ExpandProperty Result
}
```

The following examples demonstrate the rules for setting the `FileAttributeName` parameter. It is a required parameter, but it can contain an empty string for `annotations` and `activitymimeattachments` entity sets.

```http
GET [Organization URI]/api/data/v9.2/GetFileSasUrl(Target=@p1,FileAttributeName='')?@p1={'@odata.id':'annotations(<annotationid>)'}

GET [Organization URI]/api/data/v9.2/GetFileSasUrl(Target=@p1,FileAttributeName='')?@p1={'@odata.id':'activitymimeattachments(<activitymimeattachmentid>)'}

GET [Organization URI]/api/data/v9.2/GetFileSasUrl(Target=@p1,FileAttributeName='myattachment')?@p1={'@odata.id':'myfiles(<myfileid>)'}
```

[Use the Microsoft Dataverse Web API](webapi/overview.md)

---

## Limitations

The following limitations apply:

- `GetFileSasUrl` only works for image columns configured to support full-size images. [Learn to detect which image columns support full-sized images](image-column-data.md#detect-which-image-columns-support-full-sized-images)
- `GetFileSasUrl` doesn't work for environments that have [enabled customer managed keys](/power-platform/admin/customer-managed-key).