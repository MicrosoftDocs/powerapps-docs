---
title: PowerApps component framework Manifest Schema Reference | Microsoft Docs
description: 
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 06/4/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 045a395b-4475-48dd-8f67-6bc2b33cd89c
---

# Manifest schema reference

[!INCLUDE[cc-beta-prerelease-disclaimer](../../../includes/cc-beta-prerelease-disclaimer.md)]

This section contains reference documentation for manifest schema generated using the PowerApps CLI.

> [!IMPORTANT]
> The **Available for** tab shows which elements are supported by model-driven apps and canvas apps (experimental preview). It is recommended to check the **Available for** section for each individual property whether it is supported or not. For example, the **code** element is supported for both model-driven apps and canvas apps, but **html** and **img** properties in **code** elements doesn't support canvas apps. 

|Element|Description|Available for|
|----|-----------|-----|
|[code](code.md)|[!INCLUDE [code-description](includes/code-description.md)]|Model-driven apps and canvas apps (experimental preview)|
|[control](control.md)|[!INCLUDE [control-description](includes/control-description.md)]|Model-driven apps and canvas apps (experimental preview)|
|[css](css.md)|[!INCLUDE [css-description](includes/css-description.md)]|Model-driven apps and canvas apps (experimental preview)|
|[data-set](data-set.md)|[!INCLUDE [data-set-description](includes/data-set-description.md)]|Model-driven apps|
|[html](html.md)|[!INCLUDE [html-description](includes/html-description.md)]|Model-driven apps|
|[img](img.md)|[!INCLUDE [img-description](includes/img-description.md)]|Model-driven apps|
|[manifest](manifest.md)|Manifest is the metadata file that defines a component. It is an XML document that describes<br/> - The namespace of the component.<br/> - The kind of data it can be configured, either a field or a data-set.<br/> - Any properties that can be configured in the application when the component is added.<br/> - A list of resource files that the component needs.<br/> - One of them must be a JavaScript web resource. This JavaScript must include a function that will instantiate an object. This implements an interface that exposes methods that are required for the component to work. This is called the component implementation library.<br/> - The name of a JavaScript function in the component implementation library that will return an object that applies the required interface.<br/> When someone configures a component in the application, the data in the manifest filters out the available components so that only valid components for the context are available for configuration. The properties defined in the manifest for a component are rendered as configuration fields so that the person configuring the control can specify values. These property values are then available to your component function at run time.|Model-driven apps and canvas apps (experimental preview)|
|[property](property.md)|[!INCLUDE [property-description](includes/property-description.md)]|Model-driven apps and canvas apps (experimental preview)|
|[property-set](property-set.md)|[!INCLUDE [property-set-description](includes/property-set-description.md)]|Model-driven apps|
|[resources](resources.md)|[!INCLUDE [resources-description](includes/resources-description.md)]|Model-driven apps and canvas apps (experimental preview)|
|[resx](resx.md)|[!INCLUDE [resx-description](includes/resx-description.md)]|Model-driven apps and canvas apps (experimental preview)|
|[type-group](type-group.md)|[!INCLUDE [type-group-description](includes/type-group-description.md)]|Model-driven apps and canvas apps (experimental preview)|
|[feature-usage](feature-usage.md)|The feature-usage element acts as a wrapper around the `uses-feature` elements, which themselves allow developers to declare which features their component wants to use. If there are no uses-feature elements defined, the feature-usage element is not required.|Model-driven apps|

### Related topics

[PowerApps component framework Manifest Schema Reference](index.md)<br/>
[PowerApps component framework API Reference](../reference/index.md)<br/>
[PowerApps component framework Overview](../overview.md)