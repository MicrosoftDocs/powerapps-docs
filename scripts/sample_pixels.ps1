Add-Type -AssemblyName System.Drawing
foreach ($name in @('advanced-open.png','recalc1.png','label-hello-world.png','syntax-highlighting.png','three-sliders.png','insert-slider.png')) {
    $path = "C:\Users\mkaur\Downloads\github\powerapps-docs-pr\powerapps-docs\maker\canvas-apps\media\working-with-formulas\$name"
    $bmp = New-Object System.Drawing.Bitmap $path
    $h = $bmp.Height
    "--- $name ($($bmp.Width)x$h) ---"
    foreach ($y in 0,1,5,25,45,49,50,51,55) {
        if ($y -ge $h) { continue }
        $p = $bmp.GetPixel(600, $y)
        "  y={0,-3} : {1},{2},{3}" -f $y, $p.R, $p.G, $p.B
    }
    $bmp.Dispose()
}
