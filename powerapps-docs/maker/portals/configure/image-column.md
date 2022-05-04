---
title: Configure an image column on portals (preview)
description: Learn how to configure an image column on portals.
author: nageshbhat-msft
ms.topic: conceptual
ms.custom: 
ms.date: 05/04/2022
ms.subservice: portals
ms.author: nabha
ms.reviewer: ndoelman
contributors:
    - ProfessorKendrick
    - nickdoelman
---

# Configure an image column on portals (preview)

[!INCLUDE [cc-preview-features-definition](../../../includes/cc-preview-features-definition.md)]

An image column stores an image file in a column in a Dataverse table. Add an image column to a form to upload, view, modify, and delete images. The form shows a thumbnail of the image if one is available.

## Prerequisites

- **If you configure your site using the Portal Management app:** While the feature is in preview, you'll need to set the value of the site setting **Control/EnableImagePreview** to **true** to add image controls to a form.

    :::image type="content" source="media/image-column/upload-image-preview.png" alt-text="Screenshot of the Control/EnableImagePreview site setting.":::

    >[!IMPORTANT]
    > This site setting is only required during the preview period.

- **If you use [Liquid code](#liquid) or the [Web API](#web-api):** There's nothing more you need to do to add image controls to a form.

## Image URL

The image URL indicates the full URL of where the image is stored.  This can be used for development and troubleshooting.

An image URL takes the following form:

 ```{0}/Image/download.aspx?entity={1}&attribute={2}&id={3}```

where:

- **{0}** is the portal URL

- **{1}** is the logical name of the entity

- **{2}** is the logical name of the column

- **{3}** is the image ID

For example, if your portal is located at https://contososite.com, your code will look like this:

``` 
https://contososite.powerappsportals.com/Image/download.aspx?entity=contact&attribute=entityimage&id=cb059a4a-b1a6-ec11-9840-00224829604e
```


## Liquid

You can design a website using [Liquid code](../liquid/liquid-overview.md) to retrieve records from Dataverse tables. Use fetchXML and the **Entity** view to fetch image column values, like this:

```xml
    {% for item in tables.results.entities %}
        {{ item.columnname.Type }}
        {{ item.columnname.Size }}
        {{ item.columnname.Url }}
        {{ item.columnname.Value }}
    {% endfor %}
```

where:

- **Type** is the mime type of the image

- **Size** is the image size in bytes

- **Value** is the image value as a base64 string

- **Url** is the image URL

### Example: Retrieve a default contact image

> [!NOTE]
> Make sure you have [set the appropriate permissions](#create-a-table-permission) on the contact table to read the record.

```xml
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
            "Entity Image Type":"{{ item.entityimage.Type}}",
            "Entity Image Size":"{{ item.entityimage.Size}}",
            "Entity Image Url":"{{ item.entityimage.Url}}",
            "Entity Image Value":"{{ item.entityimage.Value}}"
        }
    {% endfor %}
```

## Web API

The [portals Web API](../web-api-overview.md) can be used to create, read, update, and delete images in image columns across Dataverse tables.

### Retrieve image data

To download thumbnail image data, use the following API call:

```html
    GET /_api/<entity-type>(id)/<image-attribute-name>/$value
```

Image data transferred from the web service endpoints is limited to a maximum of 16 MB in a single service call.

#### Example: Download a thumbnail

In the following example, we'll use a GET call to download a thumbnail if it exists.

HTTP request:

```html
    GET [Portal Url]/_api/accounts(62d53214-9dfa-eb11-94ee-0022482230a8)/entityimage/$value
    
    Headers:
    Content-Type: application/octet-stream
```

HTTP response:

```html
    204 No Content
    
    Body:
    Byte[ ]
```

In this example, the thumbnail doesn't exist and so no image is returned. If a thumbnail did exist, the response would return a byte array with values.

### Upload image data

To upload an image, set the value of the image column to a byte array that contains the content of the image file:

```html
    PUT or PATCH /_api<entity-type>(id)/<image-attribute-name>
```

#### Example: Upload an image

HTTP request:

```html
    PUT [Portal Url]/_api/accounts(62d53214-9dfa-eb11-94ee-0022482230a8)/entityimage

    Headers:
    Content-Type: application/octet-stream
    
    Body :
    Byte [ ]
```

### Upload profile images

Authenticated portal users can upload their picture in the profile section of the portal. The image is saved in the **Entity Image** column of the corresponding contact record in Dataverse. Users can upload images up to 10 MB.

#### Create site settings

First, you must create a site setting to allow authenticated users to upload a profile picture:

1. Sign in to [Power Apps](https://make.powerapps.com/).

1. Select the environment that contains your portal.

1. In the left pane, select **Apps**, and then open the **Portal Management** app.

    :::image type="content" source="media/image-column/add-settings-site.png" alt-text="Screenshot of the Apps list, with the Portal Management app highlighted.":::

1. In the left pane, select **Site Settings**.

1. Create a setting called **Profile/ShowImage**, and set its value to **true**. (If the setting exists, set its value to **true**.)

    :::image type="content" source="media/image-column/add-setting-showimage.png" alt-text="Screenshot of the Profile/ShowImage site setting.":::

While the feature is in preview, also add or update the following site settings:

- Set **Webapi/contact/enabled** to **true**.

- Set **Webapi/contact/fields** to **entityimage**.

:::image type="content" source="media/image-column/add-settings-webapi.png" alt-text="Screenshot of the webapi site settings.":::

#### Create a table permission

Next, you must create a table permission to allow authenticated users to upload a profile picture:

1. In the left pane, under **Security**, select **Table Permissions**, and then select **New**.

    :::image type="content" source="media/image-column/add-table-permission.png" alt-text="Screenshot of the Active Table Permissions view, with New highlighted.":::

1. Set the permission details as follows:

    - Enter a meaningful name for the permission. In our example, we've entered "Contact Profile Update Permission."

    - In the **Table Name** list, select **Contact (contact)**.

    - In **Website**, search for and select the name of your portal.

    - In the **Access Type** list, select **Self**.

    - Under **Privileges**, select **Read**, **Write**, **Append**, and **Append To**.

    :::image type="content" source="media/image-column/add-table-permission-details.png" alt-text="Screenshot of the details of a new table permission called Contact Profile Update Permission.":::

1. Select **Save & Close**.

1. In the **Active Table Permissions** view, select **Contact Profile Update Permission** (or whatever you named your new permission).

1. In the **Web Roles** section, select **Add Existing Web Role**.

1. Search for and select **Authenticated Users**, and then select **Add**.

    :::image type="content" source="media/image-column/add-auth-users-web-role.png" alt-text="Screenshot that shows Authenticated Users selected as a web role.":::
