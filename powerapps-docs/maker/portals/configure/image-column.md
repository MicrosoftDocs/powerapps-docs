---
title: Configuring an image column on portals (preview)
description: Learn how to configure an image column on portals.
author: nageshbhat-msft

ms.topic: conceptual
ms.custom: 
ms.date: 04/05/2022
ms.subservice: portals
ms.author: nabha
ms.reviewer: ndoelman
contributors:
    - ProfessorKendrick
    - nickdoelman
---
# Configuring an image column on portals (preview)

>[!NOTE]
> - This is a preview feature.  Preview features aren't meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

You can configure image column fields on basic and advanced forms to upload, view, modify, and delete images. Image column allows you to store an image file up to the specified maximum size in Dataverse table columns. The thumbnail images can be seen in the web application when viewing the form data.

:::image type="content" source="media/image-column/edit-image.png" alt-text="Navigating the edit image functionality.":::

## Enable image control on forms

You must configure site settings **Control/EnableImagePreview** and set its value to **true** to enable **Image** controls on the form. You don't require to make any configuration to make image column with Liquid code and Web API.

:::image type="content" source="media/image-column/image-preview.png" alt-text="Enable image preview.":::

>[!IMPORTANT]
> This site setting is only required during the preview period.

## Image URL

An absolute URL to display the entity image in a client

The URL is composed in following way

 ```{0}/Image/download.aspx?entity={1}&attribute={2}&id={3}``` 

0 – Portal url

1 – entity logical name

2 – column logical name

3 – image ID

## Liquid

Developers can design the website by using Liquid code to retrieve the records from Dataverse tables. Image column values can be fetched while data being queried by using fetchXML and entity view

```
    {% for item in tables.results.entities %}
        {{ item.columnname.Type }}
        {{ item.columnname.Size }}
        {{ item.columnname.Url }}
        {{ item.columnname.Value }}
    {% endfor %}
```

| Type  | Mime type of the image       |
|-------|------------------------------|
| Size  | Image size in bytes          |
| Value | Image value in base64 string |
| Url   | Image url                    |

### Example: Retrieve default contact image

> [!NOTE]
> Make sure you have configured the appropriate table permissions on the contact table to read the record.

```
    {% fetchxml contacts %}
        <fetch version="1.0" output-format="xml-platform" mapping="logical" distinct="false">
            <entity name="contact">
                <attribute name="fullname">
                <attribute name="entityimage">
            </entity>
        </fetch>
    {% endfetchxml %}

    {% for item in contacts.results.entities %}
        {
            "Full Name":"{{ item.fullname }}"
            "Entity Image Url":"{{ item.entityimage.Url}}",
            "Entity Image Size":"{{ item.entityimage.Size}}",
            "Entity Image Type":"{{ item.entityimage.Type}}",
            "Entity Image Value":"{{ item.entityimage.Value}}"
        }
    {% endfor %}
```


## Web API

The portals Web API can be used to perform, create, read, update, and delete operations on image columns across Microsoft Dataverse tables.

## Retrieving image data

To download thumbnail image data, use following APIs

```
    GET /_api/<entity-type>(id)/<image-attribute-name>/$value
```

Image data transfers from the web service endpoints are limited to a maximum of 16-MB data in a single service call.

### Example: Thumbnail download

#### Request

**HTTP** 
```
    GET [Portal Url]/_api/accounts(62d53214-9dfa-eb11-94ee-0022482230a8)/entityimage/$value
    
    Headers:
    Content-Type: application/octet-stream
``` 

#### Response

**HTTP**
```
    204 No Content
    
    Body:
    Byte[ ]
```

## Upload image data

To upload the images, set the value of the image column to a byte array that contains the content of the image file:

```
    PUT or PATCH /_api<entity-type>(id)/<image-attribute-name>
```

### Example: image upload

#### Request

```
    PUT [Portal Url]/_api/accounts(62d53214-9dfa-eb11-94ee-0022482230a8)/entityimage

    Headers:
    Content-Type: application/octet-stream
    
    Body :
    Byte [ ]
```