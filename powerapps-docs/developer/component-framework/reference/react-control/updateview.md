---
title: "ReactControl.updateView| MicrosoftDocs"
description: This method will be called for a ReactControl when any value in the property bag has changed. 
ms.author: jdaly
author: noazarur-microsoft
manager: kvivek
ms.date: 03/26/2022
ms.reviewer: jdaly
ms.topic: "reference"
applies_to: "Dynamics 365 (online)"
---
# ReactControl.updateView

[!INCLUDE[./includes/updateview-description.md](./includes/updateview-description.md)]

## Available for 

Model-driven and canvas apps

## Syntax

`updateView(context)`

## Parameters

| Parameter Name|Type|Required|Description|
| ------------- |----|--------|-----------|
|context|`context`|yes|Contains values as set up by the customizer mapped to the name defined in the manifest, as well as in the utility functions|

## Example

```TypeScript
public updateView(context: ComponentFramework.Context<IInputs>): React.ReactElement
{
    const props: IHelloWorldProps = { name: 'Hello, World'};
    return React.createElement(
        HelloWorld, props
    );
}
```

## Remarks

Set the value of the field component to the raw value from the configured field.


### Related topics

[React controls & platform libraries (Preview) ](../../react-controls-platform-libraries.md)<br />
[ReactControl](../react-control.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
