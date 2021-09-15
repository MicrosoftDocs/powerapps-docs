---
title: Template tags
description: Learn about template tags available in portal.
author: gitanjalisingh33msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 09/09/2021
ms.subservice: portals
ms.author: gisingh
ms.reviewer: tapanm
contributors:
    - tapanm-msft
    - GitanjaliSingh33msft
---

# Template tags

Template tags control the output of a template in various ways, and allow the combination of multiple templates into a single output.

## fetchxml

Allows user to query data from Microsoft Dataverse, and render the results in a page.

> [!NOTE]
> You can learn more about querying the data using fetchxml at [use FetchXML to query data](../../../developer/data-platform/use-fetchxml-construct-query.md).

```
{% fetchxml resultVariable %}
<!— Fetchxml query -->
...
{% endfetchxml %}
```

When using fetchxml to query data, ensure you don't use self-closing tags. For example, instead of `<attribute name="title"/>`, use `<attribute name="title"></attribute>` with explicit closure tag `</attribute>`.

### Results attribute

Results attribute in provided variable (such as 'resultVariable' in above sample) holds FetchXML query results and a few other attributes.

- *Entities*

    This attribute contains the result of fetchxml query. You can iterate the result and use it in your webtemplate.

    ```
    <table> 
    {% for entityVariable in resultVariable.results.entities %} 
    <tr> 
    <td>Attribut-1: {{ entityVariable.attribute1 }}</td> 
    <td>Attribut-2: {{ entityVariable.attribute2 }}</td> 
    </tr> 
    {% endfor %} 
    </table> 
    ```

- *TableName*

    Gets the logical name of the entity.

- *ExtensionData*

    Gets the structure that contains extra data.

- *MinActiveRowVersion*

    Gets the lowest active row version value.

- *MoreRecords*

    Gets whether there are more records available.

- *PagingCookie*

    Gets the current paging information.

- *TotalRecordCount*

    Gets the total number of records in the collection. <br/>
    ReturnTotalRecordCount was true when the query was executed.

- *TotalRecordCountLimitExceeded*

    Gets whether the results of the query exceeds the total record count.

### XML attribute

XML attribute in provided variable (such as 'resultVariable' in above sample) holds the resultant query which can be used to get data from Microsoft Dataverse. This attribute is useful for debugging purpose when you want to understand how table permission is getting applied on this *fetchxml* tag.  

### Other supported elements and attributes

fetchxml liquid tag supports the following attributes, and child elements.

| Element/Child element | Attributes | Child element |
| - | - | - |
| fetch | mapping <br> version <br> count  <br> page  <br> paging-cookie  <br> utc-offset  <br> aggregate  <br> distinct  <br> min-active-row-version  <br> output-format  <br> returntotalrecordcount  <br> no-lock | order <br> entity |
| order | attribute <br> alias <br> descending | |
| entity | name <br> all-attributes <br> no-attrs <br> attribute | order <br> filter <br> link-entity |
| filter | type <br> hint <br> isquickfindfields | condition <br> filter |
| link-entity | name <br> from <br> to <br> alias <br> link-type <br> visible <br> intersect <br> all-attributes <br> no-attrs <br> attribute | order <br> filter <br> link-entity |
| condition | column <br> entityname <br> attribute <br> operator <br> aggregate <br> alias <br> uiname <br> uitype <br> uihidden <br> value | value |

## include

Includes the contents of one template in another, by name. In Power Apps portals, the source of this other template will generally be a [web template](store-content-web-templates.md). This allows for the reuse of common template fragments in multiple places.  

When a template is included in another, the included template will have access to any variables defined in the parent template.

`{% include 'My Template' %}`

It's also possible to pass any number of named parameters to the include tag. These will then be defined as variables in the included template.

`{% include 'My Template' a:x, b:y %}`

## block

Used in conjunction with extends to provide template inheritance. See extends for usage.

## extends

Used in conjunction with the block tag, provides template inheritance. This allows multiple templates to use a shared layout, while overriding specific areas of the parent layout.

In Power Apps portals, the parent template name provided to the tag will generally refer to the name of a [web template](store-content-web-templates.md).  

When extends is used, it must be the first content in the template, and can only be followed by one or more block tags.

If a block defined in the parent template is not overridden, its contents in the parent template (if any) will be rendered.

## comment

Allows you to leave un-rendered code inside a Liquid template. Any content within the block will not be rendered, and any Liquid code within will not be executed.

**Code**

`Hello{% comment %}, {{ user.fullname }}{% endcomment %}. My name is Charles.`

**Output**

`Hello. My name is Charles.`

## raw

Allows output of Liquid code on a page without having it parsed and executed.

**Output**

`Hello, {{ user.fullname }}. My name is Charles.`

## substitution

When you enable the header and footer caching, and want to avoid caching of certain section output, you can use this tag. This tag provides the content block in header or footer where output of the wrapped content block doesn't get cached. This is helpful in the scenarios where user is using an object which can frequently get updated, such as request, page, language, and date. For example, refer to the header and footer web template source code update scenarios when [header and footer caching is enabled](../configure/enable-header-footer-output-caching.md).

> [!TIP]
> The URL used in [request.url](liquid-objects.md#request) can be any requested value, and gets [cached](../configure/enable-header-footer-output-caching.md) for subsequent requests. To ensure correct value in request.url, consider using substitution tag, partial URL such as ~\{WebFile path} or storing the portal URL in [Site Settings](../configure/configure-site-settings.md).

### See also

[Control flow tags](control-flow-tags.md)<br>
[Iteration tags](iteration-tags.md)<br>
[Variable tags](variable-tags.md)<br>
[Power Apps Dataverse entity tags](portals-entity-tags.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]