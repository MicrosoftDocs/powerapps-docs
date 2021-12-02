---
title: Configure choices column for portal
description: Learn how to add and configure Dataverse choices column on portal lists, forms, and templates.
author: GitanjaliSingh33msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 12/02/2021
ms.subservice: portals
ms.author: nabha
ms.reviewer: ndoelman
contributors:
    - nickdoelman
---

# Configure choices column on portals (preview)

Makers can design [basic forms](entity-forms.md) and [advanced forms](web-form-properties.md) to include [choices columns](../../../data-platform/types-of-fields.md#choices) defined in Microsoft Dataverse to provide the ability for portal users to select multiple options while submitting data, and display views with choices columns through [lists](entity-lists.md).

<!-- ND - Do we have a screen shot to add here? -->

## Allow Read access to a Web Resource table

Displaying choices control on form requires **read** permission to be set on the **Web Resource** table.

To configure read access on the web resource table:

1. Open the [Portal Management](configure-portal.md) app.

1. On the left pane, select **Table Permission**.

1. Select **New**.

1. Enter **Name.**

1. Select *Web Resource (webresource)* for **Table Name**.

1. Select your website record.

1. Select *Global* for **Scope.**

1. In **Privileges**, select *Read*.

1. Select **Save**.

1. Under the **Web Roles** section, select **Add Existing Web Role**.

1. Select the web role for the users that should see the code component in portals.

    For example, **Anonymous Users** for anonymous users, **Authenticated Users** for users authenticated by portals, or a custom web role.

1. Select **Save & Close**.

Once you add the basic form to a webpage, users assigned to the selected web role can now see the **Choices** control on the portal page.

## Basic forms and advanced forms

Maker can design the advanced form step in portal website using Dataverse form having the choices column to support selection of multiple options. Portal users can insert, modify, or clear the selection. More details on [basic forms](entity-forms.md) and [advanced forms](web-form-properties.md) configuration available in respective documentation

## List

Choices column defined in Dataverse view to display the multiple options selected for the record in a list. Choices column support quick search by typing keyword to filter the list.

> [!NOTE]
> Sorting [list](entity-lists.md) by choices column is not supported.

## Liquid

Developers can design the website using Liquid to retrieve the records from a Dataverse table. Choices column support available while querying the data using fetchXML and entity view.

```html
{% for choice in record.ChoicesColumn %}
    {{ choice.Label }}
    {{ choice.Value }}
{% endfor %} 
```
Example:

Choices *sample\_outdooractivities* values

| **Value** | **Label**         |
|-----------|-------------------|
| 1         | Swimming          |
| 2         | Hiking            |
| 3         | Mountain Climbing |
| 4         | Fishing           |
| 5         | Hunting           |
| 6         | Running           |
| 7         | Boating           |
| 8         | Skiing            |
| 9         | Camping           |

Contact table values

| **'fullname' column** | **'Sample\_outdooractivities' column** |
|-----------------------|----------------------------------------|
| Quinn Yarborough      | 1,9                                    |
| Avery Orton           | 2                                      |
| Yuri Maple            | 4                                      |
| Ravi Mundy            | 2,3,8,9                                |

Retrieve Selected Options using FetchXML

```html
{% fetchxml contacts %}
    <fetch version="1.0" output-format="xml-platform" mapping="logical" distinct="false">
        <entity name="contact">
            <attribute name="firstname" >
            <attribute name="lastname" >
            <attribute name="sample_outdooractivities" >
        </entity>
    </fetch>
{% endfetchxml %}
{% for item in contacts.results.entities %}
{
    "First Name":"{{ item.firstname }}",
    "Last Name":"{{ item.lastname }}",
    "Outdoor Activities": [
        {% for choice in item.sample_outdooractivities %}
            {{choice.Label}},
        {% endfor %}
    ]
}
{% endfor %}
```
Retrieve Selected Options using Entity View

```html
{% entitylist id:page.adx_entitylist.id %}
{% for e in entityview.records -%}
    {
    "First Name":"{{ e.firstname }}",
    "Last Name":"{{ e.lastname }}",
    "Outdoor Activities": [
    {% for choice in e. sample_outdooractivities %}
        {{choice.Label}},
    {% endfor %}
    ]
    }
{% endfor -%}
```

## Web api 

Choices column supports [Web API](../web-api-overview.md) read, create, update operations

<u>Read</u>

`GET \[Portal URI\]/\_api/contacts?$select=fullname,sample\_outdooractivities &$top=1`

Response –

```html
{
"value": \[
    {
    "@odata.etag": "W/\\"1066412\\"",
    "fullname":" Quinn Yarborough ",
    "sample\_outdooractivities ":"1,9",
    "sample\_outdooractivities @OData.Community.Display.V1.FormattedValue":"Swimming, Camping"
    }
    \]
}
```

<u>Create / Edit</u>

Method – PATCH / PUT

`\[Portal URI\]/\_api/contacts (guid)`

Body –

```html
{
"sample\_outdooractivities": "1,4,8",
}
```

> [!NOTE]
> Choices control on basic and advanced form support default theme. If you are using any of the [preset theme](../theme-overview.md) defined in portals Studio, your starter portal package must be 9.2.2112.x or higher

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]