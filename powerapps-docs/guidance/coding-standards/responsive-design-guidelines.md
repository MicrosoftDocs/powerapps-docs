---
title: Responsive design
description: Responsive design
ms.date: 04-15-2024
ms.topic: conceptual
ms.service: powerapps
author: robstand
ms.author: rstand
manager: 
---

# Responsive Design Guidelines

In the section on responsive design guidelines for Canvas apps in Power Apps, we delve into essential strategies and practices for creating applications that adapt seamlessly across various devices. This section encompasses key principles ranging from screen adaptation techniques to container utilization, settings adjustments, and detailed implementation steps. Each guideline is aimed at ensuring your Canvas app provides an optimal user experience, regardless of the device's screen size or orientation, thereby addressing one of the most critical aspects of modern app development. These guidelines are instrumental for developers looking to enhance the accessibility and user engagement of their Power Apps.

1. **Adapt to Screen Sizes**: Canvas apps should be designed to automatically adjust their layout and interface based on the device's screen size. This responsiveness ensures that the app remains functional and visually appealing across various devices, from smartphones to desktop computers.

2. **Use Containers**: Incorporate horizontal and vertical containers in app design. These containers are pivotal in dynamically organizing and aligning app components, making sure they respond effectively to changes in screen dimensions.

3. **Disable 'Scale to Fit' and Manage Aspect Ratio/Orientation:** It's vital to turn off the 'Scale to Fit' setting for enabling true app responsiveness, as this prevents mere scaling and promotes natural layout adaptation to various screen sizes. Additionally, adjusting the aspect ratio and 'Lock Orientation' settings is crucial. These adjustments ensure that the app's layout effectively responds to different screen sizes and orientations, maintaining a consistent and functional interface whether the device is in portrait or landscape mode.

4. **Responsive Layouts**: Utilize layout designs like split-screen and sidebar, which offer different user experiences on various devices. This adaptability enhances the app's functionality, making it more intuitive for users on any device.

5. **Use Formulas for Dynamic Layout**: Utilize formulas instead of fixed coordinates for positioning and sizing controls, ensuring they adapt to changes in screen dimensions for a dynamic, responsive layout.

6. **Plan for Various Devices**: Effective responsive design involves anticipating how the app will look and function on different devices. This includes decisions about resizing elements or hiding them entirely on smaller screens to optimize space and maintain usability.

7. **Practical Implementation**: Transforming a non-responsive Canvas app into a responsive one requires a systematic approach. This involves adjusting settings for responsiveness and carefully configuring container properties to ensure elements within the app adapt to different screen sizes.


