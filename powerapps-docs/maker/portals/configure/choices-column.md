---
title: Configure a choices column for portals
description: Learn how to add and configure a Dataverse choices column on portal lists, forms, and templates.
author: nageshbhat-msft

ms.topic: conceptual
ms.custom: 
ms.date: 12/09/2021
ms.subservice: portals
ms.author: nabha
ms.reviewer: ndoelman
contributors:
    - nageshbhat-msft
    - nickdoelman
---

# Configure a choices column on portals (preview)

> [!Important]
> - This is a preview feature.
> - Preview features aren't meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback.

Makers can design [basic forms](entity-forms.md) and [advanced forms](web-form-properties.md) to include [choices columns](../../data-platform/types-of-fields.md#choices) defined in Microsoft Dataverse. This feature provides the ability for portal users to select multiple options while submitting data, and display views that include choices columns through [lists](entity-lists.md).

## Prerequisites

- Your portal must be version [9.3.11.x](/power-platform/released-versions/portals/portalupdate9311x) or later to use this feature.

## Enable choices control

To enable choices controls on forms in your portal, you need to create a new [site setting](configure-site-settings.md) with the name **Control/EnableChoices** and set the value to **true**.

:::image type="content" source="media/choices-column/site-setting.png" alt-text="Control/EnableChoices site setting.":::

> [!IMPORTANT]
> This site setting is only required during the preview period.

## Basic forms and advanced forms

You can design a [basic form](entity-forms.md) or an [advanced form](web-form-properties.md) step in the portal website by using a Dataverse form that has a choices column to support the selection of multiple options. Portal users can insert, modify, or clear the selection.

:::image type="complex" source="media/choices-column/choices-form.gif" alt-text="Choices column on a form.":::
Screen showing a list of outdoor activities being created. The user expands the Select or search options box and selects some activities from the list that appears. The selected activities appear at the top of the window. The user enters the letters C a m in the box, and then selects the option Camping when it appears. At the top of the window in the list of activities, the user selects the Close button next to one of the options to deselect it.
:::image-end:::

## List

You can define a choices column in a Dataverse view to display the multiple options that are available for the record in a list. The choices column supports quick search by typing a keyword to filter the list.

:::image type="content" source="media/choices-column/choices-list.png" alt-text="Choices column on a list.":::

> [!NOTE]
> Sorting a [list](entity-lists.md) by the choices column isn't supported.

## Liquid

Developers can design the website by using Liquid to retrieve the records from a Dataverse table. Choices columns can be retrieved while the data is being queried by using fetchXML or an entity view.

```html
{% for choice in record.ChoicesColumn %}
    {{ choice.Label }}
    {{ choice.Value }}
{% endfor %} 
```

Examples of choices for *sample\_outdooractivities* values are shown in the following table.

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

Examples of contact table values are shown in the following table.

| **'fullname' column** | **'Sample\_outdooractivities' column** |
|-----------------------|----------------------------------------|
| Quinn Yarborough      | 1,9                                    |
| Avery Orton           | 2                                      |
| Yuri Maple            | 4                                      |
| Ravi Mundy            | 2,3,8,9                                |

### Retrieve selected options by using fetchXML

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

### Retrieve selected options by using an entity view

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

## Web API 

Developers can use choices columns by using the [Web API](../web-api-overview.md) read, create, and update operations.

<u>Read</u>

`GET \[Portal URI]\_api/contacts?$select=fullname,sample\_outdooractivities &$top=1`

Response –

```html
{
"value": [
    {
    "@odata.etag": "W/\\"1066412\\"",
    "fullname":" Quinn Yarborough ",
    "sample\_outdooractivities ":"1,9",
    "sample\_outdooractivities @OData.Community.Display.V1.FormattedValue":"Swimming, Camping"
    }
    ]
}
```

<u>Create / Edit</u>

Method – PATCH / PUT

`\[Portal URI]\_api/contacts (guid)`

Body –

```html
{
"sample\_outdooractivities": "1,4,8",
}
```

## Known issues

The choices control on basic and advanced forms currently only supports the default theme. If you're using any of the [preset themes](../theme-overview.md) defined in Power Apps portals Studio, the choices control won't be available.

 
[!INCLUDE[footer-include](../../../includes/footer-banner.md)]