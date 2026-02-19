---
title: Migrate to modern controls in canvas apps - Power Apps
description: Overview of breaking changes when migrating from the previous modern controls to the new modern controls in Power Apps canvas apps.
author: yogeshgupta698
ms.topic: overview
ms.custom: canvas
ms.date: 02/18/2026
ms.subservice: canvas-maker
ms.author: yogupt
ms.reviewer: mkaur
search.audienceType:
  - maker
---

# Migrate to modern controls in canvas apps

This article provides a high-level summary of changes across all nine modern controls being updated in this release. These controls replace the previous implementations with improved performance, bug fixes, and enhanced functionality.

> [!IMPORTANT]
> If your app uses any of these controls, review the per-control migration guides for detailed formula update instructions.

## Identifying controls that need updates

When you open an app that uses the previous version of a modern control, you'll see a notification on the control indicating that an update is available. The notification will include:

- A message indicating this is the previous version of the control
- A **Learn more** link that directs you to the migration documentation for that control
- An **Update** button (when available) that upgrades the control to the new version

**Before updating a control:**
1. Click the **Learn more** link to read the migration guide for that specific control
2. Review the breaking changes, property renames, and behavioral differences
3. Identify any formulas in your app that reference renamed or removed properties
4. Update your formulas according to the migration guide
5. Click the **Update** button to upgrade the control
6. Test your app thoroughly after updating

> [!NOTE]
> The **Update** button may not be available for all controls immediately. When available, it will appear alongside the **Learn more** link in the control notification.

## Which controls are updated?

| Control | Migration guide | Key changes |
|---------|----------------|-------------|
| Text | [Migrate Text control](Text/text-migration.md) | 9 property renames, enum values, new OnSelect event, DisplayMode removed |
| Number Input | [Migrate Number Input](Number%20Input/number-input-migration.md) | OnChange on blur + step clicks, TriggerOutput removed, new styling properties |
| Date Picker | [Migrate Date Picker](Date%20Picker/date-picker-migration.md) | View mode fixed, format honored, DateTimeZone respected, gallery crash fixed |
| Text Input | [Migrate Text Input](Text%20Input/text-input-migration.md) | OnChange on focus out only, TriggerOutput default = OnKeypress, View mode truly read-only |
| Tab List | [Migrate Tab List](Tab%20List/tab-list-migration.md) | New Appearance property, item order preserved, Items auto-refresh |
| Combo Box | [Migrate Combo Box](Combo%20Box/combo-box-migration.md) | SelectMultiple default = true, toggle to unselect, OnChange fires on every selection |
| Radio | [Migrate Radio](Radio/radio-migration.md) | Item order preserved, View mode read-only (not disabled), new styling properties |
| Link | [Migrate Link](Link/link-migration.md) | URL security validation (XSS protection), FontWeight fix, Wrap fix |
| Info Button | [Migrate Info Button](Info%20Button/info-button-migration.md) | Content flyout expansion fixed, click reliability improved, AcceptsFocus removed |

## Common changes across all controls

### Property renames

The following property renames apply to most or all controls:

| Old name (Previous) | New name (New) | Affected controls |
|---------------------|----------------|-------------------|
| `FontColor` | `Color` | Text, Link, Info Button, Radio, Text Input, Tab List, Number Input, Date Picker, Combo Box |
| `FontSize` | `Size` | Text, Link, Info Button, Radio, Text Input, Tab List, Number Input, Date Picker, Combo Box |
| `FontItalic` | `Italic` | Text, Link, Info Button, Radio, Text Input, Tab List, Date Picker, Combo Box |
| `FontStrikethrough` | `Strikethrough` | Text, Link, Info Button, Radio, Text Input, Date Picker, Combo Box |
| `FontUnderline` | `Underline` | Text, Link, Info Button, Radio, Text Input, Date Picker, Combo Box |
| `Weight` | `FontWeight` | Text only |
| `BorderRadius` | `RadiusTopLeft`, `RadiusTopRight`, `RadiusBottomLeft`, `RadiusBottomRight` | All controls with borders |

### New enum patterns

Many properties that previously accepted plain string values now use typed enum syntax. This affects formulas that hardcode these values.

For a full reference, see [New enum patterns in modern controls](new-enums-reference.md).

**Most common enum changes:**

