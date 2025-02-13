---
title: "Tutorial: Use dependent libraries in a component"
description: "In this tutorial, learn how to use dependent libraries with a model-driven app."
author: anuitz
ms.author: anuitz
ms.date: 02/05/2025
ms.reviewer: jdaly
ms.topic: tutorial
ms.subservice: pcf
contributors:
 - JimDaly
---
# Tutorial: Use dependent libraries in a component

> [!NOTE]
> This capability is only available for controls used in model-driven applications this will not work for canvas apps

This tutorial shows how to build a code component that is dependent on libraries that are contained in another component. 
[Learn more about dependent libraries](dependent-libraries.md)

## Goal

When you complete the steps in this tutorial you will be able to create a code component that will be dependant on a library contained in another control. In this example, for simplicity, the control containing the library wont actually be a functioning control (think of this as a pure library control) however there is no reason the dependent control could not be a fully functional control. The example will allow the framework to load the dependent contol immediately and then be expanded to show how the dependent control can be loaded on demand.

## Prerequisites

You should be with familiar with the following:-

[Create and build a code component](create-custom-controls-using-pcf.md)</br>
[Package a code component](import-custom-controls.md)</br>
[Add code components to a model-driven app](add-custom-controls-to-a-field-or-entity.md#add-a-code-component-to-a-column)</br>

## Build the library component

1. Create a new component using this command:

  `pac pcf init -n StubLibrary -ns SampleNamespace -t field -npm`

2. In your new control folder add a new folder to contain your libraries `libs` for this example create a new javascript file. This example uses a library named `myLib-v_0_0_1.js` that has a single `sayHello` function.

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
3. You will also need a new declartion file (d.ts) to describe the objects and functions contained in your library. Create a new file in the root folder of your project for `myLib-v_0_0_1.js` it looks like this `myLib.d.ts` file:

```typescript
declare module 'myLib' {
  export function sayHello(): string;
}
```
4. Add a reference to the library under the resources in the control manifest

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


5. Add a new feature control file in the root folder of your project called `featureconfig.json` containing the following:-

```json
{ 
  "pcfAllowLibraryResources": "on", 
  "pcfAllowCustomWebpack": "on" 
} 
```
6. Add a new webpack file `webpack.config.js` in the root folder of your project to ensure the libraries are not bundled with the control output as they are already packaged separately when we build the project

```typescript
/* eslint-disable */ 
"use strict"; 
 
module.exports = { 
  externals: { 
    "myLib": "myLib" 
  }, 
}  
```
7. Add an rule to turn off the check for `no-explicit-any` in the `.eslintrc.json` file:-

#### [Before](#tab/before)
```json
{
    "env": {
      "browser": true,
      "es2020": true
    },
    "extends": [
      "eslint:recommended",
      "plugin:@typescript-eslint/recommended"
    ],
    "globals": {
      "ComponentFramework": true
    },
    "parser": "@typescript-eslint/parser",
    "parserOptions": {
      "ecmaVersion": 12,
      "sourceType": "module"
    },
    "plugins": [
      "@microsoft/power-apps",
      "@typescript-eslint"
    ],
    "rules": {
      "@typescript-eslint/no-unused-vars": "off"
    }
}

```

#### [After](#tab/after)

```json
{
    "env": {
      "browser": true,
      "es2020": true
    },
    "extends": [
      "eslint:recommended",
      "plugin:@typescript-eslint/recommended"
    ],
    "globals": {
      "ComponentFramework": true
    },
    "parser": "@typescript-eslint/parser",
    "parserOptions": {
      "ecmaVersion": 12,
      "sourceType": "module"
    },
    "plugins": [
      "@microsoft/power-apps",
      "@typescript-eslint"
    ],
    "rules": {
      "@typescript-eslint/no-unused-vars": "off",
      "@typescript-eslint/no-explicit-any": "off"
    }
}

```

---

8. Finally in the `index.ts` of the control include the libraries and then bind the library to the Window (comments removed from code below for ease of reading):-

#### [Before](#tab/before)
```typescript
import { IInputs, IOutputs } from "./generated/ManifestTypes";

export class PreBuiltLibrary implements ComponentFramework.StandardControl<IInputs, IOutputs> {

    constructor()
    {

    }

    public init(context: ComponentFramework.Context<IInputs>, notifyOutputChanged: () => void, state: ComponentFramework.Dictionary, container:HTMLDivElement): void
    {
    }

    public updateView(context: ComponentFramework.Context<IInputs>): void
    {
    }

    public getOutputs(): IOutputs
    {
        return {};
    }

    public destroy(): void
    {
    }
}

```

#### [After](#tab/after)

```typescript
import { IInputs, IOutputs } from "./generated/ManifestTypes";
import * as MyLib from "myLib";

export class PreBuiltLibrary implements ComponentFramework.StandardControl<IInputs, IOutputs> {

    constructor()
    {

    }

    public init(context: ComponentFramework.Context<IInputs>, notifyOutputChanged: () => void, state: ComponentFramework.Dictionary, container:HTMLDivElement): void
    {
    }

    public updateView(context: ComponentFramework.Context<IInputs>): void
    {
    }

    public getOutputs(): IOutputs
    {
        return {};
    }

    public destroy(): void
    {
    }
}

(function () {
    (window as any).MyLib = MyLib;
})();
```

---

The library project should look like this:-

:::image type="content" source="media/dependent-library-libprojectview.png" alt-text="View of the project folder":::

## Build and package the Library component

[Create and build the code component](create-custom-controls-using-pcf.md)</br>
[Package the code component](import-custom-controls.md)</br>
[Deploy the code component](import-custom-controls.md#deploying-code-components)</br>

## Build the dependent control

1. Create a new component using this command:

  `pac pcf init -n DependencyControl -ns SampleNamespace -t field -npm`

2. Add a new feature control file in the root folder of your project called `featureconfig.json` containing the following:-

```json
{ 
  "pcfResourceDependency": "on"
} 
```

3. In the control manifest add the dependent resource, ths will be the `schemaName` of the dependent control `[solution prefix]_[namespace].[control name]` which you can find in the `solution.xml` file for the dependent control

:::image type="content" source="media/dependent-library-solutionxml.png" alt-text="View of the schemaName in the RootComponent of the solution xml file":::

#### [Before](#tab/before)
```xml
<resources> 
      <code path="index.ts" order="2"/> 
</resources> 
```

#### [After](#tab/after)

```xml
<resources> 
      <dependency type="control" name="samples_SampleNamespace.StubLibrary" order="1"/>
      <code path="index.ts" order="2"/>
</resources> 
```

---

4. Update the control (index.ts) so that it will make use of the dependent library which will be loaded onto the `Window` object when the control is loaded at runtime. 

#### [Before](#tab/before)
```typescript
    public init(context: ComponentFramework.Context<IInputs>, notifyOutputChanged: () => void, state: ComponentFramework.Dictionary, container:HTMLDivElement): void
    {
        // Add control initialization code
    }

```

#### [After](#tab/after)

```typescript
    public init(context: ComponentFramework.Context<IInputs>, notifyOutputChanged: () => void, state: ComponentFramework.Dictionary, container:HTMLDivElement): void
    {
        const controlDev = document.createElement("div");
        controlDev.innerText = (window as any).MyLib.sayHello()+" from Dependency" || "Hello World";
        container.appendChild(controlDev);
    }
```

---

5. Add an rule to turn off the check for `no-explicit-any` in the `.eslintrc.json` file:-

#### [Before](#tab/before)
```json
{
    "env": {
      "browser": true,
      "es2020": true
    },
    "extends": [
      "eslint:recommended",
      "plugin:@typescript-eslint/recommended"
    ],
    "globals": {
      "ComponentFramework": true
    },
    "parser": "@typescript-eslint/parser",
    "parserOptions": {
      "ecmaVersion": 12,
      "sourceType": "module"
    },
    "plugins": [
      "@microsoft/power-apps",
      "@typescript-eslint"
    ],
    "rules": {
      "@typescript-eslint/no-unused-vars": "off"
    }
}

```

#### [After](#tab/after)

```json
{
    "env": {
      "browser": true,
      "es2020": true
    },
    "extends": [
      "eslint:recommended",
      "plugin:@typescript-eslint/recommended"
    ],
    "globals": {
      "ComponentFramework": true
    },
    "parser": "@typescript-eslint/parser",
    "parserOptions": {
      "ecmaVersion": 12,
      "sourceType": "module"
    },
    "plugins": [
      "@microsoft/power-apps",
      "@typescript-eslint"
    ],
    "rules": {
      "@typescript-eslint/no-unused-vars": "off",
      "@typescript-eslint/no-explicit-any": "off"
    }
}

```

---

## Build and package the Dependent component

[Create and build the code component](create-custom-controls-using-pcf.md)</br>
[Package the code component](import-custom-controls.md)</br>
[Deploy the code component](import-custom-controls.md#deploying-code-components)</br>

## Add the component to a form

1. [Add the component to the model-driven form](code-components-model-driven-apps.md#add-code-components-to-model-driven-apps).

2. Navigate to the form and you should see the compenent show the text `Hello from myLib from Dependency`.

:::image type="content" source="media/dependent-library-running.png" alt-text="Image of component running in an enviornment":::

## Dependency as on demand load of a component

We can expand on this example by changing the Dependent Control to load the library resource on demand rather than have the framework load the library when the control loads. This is useful if the libraries being used by the control are very large and would impact the load time of the form.

1. Modify the control manifest of the [dependent control](tutorial-use-dependent-libraries.md#build-the-dependent-control)

#### [Before](#tab/before)
```xml
    <resources> 
        <dependency type="control" name="samples_SampleNamespace.StubLibrary" order="1"/>
        <code path="index.ts" order="2"/>
    </resources> 
```

#### [After](#tab/after)

```xml
    <platform-action action-type="afterPageLoad" />
    <feature-usage>
      <uses-feature name="Utility" required="true" />
    </feature-usage>
    <resources>
      <code path="index.ts" order="1"/>
      <dependency type="control" name="samples_SampleNamespace.StubLibrary" load-type="onDemand"/>
    </resources>
```

---
