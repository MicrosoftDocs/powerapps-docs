---
title: Configure a file column on portals (preview)
description: Learn how to configure a file column on portals.
author: nageshbhat-msft
ms.topic: conceptual
ms.custom: 
ms.date: 06/22/2022
ms.subservice: portals
ms.author: nabha
ms.reviewer: ndoelman
contributors:
    - ProfessorKendrick
    - nickdoelman
---

# Configure a file column on portals (preview)

[This topic is pre-release documentation and is subject to change.]

The **file** column is used for storing binary data. The primary intended use of this column is to store a single file, note, or attachment; however, storage of other forms of binary data is also possible. Portals maker can configure file column on Basic and Advanced form to provide upload, view, modify and delete the file. The file column provides storing file up to the specified maximum size in Microsoft Dataverse table column.

> [!NOTE]
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../../includes/cc-preview-features-definition.md)]

## Enable File control on form

You must configure site settings **Control/EnableFilePreview** and set its value to **true** to enable **file** controls on the form. You don't require to make any configuration to use file column with Liquid code or Web API.

:::image type="content" source="media/file-column/enable-file-preview.png" alt-text="Site settings menu for enable file preview with value set to true.":::

> [!IMPORTANT]
> This site setting is only required during preview period only.

## Liquid code

Liquid is an open-source template language that is integrated natively into Microsoft Power Apps portals. Developers can retrieve file column values while data is being queried by using fetchXML and entity view

```
{% for item in tables.results.entities %}
    {{ item.columnname.Name }}
    {{ item.columnname.Size }}
    {{ item.columnname.Url }}
{% endfor %}
```
| Attribute | Description | 
|-----|-----|
| Name | Name of the file associated with column |
| Size | File size in bytes |
| URL  | File download URL (Provides the Web API URL to download file. During private preview, you need to enable Web API read on this column to download file. This URL will be replaced as we reach public preview) |

Example: Retrieve file column data from contact table

Create a new file data type column in [Microsoft Dataverse](../../data-platform/create-edit-field-portal.md#create-a-column) for contact table with name 'myfileattribute'.

> [!NOTE]
> Make sure you've configured the appropriate table permission on the contact table to read record

```
{% fetchxml contacts %}
<fetch version="1.0" output-format="xml-platform" mapping="logical" distinct="false">
  <entity name="contact">
    <attribute name="fullname" />
    <attribute name="myfileattribute" />    
  </entity>
</fetch>
{% endfetchxml %}

{% for item in contacts.results.entities %}
        "Full Name":"{{ item.fullname }}"
        "Entity Image Url":"{{ item.myfileattribute.Name }}",      
        "Entity Image Size":"{{ item.myfileattribute.Size }}",
        "Entity Image Type":"{{ item.myfileattribute.Url }}" 
{% endfor %}
```

## Web API

Portals Web API can be used to perform create, read, update, and delete operations on file columns across Microsoft Dataverse tables.

### Retrieving file data

To retrieve file data, use the following APIs

```
GET /\_api/&lt;entity-type&gt;(id)/&lt;file-attribute-name&gt;/$value
```

File data transfers from the web service endpoints are limited to a maximum of 16-MB data in a single service call. File data that exceeds 16 MB must be divided into 4 MB or smaller data blocks (chunks) where each block is received in a separate API call until all file data has been received. It is your responsibility to join the downloaded data blocks to form the complete data file by combining the data blocks in the same sequence as the blocks were received.

#### Example: File download \< 16 MB

##### Request

```
HTTP
GET [Portal Url]/_api/accounts(62d53214-9dfa-eb11-94ee-0022482230a8)/myfileattribute/$value
Headers:
Content-Type: application/octet-stream
```
##### Response

```
204 No Content
Body:
Byte[ ]
```

#### Example: File download \> 16 MB

##### Request

```
HTTP
GET [Portal Url]/_api/accounts(62d53214-9dfa-eb11-94ee-0022482230a8)/myfileattribute/$value
Headers:
Content-Type: application/octet-stream
Range: bytes=0-1023
```

##### Response

```
HTTP
204 No Content
Body:
Byte[ ]
```

### Upload file data

To upload the file, set the value of the file column to a byte array that contains the content of the file

```
PUT or PATCH /\_api/&lt;entity-type&gt;(id)/&lt;file-attribute-name&gt;
```

#### Example: file upload

##### Request

```
HTTP
PUT [Portal Url]/_api/accounts(62d53214-9dfa-eb11-94ee-0022482230a8)/ myfileattribute
Headers:
Content-Type: application/octet-stream
Body :
Byte [ ]
```