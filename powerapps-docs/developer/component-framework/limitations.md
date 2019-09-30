---
title: "Limitations of PowerApps component framework | MicrosoftDocs"
description: "Limitations using PowerApps component framework"
author: nkrb
manager: kvivek
ms.date: 10/01/2019
ms.service: "powerapps"
ms.topic: "index-page"
ms.assetid: 18e88d702-3349-4022-a7d8-a9adf52cd34f
ms.author: "nabuthuk"
---

# Limitations of PowerApps component framework

With the release of PowerApps component framework, you can now create your own code components to improve the user experience in model-driven apps. Even though you can create your own components, there are some limitations that restrict developers implementing some features in the code components. Below are some of the limitations:

1. Only the *field* type of components are supported in the experimental preview for canvas apps and not the *dataset* type components. 
2. Common Data Service dependent APIs, including WebAPI along with few other APIs, are not available for this experimental preview. For individual API availability for this experimental preview release, see [PowerApps component framework API reference](reference/index.md).
3. Code components should bundle all the code including external library content into the primary code bundle. To see an example of how the PowerApps command line interface can help with bundling your external library content into a component-specific bundle, see [Angular flip component](sample-controls/angular-flip-control.md) example.

   > [!NOTE]
   > Support for shared libraries across components using library nodes in the component manifest is not yet supported. We are reviewing this and will be adding this capability in future release.

## Related topics

[PowerApps component framework API Reference](reference/index.md)<br/>
[PowerApps component framework Overview](overview.md)
