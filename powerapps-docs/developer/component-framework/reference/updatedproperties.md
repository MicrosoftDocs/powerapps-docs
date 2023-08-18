---
title: updatedProperties (Power Apps component framework API reference) | Microsoft Docs
description: Provides updatesProperties related methods.
ms.author: noazarur
author: noazarur-microsoft
ms.date: 05/27/2022
ms.reviewer: jdaly
ms.topic: reference
ms.subservice: pcf
contributors:
 - JimDaly
---

# updatedProperties

Provides information on what has changed in the `updateView` method. The information could be change in the property value, component or browser resize event.

**Type**: `string[]`

| Array Values | Available for                | Description                              |
| ------------ | ---------------------------- | ---------------------------------------- |
| layout       | Model-driven and Canvas apps | Dimensions for the control were updated. |
| dataset      | Model-driven and Canvas apps | Records were updated.                    |
| records      | Canvas apps                  | Records were updated.                    |
| columns      | Canvas apps                  | Columns were updated.                    |
| sortorder    | Canvas apps                  | Sort order was updated.                  |
| page         | Canvas apps                  | Pagination information was updated.      |
| filter       | Canvas apps                  | Filtering was updated.                   |
| commands     | Canvas apps                  | Commands were were updated.              |

Additionally, use [loading attribute](../reference/dataset.md#loading) of the dataset that indicates whether the dataset is loading or not.

## Available for
Model-driven and canvas apps


## Example

```typescript
public updateView(context: ComponentFramework.Context<IInputs>): void
{
  // check if the updateView call has updated the sampleProperty
  if(context.updateProperties.indexOf("SampleProperty")> -1)
  {
      this._value = context.parameters.sampleProperty.raw;
  }
  // update isFullScreen flag based on the context
  if(-1!== context.updatedProperties.indexOf("fullscreen_open"))
  {
        this._isFullScreen =true;
  }
  else if(-1!== context.updatedProperties.indexOf("fullscreen_open"))
  {
          this._isFullScreen =false;
  }
}
```

### Related articles

[Dataset loading attribute](../reference/dataset.md#loading)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
