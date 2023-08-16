---
title: "Power Apps Test Engine control support matrix (preview)"
description: Supported controls for the Power Apps Test Engine
author: jt000
ms.subservice: developer
ms.author: jasontre
ms.date: 08/11/2023
ms.reviewer: jdaly
ms.topic: article
contributors:
 - JimDaly
---

# Power Apps Test Engine control support matrix (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

## Overview

Power Apps Test Engine only supports a subset of the full list control supported in Power Apps. The support depends on if the control is [top-level ](#top-level)(i.e. not nested within a gallery or component), [nested within a gallery](#nested-in-a-gallery), or [nested within a component](#nested-in-a-component). Below you will find a list of controls and their support.

### Top Level

| Control | [Assert](powerfx.md#assert) | [Wait](powerfx.md#wait) | [SetProperty](powerfx.md#setproperty) | [Select](powerfx.md#select) |
| :--- | :---: | :---: | :---: | :---: |
| Address input | | | | n/a |
| Audio | | | | n/a |
| Barcode scanner | | | | n/a |
| Button | | | | |
| Camera | | | | |
| Business Card Reader | | | | n/a |
| Check box | | | | |
| Column chart | | | | |
| Combo box | | | | |
| Container | &#9747; | &#9747; | n/a | n/a |
| Data table | | | | n/a |
| Date picker | | | | |
| Drop down | | | | |
| Export Data | | | | |
| Gallery | | | | |
| HTML text | | | | |
| Icon | | | | |
| Image | | | | |
| Import | | | | |
| Line chart | | | | |
| List box | | | | |
| Map | | | &#9747; | |
| Measuring Camera | | | | |
| Microphone | | | | |
| PDF viewer | | &#9747; | n/a | n/a |
| Pen input | | | n/a | |
| Pie chart | | | | n/a |
| Radio | | | | |
| Rating | | | | |
| Rich text editor | | | | n/a |
| Shape | | | n/a | |
| Slider | | | | |
| Label | | | | |
| Text input | | | | |
| Timer | | | | |
| Toggle | | | | |
| Video | | | n/a | n/a |
| 3D Object | | | n/a | |
| View in MR | | | | |
| View shape in MR | | | | n/a |
| Add picture | n/a | n/a | n/a | |
| Edit form | n/a | n/a | n/a | n/a |
| Display form | n/a | n/a | n/a | n/a |
| Power BI tile | n/a | n/a | n/a | |
| Stream Video | n/a | n/a | n/a | n/a |

### Nested in a Gallery

| Control | [Assert](powerfx.md#assert) | [Wait](powerfx.md#wait) | [SetProperty](powerfx.md#setproperty) | [Select](powerfx.md#select) |
| :--- | :---: | :---: | :---: | :---: |
| Address input | | | | n/a |
| Audio | | | | n/a |
| Barcode scanner | | | | n/a |
| Button | | | | |
| Camera | | | | |
| Business Card Reader | | | | n/a |
| Check box | | | | |
| Column chart | &#9747; | &#9747; | &#9747; | &#9747; |
| Combo box | | | | |
| Container | &#9747; | &#9747; | n/a | n/a |
| Data table | n/a | n/a | n/a | n/a |
| Date picker | | | | &#9747; |
| Drop down | | | | &#9747; |
| Export Data | | | | &#9747; |
| Gallery | | | | |
| HTML text | | | | |
| Icon | | | | |
| Image | | | | &#9747; |
| Import | | | | &#9747; |
| Line chart | &#9747; | &#9747; | &#9747; | &#9747; |
| List box | | | | &#9747; |
| Map | n/a | n/a | n/a | n/a |
| Measuring Camera | | | | &#9747; |
| Microphone | | | | |
| PDF viewer | n/a | n/a | n/a | n/a |
| Pen input | | | n/a | |
| Pie chart | &#9747; | &#9747; | &#9747; | n/a |
| Radio | | | | |
| Rating | | | | &#9747; |
| Rich text editor | n/a | n/a | n/a | n/a |
| Shape | | | n/a | |
| Slider | | | | |
| Label | | | | |
| Text input | | | | |
| Timer | | | | |
| Toggle | | | | |
| Video | | | n/a | n/a |
| 3D Object | n/a | n/a | n/a | n/a |
| View in MR | | | | |
| View shape in MR | &#9747; | &#9747; | | n/a |
| Add picture | n/a | n/a | n/a | |
| Edit form | n/a | n/a | n/a | n/a |
| Display form | n/a | n/a | n/a | n/a |
| Power BI tile | n/a | n/a | n/a | |
| Stream Video | n/a | n/a | n/a | n/a |

### Nested in a Component

| Control | [Assert](powerfx.md#assert) | [Wait](powerfx.md#wait) | [SetProperty](powerfx.md#setproperty) | [Select](powerfx.md#select) |
| :--- | :---: | :---: | :---: | :---: |
| Address input | | | &#9747; | n/a |
| Audio | n/a | n/a | &#9747; | n/a |
| Barcode scanner | | | &#9747; | n/a |
| Button | | | &#9747; | |
| Camera | | &#9747; | &#9747; | |
| Business Card Reader | | | &#9747; | n/a |
| Check box | | | &#9747; | |
| Column chart | &#9747; | &#9747; | &#9747; | |
| Combo box | &#9747; | &#9747; | &#9747; | |
| Container | &#9747; | &#9747; | n/a | n/a |
| Data table | n/a | n/a | n/a | n/a |
| Date picker | &#9747; | &#9747; | &#9747; | |
| Drop down | | | &#9747; | |
| Export Data | | | &#9747; | |
| Gallery | | &#9747; | &#9747; | &#9747; |
| HTML text | | | &#9747; | |
| Icon | &#9747; | &#9747; | &#9747; | |
| Image | | &#9747; | &#9747; | |
| Import | | | &#9747; | |
| Line chart | &#9747; | &#9747; | &#9747; | |
| List box | | | &#9747; | |
| Map | | &#9747; | &#9747; | |
| Measuring Camera | | | &#9747; | |
| Microphone | | &#9747; | &#9747; | |
| PDF viewer | | &#9747; | n/a | n/a |
| Pen input | n/a | n/a | n/a | n/a |
| Pie chart | &#9747; | &#9747; | &#9747; | n/a |
| Radio | | | &#9747; | |
| Rating | | &#9747; | &#9747; | |
| Rich text editor | | | &#9747; | n/a |
| Shape | n/a | n/a | n/a | |
| Slider | | &#9747; | &#9747; | |
| Label | | | &#9747; | |
| Text input | | | &#9747; | |
| Timer | | &#9747; | &#9747; | |
| Toggle | &#9747; | &#9747; | &#9747; | |
| Video | | &#9747; | n/a | n/a |
| 3D Object | | | n/a | |
| View in MR | | | &#9747; | |
| View shape in MR | | | &#9747; | n/a |
| Add picture | n/a | n/a | n/a | |
| Edit form | n/a | n/a | n/a | n/a |
| Display form | n/a | n/a | n/a | n/a |
| Power BI tile | n/a | n/a | n/a | |
| Stream Video | n/a | n/a | n/a | n/a |

### See also

[Power Apps Test Engine overview (preview)](overview.md)   
[Power Apps Test Engine YAML format (preview)](yaml.md)   
[Power Apps Test Engine Power Fx functions (preview)](powerfx.md)