---
title: Dependent Libraries
description: Explains how to use dependent libraries with PowerApps Component Framework (PCF) controls.
author: anuitz
ms.author: anuitz
ms.date: 02/05/2025
ms.reviewer: jdaly
ms.topic: article
ms.subservice: pcf
contributors:
 - JimDaly
---
# Dependent Libraries

A common requirement when building custom components with the Power Apps Component Framework is the ability to use one or more existing libraries in the component.  You can do this in a model-driven app by referencing a library that is contained in another control which is loaded as a dependency to a custom control.

## Dependency as a library in another component

If you are using a prebuilt library in multiple controls then it is not desirable to have a copy of this library in every control. 

:::image type="content" source="media/dependent-library-before-example.png" alt-text="TODO  Add a description of the diagram":::
<!-- TODO Need source VDX for diagram -->

This creates an overhead of maintenance in the build processes if you are updating the library and if the libraries happen to be large in size this would inflate the size of the package for each of your custom controls and increase form load time when the controls are initially loaded into the browser.
It would be preferable to load the library once on the form and have each of the controls that require to use it simply access it at runtime. This can now be achieved by creating a Library Control (note this can be a real control or simply a stub control) that the framework understands is a dependency to the controls so it will load it at runtime.

:::image type="content" source="media/dependent-library-after-example.png" alt-text="TODO  Add a description of the diagram":::
<!-- TODO Need source VDX for diagram -->

This way you can independently maintain the library in the Library Control and the dependent controls do not need to have a copy of the library bundled with them.


## Dependency as on demand load of a component

In addition to specifying a dependency in the manifest of your control (where you set the order these are loaded) there is also the ability to specify that the dependency to be loaded on demand. This provides the flexibility for more complex controls to only load dependencies as they are required especially if the dependencies are larger libraries. 

:::image type="content" source="media/dependent-library-on-demand-load.png" alt-text="TODO Add a description of the diagram":::
<!-- TODO Need source VDX for diagram -->




## How it works

TODO: In the tutorial I seem mentions of new files: `featureconfig.json` and `webpack.config.js`.

This section could explain how the data in these files  is used to make this work?
But leave the step-by-step instructions for the tutorial

### featureconfig.json

This file has two properties: `pcfAllowLibraryResources` and `pcfAllowCustomWebpack` that you can set to `on` or `off`.


### webpack.config.js

Can we link to https://webpack.js.org/configuration/ to explain what this is?

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

[Tutorial: Use dependent libraries in a component](tutorial-use-dependent-libraries.md)   

