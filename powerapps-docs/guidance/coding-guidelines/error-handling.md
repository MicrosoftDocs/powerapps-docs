---
title: Handling errors in Power Apps
description: Discover best practices for error handling in Power Apps, including validation, patching, and custom error messages.
ms.date: 02/25/2026
ms.topic: concept-article
ms.subservice: guidance
ms.service: powerapps
author: robstand
ms.author: rstand
ms.custom:
  - ai-gen-docs-bap
  - ai-gen-description
  - ai-seo-date:07/15/2025
---

# Error handling

Power Fx supports formula-level error handling. This feature is turned on by default for all new apps. However, some older apps might have it turned off in app **Settings**. We recommend keeping this feature turned on.

1. You can check by opening a canvas app for editing.
1. Go to **Settings** > **Updates** > **Retired** tab.
1. Make sure **Disable formula-level management** is turned off.


When this setting is enabled, you can use formulas like `IfError`, `IsError`, `Error`, and `IsBlankorError`. These functions help you detect errors, provide alternative values, or take specific actions based on the error. When you turn on this setting, you can write null or blank values to data sources. When you turn off this feature, errors are returned as blank values.

## Validation error handling

These functions help validate inputs like incorrect formats or required fields. Use `If` statements or functions like `IsBlank` and `IsError` to validate user input. Provide clear error messages and prevent further processing until the input is corrected.

```powerappsfl
If( IsBlank(TextInput.Text),
    Notify("Field cannot be blank", 
    NotificationType.Error),
    // Continue with processing
)
```

## Patch function error handling

Similar to the previous example, `Error` functions help catch errors while patching data to a data source. The `Patch` function reports errors in two ways.

It can return an error value as the result of the operations.

```powerappsfl
UpdateContext(
    {   
    result : Patch(
             Feeds,
             Defaults(Feeds),
             {
                 createdon: Now(),
                 crde8_content: TextInput1_1.Text
                 cr9ce_imageurl: filename
             }
        )
    }
)
```

You can detect errors by using `IsError` and replace or suppress them by using `IfError`.

```powerappsfl
IfError(result, Notify("There was an issue saving data" , NotificationType.Error));
IfError(result, Notify("There was an issue saving data" , & FirstError.Message, NotificationType.Error))

If(
    IsError(
        Patch(
            Feeds,
            Defaults(Feeds),
            {
                createdon: Now(),
                crde8_content: TextInput1_1.Txt,
                cr9ce_imageurl: filename        
            }
        )
    ),
    Notify("Error: There was an issue saving data", NotificationType.Error)
)
```

### Forms error handling

When you use Forms to submit data by using the `SubmitForm` function, use the Form control property `OnFailure` to notify users of error messages.

```powerappsfl
// OnSelect property of the form's submit button
SubmitForm(frm_SubmitData);

// OnSuccess property of the form
Navigate('Success Screen');

// OnFailure property of the form
Notify("Error: the invoice could not be created", NotificationType.Error);
```

### Custom error message by using the OnError property

The Power Apps `OnError` property captures all unhandled errors in your app. By using the `OnError` property, you can run an expression every time the app encounters an unhandled error. For example, you can store the error in a variable or use a function like `IfError` to replace the error with another value. To use the [`OnError` property](/power-platform/power-fx/reference/object-app#onerror-property), add it to the app where you want to handle errors. Then, write a formula in the `OnError` property box to specify the error message you want to display.

`App.OnError` can't replace the error like `IfError` can. When `App.OnError` runs, the error already happened and the result already went through other formulas. `App.OnError` only controls how the error is reported to the end user. It also provides a way for the maker to log the error if they want.

This code on `App.OnError` can help locate the source of the error:

```powerappsfl
Notify(
    Concatenate(
        FirstError.Message,
        ", Observed: ",
        FirstError.Observed,
        ", Source: ",
        FirstError.Source
    ),
    NotificationType.Error
)
```

## Related information

[Power Fx error handling](/power-platform/power-fx/error-handling)

## Next step

> [!div class="nextstepaction"]
> [Monitoring and testing](monitoring-testing.md)
