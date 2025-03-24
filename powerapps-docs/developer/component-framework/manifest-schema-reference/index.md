---
title: Power Apps component framework manifest schema reference | Microsoft Docs
description: This section contains reference documentation for manifest schema generated using Microsoft Power Platform CLI.
author: anuitz
ms.author: anuitz
ms.date: 03/24/2025
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# Manifest schema reference

This section contains reference documentation for manifest schema generated using Microsoft Power Platform CLI.

> [!IMPORTANT]
> The **Available for** tab shows which elements are supported by model-driven and canvas apps. It is recommended to check the **Available for** section for each individual property whether it is supported or not. For example, the **code** element is supported for both model-driven and canvas apps, but **html** and **img** properties in **code** elements doesn't support canvas apps.

|Element|Description|Available for|
|----|-----------|-----|
|[code](code.md)|[!INCLUDE [code-description](includes/code-description.md)]|Model-driven and canvas apps|
|[control](control.md)|[!INCLUDE [control-description](includes/control-description.md)]|Model-driven and canvas apps|
|[css](css.md)|[!INCLUDE [css-description](includes/css-description.md)]|Model-driven and canvas apps|
|[data-set](data-set.md)|[!INCLUDE [data-set-description](includes/data-set-description.md)]|Model-driven apps|
|[domain](domain.md)|[!INCLUDE [domain-description](includes/domain-description.md)]|Canvas apps|
|[dependency](dependency.md)|[!INCLUDE [dependency-description](includes/dependency-description.md)]|Model-driven apps|
|[external-service-usage](external-service-usage.md)|[!INCLUDE [external-service-usage-description](includes/external-service-usage-description.md)]|Canvas apps|
|[event element](event.md)|[!INCLUDE [event-description](includes/event-description.md)]|Canvas apps|
|[feature-usage](feature-usage.md)|The feature-usage element acts as a wrapper around the `uses-feature` elements, which themselves allow developers to declare which features their component wants to use. If there are no uses-feature elements defined, the feature-usage element is not required.|Model-driven apps|
|[img](img.md)|[!INCLUDE [img-description](includes/img-description.md)]|Model-driven apps|
|[manifest](manifest.md)|Manifest is the metadata file that defines a component. It is an XML document that describes<br/> - The namespace of the component.<br/> - The kind of data it can be configured, either a field or a data-set.<br/> - Any properties that can be configured in the application when the component is added.<br/> - A list of resource files that the component needs.<br/> - One of them must be a JavaScript web resource. This JavaScript must include a function that will instantiate an object. This implements an interface that exposes methods that are required for the component to work. This is called the component implementation library.<br/> - The name of a JavaScript function in the component implementation library that will return an object that applies the required interface.<br/> When someone configures a component in the application, the data in the manifest filters out the available components so that only valid components for the context are available for configuration. The properties defined in the manifest for a component are rendered as configuration fields so that the person configuring the control can specify values. These property values are then available to your component function at run time.|Model-driven and canvas apps|
|[platform-action](platform-action.md)|[!INCLUDE [platform-action-description](includes/platform-action-description.md)]|Model-driven and canvas apps|
|[platform-library](platform-library.md)|[!INCLUDE [platform-library-description](includes/platform-library-description.md)]|Model-driven and canvas apps|
|[property-dependencies](property-dependencies.md)|[!INCLUDE [property-dependencies-description](includes/property-dependencies-description.md)]|Canvas apps|
|[property-dependency](property-dependency.md)|[!INCLUDE [property-dependency-description](includes/property-dependency-description.md)]|Canvas apps|
|[property-set](property-set.md)|[!INCLUDE [property-set-description](includes/property-set-description.md)]|Model-driven apps|
|[property](property.md)|[!INCLUDE [property-description](includes/property-description.md)]|Model-driven and canvas apps|
|[resources](resources.md)|[!INCLUDE [resources-description](includes/resources-description.md)]|Model-driven and canvas apps|
|[resx](resx.md)|[!INCLUDE [resx-description](includes/resx-description.md)]|Model-driven and canvas apps|
|[type](type.md)|[!INCLUDE [type-description](includes/type-description.md)]|Model-driven apps|
|[type-group](type-group.md)|[!INCLUDE [type-group-description](includes/type-group-description.md)]|Model-driven and canvas apps|
|[types](types.md)|[!INCLUDE [types-description](includes/types-description.md)]|Model-driven and canvas apps|
|[uses-feature](uses-feature.md)|[!INCLUDE [uses-feature-description](includes/uses-feature-description.md)]|Model-driven apps|


### Related articles

[Power Apps component framework manifest schema reference](index.md)   
[Power Apps component framework API reference](../reference/index.md)   
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]