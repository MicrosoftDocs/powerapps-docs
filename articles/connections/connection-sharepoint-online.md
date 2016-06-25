<properties
	pageTitle="Overview of the SharePoint connection | Microsoft PowerApps"
	description="See the available SharePoint functions, responses, and examples"
	services=""
	suite="powerapps"
	documentationCenter="" 	
	authors="AFTOwen"
	manager="erikre"
	editor=""
	tags="" />

<tags
ms.service="powerapps"
ms.devlang="na"
ms.topic="article"
ms.tgt_pltfrm="na"
ms.workload="na"
ms.date="06/18/2016"
ms.author="anneta"/>

# Connect to SharePoint in PowerApps

![SharePoint](./media/connection-sharepoint-online/sharepointicon.png)

Connect to a SharePoint site when you create an app automatically from data, manage connections in powerapps.com, update an existing app, or build an app from scratch.

## What's new ##
In early July 2016, we added support for on-premises data gateways so that you can connect to on-premises SharePoint sites as well as SharePoint Online sites.

## Known issues ##
You can add data from a list but not a library. In addition, not all types of columns are supported, and not all types of columns support all types of cards.

| Column type | Support | Default cards |
|---|---|----|
| Single line of text | Yes | View text |
| Multiple lines of text | Yes | View text |
| Choice | Yes (read-only) | View lookup |
| Number | Yes | View percentage<br>View rating<br>View text |
| Currency | Yes | View percentage<br>View rating<br>View text
| Date and Time | Yes | View text |
| Lookup | Yes (as of release 2.0.440) | View lookup<br>Edit lookup (as of release 2.0.440) |
| Boolean (Yes/No) | Yes | View text<br>View toggle |
| Person or Group | Yes (as of release 2.0.440) | View lookup<br>Edit lookup (as of release 2.0.440) |
| Hyperlink | Yes | View URL<br>View text |
| Picture | Yes (read-only) | View image<br>View text |
| Calculated | Yes (read-only) |   |
| Task Outcome | No |  |
| External data | No |  |
| Managed Metadata | Yes (as of release 2.0.440) | View lookup<br>Edit lookup (as of release 2.0.440) |

Moreover, PowerApps doesn't support columns that support multiple values or selections.

- For Lookup columns, the **Allow multiple values** checkbox must be cleared.

	![Check box to allow multiple values in a Lookup column](./media/connection-sharepoint-online/lookup.png)

- For Managed Metadata columns, the **Allow multiple values** checkbox must be cleared.

	![Check box to allow multiple values in a Managed Metadata column](./media/connection-sharepoint-online/metadata.png)

- For Person or Group columns, the **No** option under **Allow multiple selections** must be selected.

	![Options to allow multiple selections for a Person or Group column](./media/connection-sharepoint-online/person-group.png)

- For Choice columns, the **Drop-Down Menu** or **Radio Buttons** option under **Display choices using** must be selected.

	![Options to display choices for a Choice column](./media/connection-sharepoint-online/choice.png)

## Connect to SharePoint ##
**When PowerApps creates an app for you**

