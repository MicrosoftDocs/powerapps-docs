---
title: updatedProperties | Microsoft Docs
description: Provides updatesProperties related methods.
keywords:
ms.author: jdaly
author: noazarur-microsoft
manager: kvivek
ms.date: 03/12/2022
ms.reviewer: jdaly
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
---

# updatedProperties

Provides information on what has changed in the `updateView` method. The information could be change in the property value, component or browser resize event.

## Available for

Model-driven and canvas apps

## Example

```typescript
public updateView(context: ComponentFramework.Context<IInputs>): void
{
  // check if thi updateView call ahs update on sampleProperty
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

### Related topics

[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework overview](../overview.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
