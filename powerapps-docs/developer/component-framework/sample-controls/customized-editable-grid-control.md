---
title: Customized editable grid  | Microsoft Docs
description: "This sample demonstrates how to customize the editable grid control"
author: clromano
ms.author: clromano
ms.date: 07/25/2022
ms.reviewer: jdaly
ms.topic: sample
ms.subservice: pcf
search.audienceType: 
  - developer
contributors:
 - JimDaly
 - aliry
---

# Customized editable grid

This sample demonstrates how to customize the Power Apps editable grid control as described in [Customize the editable grid control](../customize-editable-grid-control.md).

This sample changes the main grid page for a table that is configured to use this control. All text columns will use green text. Any values for the `creditlimit` column will display as blue if the value is greater than 100,000 and red otherwise.

:::image type="content" source="../media/editable-grid-control-sample-customized-account-main-grid.png" alt-text="Customized grid for account enitity showing text field with green":::

## Available for

Model-driven apps

## Code

You can find the code for sample here: [PowerApps-Samples/component-framework/PowerAppsGridCustomizerControl/](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework/PowerAppsGridCustomizerControl).

The key change is to [PAGridCustomizer/customizers/CellRendererOverrides.tsx ](https://github.com/microsoft/PowerApps-Samples/blob/master/component-framework/PowerAppsGridCustomizerControl/PAGridCustomizer/customizers/CellRendererOverrides.tsx).

This sample uses the following override for the cell renderer to change the text color for text fields to green, and the color of the `creditlimit` column depends on the value.


```typescript
import { Label } from '@fluentui/react';
import * as React from 'react';
import { CellRendererOverrides } from '../types';

export const cellRendererOverrides: CellRendererOverrides = {
    ["Text"]: (props, col) => {
        // Render all text cells in green font
        return <Label style={{ color: 'green' }}>{props.formattedValue}</Label>
    },
    ["Currency"]: (props, col) => {
        // Only override the cell renderer for the CreditLimit column
        if (col.colDefs[col.columnIndex].name === 'creditlimit') {
            // Render the cell value in blue when the value is more than $100,000 and red otherwise
            if ((props.value as number) > 100000) {
                return <Label style={{ color: 'blue' }}>{props.formattedValue}</Label>
            }
            else {
                return <Label style={{ color: 'red' }}>{props.formattedValue}</Label>
            }
        }
    }
}
```

### Related articles

[Customize the editable grid control (Preview)](../customize-editable-grid-control.md)<br/>
[Download sample components](https://github.com/microsoft/PowerApps-Samples/tree/master/component-framework)<br/>
[How to use the sample components](../use-sample-components.md)<br/>
[Power Apps component framework API reference](../reference/index.md)<br/>
[Power Apps component framework manifest schema reference](../manifest-schema-reference/index.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
