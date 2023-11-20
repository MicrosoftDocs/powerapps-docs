The `pfx-default-value` property value enables using PFX expressions to evaluate events and properties instead of static default values. This can be used for:

- Responsively sizing the control
- Accessing connectors
- Providing sample data
- Referencing theme properties
- Custom events

> [!NOTE]
> - Any PFX can be used, but it is up to the developer to make sure the PFX expression is valid when importing the control.
> - If using inner quotes or other special characters, it is best to wrap the value in single quotes, For example: `pfx-default-value='"Test"'`
> - Other controls (including screens) and their properties can be referenced, but it must be written as: `%ControlName.ID%.ControlProperty`. For example: `pfx-default-value='SubmitForm(%MyFormName.ID%)'`
> - Enums, like DisplayType and ScreenTransition, must be written as: `%EnumName.RESERVED%.EnumValue`. For example: `pfx-default-value='Back(%ScreenTransition.RESERVED%.Cover)'`
> - If `pfx-default-value` is included, then it takes precedence over `default-value`.