| Property | Old (string) | New (enum) | Affected controls |
|----------|-------------|------------|-------------------|
| `Align` | `"Start"` or `""` | `Align.Left` | Text, Link, Text Input, Number Input, Tab List |
| `VerticalAlign` | `""` | `VerticalAlign.Middle` | Text, Link |
| `FontWeight` | `"Regular"` | `FontWeight.Normal` | All controls with text |
| `ValidationState` | `"None"` | `ValidationState.None` | Date Picker, Text Input, Number Input, Combo Box, Radio |
| `Appearance` | `"FilledDarker"` | `Appearance.FilledDarker` | Date Picker, Text Input, Number Input, Combo Box |
| `DisplayMode` | *(No change, already enum)* | `DisplayMode.Edit` | Date Picker, Text Input, Radio, Combo Box, Tab List, Info Button |

> [!NOTE]
> **FontWeight.Medium removed**: If your previous control used `FontWeight.Medium`, it will automatically map to `FontWeight.Normal` in the new version. The available values are: `Bold`, `Semibold`, `Normal`, and `Lighter`.

### BorderRadius split into corner-specific properties

All controls that previously had a single **BorderRadius** property now have four separate properties for each corner:

```
// Previous version
Control.BorderRadius = 8

// New version
Control.RadiusTopLeft = 8
Control.RadiusTopRight = 8
Control.RadiusBottomLeft = 8
Control.RadiusBottomRight = 8
```

This gives you more flexibility to create controls with different corner radii (e.g., rounded top corners only).

### OnChange behavior improvements

Several controls have updated **OnChange** event behavior to fire at more appropriate times:

| Control | Previous OnChange | New OnChange | Impact |
|---------|------------------|--------------|--------|
| Text Input | Every keystroke | Focus out (blur) only | **CRITICAL** - Major performance improvement, may require formula updates |
| Number Input | Every keystroke | Focus out + step button clicks | Major performance improvement |
| Combo Box | Delayed/Focus out | Every selection/deselection | More responsive interaction |
| Radio | Sometimes inconsistent | Every selection reliably | Improved reliability |

**Migration tip:** For controls where OnChange no longer fires on every keystroke, reference the control's output property (e.g., `TextInput1.Text`) directly in other formulas if you need immediate per-keystroke updates.

### TriggerOutput changes

For controls with a **TriggerOutput** property:

| Control | Change | Impact |
|---------|--------|--------|
| Text Input | Default changed from **FocusOut** to **OnKeypress** | Text updates immediately on keystroke (Delayed in forms) |
| Number Input | **TriggerOutput** property removed entirely | No longer available |
| Combo Box | No longer fires OnChange | TriggerOutput and OnChange are now independent |
| Text Input | No longer fires OnChange | TriggerOutput and OnChange are now independent |

### DisplayMode.View read-only behavior

Controls that support **DisplayMode** now properly show a read-only visual state (not a disabled/grayed-out state) when **DisplayMode** is set to `DisplayMode.View`.

**Affected controls:** Date Picker, Text Input, Radio, Combo Box

**Previous behavior (bug):** View mode either still allowed editing or appeared disabled/grayed-out.

**New behavior (fixed):** View mode displays data clearly in a read-only state without appearing disabled.

### AcceptsFocus removed

The **AcceptsFocus** property has been removed from controls that had it. The controls now automatically manage focus behavior for accessibility.

**Affected controls:** Link, Info Button, Combo Box

**Migration:** Remove any formulas that reference `AcceptsFocus`. The controls handle focus automatically.

### Improved mobile defaults

All controls now ship with mobile-optimized defaults when added to a mobile layout canvas. These include:

- Larger widths and heights for easier touch interaction
- Larger font sizes (typically 24pt for mobile)
- Appropriate padding and spacing

### Updated command bar and right-click menus

All controls have updated command bar menus and right-click floatie menus in the authoring experience with quick access to the most commonly used style properties:

- Font and Font size
- Font color
- Background color (Fill)
- Alignment
- Border properties

## Critical security fix

### Link control URL validation

The **Link** control now validates and sanitizes URLs to prevent XSS (cross-site scripting) attacks. URLs using `javascript:` or other unsafe protocols are blocked.

**Previous behavior (security vulnerability):** The URL property accepted any URL including `javascript:` URIs that could execute malicious code.

**New behavior (security fix):** URLs are validated and unsafe protocols are blocked.

**Migration:** Review all Link controls and ensure they use standard `https://` or `http://` URLs. Remove any `javascript:` URIs.

## How to identify affected apps

To find apps that may need updates:

1. **Open the app** - You'll see notifications on controls that can be updated
2. **Click "Learn more"** - Review the migration guide for each control
3. **Search your formulas** for renamed properties:
   - `FontColor`, `FontSize`, `FontItalic`, `FontStrikethrough`, `FontUnderline`
   - `Weight` (Text control only)
   - `BorderRadius` (now split into 4 corner properties)
   - `AcceptsFocus` (removed from Link, Info Button, Combo Box)
   - `DisplayMode` (removed from Text control)