For more information, see [create an app automatically from a SharePoint list](app-from-sharepoint.md#create-an-app).

**When you update an app or build one from scratch**

**When you open powerapps.com**

## View the available functions ##
This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[GetOnNewItems](connection-sharepoint-online.md#getonnewitems) | When an item is created in a SharePoint list |
|[GetOnUpdatedItems](connection-sharepoint-online.md#getonupdateditems) | When an existing item is modified in a SharePoint list |
|[GetItems](connection-sharepoint-online.md#getitems) | Retrieves items from a SharePoint list |
|[PostItem](connection-sharepoint-online.md#postitem) | Creates an item in a SharePoint list |
|[GetItem](connection-sharepoint-online.md#getitem) | Retrieves a single item from a SharePoint list |
|[DeleteItem](connection-sharepoint-online.md#deleteitem) | Deletes an item from a SharePoint list |
|[PatchItem](connection-sharepoint-online.md#patchitem) | Updates an item in a SharePoint list |
|[GetColumnValues](connection-sharepoint-online.md#getcolumnvalues) | Retrieves possible values for a SharePoint column |
|[GetTables](connection-sharepoint-online.md#gettables) | Retrieves SharePoint lists from a site |

<!--NotAvailableYet
## GetFileMetadata
Get file metadata using id: Used for getting a file metadata on Document Library

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint Site URL. E.g. http://contoso.sharepoint.com/sites/mysite|
|id|string|yes|Unique identifier of the file|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|Id|string|No | |
|Name|string|No | |
|DisplayName|string|No | |
|Path|string|No | |
|LastModified|string|No | |
|Size|integer|No | |
|MediaType|string|No | |
|IsFolder|boolean|No | |
|ETag|string|No | |
|FileLocator|string|No | |


## UpdateFile
Update file: Used for updating a file on Document Library

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint Site URL. E.g. http://contoso.sharepoint.com/sites/mysite|
|id|string|yes|Unique identifier of the file|
|body|string |yes|The Content of the file|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|Id|string|No | |
|Name|string|No | |
|DisplayName|string|No | |
|Path|string|No | |
|LastModified|string|No | |
|Size|integer|No | |
|MediaType|string|No | |
|IsFolder|boolean|No | |
|ETag|string|No | |
|FileLocator|string|No | |


## DeleteFile
Delete file: Used for deleting a file on Document Library

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint Site URL. E.g. http://contoso.sharepoint.com/sites/mysite|
|id|string|yes|Unique identifier of the file|

#### Output properties
None.


## GetFileMetadataByPath
Get file metadata using path: Used for getting a file metadata on Document Library

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint Site URL. E.g. http://contoso.sharepoint.com/sites/mysite|
|path|string|yes|Path of the file|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|Id|string|No | |
|Name|string|No | |
|DisplayName|string|No | |
|Path|string|No | |
|LastModified|string|No | |
|Size|integer|No | |
|MediaType|string|No | |
|IsFolder|boolean|No | |
|ETag|string|No | |
|FileLocator|string|No | |


## GetFileContentByPath
Get file using path: Used for getting a file on Document Library

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint Site URL. E.g. http://contoso.sharepoint.com/sites/mysite|
|path|string|yes|Path of the file|

#### Output properties
None.


## GetFileContent
Get file using id: Used for getting a file on Document Library

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint Site URL. E.g. http://contoso.sharepoint.com/sites/mysite|
|id|string|yes|Unique identifier of the file|

#### Output properties
None.


## CreateFile
Create file: Used for uploading a file on Document Library

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint Site URL. E.g. http://contoso.sharepoint.com/sites/mysite|
|folderPath|string|yes|The path to the folder|
|name|string|yes|Name of the file|
|body| string |yes|The Content of the file|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|Id|string|No | |
|Name|string|No | |
|DisplayName|string|No | |
|Path|string|No | |
|LastModified|string|No | |
|Size|integer|No | |
|MediaType|string|No | |
|IsFolder|boolean|No | |
|ETag|string|No | |
|FileLocator|string|No | |


## CopyFile
Copy file: Used for copying a file on Document Library

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint Site URL. E.g. http://contoso.sharepoint.com/sites/mysite|
|source|string|yes|Path to the source file|
|destination|string|yes|Path to the destination file|
|overwrite|boolean|no|Whether or not to overwrite an existing file|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|Id|string|No | |
|Name|string|No | |
|DisplayName|string|No | |
|Path|string|No | |
|LastModified|string|No | |
|Size|integer|No | |
|MediaType|string|No | |
|IsFolder|boolean|No | |
|ETag|string|No | |
|FileLocator|string|No | |


## OnNewFile
When a file is created: Triggers a flow when a new file is created in a SharePoint folder

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint site url|
|folderId|string|yes|Unique identifier of the folder in SharePoint|

#### Output properties
None.


## OnUpdatedFile
When a file is modified: Triggers a flow when a file is modified in a SharePoint folder

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint site url|
|folderId|string|yes|Unique identifier of the folder in SharePoint|

#### Output properties
None.


## ListFolder
List folder: List the files on a folder

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint Site URL. E.g. http://contoso.sharepoint.com/sites/mysite|
|id|string|yes|Unique identifier of the file|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|Id|string|No | |
|Name|string|No | |
|DisplayName|string|No | |
|Path|string|No | |
|LastModified|string|No | |
|Size|integer|No | |
|MediaType|string|No | |
|IsFolder|boolean|No | |
|ETag|string|No | |
|FileLocator|string|No | |


## ListRootFolder
List root folder: List the files on Root folder

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint Site URL. E.g. http://contoso.sharepoint.com/sites/mysite|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|Id|string|No | |
|Name|string|No | |
|DisplayName|string|No | |
|Path|string|No | |
|LastModified|string|No | |
|Size|integer|No | |
|MediaType|string|No | |
|IsFolder|boolean|No | |
|ETag|string|No | |
|FileLocator|string|No | |


## ExtractFolderV2
Extract folder: Used for extracting a folder on Document Library

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint Site URL. E.g. http://contoso.sharepoint.com/sites/mysite|
|source|string|yes|Path to the source file|
|destination|string|yes|Path to the destination folder|
|overwrite|boolean|no|Whether or not to overwrite an existing file|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|Id|string|No | |
|Name|string|No | |
|DisplayName|string|No | |
|Path|string|No | |
|LastModified|string|No | |
|Size|integer|No | |
|MediaType|string|No | |
|IsFolder|boolean|No | |
|ETag|string|No | |
|FileLocator|string|No | |
-->

### GetOnNewItems
When a new item is created: When a new item is created in a SharePoint list

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint Site url (example: http://contoso.sharepoint.com/sites/mysite)|
|table|string|yes|SharePoint list name|
|$skip|integer|no|Number of entries to skip (default = 0)|
|$top|integer|no|Maximum number of entries to retrieve (default = 256)|
|$filter|string|no|An ODATA filter query to restrict the number of entries|
|$orderby|string|no|An ODATA orderBy query for specifying the order of entries|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|value|array|No | |


### GetOnUpdatedItems
When an existing item is modified: When an existing item is modified in a SharePoint list

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint Site url (example: http://contoso.sharepoint.com/sites/mysite)|
|table|string|yes|SharePoint list name|
|$skip|integer|no|Number of entries to skip (default = 0)|
|$top|integer|no|Maximum number of entries to retrieve (default = 256)|
|$filter|string|no|An ODATA filter query to restrict the number of entries|
|$orderby|string|no|An ODATA orderBy query for specifying the order of entries|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|value|array|No | |


### GetItems
Get items: Retrieves items from a SharePoint list

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint site url (example: http://contoso.sharepoint.com/sites/mysite)|
|table|string|yes|SharePoint list name|
|$skip|integer|no|Number of entries to skip (default = 0)|
|$top|integer|no|Maximum number of entries to retrieve (default = 256)|
|$filter|string|no|An ODATA filter query to restrict the number of entries|
|$orderby|string|no|An ODATA orderBy query for specifying the order of entries|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|value|array|No | |


### PostItem
Create item: Creates a new item in a SharePoint list

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint Site url (example: http://contoso.sharepoint.com/sites/mysite)|
|table|string|yes|SharePoint list name|
|item| |yes|Item to create|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|ItemInternalId|string|No |


### GetItem
Get item: Retrieves a single item from a SharePoint list

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint Site url (example: http://contoso.sharepoint.com/sites/mysite)|
|table|string|yes|SharePoint list name|
|id|integer|yes|Unique identifier of item to be retrieved|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|ItemInternalId|string|No |


### DeleteItem
Delete item: Deletes an item from a SharePoint list

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint Site url (example: http://contoso.sharepoint.com/sites/mysite)|
|table|string|yes|SharePoint list name|
|id|integer|yes|Unique identifier of item to be deleted|

#### Output properties
None.


### PatchItem
Update item: Updates an item in a SharePoint list

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint Site url (example: http://contoso.sharepoint.com/sites/mysite)|
|table|string|yes|SharePoint list name|
|id|integer|yes|Unique identifier of item to be updated|
|item| |yes|Item with changed properties|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|ItemInternalId|string|No |

### GetColumnValues
Get column values: Retrieves possible values for a SharePoint column

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint Site url (example: http://contoso.sharepoint.com/sites/mysite)|
|table|string|yes|SharePoint list name|
|column|string|yes|Column name|
|$search|string|no|An search string to look for values|

#### Output properties
None.


### GetTables
Get lists: Retrieves SharePoint lists from a site

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|SharePoint site url (example: http://contoso.sharepoint.com/sites/mysite)|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|value|array|No | |


### Helpful links
See all the [available connections](../connections-list.md).  
Learn how to [add connections](../add-manage-connections.md) to your apps.
