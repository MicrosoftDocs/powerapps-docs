---
title: "Use variable tags for a portal | MicrosoftDocs"
description: "Learn about variable tags available in portal"
author: sbmjais
manager: shujoshi
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/07/2019
ms.author: shjais
ms.reviewer:
---

# Variable tags

Variable tags are used to create new Liquid variables.

## assign

Creates a new variable. Assignments can also use [filters](liquid-filters.md) to modify the value.  

**Code**

```
{% assign is_valid = true %}

{% if is_valid %}

It is valid.

{% endif %}

{% assign name = dave bowman' | upcase %}

{{ name }}
```

**Output**

```
It is valid.

DAVE BOWMAN
```

## capture

Captures the content within its block and assigns it to a variable. This content can then be rendered later by using output tags.

**Code**

```
{% capture hello %}Hello, {{ user.fullname }}.{% endcapture %}

{{ hello }}

{{ hello }}
```

**Output**

```
Hello, DAVE BOWMAN.

Hello, DAVE BOWMAN.
```

### See also

[Control flow tags](control-flow-tags.md)<br>
[Iteration tags](iteration-tags.md)<br>
[Template tags](template-tags.md)<br>
[PowerApps common data service entity tags](portals-entity-tags.md)
