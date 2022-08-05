---
title: Configure a file column on portals (preview)
description: Learn how to configure a file column to store binary data on portals.
author: nageshbhat-msft
ms.topic: conceptual
ms.custom: 
ms.date: 08/05/2022
ms.subservice: portals
ms.author: nabha
ms.reviewer: ndoelman
contributors:
    - ProfessorKendrick
    - nickdoelman
---

# Configure a file column on portals (preview)

[This topic is pre-release documentation and is subject to change.]

A file column is used for storing binary data. This column is primarily used to store a single file, note, or attachment; however, it's possible to store other forms of binary data. You can configure a file column on basic and advanced forms to provide the capability to upload, view, modify, or delete the file. The file column can store files up to the specified maximum size of a Microsoft Dataverse table column.

:::image type="content" source="media/file-column/file-upload.gif" alt-text="Animation of a table with fields for Product Number, Product Name,and Product Catalogue. To populate the Product Catalogue field, the user selects Choose File and then browses to a PDF file to upload and use for the Product Catalogue.":::

> [!NOTE]
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../../includes/cc-preview-features-definition.md)]
> - This feature is available with portals website version [9.4.7.xx](/power-platform/released-versions/portals/portalupdate947x).

## Enable the file control on form

You must configure the site setting **Control/EnableFilePreview** and set its value to **true** to enable file controls on the form. You don't have to make any configuration to use file columns with Liquid code or Web API.

:::image type="content" source="media/file-column/enable-file-preview.png" alt-text="Site settings menu for enabling file preview, with the value set to true.":::

> [!IMPORTANT]
> - This site setting is required during the preview period.
> - You can't upload a file by using **Insert** mode on a basic form or an advanced form step.

## Liquid code

Liquid is an open-source template language that's integrated natively into Microsoft Power Apps portals. Developers can retrieve file column values when they query data by using fetchXML and entity view.

```
{% for item in tables.results.entities %}
    {{ item.columnname.Name }}
    {{ item.columnname.Size }}
    {{ item.columnname.Url }}
{% endfor %}
```

| Attribute | Description | 
|-----|-----|
| Name | The name of the file associated with the column |
| Size | File size, in bytes |
| URL  | File download URL |

### Example: Retrieve file column data from a contact table

Create a new file data type column in [Dataverse](../../data-platform/create-edit-field-portal.md#create-a-column) for a contact table with the name **myfileattribute**.

> [!NOTE]
> Make sure you've configured the appropriate table permission on the contact table to read the record.

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
        "Entity File Url":"{{ item.myfileattribute.Name }}",      
        "Entity File Size":"{{ item.myfileattribute.Size }}",
        "Entity File Type":"{{ item.myfileattribute.Url }}" 
{% endfor %}
```

## Web API

Portals Web API can be used to perform create, read, update, and delete operations on file columns across Dataverse tables.

> [!NOTE]
> Make sure you've configured the appropriate Web API [site settings](../web-api-overview.md#site-settings-for-the-web-api) for the tables and file columns you want to access.

### Retrieving file data

To retrieve file data, use the API request described in the following examples.

```
GET /_api/<entity-type>(id)/<file-attribute-name>/$value
```

File data transfers from the web service endpoints are limited to a maximum of 16 MB of data in a single service call. File data that exceeds 16 MB must be divided into 4-MB or smaller data blocks (chunks), where each block is received in a separate API call until all file data has been received. It's your responsibility to join the downloaded data blocks to form the complete data file, by combining the data blocks in the same sequence as the blocks were received.

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

To upload the file, set the value of the file column to a byte array that contains the content of the file.

```
PUT or PATCH /_api/<entity-type>(id)/<file-attribute-name>
```

#### Example: File upload

##### Request

```
HTTP
PUT [Portal Url]/_api/accounts(62d53214-9dfa-eb11-94ee-0022482230a8)/myfileattribute
Headers:
Content-Type: application/octet-stream
Body :
Byte [ ]
```
