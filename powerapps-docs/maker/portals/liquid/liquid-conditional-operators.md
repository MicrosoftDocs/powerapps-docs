---
title: Available Liquid conditional operators
description: Learn about the available liquid conditional operators in a portal.
author: gitanjalisingh33msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2020
ms.subservice: portals
ms.author: gisingh
ms.reviewer: tapanm
contributors:
    - tapanm-msft
    - GitanjaliSingh33msft
---

# Available Liquid conditional operators

When used in conditional statements (**if**,**unless**), some Liquid values will be treated as true, and some will be treated as false.

In Liquid, null and the Boolean value false are treated as false;everything else is treated as true. Empty strings, empty arrays, etc. are treated as true. For examples,

```
{% assign empty_string = "" %}
{% if empty_string %}
<p>This will render.</p>
{% endif %}
```
You can test for empty strings and arrays using the special value empty if necessary.

```
{% unless page.title == empty %}
<h1>{{ page.title }}</h1>
{% endunless %}
```
You can also test the size of [Liquid types](liquid-types.md), [Liquid types](liquid-types.md), or [Liquid types](liquid-types.md) using the special size property.

```
{% if page.children.size > 0 %}
<ul>
{% for child in page.children %}
<li>{{ child.title }}</li>
{% endfor %}
</ul>
{% endif %}
```

## Summary

|   Operator                        | True | False |
|---------------------------|------|-------|
| True                      | ×    |       |
| False                     |      | ×     |
| Null                      |      | ×     |
| String                    | ×    |       |
| empty string              | ×    |       |
| 0                         | ×    |       |
| 1, 3.14                   | ×    |       |
| array or dictionary       | ×    |       |
| empty array or dictionary | ×    |       |
| Object                    | ×    |       |

### See also

[Store source content by using web templates](store-content-web-templates.md)  
[Understand Liquid operators](liquid-operators.md)  
[Liquid types](liquid-types.md)  
[Liquid Objects](liquid-objects.md)  
[Liquid Tags](liquid-tags.md)  
[Liquid Filters](liquid-filters.md)  


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]