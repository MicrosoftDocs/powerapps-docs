---
title: "Limitations of Power Apps component framework | MicrosoftDocs"
description: "Limitations using Power Apps component framework"
author: anuitz
ms.author: anuitz
ms.date: 12/04/2024
ms.reviewer: jdaly
ms.topic: article
ms.subservice: pcf
contributors:
 - JimDaly
---

# Limitations 

With Power Apps component framework, you can create your own code components to improve the user experience in Power Apps and Power Pages. Even though you can create your own components, there are some limitations that restrict developers implementing some features in the code components. Below are some of the limitations:

1. Microsoft Dataverse dependent APIs, including WebAPI, are not available for Power Apps canvas applications yet. For individual API availability,  see [Power Apps component framework API reference](reference/index.md).

2. Code components should either use [React controls & platform libraries](react-controls-platform-libraries.md) or bundle all the code including external library content into the primary code bundle. To see an example of how the Power Apps command line interface can help with bundling your external library content into a component-specific bundle, see [Angular flip component](sample-controls/angular-flip-control.md) example.

3. Code components should not use the HTML web storage objects, like `window.localStorage` and `window.sessionStorage`, to store data. Data stored locally on the user's browser or mobile client is not secure and not guaranteed to be available reliably.

## Related topics

[Power Apps component framework API reference](reference/index.md)<br/>
[Power Apps component framework overview](overview.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
