---
title: Accessibility properties | Microsoft Docs
description: Reference information about properties such as TabIndex, Tooltip
author: fikaradz
manager: kvivek
ms.service: powerapps
ms.topic: reference
ms.custom: canvas
ms.reviewer: anneta
ms.date: 01/26/2017
ms.author: fikaradz
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Accessibility properties in PowerApps
Configuration of properties that aid alternative ways of interacting with controls suitable for users with disabilities.

### Properties
**AccessibleLabel** – Label for screen readers. An empty value for Image, Icon and Shape controls will make the controls invisible to the screen reader and treated as decorations.

**Live** – How changes to content should be announced to screen readers. Only available in **[Label](control-text-box.md)** control.
* When set to **Off**, changes are not announced to screen readers.
* When set to **Polite**, dynamic changes are announced when the screen reader has finished speaking.
* When set to **Assertive**, dynamic changes are immediately announced, interrupting any current utterances of the screen reader.
Learn how to [announce dynamic changes with live regions](../accessible-apps-live-regions.md).

**TabIndex** –  Keyboard navigation order in relation to other controls.

Default value of zero specifies default tab order, based on control's XY coordinate.  Setting a value higher than zero will move the control's tab order ahead of all controls with the default values.  A control with TabIndex value of 2 will precede one with TabIndex of 3 or higher when tabbed.

Note that containers such as Form and Gallery controls will always tab through all elements of the container before proceeding to controls outside of the container.  The container's tab order is that of the lowest value TabIndex of a child control.

Setting TabIndex to -1 will disable tab access to the control; in case of Images, Icons and Shapes, they will be made non-interactive elements.
