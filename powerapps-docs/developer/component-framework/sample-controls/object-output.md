---
title: "Object Output Component Sample| Microsoft Docs"
description: "Learn how you can use the object outout APIs."
ms.author: noazarur
author: noazarur-microsoft
ms.date: 06/07/2023
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# Object Output Component

[This article is pre-release documentation and is subject to change.]

This sample component shows how to use object type output properties. This component generates a static object and output via a property which then can be accessed in a canvas app or via client APIs in a model form.

## Available for

Model-driven apps and Canvas apps

## Prerequisites

Familiarity [creating code components](../implementing-controls-using-typescript.md).

## Code

You can find the complete code sample here: [PowerApps-Samples/component-framework/ObjectOutputControl/](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/ObjectOutputControl).

The manifest includes an object type property called `Data` and a hidden property called `DataSchema` . The DataSchema property is needed only for Canvas apps and used by platform to get the output object schema.
We also need to create a property dependency between these two properties.

```typescript
<!-- A hidden property used by Canvas to get the output object schema -->
<property name="DataSchema"
   display-name-key="DataSchema"
   description-key="DataSchema"
   of-type="SingleLine.Text"
   usage="input"
   hidden="true" />
<!-- The object type output property -->
<property name="Data"
   display-name-key="Data"
   description-key="Data"
   of-type="Object"
   usage="output"
   hidden="false"
   default-value="" />
<property-dependencies>
   <!-- Define the dependency between schema and the object type property -->
   <property-dependency input="DataSchema"
      output="Data"
      required-for="schema" />
</property-dependencies>
```

In the index.ts file we need to add [getOutputSchema](../reference/control/getoutputschema.md) method to provide the output object schema. When the control is added to a Canvas App, the platform will call to this method prior to control initialization to receive the output object(s) schema(s).

```typescript
public async getOutputSchema(context: ComponentFramework.Context<IInputs>): Promise<Record<string, unknown>> {
   return Promise.resolve({
      Data: StaticDataSchema
   });
}
```

Update the `getOutput` method to return value for the output property.

```typescript
public getOutputs(): IOutputs {
   return {
      Data: this._staticData
   };
}
```

The `onLoadData` method will be called when the **Load Data** button is pressed to load the data to the output object and notify the platform about the output changes. This will trigger onChange behavior in the Canvas App for the control or [OnOutputChange](../../model-driven-apps/clientapi/reference/events/onoutputchange.md) event for client APIs.

```typescript
private onLoadData = async () => {
   this._staticData = StaticData;
   this._staticData.loadCounter = (this._staticData.loadCounter || 0) + 1;
   this.notifyOutputChanged();
}
```

### Related topics

[onOutputChange Event](../../model-driven-apps/clientapi/reference/events/onoutputchange.md)  
[StandardControl.getOutputSchema](../reference/control/getoutputschema.md)  
[ReactControl.getOutputSchema](../reference/react-control/getoutputschema.md)  
[StandardControl.getOutputs](../reference/control/getoutputs.md)  
[ReactControl.getOutputs](../reference/react-control/getOutputs.md)  

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
