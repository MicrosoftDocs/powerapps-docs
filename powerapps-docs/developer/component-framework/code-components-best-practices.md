---
title: Code components best practices  | Microsoft Docs
description: Best practices and guidance on how to use code components
keywords:
ms.author: nabuthuk
author: Nkrb
manager: kvivek
ms.date: 06/28/2021
ms.service: "powerapps"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 5d100dc3-bd82-4b45-964c-d90eaebc0735
---


# Best practices and guidance for code components

Developing, deploying, and maintaining code components needs a combination of knowledge that includes the following:

- Power Apps component framework
- Microsoft Power Apps
- Microsoft Dataverse
- TypeScript & JavaScript
- HTML Browser User Interface Development
- Azure DevOps/GitHub

This article outlines established best practices and guidance for professional developers developing code components and aims to provide the rational and benefits behind each, so that your code components can benefit from the usability, supportability, and performance improvements that they provide.

## Power Apps component framework

This section contains best practice and guidance relating to the Power Apps component framework itself.

#### Avoid deploying development builds to Dataverse

Code components can be built in [production or development mode](code-components-alm.md#building-pcfproj-code-component-projects). Avoid deploying development builds to Dataverse since they adversely affect performance and can even be blocked from deployment due to their size. Even if you plan to deploy a release build later, it can be easy to forget to redeploy if you do not have an automated release pipeline. Instead, use the techniques described in [Debugging custom controls](debugging-custom-controls.md).

#### Avoid using unsupported framework methods

These may include using undocumented internal functions that exist on the `ComponentFramework.Context`. These methods may work but because they are not supported, they may stop working in future versions.

#### Use `init` method to request network required resources

When a code component is loaded by the hosting context, the [init](reference\control\init.md) method is first called. Use this method to request any network resources such as metadata instead of waiting until the `updateView` method. If the `updateView` method is called before the requests return, your code component must handle this state and provide a visual loading indicator.

#### Clean up resources inside the `destroy` method

When a code component is removed from the browser DOM, the [destroy](reference\control\destroy.md) method is called. Use this method to close any `WebSockets`, remove  event handlers that are added outside of the container element. If you are using React, use `ReactDOM.unmountComponentAtNode` inside the destroy method. This prevents any performance issues caused by code components being loaded and unloaded within a given browser session.

#### Avoid unnecessary calls to refresh on a dataset property

If your code component is of type dataset, the bound dataset properties expose a [`refresh`](reference\dataset\refresh.md) method that causes the hosting context to reload the data. Calling this method more adversely affects your code components performance.

#### Minimize calls to `notifyOutputChanged` 

In some circumstances, it is undesirable for updates to a UI control (such as keypresses or mouse move events) to each call `notifyOutputChanged` this would result in many more events propagating to the parent context than needed. Instead, consider using an event when a control loses focus, or when the user's touch or mouse event has completed.

#### Check API availability

When developing code components for different hosts (model-driven, canvas, portals) always check the availability of the APIs you are using for support on those platforms. For example, `context.webAPI` is not available in canvas apps. For individual API availability,  see [Power Apps component framework API reference](reference/index.md).

## Model-driven apps

This section contains best practice and guidance relating to code components within model-driven apps.

#### Do not interact directly with formContext

If you have developed model-driven JavaScript web resources you may be used to accessing the model-driven formContext to access attributes, controls, and call API methods such as `save`, `refresh` and `setNotification`. Code components are expected to work across various products like model-driven apps, canvas apps, dashboards. Hence, they cannot have a dependency on formContext. A work-around is to make the code component bound to a column and add an `OnChange` event handler to that column. The code component can update the column value, and the `OnChange` event handler can access the form context. Support for the custom events will be added in the future, which will be able to be used for communicating changes outside of a control without adding a column configuration.

#### Limit size and frequency of calls to the WebApi

When using the `context.WebApi` methods, limit both the number of calls and amount of data that is interacted with. Each time you call the WebApi it will count towards the user's API entitlement and service protection limits. When performing CRUD operations on records, consider the size of the payload. In general, larger the request payload, the slower your code component will be.

## Canvas apps

This section contains best practice and guidance relating to code components within canvas apps.

#### Minimize the number of controls on a screen

Each time you add a control to your canvas app it takes a finite amount of time to render. The more controls you add, the longer the render time will be. Carefully measure performance of your code components as you add more to a screen using the Developer Tools Performance tools. 

At this time, each code component will bundle their own library of shared libraries such as Fluent UI and React. Loading multiple instances of the same library will not load these libraries multiple times, however loading multiple different code components will result in the browser loading multiple bundled versions of these libraries. In the future, these libraries will be able to be loaded and shared with code components.

#### Allow makers to style your code component

When app makers consume code components from inside a canvas app, they will want to use a style that matches the rest of their app. Use input properties to provide customization options for theme elements such as color and size. When using Microsoft Fluent UI, map these properties to the theme elements provided by the library. In the future, theming support will be added to code components to make this process easier. 

#### Follow canvas apps performance best practices

Canvas apps provides a wide set of best practices from inside the app and solution checker. Ensure your apps follow these recommendations before you add code components. More information:

- [Tips to improve canvas app performance](/powerapps/maker/canvas-apps/performance-tips)
- [Considerations for optimized performance in Power Apps](https://powerapps.microsoft.com/blog/considerations-for-optimized-performance-in-power-apps/)

## TypeScript and JavaScript

This section contains best practice and guidance relating to TypeScript & JavaScript within code components.

#### ES5 vs ES6

By default, code components target ES5 to support older browsers (for example, Internet Explorer 11). If you do not need to support these older browsers, you can change the target to ES6 inside your `pcfproj` folder's `tsconfig.json`. More information: [ES5 vs ES6](debugging-custom-controls.md#es5-vs-es6).

#### Module imports

Always bundle the modules that you require as part of your code component instead of using scripts that are required to be loading using a `SCRIPT` tag. For example, if you wanted to use a third party charting API where the sample shows adding  `<script type="text/javascript" src="somechartlibrary.js></script>` to the page, this would not be supported inside a code component. Bundling all of the required modules both isolates the code component from other libraries and also supports running in offline mode.

> [!NOTE]
> Support for shared libraries across components using library nodes in the component manifest is not yet supported. We are reviewing this and will be adding this capability in future release.

#### Linting

Linting is where a tool to scan code for potential issues. The template used by `pac pcf init` installs the `eslint` module to your project and configures it by adding an `.eslintrc.json` file. `Eslint` requires configuring for TypeScript and React coding styles. It can also be used to fix some of these issues automatically where possible. To configure, at the command-line use:

```shell
npx eslint --init
```

Then answer the following questions when prompted:

- How would you like to use `ESLint`?
  Answer: **To check syntax, find problems, and enforce code style**

- What type of modules does your project use?
  Answer: **JavaScript modules (import/export)**

- Which framework does your project use?
  Answer: **React**

- Does your project use TypeScript? 
  Answer: **Yes**

- Where does your code run?
  Answer: **Browser**

- How would you like to define a style for your project?
  Answer: **Answer questions about your style**

- What format do you want your config file to be in?
  Answer: **JSON** (This will update the existing `.eslintrc.json`)

- What style of indentation do you use?

  Answer: **Spaces** (This is the VSCode default)

- What quotes do you use for strings?
  Answer: **Single**

- What line endings do you use?
  Answer: **Windows** (This is the VSCode default CRLF line endings style)

- Do you require semicolons?
  Answer: **Yes**

> [!NOTE]
>
> You can customize this configure to suit your particular needs (for example, if you are not using React). More information: [Getting started with ESLint](https://eslint.org/docs/user-guide/getting-started).

Before you can run `eslint`, you need to add some scripts to the `package.json`:

```json
 "scripts": {
    ...
    "lint": "eslint MY_CONTROL_NAME --ext .ts,.tsx",
    "lint:fix": "npm run lint -- --fix"
  }
```


The `eslint` script accepts the folder that contains your code - replace **MY_CONTROL_NAME** to be the same name as the code component used when calling `pac pcf init`. 

Now at the command-line you can use:

```shell
npm run lint:fix
```

This will tidy up code in the project to match your chosen style, and it will also report some issues that we will resolve later.

> [!NOTE]
> ESLint will point out problems with the template code initially (e.g. empty constructor). You can add inline comments to instruct ESLint to exclude the rules such as:
>
> `// eslint-disable-next-line @typescript-eslint/no-empty-function`
>
> Additionally, you can add files to ignore (for example, the automatically generated interfaces), by adding the following to the `.eslintrc.json`:
> ```
> "ignorePatterns": ["**/generated/*.ts"]
> ```
> More information: [ignorePatterns in config files](https://eslint.org/docs/user-guide/configuring/ignoring-code#ignorepatterns-in-config-files).

> [!TIP]
> You can install Visual Studio Code extension that will use the project's `.eslintrc.json` file to provide code highlighting of any issues detected, with the option to fix them directly inside the IDE. More information: [Managing Extensions in Visual Studio Code](https://code.visualstudio.com/docs/editor/extension-marketplace).


## HTML browser user interface development

This section contains best practice and guidance relating to HTML browser user interface development.

### Use Microsoft Fluent UI React

[Fluent UI React](https://developer.microsoft.com/fluentui#/get-started/web) is the official [open source](https://github.com/microsoft/fluentui) React front-end framework designed to build experiences that fit seamlessly into a broad range of Microsoft products. Power Apps itself uses Fluent UI, meaning you will be able to create UI that is consistent with the rest of your apps.

#### Use path-based imports from fluent to reduce bundle size

At this time, the code component templates used with `pac pcf init` will not use tree-shaking, which is the process where `webpack` will detect where there are modules imported that are not used and remove them. This means if you import from Fluent UI using the following, it will import and bundle the entire library:

```typescript
import { Button } from '@fluentui/react'
```

To avoid this you can use path-based imports, where the specific library component is imported using the explicit path:

```typescript
import { Button } from '@fluentui/react/lib/Button';
```

This reduces your bundle size both in development and release builds.

You can take advantage of tree shaking (which only affects release/production builds) by updating your `tsconfig.json` to use the following module configuration inside the `compilerOptions` section:

```json
"module": "es2015",
"moduleResolution": "node"
```

More information: [Fluent UI - Advanced usage](https://github.com/microsoft/fluentui/wiki/Advanced-Usage).

#### Optimize React rendering

When using React it is important to follow React specific best practices regarding minimizing rendering of components, resulting in a more responsive user interface. Some of these best practices are:

- Only make a call to `ReactDOM.render` inside the `updateView` method when a bound property or framework aspect has changed that requires the user interface to reflect the change. You can use [updatedProperties](reference\updatedproperties.md) to determine which have changed.
- Use [PureComponent](https://reactjs.org/docs/react-api.html#reactpurecomponent) (with class components) or [React.memo](https://reactjs.org/docs/react-api.html#reactmemo) (with function components) where possible to avoid unnecessary re-renders of components when its input props have not mutated.
- For large React components, deconstruct your user interface into smaller components to improve performance.
- Avoid use of arrow functions and function binding inside the render function as this will create a new callback closure with each render and cause the child component to always re-render when the parent component is rendered. Instead use function binding in the constructor or use class field arrow functions. See [Handling Events - React](https://reactjs.org/docs/handling-events.html).

#### Check accessibility

Ensure that code components are accessible and can be used by keyboard only and screen-reader users:

- Provide keyboard navigation alternatives to mouse/touch events. For example, if your component provides a drop-down list, ensure that a user can use tab to set focus and then navigate the options using the arrow keys.
- Ensure that `alt` and [ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA) (Accessible Rich Internet Applications) attributes are set so that screen readers will announce an accurate representation of the code components interface. The Microsoft Fluent UI library makes this easy since many of the components are already accessible and screen reader compatible. 
- Modern browser developer tools today have good tools to inspect accessibility. Use these tools to look for common accessibility issues with your code component.

More information: [Create accessible canvas apps in Power Apps](/powerapps/maker/canvas-apps/accessible-apps).

#### Always use asynchronous network calls

When making network calls, never use a synchronous blocking request since this causes the app to stop responding and cause slow performance. More information: [Interact with HTTP and HTTPS resources asynchronously](/powerapps/developer/model-driven-apps/best-practices/business-logic/interact-http-https-resources-asynchronously).

#### Write code for multiple browsers

Model-driven apps, canvas apps and portals all support multiple browsers. Be sure to use only techniques that are supported on all modern browsers, and test with a representative set of browsers for your intended audience. Support for Internet Explorer 11 is set for removal, however at this time it still may be in use by some users.

- [Limits and configurations](/powerapps/maker/canvas-apps/limits-and-config)
- [Supported web browsers](https://docs.microsoft.com/power-platform/admin/supported-web-browsers-and-mobile-devices)
- [Browsers used by office](https://docs.microsoft.com/office/dev/add-ins/concepts/browsers-used-by-office-web-add-ins)

#### Code components should plan for supporting multiple clients & screen formats

Code components can be rendered in multiple clients (model-driven apps, canvas apps, portals) & screen formats (mobile, tablet, web). When used in model-driven apps, dataset code components can be placed on main-form grids, related record grids, subgrids, or dashboards. When used in canvas apps, code components can be placed inside responsive containers that resize dynamically using configuration provided by the app maker.

- Using  [`trackContainerResize`](reference\mode\trackcontainerresize.md) allows code components to respond to changes in the available width and height. In some cases, this may mean rendering a different user interface that fits the space available. Using `allocatedHeight` and `allocatedWidth` can be combined with [`getFormFactor`](reference\client\getformfactor.md) to determine if the code component is running on a Mobile, Tablet or Web client. For an example of this, see the [Choices Picker sample](tutorial-create-model-driven-field-component.md) that renders using a drop-down instead of the icon choice picker when on narrow or mobile form factors. 
- Implementing [`setFullScreen`](reference\mode\setfullscreen.md) allows users to expand to use the entire available screen available where space is limited. For an example of this, see the [Canvas App Grid sample](tutorial-create-canvas-dataset-component.md).
- If a code component cannot provide a meaningful experience in the given container size, it should disable functionality appropriately and provide feedback to the user.

#### Always use scoped CSS rules

When you implement styling to your code components using CSS, ensure that the CSS is scoped to your control using the automatically generated CSS classes applied to the container `DIV` element for your component. If your CSS is scoped globally, it will likely break the existing styling of the form or screen where the code component is rendered. If using a third-party CSS framework, use a version of that framework that is already namespaced or otherwise wrap that framework in a namespace manually either by hand or using a CSS preprocessor.

For example, if your namespace is `SampleNamespace` and your code component name is `LinearInputComponent`, you would add a custom CSS rule using:

```css
.SampleNamespace\.LinearInputComponent rule-name
```

#### Avoid use of web storage objects

Code components should not use the HTML web storage objects, like `window.localStorage` and `window.sessionStorage`, to store data. Data stored locally on the user's browser or mobile client is not secure and not guaranteed to be available reliably.

## ALM/Azure DevOps/GitHub

See the article on [Code Component Application Lifecycle Management (ALM)](code-components-alm.md) for best practices on code components with ALM/Azure DevOps/GitHub.

## Related topics

[What are code components](custom-controls-overview.md)<br/>
[Code components for canvas apps](component-framework-for-canvas-apps.md)<br/>
[Create and build a code component](create-custom-controls-using-pcf.md)<br/>
[Learn Power Apps component framework](/learn/paths/use-power-apps-component-framework)<br/>
[Use code components in Power Apps portals](../../maker/portals/component-framework.md)
