# 启动
Start-ScheduledTask -TaskName "SeelenIdleKiller"
# 检查
Get-ScheduledTask -TaskName "SeelenIdleKiller" | Select-Object TaskName, State
# 停止
Stop-ScheduledTask -TaskName "SeelenIdleKiller"
# 检测
$csvPath = "C:\Users\MZH\Desktop\监控日志.csv"
"Readings,Timestamp,CounterSamples" | Set-Content -Path $csvPath
while ($true) {
    $data = Get-Counter @(
        "\process(seelen-ui)\% processor time"
        "\process(msedgewebview2*)\% processor time"
        "\physicaldisk(_total)\% disk time"
        "\processor(_total)\% processor time"
    )
    $data | Export-Csv -Path $csvPath -Append -NoTypeInformation
    Write-Host "$(Get-Date -Format HH:mm:ss) - logged"
    Start-Sleep -Seconds 5
}