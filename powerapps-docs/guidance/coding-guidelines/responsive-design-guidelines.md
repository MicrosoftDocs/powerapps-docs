---
title: Responsive design guidelines in Power Apps
description: Learn best practices for designing responsive, accessible canvas apps that adapt to different screen sizes and orientations.
#customer intent: As a Power Apps maker, I want to design a responsive canvas app so that people can use it across supported devices and screen sizes.
ms.date: 08/28/2026
ms.topic: best-practice
author: robstand
ms.author: rachaudh
ms.reviewer: edoyle
---

# Responsive design guidelines

Responsive canvas apps adapt their layout and navigation to the available viewport instead of scaling a fixed canvas. Design responsive behavior intentionally so that the app remains usable in every supported window size, device orientation, zoom level, and input mode.

Each of the following guidelines is aimed at ensuring your canvas app provides an optimal user experience, regardless of the device's screen size or orientation. These guidelines address one of the most critical aspects of modern app development. These guidelines are instrumental for developers looking to enhance the accessibility and user engagement of their Power Apps.

## Adapt to screen sizes

Canvas apps should be designed to automatically adjust their layout and interface based on the device's screen size. This responsiveness ensures that the app remains functional and visually appealing across various devices, from smartphones to desktop computers.

## Use auto-layout containers

Use horizontal and vertical auto-layout containers as the primary structure for a responsive screen. These containers dynamically organize and align app components, making sure they respond effectively to changes in screen dimensions.

### Disable *Scale to Fit* and manage aspect ratio and orientation

Turn off the **Scale to Fit** setting to enable true app responsiveness. This setting prevents scaling and promotes natural layout adaptation to various screen sizes. Also, adjust the aspect ratio and **Lock Orientation** settings. These adjustments ensure that the app's layout effectively responds to different screen sizes and orientations. The app maintains a consistent and functional interface whether the device is in portrait or landscape mode.

### Use responsive layouts

Use layout designs like split-screen and sidebar, which offer different user experiences on various devices. This adaptability enhances the app's functionality, making it more intuitive for users on any device.

### Use formulas for dynamic layout

Use formulas instead of fixed coordinates for positioning and sizing controls. This approach ensures they adapt to changes in screen dimensions for a dynamic, responsive layout.

### Plan for various devices

Effective responsive design involves anticipating how the app looks and functions on different devices. This anticipation includes decisions about resizing elements or hiding them entirely on smaller screens to optimize space and maintain usability.

### Practical implementation

Transforming a nonresponsive canvas app into a responsive one requires a systematic approach. This approach involves adjusting settings for responsiveness and carefully configuring container properties to ensure elements within the app adapt to different screen sizes.

## Resources

- [Create responsive layouts in canvas apps](../../maker/canvas-apps/create-responsive-layout.md)
- [Building responsive canvas apps](../../maker/canvas-apps/build-responsive-apps.md)
- [Organize controls in accessible canvas apps](../../maker/canvas-apps/accessible-apps-structure.md)
- [Review a canvas app for accessibility](../../maker/canvas-apps/accessibility-checker.md)
- [Overview of modern controls and themes in canvas apps](../../maker/canvas-apps/controls/modern-controls/overview-modern-controls.md)
- [Recent updates to modern controls in canvas apps](../../maker/canvas-apps/controls/modern-controls/modern-control-updates.md)
- [Recommendations for optimizing layout](/power-platform/well-architected/experience-optimization/layout)

## Next step

> [!div class="nextstepaction"]
> [Code readability](code-readability.md)
