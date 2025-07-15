---
title: Handling errors in Power Apps
description: Discover best practices for error handling in Power Apps, including validation, patching, and custom error messages.
ms.date: 07/15/2025
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

Power Fx includes a preview feature that enables formula-level error handling. By default, this feature is turned on in Settings.

:::image type="content" source="media/image28.png" alt-text="Screenshot of Upcoming features in Settings showing Formula-level error management set to On.":::

This setting provides access to formulas like `IfError`, `IsError`, `Error`, and `IsBlankorError`. These functions allow you to detect errors, provide alternative values, or take specific actions based on the error.

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

You can detect errors with `IsError` and replace or suppress them with `IfError`.

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

When you use Forms to submit data with the `SubmitForm` function, use the Form control property `OnFailure` to notify users of error messages.

```powerappsfl
// OnSelect property of the form's submit button
SubmitForm(frm_SubmitData);

// OnSuccess property of the form
Navigate('Success Screen');

// OnFailure property of the form
Notify("Error: the invoice could not be created", NotificationType.Error);
```

### Custom error message with OnError property

The Power Apps `OnError` property lets you capture all unhandled errors in your app. The `OnError` property gives you the ability to execute an expression that runs every time an error isn't handled by the app (such as storing it in a variable or using a function such as `IfError` to replace it with some other value). To use the [`OnError` property](/power-platform/power-fx/reference/object-app#onerror-property), you need to add it to the app that you want to apply it to. Then, you can specify the error message that you want to display by writing a formula in the `OnError` property box.

It's important to note that `App.OnError` can't replace the error in the same way that `IfError` can. At the point that `App.OnError` is executed, the error has already happened, and the result has propagated through other formulas. `App.OnError` only controls how the error is reported to the end user and provides a hook for the maker to log the error if desired.

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
