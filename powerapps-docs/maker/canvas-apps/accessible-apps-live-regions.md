---
title: Announce dynamic changes with live regions for canvas apps
description: How to use live regions to notify screen readers of dynamic changes in canvas apps
author: tahoon-ms
ms.service: powerapps
ms.topic: article
ms.custom: canvas
ms.date: 02/18/2021
ms.author: tahoon
search.audienceType:
  - maker
search.app:
  - PowerApps
contributors:
  - tahoon-ms
  - chmoncay
  - tapanm-msft
---

# Announce dynamic changes with live regions for canvas apps

Dynamic changes pose challenges to the visually-impaired. Users who access an app through a screen reader are focused on one part of the app. If a change happens elsewhere, those users won't be aware of it.

You can solve this problem by adding live regions, which screen readers track. If content changes in a live region, a screen reader will announce that change.

The underlying mechanism for live regions are [aria-live regions](https://www.w3.org/TR/wai-aria-1.1/#dfn-live-region), so the same guidelines apply.

## Example uses of live regions

You can use live regions to notify users when events such as these occur:

* A validation error occurs in a form.
* An action triggered by a button is successful. For example, a user might select a button to add an item to a collection, and a live region could show the message "Item added".
* The user selected a different tab.
* A background timer refreshes a news feed.

## Create and configure a live region

You can configure only a **[Label](controls/control-text-box.md)** control as a live region. Its **Live** property determines what type of live region it is.

* **Off**: Not a live region. Screen readers don't announce changes.
* **Polite**: Screen readers announce changes after finishing speaking. Use this value for non-critical notifications that don't require immediate attention.
* **Assertive**: Screen readers interrupt themselves to announce changes immediately. Use this for critical notifications that require immediate attention.

If the text content of a live region changes, screen readers will announce the entire text content, not just the changed portion. If the value of the **[Text](controls/properties-core.md)** property is set to the empty string **""**, the screen reader doesn't announce anything.

To repeat a message, clear text contents by setting the value of the **[Text](controls/properties-core.md)** property to the empty string **""** and then set the value to the message again.

## Best practices

* Always set **[Visible](controls/properties-core.md)** to true. Some screen readers don't detect live regions that disappear and reappear.
* Avoid changing the value of **[Live](controls/properties-accessibility.md)**. Some screen readers don't detect when a non-live region becomes live and vice-versa.
* Position the live region in a logical position in the app, even if it isn't visible. Ensure that its contents are sensible in context with the elements before and after it. Users can access a live region anytime through regular navigation with a screen reader, not just when changes happen.

## Next steps

[Use the Accessibility checker](accessibility-checker.md)

### See also

- [Create accessible apps](accessible-apps.md)
- [Accessible app structure](accessible-apps-structure.md)
- [Accessible colors in Power Apps](accessible-apps-color.md)
- [Show or hide content from assistive technologies for canvas apps](accessible-apps-content-visibility.md)
- [Accessibility limitations in canvas apps](accessible-apps-limitations.md)
- [Accessibility properties](controls/properties-accessibility.md)
