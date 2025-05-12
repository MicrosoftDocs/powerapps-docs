---
title: Dependent Libraries (preview)
description: Explains how to use dependent libraries with Power Apps Component Framework (PCF) controls.
author: anuitz
ms.author: anuitz
ms.date: 03/24/2025
ms.reviewer: jdaly
ms.topic: article
ms.subservice: pcf
contributors:
 - JimDaly
 - kierantpetrie
---
# Dependent Libraries (preview)

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

With model-driven apps, you can reuse a prebuilt library contained in another component that is loaded as a dependency to more than one component.

Having copies of a prebuilt library in multiple controls is undesirable. Reusing existing libraries improves performance, especially when the library is large, by reducing the load time for all components that use the library. Library reuse also helps reduce the maintenance overhead in build processes.

:::row:::
   :::column span="":::
      Before
   :::column-end:::
   :::column span="":::
      After
   :::column-end:::
:::row-end:::
:::row:::
   :::column span="":::
      :::image type="content" source="media/dependent-library-before-example.png" alt-text="Diagram showing custom library files contained in each pcf component":::
   :::column-end:::
   :::column span="":::
      :::image type="content" source="media/dependent-library-after-example.png" alt-text="Diagram showing components calling a shared function from a Library Control":::
   :::column-end:::
:::row-end:::

To use dependent libraries, you need to:

- Create a *Library component* that contains the library. This component can provide some functionality or only be a container for the library.
- Configure another component to depend on the library loaded by the library component.

By default, the library loads when the dependent component loads, but you can [configure it to load on demand](#dependency-as-on-demand-load-of-a-component).

This way you can independently maintain the library in the Library Control and the dependent controls don't need to have a copy of the library bundled with them.

## How it works

You need to add configuration data to your component project so that the build process deploys your libraries the way you want. Set this configuration data by adding or editing the following files:

- [featureconfig.json](#featureconfigjson)
- [webpack.config.js](#webpackconfigjs)
- Edit the manifest schema to [Register dependencies](#register-dependencies)

### featureconfig.json

Add this file to override the default feature flags for a component without modifying the files generated in the `node_modules` folder.

The following table describes the feature flags you can set in `featureconfig.json`:

|Name|Description|
|---|---|
|`pcfResourceDependency`|Enables the component to use a library resource.|
|`pcfAllowCustomWebpack`|Enables the component to use a custom web pack. This feature must be enabled for components that define a library resource.|

By default, these values are `off`. Set them to `on` to override the default. For example:

```json
{ 
  "pcfAllowCustomWebpack": "on" 
} 
```

```json
{ 
   "pcfResourceDependency": "on",
   "pcfAllowCustomWebpack": "off" 
} 
```

### webpack.config.js

The build process for components uses [Webpack](https://webpack.js.org/) to bundle the code and dependencies into a deployable asset. To exclude your libraries from this bundling, add a `webpack.config.js` file to the project root folder that specifies the alias of the library as `externals`. [Learn more about the Webpack externals configuration option](https://webpack.js.org/configuration/externals/)

This file might look like the following when the library alias is `myLib`.

```typescript
/* eslint-disable */ 
"use strict"; 

module.exports = { 
  externals: { 
    "myLib": "myLib" 
  }, 
}  
```


### Register dependencies

Use the [dependency element](manifest-schema-reference/dependency.md) within [resources](manifest-schema-reference/resources.md) of the manifest schema.

```xml
<resources>
  <dependency
    type="control"
    name="samples_SampleNS.SampleStubLibraryPCF"
    order="1"
  />
  <code path="index.ts" order="2" />
</resources>

```

### Dependency as on demand load of a component

Rather than loading the dependent library when a component loads, you can load the dependent library on demand. Loading on demand provides the flexibility for more complex controls to only load dependencies when they're required, especially if the dependent libraries are large.

:::image type="content" source="media/dependent-library-on-demand-load.png" alt-text="Diagram showing the use of a function from a library where the library is loaded on demand":::

<!-- See source \media\src\pcf_events_dependencies_diagrams.vsdx -->

To enable on demand loading, you need to:

1. Add these [platform-action element](manifest-schema-reference/platform-action.md), [feature-usage element](manifest-schema-reference/feature-usage.md), and [uses-feature element](manifest-schema-reference/uses-feature.md) child elements to the [control element](manifest-schema-reference/control.md):

   ```xml
   <platform-action action-type="afterPageLoad" />
   <feature-usage>
      <uses-feature name="Utility"
         required="true" />
   </feature-usage>
   ```

1. Set the `load-type` attribute of the [dependency element](manifest-schema-reference/dependency.md) to `onDemand`.

   ```xml
   <dependency type="control"
         name="samples_SampleNamespace.StubLibrary"
         load-type="onDemand" />
   ```

### Next steps

Try a tutorial that walks you through creating a dependent library.

> [!div class="nextstepaction"]
> [Tutorial: Use dependent libraries in a component](tutorial-use-dependent-libraries.md)