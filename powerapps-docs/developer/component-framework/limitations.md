---
title: "Limitations of PowerApps component framework | MicrosoftDocs"
description: "Limitations using PowerApps component framework"
author: nkrb
manager: kvivek
ms.date: 04/23/2019
ms.service: "powerapps"
ms.topic: "index-page"
ms.assetid: 18e88d702-3349-4022-a7d8-a9adf52cd34f
ms.author: "nabuthuk"
---

# Limitations of PowerApps component framework

[!INCLUDE[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

With the release of PowerApps component framework, you can now create your own code components to improve the user experience in model-driven apps. Even though you can create your own components, there are some limitations that restrict developers implementing some features in the code components. Below are some of the limitations:

## Support for external libraries

For public preview, components should bundle all code including external library content into the primary code bundle. To see an example of how the PowerApps command line interface can help with bundling your external library content into a component-specific bundle, see [Angular flip component](sample-controls/angular-flip-control.md) example.

> [!NOTE]
> Support for shared libraries across components using library nodes in component manifest is not supported for Public preview. We are reviewing this and will be adding this capability in future release.

## Related topics

[PowerApps component framework API Reference](reference/index.md)<br/>
[PowerApps component framework Overview](overview.md)
