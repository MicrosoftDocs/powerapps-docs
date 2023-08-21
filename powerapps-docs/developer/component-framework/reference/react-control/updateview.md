---
title: "ReactControl.updateView (Power Apps component framework API reference)| MicrosoftDocs"
description: This method will be called for a ReactControl when any value in the property bag has changed. 
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
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


### Related articles

[React controls & platform libraries (Preview) ](../../react-controls-platform-libraries.md)<br />
[ReactControl](../react-control.md)<br/>
[Power Apps component framework API reference](../../reference/index.md)<br/>
[Power Apps component framework overview](../../overview.md)


[!INCLUDE[footer-include](../../../../includes/footer-banner.md)]
