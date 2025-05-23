---
title: Handling errors in Power Apps
description: Learn about best practices for error handling in Power Apps
ms.date: 06/12/2024
ms.topic: concept-article
ms.subservice: guidance
ms.service: power-platform
author: robstand
ms.author: rstand
manager: 
---

# Error handling

Power Fx language has a new preview feature to enable Formula level error handling. This is by default turned On in the Settings.

![A screenshot of Upcoming features in Settings showing Formula-level error management is set to On](media/image28.png)

This setting gives access to formulas like `IfError`, `IsError`, `Error`, and `IsBlankorError`. These functions allow you to detect errors, provide alternative values, or take specific actions based on the encountered error.

## Validation Error Handling

Above functions can help with validating inputs such as incorrect format or required fields. Use `If` statements or functions like `IsBlank` and `IsError` to validate user input. Provide clear error messages and prevent further processing until the input is corrected.

```powerappsfl
If( IsBlank(TextInput.Text),
    Notify("Field cannot be blank", 
    NotificationType.Error),
    // Continue with processing
)
```

## Patch Function Error Handling

Similar to the previous example, `Error` functions can help catch errors while patching data to data source. `Patch` function reports errors in 2 ways.

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

Errors can be detected with `IsError` and replaced or suppressed with `IfError`

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

### Forms Error Handling

When using Forms to submit data via `SubmitForm` function, using Form control property `OnFailure` to notify the error message.

```powerappsfl
// OnSelect property of the form's submit button
SubmitForm(frm_SubmitData);

// OnSuccess property of the form
Navigate('Success Screen');

// OnFailure property of the form
Notify("Error: the invoice could not be created", NotificationType.Error);
```

### Custom Error Message with OnError Property

Power Apps `OnError` is a property on your app which lets you capture all your unhandled errors. The `OnError` property gives you the ability to execute an expression that runs every time an error is not handled by the app (such as storing it in a variable or using a function such as `IfError` to replace it with some other value). To use the [`OnError` property](/power-platform/power-fx/reference/object-app#onerror-property), you need to add it to the app that you want to apply it to. Then, you can specify the error message that you want to display by writing a formula in the `OnError` property box.

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
## Next step

> [!div class="nextstepaction"]
> [Monitoring and testing](monitoring-testing.md)
