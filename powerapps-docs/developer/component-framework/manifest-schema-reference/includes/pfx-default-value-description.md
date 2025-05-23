Use the `pfx-default-value` property value to evaluate events and properties using Power Fx expressions instead of static default values. You can use this to:

- Responsively size the control
- Access connectors
- Provide sample data
- Reference theme properties
- Custom events

> [!NOTE]
> - You can use any Power Fx expression, but you must make sure the expression is valid when importing the control.
> - If you use inner quotes or other special characters, wrap the value in single quotes, For example: `pfx-default-value='"Test"'`
> - You can reference other controls (including screens) and their properties. Write these references as: `%ControlName.ID%.ControlProperty`. For example: `pfx-default-value='SubmitForm(%MyFormName.ID%)'`
> - Write enums, like `DisplayType` and `ScreenTransition`  as: `%EnumName.RESERVED%.EnumValue`. For example: `pfx-default-value='Back(%ScreenTransition.RESERVED%.Cover)'`
> - If `pfx-default-value` is included, then it takes precedence over `default-value`.
