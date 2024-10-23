---
title: Power Platform Source Code Integration (preview)
description: Learn how to work with Canvas Apps when using the Power Platform Source Code Integration.
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

To effectively manage ALM, it's recommended to use solutions. Canvas apps packages don’t support ALM and should only be used for basic import and export capabilities when Dataverse isn’t accessible.

In a solution, canvas apps are included as binary .msapp files. Although this will work for ALM, you can't manage a binary file as a source code.

When using the Native Source Code Integration, we extract the content of the .msapp in multiple folder and files. 
All files used by canvas apps are visible, but only files in the folder /src are realiable for source control. 

A canvas app has the following structure:
    - Controls: Serialization of the visual controls
    - Datasource: References
    - …
    - Src: source control representes as pa.yaml files.
    