4. **Search for string-based enum values:**
   - `"Start"`, `"Center"`, `"End"` (use `Align.Left`, `Align.Center`, `Align.Right`)
   - `"Regular"`, `"Bold"` (use `FontWeight.Normal`, `FontWeight.Bold`)
   - `"None"`, `"Error"` (use `ValidationState.None`, `ValidationState.Error`)
5. **Review OnChange formulas** in Text Input and Number Input apps that depended on every-keystroke firing

## Migration checklist

Use this checklist when migrating your app:

### 1. Read control-specific migration guides
- [ ] Review migration guide for each control type you use
- [ ] Note all breaking changes and property renames

### 2. Update property names
- [ ] Replace `FontColor` → `Color`
- [ ] Replace `FontSize` → `Size`
- [ ] Replace `FontItalic` → `Italic`
- [ ] Replace `FontStrikethrough` → `Strikethrough`
- [ ] Replace `FontUnderline` → `Underline`
- [ ] Replace `Weight` → `FontWeight` (Text control only)
- [ ] Replace `BorderRadius` → `RadiusTopLeft`, `RadiusTopRight`, etc.

### 3. Update enum values
- [ ] Replace string alignment values with `Align` enum
- [ ] Replace string validation values with `ValidationState` enum
- [ ] Replace string appearance values with `Appearance` enum
- [ ] Update `FontWeight` values to enum (remove `Medium` if used)

### 4. Update OnChange logic
- [ ] Review Text Input and Number Input **OnChange** formulas
- [ ] Adjust for new timing (blur instead of keystroke)
- [ ] Use output properties directly for immediate updates

### 5. Review TriggerOutput
- [ ] Update Text Input **TriggerOutput** if you relied on FocusOut default
- [ ] Remove **TriggerOutput** references from Number Input
- [ ] Remove logic that expected TriggerOutput to fire OnChange

### 6. Remove obsolete properties
- [ ] Remove **AcceptsFocus** references (Link, Info Button, Combo Box)
- [ ] Remove **DisplayMode** from Text controls
- [ ] Remove **Required** property from Date Picker (use ValidationState instead)

### 7. Test security changes
- [ ] Review all Link control URLs
- [ ] Remove any `javascript:` URIs
- [ ] Ensure all links use `https://` or `http://`

### 8. Test bug fixes
- [ ] Verify Date Picker **Format** and **DateTimeZone** work correctly
- [ ] Test Radio and Tab List item ordering
- [ ] Verify **View** mode displays correctly (not disabled)
- [ ] Test Info Button content expansion
- [ ] Test Combo Box multi-select toggle behavior

### 9. Click the Update button
- [ ] Update each control using the **Update** button when available
- [ ] Test the updated control thoroughly
- [ ] Verify all formulas work correctly

## Common migration examples

### Example 1: Update font properties

**Previous version:**
```
Control.FontColor = Color.Blue
Control.FontSize = 16
Control.FontItalic = true
```

**New version:**
```
Control.Color = Color.Blue
Control.Size = 16
Control.Italic = true
```

### Example 2: Update alignment enums

**Previous version:**
```
Control.Align = "Center"
Control.VerticalAlign = ""
```

**New version:**
```
Control.Align = Align.Center
Control.VerticalAlign = VerticalAlign.Middle
```

### Example 3: Update BorderRadius

**Previous version:**
```
Control.BorderRadius = 8
```

**New version:**
```
Control.RadiusTopLeft = 8
Control.RadiusTopRight = 8
Control.RadiusBottomLeft = 8
Control.RadiusBottomRight = 8
```

### Example 4: Update OnChange for Text Input

**Previous version (fired on every keystroke):**
```
TextInput1.OnChange = Patch(
    Customers,
    LookUp(Customers, ID = varID),
    {Name: TextInput1.Text}
)
```

**New version (fires on blur):**
```
// Same formula, but now runs only when user leaves field
TextInput1.OnChange = Patch(
    Customers,
    LookUp(Customers, ID = varID),
    {Name: TextInput1.Text}
)

// For immediate filtering, reference Text directly
FilteredCustomers = Filter(Customers, TextInput1.Text in CustomerName)
```

## See also

- [Modern controls overview](overview-modern-controls.md)
- [New enum patterns reference](new-enums-reference.md)
- Individual control migration guides (see table above)
