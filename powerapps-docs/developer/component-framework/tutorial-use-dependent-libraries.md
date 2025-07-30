---
title: "Tutorial: Use dependent libraries in a component"
description: "In this tutorial, learn how to use dependent libraries with a model-driven app."
author: anuitz
ms.author: anuitz
ms.date: 04/04/2025
ms.reviewer: jdaly
ms.topic: tutorial
ms.subservice: pcf
contributors:
 - JimDaly
 - kierantpetrie
---
# Tutorial: Use dependent libraries in a component

[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

This tutorial shows how to build a code component for model-driven apps that is dependent on libraries that are contained in another component.
[Learn more about the dependent libraries preview](dependent-libraries.md)

## Goal

Follow the steps in this tutorial to create a library control and a control that depends on it. This tutorial contains the following steps:

1. [Build the library component](#1-build-the-library-component): Create a component that only contains the reusable library. For simplicity, this control only contains the reusable library. There's no reason it couldn't also provide functionality.
1. [Build the dependent control](#2-build-the-dependent-control): Create a component that uses the library defined in the library control and add it to a form of a model-driven app to verify that it works.
1. [Load dependent library on demand](#3-load-dependent-library-on-demand): Expand on the example to make the dependent component load the library resource on demand rather than have the framework load the library when the control loads.

## Prerequisites

You should already know how to:

- [Create and build a code component](create-custom-controls-using-pcf.md)
- [Package a code component](import-custom-controls.md)
- [Add code components to a model-driven app](add-custom-controls-to-a-field-or-entity.md#add-a-code-component-to-a-column)

## 1. Build the library component

This component doesn't provide any capabilities by itself. It's simply a container for the library.

The first step is to create a new component using the [pac pcf init command](/power-platform/developer/cli/reference/pcf#pac-pcf-init):

   ```cmd
   pac pcf init -n StubLibrary -ns SampleNamespace -t field -npm
   ```

### Define the library

1. You need a new declaration file (d.ts) to describe the objects and functions contained in your library. Create a new file in the root folder of your project named `myLib.d.ts`:

   ```typescript
   declare module 'myLib' {
     export function sayHello(): string;
   }
   ```
   
1. We are going to expose our library as an UMD module, and we need to put the variable in the global scope. For this we need a new declaration file (d.ts). Create a new file in the root folder of your project named `global.d.ts`:

   ```typescript
   /* eslint-disable no-var */
   declare global {
     var myLib: typeof import('myLib');
   }

   export { };
   ```

1. Update tsconfig.json to allow UMD modules and javascript code as follows:

   #### [Before](#tab/before)
   
   ```json
   {
       "extends": "./node_modules/pcf-scripts/tsconfig_base.json",
       "compilerOptions": {
           "typeRoots": ["node_modules/@types"]
       }
   }
   ```
   
   #### [After](#tab/after)
   
   ```json
   {
       "extends": "./node_modules/pcf-scripts/tsconfig_base.json",
       "compilerOptions": {
           "typeRoots": ["node_modules/@types"],
           "allowJs": true,
           "allowUmdGlobalAccess": true,
           "outDir": "dist"
       },
   }
   ```
   ---

### Add the library

In your new control folder, add a new folder to contain your libraries `libs` for this example create a new JavaScript file. This example uses a library named `myLib-v_0_0_1.js` that has a single `sayHello` function.

   ```javascript
   // UMD module pattern
   var myLib = (function (exports) {
   "use strict";

   function sayHello() {
      return "Hello from myLib";
   }

   exports.sayHello = sayHello;

   return exports;
   })(/** @type {import('myLib')}  */ ({}));
   ```

### Add Configuration data

1. Add a file named `featureconfig.json` in the root folder of the project.
1. Add the following text to the `featureconfig.json` file:

   ```json
   {
     "pcfAllowCustomWebpack": "on",
     "pcfAllowLibraryResources": "on"
   }
   ```

   [Learn more about the featureconfig.json file](dependent-libraries.md#featureconfigjson)

1. Add a new `webpack.config.js` file in the root folder of your project. This configuration data ensures that the libraries aren't bundled with the control output. Bundling isn't necessary because they're already packaged separately when you build the project.

   ```typescript
   /* eslint-disable */
   "use strict";

   module.exports = {
     externals: {
       "myLib": "myLib"
     },
   }
   ```

   [Learn more about the webpack.config.js file](dependent-libraries.md#webpackconfigjs)

1. Add a reference to the library under the `resources` in the control manifest.

#### [Before](#tab/before)

```xml
<resources> 
  <code path="index.ts" order="1"/> 
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

### Add the library to window

The last step is to edit the `index.ts` of the control to bind the library to the [window](https://developer.mozilla.org/docs/Web/API/Window).

#### [Before](#tab/before)

```typescript
import { IInputs, IOutputs } from "./generated/ManifestTypes";

export class StubLibrary
implements ComponentFramework.StandardControl<IInputs, IOutputs>
{
 constructor() {
   // Empty
 }

 public init(
    context: ComponentFramework.Context<IInputs>,
    notifyOutputChanged: () => void,
    state: ComponentFramework.Dictionary,
    container: HTMLDivElement
 ): void {
   // Add control initialization code
 }

 public updateView(context: ComponentFramework.Context<IInputs>): void {
   // Add code to update control view
 }

 public getOutputs(): IOutputs {
    return {};
 }

  public destroy(): void {
    // Add code to cleanup control if necessary
  }
}
```

#### [After](#tab/after)

```typescript
import * as myLib from 'myLib';
import { IInputs, IOutputs } from "./generated/ManifestTypes";

export class StubLibrary
implements ComponentFramework.StandardControl<IInputs, IOutputs>
{
 constructor() {
   // Empty
 }

 public init(
    context: ComponentFramework.Context<IInputs>,
    notifyOutputChanged: () => void,
    state: ComponentFramework.Dictionary,
    container: HTMLDivElement
 ): void {
   // Add control initialization code
 }

 public updateView(context: ComponentFramework.Context<IInputs>): void {
   // Add code to update control view
 }

 public getOutputs(): IOutputs {
    return {};
 }

  public destroy(): void {
    // Add code to cleanup control if necessary
  }
}

(function () {
   window.myLib = myLib;
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

## 2. Build the dependent control

Now that you have a library control, you need a control to depend on it.

1. Create a new component using this command:

   ```cmd
   pac pcf init -n DependencyControl -ns SampleNamespace -t field -fw react -npm
   ```

1. Add a new feature control file in the root folder of your project called `featureconfig.json` containing the following text:

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
         order="1" />
      <platform-library name="React"
         version="16.14.0" />
      <platform-library name="Fluent"
         version="9.46.2" />
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
      <platform-library name="React"
         version="16.14.0" />
      <platform-library name="Fluent"
         version="9.46.2" />    
</resources> 
```

---

### Add Global.d.ts

Since the StubLibrary is exposed as an UMD module, we need to put the variable in the global scope. For this we need a new declaration file (d.ts). Create a new file in the root folder of your project named `global.d.ts`:

```typescript
/* eslint-disable no-var */

interface MyLib {
      sayHello(): string;
}

declare global {
      var myLib: MyLib;
}

export { };

```

### Use the library function

Update the component `HelloWorld.tsx` file so that it uses a function from the dependent library. The library is loaded into the `Window` object at runtime.

#### [Before](#tab/before)

```typescript
import * as React from 'react';
import { Label } from '@fluentui/react-components';

export interface IHelloWorldProps {
  name?: string;
}

export class HelloWorld extends React.Component<IHelloWorldProps> {
  public render(): React.ReactNode {
    return (
      <Label>
        {this.props.name}
      </Label>
    )
  }
}

```

#### [After](#tab/after)

```typescript
import * as React from 'react';
import { Label } from '@fluentui/react-components';

export interface IHelloWorldProps {
  name?: string;
}

export class HelloWorld extends React.Component<IHelloWorldProps> {
  public render(): React.ReactNode {
    return (
      <Label>
        { window.myLib.sayHello() + " from Dependency" || "Hello World"}
      </Label>
    )
  }
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

## 3. Load dependent library on demand

You can expand on this example by changing the dependent component to load the library resource on demand rather than have the framework load the library when the component loads. On demand load behavior is useful if the libraries being used by the control are large and would increase the load time of the form.

### Specify on demand load behavior

To specify on demand load behavior, modify the control manifest of the component created in [2. Build the dependent control](#2-build-the-dependent-control).

#### [Before](#tab/before)

```xml
<resources>
    <dependency type="control"
        name="samples_SampleNamespace.StubLibrary"
        order="1" />
    <code path="index.ts"
        order="2" />
    <platform-library name="React" version="16.14.0" />
    <platform-library name="Fluent" version="9.46.2" />
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
    <platform-library name="React" version="16.14.0" />
    <platform-library name="Fluent" version="9.46.2" />  
</resources>
```

---

### Modify the dependent component to load library on demand

Modify the `HelloWorld.tsx` to add a state and methods to update it once the dependency loads.

#### [Before](#tab/before)

```typescript
import * as React from 'react';
import { Label } from '@fluentui/react-components';

export interface IHelloWorldProps {
  name?: string;
}

export class HelloWorld extends React.Component<IHelloWorldProps> {
  public render(): React.ReactNode {
    return (
      <Label>
        { window.myLib.sayHello() + " from Dependency" || "Hello World"}
      </Label>
    )
  }
}
```

#### [After](#tab/after)

```typescript
import * as React from 'react';
import { Label } from '@fluentui/react-components';

export interface IHelloWorldProps {
  name?: string;
}

export class HelloWorld extends React.Component<IHelloWorldProps, { loaded: boolean }> {
  constructor(props: IHelloWorldProps) {
    super(props);
    this.state = {
      loaded: false
    };
  }

  public afterPageLoad() {
    this.setState({ loaded: true });
  }

  public render(): React.ReactNode {
    return (
      <Label>
          {this.state.loaded ? window.myLib.sayHello() + " Dependency On Demand Load" : 'Loading...'}
      </Label>
    )
  }
}
```

---

### Update index.ts

When the script is loaded on demand, you need to make slight adjustments to how the component is created and initialized. For example, new variables for references to the context and the container to update the state.

Most importantly add a `getActions` method to react to the On Load and request the dependent control to be loaded.

#### [Before](#tab/before)

```typescript
import { IInputs, IOutputs } from "./generated/ManifestTypes";
import { HelloWorld, IHelloWorldProps } from "./HelloWorld";
import * as React from "react";

export class DependencyControl implements ComponentFramework.ReactControl<IInputs, IOutputs> {
    private notifyOutputChanged: () => void;

    constructor() {
        // Empty
    }

    public init(
        context: ComponentFramework.Context<IInputs>,
        notifyOutputChanged: () => void,
        state: ComponentFramework.Dictionary
    ): void {
        this.notifyOutputChanged = notifyOutputChanged;
    }

    public updateView(context: ComponentFramework.Context<IInputs>): React.ReactElement {
        const props: IHelloWorldProps = { name: 'Power Apps' };
        return React.createElement(
            HelloWorld, props
        );
    }

    public getOutputs(): IOutputs {
        return { };
    }

    public destroy(): void {
        // Add code to cleanup control if necessary
    }
}

```

#### [After](#tab/after)

```typescript
import { IInputs, IOutputs } from "./generated/ManifestTypes";
import { HelloWorld} from "./HelloWorld";
import * as React from "react";

export class DependencyControl implements ComponentFramework.ReactControl<IInputs, IOutputs> {
    private theComponent: ComponentFramework.ReactControl<IInputs, IOutputs>;
    private notifyOutputChanged: () => void;
    private context: ComponentFramework.Context<IInputs>;
    private mainContainerRef: React.RefObject<HelloWorld> = React.createRef<HelloWorld>();

    constructor() { 
        // Empty
    }

    public init(
        context: ComponentFramework.Context<IInputs>,
        notifyOutputChanged: () => void,
        state: ComponentFramework.Dictionary
    ): void {
        this.notifyOutputChanged = notifyOutputChanged;
        this.context = context;
    }

    public updateView(context: ComponentFramework.Context<IInputs>): React.ReactElement {
        return React.createElement(
            HelloWorld, {ref: this.mainContainerRef }
        );
    }

    public getOutputs(): IOutputs {
        return { };
    }

    public getActions(): {afterPageLoad: ()=>Promise<void>} {
        return {
            afterPageLoad: async () => {
                console.log("afterPageLoad");
                const loadedControl = await this.context.utils.loadDependency?.("samples_SampleNamespace.StubLibrary");
                if (loadedControl) {
                    this.mainContainerRef.current?.afterPageLoad();
                  } 
            },
        };
    }

    public destroy(): void {
        // Add code to cleanup control if necessary
    }
}
```

---

### Final steps

1. Update the version number of the control in the `ControlManifest.Input.xml` and the version in the `Solution.xml`
1. Rebuild, package, deploy, and publish the solution with the updated control.

### Verify results

Now, when the page loads you see the control load with `Loading...` displayed.

:::image type="content" source="media/dependent-library-loading.png" alt-text="Image of component while the form loads" lightbox="media/dependent-library-loading.png":::

Once the page loads, the control updates to display `Hello from myLib Dependency On Demand Load`.

:::image type="content" source="media/dependent-library-loaded.png" alt-text="Image of component once the form has loaded" lightbox="media/dependent-library-loaded.png":::

### Related articles

[Dependent Libraries (preview)](dependent-libraries.md)
