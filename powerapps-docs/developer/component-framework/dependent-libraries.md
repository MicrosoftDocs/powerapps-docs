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

With model-driven apps, you can re-use a prebuilt library contained in another component that is loaded as a dependency to more than one component.

> [!NOTE]
> Components for canvas apps can't use dependent libraries.

Having a copy of a prebuilt library in multiple controls isn't desirable. Reusing existing libraries improves performance when the library is large by reducing the load time for all components that use the library.  Library reuse also helps reduce the maintenance overhead in build processes.

|Before|After|
|---|---|
|:::image type="content" source="media/dependent-library-before-example.png" alt-text="Diagram showing custom library files contained in each pcf component":::|:::image type="content" source="media/dependent-library-after-example.png" alt-text="Diagram showing components calling a shared function from a Library Control":::|

To use dependent libraries, you need to:

- Create a *Library component* that contains the library. This component can provide some functionality or simply be a container for the library.
- Configure









It would be preferable to load the library once on the form and have each of the controls that require to use it simply access it at runtime. This can now be achieved by creating a Library Control (note this can be a real control or simply a stub control) that the framework understands is a dependency to the other controls so it will load it at runtime.




This way you can independently maintain the library in the Library Control and the dependent controls do not need to have a copy of the library bundled with them.


## Dependency as on demand load of a component

In addition to specifying a dependency in the manifest of your control (where you set the order these are loaded) there is also the ability to specify that the dependency to be loaded on demand. This provides the flexibility for more complex controls to only load dependencies as they are required especially if the dependencies are larger libraries. 

:::image type="content" source="media/dependent-library-on-demand-load.png" alt-text="Diagram showing the use of a function from a library where the library is loaded on demand":::
<!-- See source \media\src\pcf_events_dependencies_diagrams.vsdx -->


## How it works


<!--Is the feature flag file still required?--> 

For a component to be able to use a library that is contained in another control, the component needs declare that it is using library resources and is also required to have a webpack configuration file that allows it to use custom webpack configuration to bundle the library when the solution is built. 

This is achieved by using a feature control file with two properties and a webpack configuration file outlining the configuration for the webpack bundling process.

### featureconfig.json

This file allows the override of the default feature flags for a PCF control without modifying the files generated in the `node_modules` folder. 

To use libraries in a control the following feature flags`pcfAllowLibraryResources` and `pcfAllowCustomWebpack` should be overriden and set to `on` it is `off` byt default. 

To use a dependent component in a control the following feature flag `pcfResourceDependency` should be overridden set to `on` it is `off` byt default.

### webpack.config.js

<!--Someone please check my description below is accurate -->
When a PCF control is built ![Webpack](https://webpack.js.org/) is used at build-time to bundle the code and dependencies into a deployable asset. To ensure that the libraries are not bundled as part of the code component, as the folder and library files are included separaetly in the packaged component, an additional configuration file is added to the project root folder `webpack.config.js` that should specify the library alias's as `externals` (see https://webpack.js.org/configuration/externals/ for more information).


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

