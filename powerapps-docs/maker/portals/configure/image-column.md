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
---
# Configuring an image column on portals (preview)

>[!NOTE]
> - This is a preview feature.  Preview features aren't meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

Portals maker can configure image column fields on Basic and Advanced forms to upload, view, modify and delete the images. Image column provides storing image file up to the specified maximum size in Microsoft Dataverse table column. The thumbnail images can be seen in the web application when viewing the form data.

:::image type="content" source="media/image-column/edit-image.png" alt-text="Navigating the edit image functionality.":::

## Enable Image control on form

You must configure site settings **Control/EnableImagePreview** and set its value to **true** to enable **Image** controls on the form. You don't require to make any configuration to make image column with Liquid code and Web API.

:::image type="content" source="media/image-column/image-preview.png" alt-text="Enable image preview.":::

>[!IMPORTANT]
> This site setting is only required during the preview period.

## Image URL

An absolute URL to display the entity image in a client

The URL is composed in following way

|                                                         |
|---------------------------------------------------------|
| ```{0}/Image/download.aspx?entity={1}&attribute={2}&id={3}``` |

0 – Portal url

1 – entity logical name

2 – column logical name

3 – image ID

## Liquid

Developers can design the website by using Liquid code to retrieve the records from Dataverse tables. Image column values can be fetched while data being queried by using fetchXML and entity view

| ```{% for item in tables.results.entities %}</br>{{ item.columnname.Type }}</br>{{ item.columnname.Size }}</br>{{ item.columnname.Url }}</br>{{ item.columnname.Value }}</br>{% endfor %}``` |
|-------------------------|

| Type  | Mime type of the image       |
|-------|------------------------------|
| Size  | Image size in bytes          |
| Value | Image value in base64 string |
| Url   | Image url                    |

Example: Retrieve default contact image

Note: Make sure you have configured appropriate table permission on contact table to read the record

| ```{% fetchxml contacts %}</br>&lt;fetch version="1.0" output-format="xml-platform" mapping="logical" distinct="false"&gt;</br>&lt;entity name="contact"&gt;</br>&lt;attribute name="fullname" /&gt;</br>&lt;attribute name="entityimage" /&gt;</br>&lt;/entity&gt;</br>&lt;/fetch&gt;</br>{% endfetchxml %}</br>{% for item in contacts.results.entities %}</br>{</br>"Full Name":"{{ item.fullname }}"</br>"Entity Image Url":"{{ item.entityimage.Url}}",</br>"Entity Image Size":"{{ item.entityimage.Size}}",</br>"Entity Image Type":"{{ item.entityimage.Type}}" ,</br>"Entity Image Value":"{{ item.entityimage.Value}}"</br>}</br>{% endfor %}``` |
|-------------------------|

## Web API

Portals Web API can be used to perform, create, read, update, and delete operations on image columns across Microsoft Dataverse tables.

## Retrieving image data

To download thumbnail image data, use following APIs

|                                                                        |
|------------------------------------------------------------------------|
| ```GET /\_api/&lt;entity-type&gt;(id)/&lt;image-attribute-name&gt;/$value``` |

Image data transfers from the web service endpoints are limited to a maximum of 16-MB data in a single service call.

### Example: Thumbnail download

#### Request

| HTTP |
|-------------------------|
| ```GET [Portal Url]/_api/accounts(62d53214-9dfa-eb11-94ee-0022482230a8)/entityimage/$value</br>Headers:</br>Content-Type: application/octet-stream``` |

#### Response

| HTTP |
|-------------------------|
| ```204 No Content</br>Body:</br>Byte[ ]``` |

## Upload image data

To upload the images, set the value of the image column to a byte array that contains the content of the image file

|                                                                          |
|--------------------------------------------------------------------------|
| ```PUT or PATCH /\_api/&lt;entity-type&gt;(id)/&lt;image-attribute-name&gt;``` |

### Example: image upload

#### Request

| HTTP |
|-------------------------|
| ```PUT [Portal Url]/_api/accounts(62d53214-9dfa-eb11-94ee-0022482230a8)/entityimage</br>Headers:</br>Content-Type: application/octet-stream</br>Body :</br>Byte [ ]``` |