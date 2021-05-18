---
title: ReadNFC function | Microsoft Docs
description: Reference information, including syntax, for the ReadNFC function in Power Apps
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 05/18/2021
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# ReadNFC function in Power Apps
Reads a Near Field Communication (NFC) tag.

## Description
Use **ReadNFC** to read an NFC tag that is in close proximity to your device.  When invoked, the screen will display directions for scanning an NFC tag, and will only return after a tag has been scanned or a timeout expires.  

**ReadNFC** returns a record of information about the tag that has been read.  The record contains:

| Field | Type | Description |
|----|----|----|
| **RTD** | Text | The tag's Record Type Definition (RTD).  Only RTD_TEXT and RTD_URI are supported at this time. |
| **TNF** | Number | The tag's Type Name Format (TNF). Only TNF_WELL_KNOWN is supported at this time.  |
| **Text** | Text | The text payload of the NFC tag if RTD is RTD_TEXT, *blank* otherwise.   | 
| **URI** | Hyperlink | The URI payload of the NFC tag if RTD is RTD_URI, *blank* otherwise.  |

If the tag is not supported, for example the TNF is not TNF_WELL_KNOWN, or the scan timeoud out, then the record itself will be *blank* (and all fields will be *blank* too).

Always check the payload value for *blank* using the [**IsBlank**](function-isblank-isempty.md) function before using it.  You do not need to check the **RTD** and **TNF** values yourself as they must be the correct values for **Text** and **URI** to have a non *blank* value.

Additional **RTD** and **TNF** values may be supported in the future.  If more values are supported, additional payload fields will also be added.  The raw **RTD** and **TNF** values are provided for informational purposes.  Information about these values and their use is available through the [NFC Forum](https://nfc-forum.org) and many other books and articles on NFC.

If NFC is not supported on the device, a message will be shown to the user and the function will return a *blank* record. 

**ReadNFC** can only be used in [behavior formulas](../working-with-formulas-in-depth.md).

## Syntax
**ReadNFC**()

## Examples

Reads an NFC tag and displays the result.  If the result is Text or URI, displays that value to the user.  The [**With**](function-with.md) function is used to make the fields of the return record easily accessible.  

```powerapps-dot
With( ReadNFC(), 
      If( Not IsBlank( Text ), 
            Notify( "Read Text: " & Text ), 
          Not IsBlank( URI ),
            Notify( "Read URI: " & URI ),
          Notify( "Didn't read Text or URI" )
      )
)
```

Reads an NFC tag and displays type information about the result.

```powerapps-dot
With( ReadNFC(), Notify( "Tag TNF: " & TNF & ", RTD: " & RTD ) )
```

Collects read NFC tags for later use.

```powerapps-dot
Collect( ScannedTags, ReadNFC() )
```

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]