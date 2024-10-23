---
title: Source Code files for Canvas apps (pa.yaml)
description: Learn about Source Code files for canvas apps.
author: marcelbf
ms.author: marcelbf
ms.date: 10/17/2024
ms.topic: conceptual
ms.reviewer: 
ms.subservice: canvas-maker
ms.collection: get-started
search.audienceType: 
  - maker  
ms.custom:
  - canvas  
---

# Source Code files for Canvas apps (preview)

In this article, you'll learn about the source code files of a canvas app.

We use YAML as our language. There are already a large number of editors, tools, and libraries for manipulating YAML. YAML is also human-readable. 

>[NOTE]
> We support only a restricted subset of YAML. Only the constructs described in this document are supported.

## How to access the Source Code files

Source code for Canvas Apps is represented as pa.yaml files.

You can [export your canvas app as a .msapp file](../canvas-apps/export-import-single-app.md#export-msapp-files-in-power-apps). A msapp file is collection of files compacted in a binary file, including the source code.

You can extract the files using Power Platform CLI 

In the extracted msapp, only files within the directory \src are source code files intented to be used with source control.

>[!IMPORTANT]
> Only *.pa.yaml files within "\src" folder can be used as source code.

### pa.yaml files



In the directory "\Src" you will have:



Bynary

To support


> [!TIP]
> To effectively ALM, it's recommended to use solutions. Canvas apps packages don’t support ALM and should only be used for basic import and export capabilities when Dataverse isn’t accessible.

Warning: YAML source code for Canvas Apps is in preview. The schema is being actively developed. Content may be incomplete and subject to change.
This file is read-only and should only be used to review changes made within Power Apps Studio. This file isn't used when loading the app. External editing, merging and conflict resolution are not supported.
