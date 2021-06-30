---
title: Variable tags
description: Learn about variable tags available in portal.
author: gitanjalisingh33msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2020
ms.author: gisingh
ms.reviewer: tapanm
contributors:
    - tapanm-msft
    - GitanjaliSingh33msft
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
[Dataverse entity tags](portals-entity-tags.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]