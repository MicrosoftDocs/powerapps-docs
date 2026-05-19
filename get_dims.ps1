Add-Type -AssemblyName System.Drawing
$base = 'c:\Users\mkaur\Downloads\github\powerapps-docs-pr\powerapps-docs\maker\canvas-apps\media\data-platform-create-app-scratch'
foreach ($n in @('close-data.png','gallery-items.png','final-browse.png','field-list.png','rename-browse.png','choose-or-add-fields.png','refresh-icon.png','plus-icon.png','next-icon.png','cancel-icon.png','checkmark-icon.png','trash-icon.png')) {
    $p = Join-Path $base $n
    if (Test-Path $p) {
        $img = [System.Drawing.Image]::FromFile($p)
        Write-Host "$n : $($img.Width) x $($img.Height)"
        $img.Dispose()
    } else {
        Write-Host "$n : File not found"
    }
}
