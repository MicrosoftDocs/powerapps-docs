---
title: "Grant limited access to Dataverse files using shared access signatures" 
description: "Learn how to create a shared access signature URL that enables anyone to download the file or image from Dataverse" 
ms.date: 09/11/2024
ms.reviewer: jdaly
ms.topic: how-to
author: JimDaly
ms.subservice: dataverse-developer
ms.author: jdaly
search.audienceType: 
  - developer
contributors:
 - JimDaly
---
# Grant limited access to Dataverse files using shared access signatures

For one hour, anyone can download a file stored in Dataverse using a url generated using the `GetFileSasUrl` message. This url provides anonymous access for anyone during this hour, starting when the url is generated. The person calling `GetFileSasUrl` to generate the url must have access to the record containing the file.

Files can be attachments, notes, file columns, or image columns. [Some limitations apply](#limitations)

> [!NOTE]
> Administrators can configure the tenant to limit downloads based on the IP address of client applications using the [SAS IP restriction feature (preview)](/power-platform/admin/security/data-storage#storage-shared-access-signature-sas-ip-restriction). When this is enabled, users will get a 401 error when the IP address for their computer does't meet the restrictions set for the tenant and they try to download the file.

## Parameters

The `GetFileSasUrl` message has the following parameters:

|Name|Type|Description|
|---------|---------|---------|
|`Target`|[EntityReference](/dotnet/api/microsoft.xrm.sdk.entityreference)/<br />[crmbaseentity ](/power-apps/developer/data-platform/webapi/reference/crmbaseentity)|Identifies the table row with the file or image data.|
|`FileAttributeName`|string|Identifies the name of the file or image column with the data. For note and attribute records, this value must be an empty string.|
|`DataSource`|string|A value of "`retained`" or "`bin`" when the record was flagged for [long-term data retention](long-term-retention.md) or deleted in a table with the [recycle bin feature enabled](restore-deleted-records.md).|

## Response

The data returned by the `GetFileSasUrl` message has a `Result` property with this data:

|Name|Type|Description|
|---------|---------|---------|
|`FileName`|string|The file name.|
|`FileSizeInBytes`|int64|The file size in bytes.|
|`MimeType`|string|The mime type of the file.|
|`SasUrl`|string|The shared access signature (SAS) URL that can be used to access the file.|


## Examples

These example functions show how to use the `GetFileSasUrl` message with both the SDK for .NET and Web API.

### [SDK for .NET](#tab/sdk)

This static `GetFileSasUrl` method uses the [GetFileSasUrlRequest ](/dotnet/api/microsoft.crm.sdk.messages.getfilesasurlrequest) and [GetFileSasUrlResponse](/dotnet/api/microsoft.crm.sdk.messages.getfilesasurlresponse) classes. The [GetFileSasUrlResponse.Result property](/dotnet/api/microsoft.crm.sdk.messages.getfilesasurlresponse.result) returns a [FileSasUrlResponse class](/dotnet/api/microsoft.xrm.sdk.filesasurlresponse) instance with information needed to anonymously download a file.

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

    if (target.LogicalName == "annotation" ||
        target.LogicalName == "activitymimeattachment"){

        //FileAttributeName is required
        request.FileAttributeName = string.Empty;

    }
    else
    {

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

This `Get-FileSasUrl` PowerShell function uses the [GetFileSasUrl function](/power-apps/developer/data-platform/webapi/reference/getfilesasurl) which returns a [GetFileSasUrlResponse complex type](/power-apps/developer/data-platform/webapi/reference/getfilesasurlresponse). The `GetFileSasUrlResponse.Result` property is a [FileSasUrlResponse complex type](/power-apps/developer/data-platform/webapi/reference/filesasurlresponse) instance with information needed to anonymously download a file.


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

   if ($setName -eq 'annotations' -or $setName -eq 'activitymimeattachments') {

      $query += "''" # empty string
   }
   else {
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

The following examples demonstrate the rules for setting the `FileAttributeName` parameter. It's a required parameter, but it can contain an empty string for `annotations` and `activitymimeattachments` entity sets.

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
- `GetFileSasUrl` doesn't work for environments that [continue to use self-manage database encryption key feature (BYOK)](/power-platform/admin/manage-encryption-key). Customers using BYOK need to [migrate to use customer managed key (CMK)](/power-platform/admin/cmk-migrate-from-byok) to use `GetFileSasUrl`.

### See also

[Files and images overview](files-images-overview.md)   
[Use file column data](file-column-data.md)   
[Use image column data](image-column-data.md)   
[Use file data with Attachment and Note records](attachment-annotation-files.md)
