---
title: "Limitations of Power Apps component framework | MicrosoftDocs"
description: "Limitations using Power Apps component framework"
author: nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.topic: "index-page"
ms.assetid: 18e88d702-3349-4022-a7d8-a9adf52cd34f
ms.author: "nabuthuk"
---

# Limitations 

With the release of Power Apps component framework, you can now create your own code components to improve the user experience in model-driven apps and canvas apps. Even though you can create your own components, there are some limitations that restrict developers implementing some features in the code components. Below are some of the limitations:

1. Common Data Service dependent APIs, including WebAPI along with few other APIs, are not available for this experimental preview. For individual API availability for this experimental preview release, see [Power Apps component framework API reference](reference/index.md).
2. Code components should bundle all the code including external library content into the primary code bundle. To see an example of how the Power Apps command line interface can help with bundling your external library content into a component-specific bundle, see [Angular flip component](sample-controls/angular-flip-control.md) example.

   > [!NOTE]
   > Support for shared libraries across components using library nodes in the component manifest is not yet supported. We are reviewing this and will be adding this capability in future release.

## Related topics

[Power Apps component framework API reference](reference/index.md)<br/>
[Power Apps component framework overview](overview.md)
