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

When you complete the steps in this tutorial you will be able to create a code component that will be dependant on a library contained in another control. In this example, for simplicity, the control containing the library wont actually be a functioning control (think of this as a pure library control) however there is no reason dependent control could not be a fully functional control. The example will allow the framework to load the dependent contol immediately and then be expanded to show how the dependent control can be loaded on demand.

## Prerequisites

You should be with familiar with the following:-

[Create and build a code component](create-custom-controls-using-pcf.md)</br>
[Package a code component](import-custom-controls.md)</br>
[Add code components to a model-driven app](add-custom-controls-to-a-field-or-entity.md#add-a-code-component-to-a-column)</br>
[Add components to a canvas app](component-framework-for-canvas-apps.md#add-components-to-a-canvas-app)</br>

## Dependency as a library in another component

1. Create a new component using this command:

  `pac pcf init -n StubLibrary -ns SampleNamespace -t field -npm`

1. In your new project add a new folder to contain your libraries `libs` for this example create a new javascript file. This example uses a library named `myLib-v_0_0_1.js` that has a single `sayHello` function.

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
1. You will also need a new declartion file (d.ts) for the the libray to describe the objects and functions contained in your library. Create a new file in the root folder of your project for `myLib-v_0_0_1.js` it looks like this `myLib.d.ts` file:

```typescript
declare module 'myLib' {
  export function sayHello(): string;
}
```
1. Add a reference to the library under the resources in the control manifest

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


1. Add a new feature control file in the root folder of your project called `featureconfig.json` containing the following:-

```json
{ 
  "pcfAllowLibraryResources": "on", 
  "pcfAllowCustomWebpack": "on" 
} 
```
1. Add a new webpack file `webpack.config.js` in the root folder of your project to ensure the libraries are bundled when we build the project

```typescript
/* eslint-disable */ 
"use strict"; 
 
module.exports = { 
  externals: { 
    "myLib": "myLib" 
  }, 
}  
```
1. Finally in the `index.ts` of the control include the libraries and then bind the library to the Window (comments removed from code below for ease of reading):-

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

## Dependency as on demand load of a component
