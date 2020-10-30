---
title: 'Horizontal container: reference | Microsoft Docs'
description: Information, including properties and examples, about the Horizontal container control
author: emcoope-msft
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: nabuthuk
ms.date: 10/30/2020
ms.author: emcoope-msft
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Horizontal container control 

Horizontal container control determine the position of the child components so that you never have to set X, Y for a component inside the container.

## Description

**Horizontal** container control distribute the available space to its child components based on the settings, as well as determines alignment of the child components.

## Key properties

**[Color](properties-color-border.md)** – The color of text in a control.

**[Font](properties-text.md)** – The name of the family of fonts in which text appears.

**HtmlText** – Text that appears in an HTML text control and that may contain HTML tags.

## Additional properties

**[BorderColor](properties-color-border.md)** – The color of a control's border.

**[BorderStyle](properties-color-border.md)** – Whether a control's border is **Solid**, **Dashed**, **Dotted**, or **None**.

**[BorderThickness](properties-color-border.md)** – The thickness of a control's border.

**[Color](properties-color-border.md)** - The color of the container control.

**[Fill](properties-color-border.md)** – The background color of a control.

**[Height](properties-size-location.md)** – The distance between a control's top and bottom edges.

**Direction** - Defines in what direction the container layouts its child components. **Horizontal** and **Vertical**.

**Justify (vertical)** - Defines how child elements are aligned with the primary axis.**Start**, **End**, **Center**, **Space Between**.

**Align (Horizontal)** - Defines how child components are positioned in the container, in the off axis (opposite from `LayoutDirection`). **Start**, **Center**, **End**, **Stretch**.

**Gap** - Defines the space between containers child components in pixels. 

**Horizontal Overflow** - Defines whether the container shows scrollbars or remove content when it is too large to fit. **Scroll** and **Hide**.

**Vertical Overflow** - Defines whether the container shows scrollbars or remove content when it is too large to fit. **Scroll** and **Hide**.

**Wrap** -  Defines whether the content wraps to a new row or column when it cannot fit.

**Align in container** - Defines how the individual component is aligned to the parent. The default value, **Set by container**, inherits the value from the parent’s `LayoutAlignItems` property, while other properties can be used to customize the alignment for the individual child component. **Set by container**, **Start**, **End**, **Center**, and **Stretch**. 

**Fill portions** - Defines how the individual component grows when there is more screen real-estate assigned to its parent.  The number represents the portion of the extra space given to the component out of all the available extra space claimed by children of its parent.  For example, if child A has `Fill portions` set to 1 and child B has `Fill portions` set to 2, child A gets 1/3 of the extra space available while child B gets 2/3 of the extra available space.

**Minimum width** - Represent the minimum size of the component in the direction of the `Fill portions` (that is, the parent’s `Direction`).

**[PaddingBottom](properties-size-location.md)** – The distance between text in a control and the bottom edge of that control.

**[PaddingLeft](properties-size-location.md)** – The distance between text in a control and the left edge of that control.

**[PaddingRight](properties-size-location.md)** – The distance between text in a control and the right edge of that control.

**[PaddingTop](properties-size-location.md)** – The distance between text in a control and the top edge of that control.

**[Visible](properties-core.md)** – Whether a control appears or is hidden.

**[Width](properties-size-location.md)** – The distance between a control's left and right edges.

**[X](properties-size-location.md)** – The distance between the left edge of a control and the left edge of its parent container (screen if no parent container).

**[Y](properties-size-location.md)** – The distance between the top edge of a control and the top edge of the parent container (screen if no parent container).


## Example

### Screen reader support

### Keyboard support
