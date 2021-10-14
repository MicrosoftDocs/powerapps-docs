---
title: Available Liquid types
description: Learn about the available liquid types in a portal.
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

# Available Liquid types

Liquid objects can return one of seven basic types: **String**, **Number**, **Boolean**, **Array**, **Dictionary**, **DateTime**, or **Null**. Liquid variables can be initialized by using the **assign** or **capture** tags.

## String

A String is declared by wrapping text in single or double quotes.

```
{% assign string_a = "Hello World!" %}

{% assign string_b = 'Single quotes work too.' %}
```

Get the number of characters in a string with the size property.

```
{{ string_a.size }} <!-- Output: 12 -->
```

## Number

Numbers can be integers or floats.

```
{% assign pi = 3.14 %}

{% if page.title.size > 100 %}

This page has a long title.

{% endif %}
```

## Boolean

A Boolean is either true or false.

```
{% assign x = true %}

{% assign y = false %}

{% if x %}

This will be rendered, because x is true.

{% endif %}
```

## Array

An array holds a list of values of any type. You can access a given item by (zero-based) index using \[ \], iterate over them using the **for tag**, and get the number of items in the array using the size property.

```
{% for view in entitylist.views %}

{{ view.name }}

{% endfor %}

{{ entitylist.views[0] }}

{% if entitylist.views.size > 0 %}

This list has {{ entitylist.views.size }} views.

{% endif %}
```

## Dictionary

Dictionaries hold a collection of values that can be accessed by a string key. You can access a given item by string key using \[ \], iterate over them using the **for tag**, and get the number of items in the dictionary using the size property.

```
{{ request.params[ID] }}

{% if request.params.size > 0 %}

The request parameters collection contains some items.

{% endif %}
```

## DateTime

A DateTime object represents a specific date and time.

```
{{ page.modifiedon | date: 'f' }}
```

## Null

Null represents an empty or non-existent value. Any outputs that attempt to return a null value will render nothing. It will be treated as false in conditions.

```
{% if request.params[ID] %}

This will render if the ID request parameter is NOT null.

{% endif %}
```

### See also

[Store source content by using web templates](store-content-web-templates.md)  
[Understand Liquid operators](liquid-operators.md)  
[Conditional](liquid-conditional-operators.md)  
[Liquid Objects](liquid-objects.md)  
[Liquid Tags](liquid-tags.md)  
[Liquid Filters](liquid-filters.md)  


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]