---
title: "Tutorial: Use dependent libraries in a component"
description: "In this tutorial, learn how to use dependent libraries with a model-driven app."
author: anuitz
ms.author: anuitz
ms.date: 02/13/2025
ms.reviewer: jdaly
ms.topic: tutorial
ms.subservice: pcf
contributors:
 - JimDaly
---
# Tutorial: Use dependent libraries in a component

This tutorial shows how to build a code component for model-driven apps that is dependent on libraries that are contained in another component.
[Learn more about dependent libraries](dependent-libraries.md)

## Goal

Follow the steps in this tutorial to create a library control and a control that depends on it. This tutorial contains the following steps:

1. In [Build the library component](#build-the-library-component), you will create a simple component that only contains the re-usable library. For simplicity, this control only contains the re-usable library. There is no reason it couldn't also provide functionality.
1. In [Build the dependent control](#build-the-dependent-control), you will create a component that uses the library defined in the library control and add it to a form to verify that it works.
1. In [Dependency as on demand load of a component](#dependency-as-on-demand-load-of-a-component), you can expand on the example make the dependent component load the library resource on demand rather than have the framework load the library when the control loads.


## Prerequisites

You should already know how to:

- [Create and build a code component](create-custom-controls-using-pcf.md)
- [Package a code component](import-custom-controls.md)
- [Add code components to a model-driven app](add-custom-controls-to-a-field-or-entity.md#add-a-code-component-to-a-column)

## Build the library component

This component doesn't provide any capabilities by itself. It is simply a container for the library.

The first step is to create a new component using the [pac pcf init command](/power-platform/developer/cli/reference/pcf#pac-pcf-init):

   `pac pcf init -n StubLibrary -ns SampleNamespace -t field -npm`

### Define the library

1. In your new control folder add a new folder to contain your libraries `libs` for this example create a new javascript file. This example uses a library named `myLib-v_0_0_1.js` that has a single `sayHello` function.

   ```javascript
   // UMD module pattern
   var myLib = (function (exports) {
   'use strict';

   function sayHello() {
      return "Hello from myLib";
   }

   exports.sayHello = sayHello;

   return exports;

   }({}));

   ```

1. You need new declaration file (d.ts) to describe the objects and functions contained in your library. Create a new file in the root folder of your project for `myLib-v_0_0_1.js` it looks like this `myLib.d.ts` file:

   ```typescript
   declare module 'myLib' {
   export function sayHello(): string;
   }
   ```

1. Add a reference to the library under the resources in the control manifest.

#### [Before](#tab/before)

```xml
<resources> 
      <code path="index.ts" order="2"/> 
</resources> 
```

#### [After](#tab/after)

```xml
<resources> 
      <library name="myLib" version=">=1" order="1"> 
        <packaged_library path="libs/myLib-v_0_0_1.js" version="0.0.1" /> 
      </library> 
      <code path="index.ts" order="2"/> 
</resources> 
```

---

### Add Configuration

1. Add a file named `featureconfig.json` in the root folder of the project.
1. Add the following to the `featureconfig.json` file

   ```json
   { 
     "pcfAllowLibraryResources": "on", 
     "pcfAllowCustomWebpack": "on" 
   } 
   ```

   **TODO**: Briefly why both of these settings are "on".

   [Learn more about the featureconfig.json file](dependent-libraries.md#featureconfigjson)

1. Add a new webpack file named `webpack.config.js` in the root folder of your project. This ensures that the libraries aren't bundled with the control output. This isn't necessary because they are already packaged separately when you build the project.

   ```typescript
   /* eslint-disable */ 
   "use strict"; 
   
   module.exports = { 
     externals: { 
       "myLib": "myLib" 
     }, 
   }  
   ```

1. Edit the `.eslintrc.json` file to modify the `rules` to add a rule to turn off the check for [no-explicit-any](https://typescript-eslint.io/rules/no-explicit-any/).

<!-- TODO Briefly explain why this is necessary.  Is it always necessary, or only because of how MyLib is configured? -->

#### [Before](#tab/before)

```json
   "rules": {
      "@typescript-eslint/no-unused-vars": "off"
   }
```

#### [After](#tab/after)

```json
   "rules": {
      "@typescript-eslint/no-unused-vars": "off",
      "@typescript-eslint/no-explicit-any": "off"
   }
```

---

### Add library to window

The last step is edit the `index.ts` of the control to bind the library to the window.

#### [Before](#tab/before)

```typescript
import { IInputs, IOutputs } from "./generated/ManifestTypes";

export class PreBuiltLibrary
implements ComponentFramework.StandardControl<IInputs, IOutputs>
{
constructor() {}

public init(
   context: ComponentFramework.Context<IInputs>,
   notifyOutputChanged: () => void,
   state: ComponentFramework.Dictionary,
   container: HTMLDivElement
): void {}

public updateView(context: ComponentFramework.Context<IInputs>): void {}

public getOutputs(): IOutputs {
   return {};
}

public destroy(): void {}
}

```

#### [After](#tab/after)

```typescript
import { IInputs, IOutputs } from "./generated/ManifestTypes";

export class PreBuiltLibrary
implements ComponentFramework.StandardControl<IInputs, IOutputs>
{
constructor() {}

public init(
   context: ComponentFramework.Context<IInputs>,
   notifyOutputChanged: () => void,
   state: ComponentFramework.Dictionary,
   container: HTMLDivElement
): void {}

public updateView(context: ComponentFramework.Context<IInputs>): void {}

public getOutputs(): IOutputs {
   return {};
}

public destroy(): void {}
}

(function () {
   (window as any).MyLib = MyLib;
})();
```

---

The library project should look like this:-

:::image type="content" source="media/dependent-library-libprojectview.png" alt-text="View of the project folder":::

### Build and package the library component

To finish the library component, complete the following steps as usual:

1. [Create and build the code component](create-custom-controls-using-pcf.md)
1. [Package the code component](import-custom-controls.md)
1. [Deploy the code component](import-custom-controls.md#deploying-code-components)

## Build the dependent control

Now that you have a library control, you need a control to depend on it.

1. Create a new component using this command:

   `pac pcf init -n DependencyControl -ns SampleNamespace -t field -npm`

1. Add a new feature control file in the root folder of your project called `featureconfig.json` containing the following:

   ```json
   { 
     "pcfResourceDependency": "on"
   } 
   ```

1. Add the dependent resource in the control manifest. 

   Use the `schemaName` of the dependent control `[solution prefix]_[namespace].[control name]` which you can find in the `solution.xml` file for the dependent component. The XML in the solution.xml file might look like this:

   ```xml
   <RootComponents>
   <RootComponent
      type="66"
      schemaName="samples_SampleNamespace.StubLibrary"
      behavior="0"
   />
   </RootComponents>
   ```

#### [Before](#tab/before)

```xml
<resources>
    <code path="index.ts"
        order="2" />
</resources> 
```

#### [After](#tab/after)

```xml
<resources>
    <dependency type="control"
        name="samples_SampleNamespace.StubLibrary"
        order="1" />
    <code path="index.ts"
        order="2" />
</resources> 
```

---

### Use the library function

Update the component `index.ts` file so that it uses a function from the dependent library. The library is loaded into the `Window` object at runtime.

#### [Before](#tab/before)

```typescript
public init(
   context: ComponentFramework.Context<IInputs>,
   notifyOutputChanged: () => void,
   state: ComponentFramework.Dictionary,
   container: HTMLDivElement
): void {
   // Add control initialization code
}

```

#### [After](#tab/after)

```typescript
public init(
   context: ComponentFramework.Context<IInputs>,
   notifyOutputChanged: () => void,
   state: ComponentFramework.Dictionary,
   container: HTMLDivElement
): void {
      const controlDev = document.createElement("div");
      controlDev.innerText = (window as any).MyLib.sayHello()+" from Dependency" || "Hello World";
      container.appendChild(controlDev);
}
```

---


### Disable the check for no-explicit-any

Edit the `.eslintrc.json` file to modify the `rules` to add a rule to turn off the check for [no-explicit-any](https://typescript-eslint.io/rules/no-explicit-any/).

<!-- TODO Briefly explain why this is necessary.  Is it always necessary, or only because of how MyLib is configured? -->

#### [Before](#tab/before)

```json
   "rules": {
      "@typescript-eslint/no-unused-vars": "off"
   }
```

#### [After](#tab/after)

```json
   "rules": {
      "@typescript-eslint/no-unused-vars": "off",
      "@typescript-eslint/no-explicit-any": "off"
   }
```

---

### Build and package the dependent component

To finish the dependent component, complete the following steps as usual:

1. [Create and build the code component](create-custom-controls-using-pcf.md)
1. [Package the code component](import-custom-controls.md)
1. [Deploy the code component](import-custom-controls.md#deploying-code-components)

### Add the component to a form

1. [Add the component to the model-driven form](code-components-model-driven-apps.md#add-code-components-to-model-driven-apps).

1. Navigate to the form and you should see the component show the text `Hello from myLib from Dependency`.

   :::image type="content" source="media/dependent-library-running.png" alt-text="Image of component running in an environment":::

## Dependency as on demand load of a component

We can expand on this example by changing the dependent component to load the library resource on demand rather than have the framework load the library when the component loads.

This is useful if the libraries being used by the control are very large and would impact the load time of the form.

To do this, modify the control manifest of the [dependent control](tutorial-use-dependent-libraries.md#build-the-dependent-control)

#### [Before](#tab/before)

```xml
<resources>
    <dependency type="control"
        name="samples_SampleNamespace.StubLibrary"
        order="1" />
    <code path="index.ts"
        order="2" />
</resources>
```

#### [After](#tab/after)

```xml
<platform-action action-type="afterPageLoad" />
<feature-usage>
    <uses-feature name="Utility"
        required="true" />
</feature-usage>
<resources>
    <code path="index.ts"
        order="1" />
    <dependency type="control"
        name="samples_SampleNamespace.StubLibrary"
        load-type="onDemand" />
</resources>
```

---
