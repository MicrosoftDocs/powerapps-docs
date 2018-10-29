---
title: Announce dynamic changes with live regions | Microsoft Docs
description: How to use live regions to notify screen readers of dynamic changes in canvas apps
author: tahoon
ms.service: powerapps
ms.topic: article
ms.custom: canvas
ms.date: 10/22/2018
ms.author: tahoon
search.audienceType:
  - maker
search.app:
  - PowerApps
---
# Announce dynamic changes with live regions for canvas apps in PowerApps
Dynamic changes pose challenges to the visually-impaired. When using a screen reader to access the app, they will be focused on one part of the app. If a change happens elsewhere, they will not be aware of it.

Live regions can solve this problem. These are regions in an app that are tracked by screen readers. When content changes in these regions, screen readers will announce them.

The underlying mechanism for live regions are [aria-live regions](https://www.w3.org/TR/wai-aria-1.1/#dfn-live-region), so the same guidelines apply.

## Example uses of live regions
* Notify users about validation errors in a form.
* Notify users when an action triggered by a button is successful. For example, if selecting a button adds an item to a collection, a live region could show the message "Item added".
* Notify users when a new tab is selected.
* Periodically notify users when a background timer refreshes a news feed.

## Create and configure a live region
Only the **[Label](controls/control-text-box.md)** control can be configured as a live region. Its **Live** property determines what type of live region it is.
* **Off**: Not a live region. Changes are not announced to screen readers.
* **Polite**: Dynamic changes are announced when the screen reader has finished speaking. Used for non-critical notifications that do not require immediate attention.
* **Assertive**: Dynamic changes are immediately announced, interrupting any current utterances by the screen reader. Use this for critical notifications that require immediate attention.

Screen readers will announce the entire text content of a live region when it changes, not just the changed portion. If **[Text](properties-core.md)** is set to the empty string **""**, then nothing will be announced.

To repeat a message, clear text contents by setting **[Text](properties-core.md)** to the empty string **""**, then set it to the message again.

## Best practices
* Always set **[Visible](controls/properties-core.md)** to true. Some screen readers do not detect live regions if they disappear and appear again.
* Avoid changing the value of **[Live](controls/properties-accessibility.md)**. Some screen readers do not detect when a non-live region becomes live and vice-versa.
* Position the live region in a logical position in the app, even if it is not visible visually. Ensure that its contents are sensible in context with the elements before and after it. Live regions are accessible anytime through regular navigation with a screen reader, not just when changes happen.

## Next steps
Learn how to [show content to screen readers only](accessible-apps-content-visibility.md) if the live region should be hidden from sighted users.
